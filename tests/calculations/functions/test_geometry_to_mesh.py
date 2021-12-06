# -*- coding: utf-8 -*-
"""Tests for the :mod:`aiida_fenics.calculations.functions.geometry_to_mesh` module."""
from aiida.orm import CalcFunctionNode, Int, SinglefileData
import pytest

from aiida_fenics.calculations.functions.geometry_to_mesh import geometry_to_mesh


@pytest.mark.usefixtures('with_backend')
def test_geometry_to_mesh(get_geometry, get_mesh):
    """Test the ``geometry_to_mesh`` calcfunction."""
    geometry = get_geometry('unit_square')
    mesh = get_mesh('unit_square.msh')
    results, node = geometry_to_mesh.run_get_node(SinglefileData(geometry), Int(2))

    assert isinstance(node, CalcFunctionNode)
    assert node.is_finished_ok

    assert 'mesh' in results
    assert isinstance(results['mesh'], SinglefileData)
    assert results['mesh'].get_content() == mesh.read_text()
