# -*- coding: utf-8 -*-
"""Calcfunction to compute the mesh from a geometry using gmsh."""
import shutil
import subprocess
import tempfile

from aiida.engine import calcfunction
from aiida.orm import Int, SinglefileData

from aiida_fenics.utils.logging import suppress_output


@calcfunction
def geometry_to_mesh(geometry: SinglefileData, dimension: Int):
    """Compute the mesh from a geometry using gmsh."""
    executable = shutil.which('gmsh')

    with tempfile.NamedTemporaryFile('w') as source:

        source.write(geometry.get_content())
        source.flush()

        with tempfile.NamedTemporaryFile(suffix='.msh') as target:
            parameters = [executable, f'-{dimension.value}', '-o', target.name, source.name]
            with suppress_output():
                subprocess.call(parameters)
            output_mesh = SinglefileData(target)

    return {'mesh': output_mesh}
