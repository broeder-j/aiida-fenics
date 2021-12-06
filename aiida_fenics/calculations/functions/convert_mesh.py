# -*- coding: utf-8 -*-
"""Calcfunction to convert a mesh to a different output format."""
import pathlib
import tempfile

from aiida.engine import calcfunction
from aiida.orm import SinglefileData, Str
import meshio


@calcfunction
def convert_mesh(mesh: SinglefileData, input_format, output_format: Str):
    """Convert a mesh to a different output format."""
    with tempfile.NamedTemporaryFile(mode='wb') as source:

        # The :meth:`meshio.read` does not always support buffers so we need to write the content to a file on disk.
        with mesh.open(mode='rb') as handle:
            source.write(handle.read())
            source.flush()
            parsed = meshio.read(source.name, file_format=input_format.value)

    with tempfile.TemporaryDirectory() as dirpath:
        filepath = (pathlib.Path(dirpath) / mesh.filename).with_suffix(f'.{output_format.value}')
        parsed.write(filepath, file_format=output_format.value)
        converted_mesh = SinglefileData(filepath)
        results = {'mesh': converted_mesh}

        # The XDMF output format also generates an auxiliary output file with the extension `.h5`.
        if output_format == 'xdmf':
            results['h5'] = SinglefileData(filepath.with_suffix('.h5'))

    return results
