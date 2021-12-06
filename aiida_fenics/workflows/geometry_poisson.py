# -*- coding: utf-8 -*-
"""Workflow to solve the Poisson equation for a geometry file."""
from aiida.engine import WorkChain
from aiida.orm import Int, SinglefileData, Str

from aiida_fenics.calculations.functions import convert_mesh, geometry_to_mesh


class GeometryPoisson(WorkChain):
    """Workflow to solve the Poisson equation for a geometry file."""

    @classmethod
    def define(cls, spec):
        """Define the process specification."""
        super().define(spec)
        spec.input('geometry', valid_type=SinglefileData)
        spec.input('dimension', valid_type=Int)

        spec.outline(
            cls.geometry_to_mesh,
            cls.convert_mesh,
            cls.results,
        )

        spec.output('mesh', valid_type=SinglefileData, help='The mesh computed from the input geometry.')
        spec.output('mesh_xdmf', valid_type=SinglefileData, help='The mesh converted into XDMF format.')
        spec.output('mesh_h5', valid_type=SinglefileData, help='The auxiliary file to the XDMF mesh.')

    def geometry_to_mesh(self):
        """Compute the mesh from the input geometry."""
        results = geometry_to_mesh(self.inputs.geometry, self.inputs.dimension)
        self.ctx['mesh'] = results['mesh']

    def convert_mesh(self):
        """Convert the computed mesh to XDMF."""
        results = convert_mesh(self.ctx['mesh'], Str('gmsh'), Str('xdmf'))
        self.ctx['mesh_xdmf'] = results['mesh']
        self.ctx['mesh_h5'] = results['h5']

    def results(self):
        """Attach the output nodes."""
        self.out('mesh', self.ctx['mesh'])
        self.out('mesh_xdmf', self.ctx['mesh_xdmf'])
        self.out('mesh_h5', self.ctx['mesh_h5'])
