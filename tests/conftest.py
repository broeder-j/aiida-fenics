# -*- coding: utf-8 -*-
# pylint: disable=redefined-outer-name,unused-argument
"""Configuration and fixtures for unit test suite."""
import pathlib

import pytest

pytest_plugins = ['aiida.manage.tests.pytest_fixtures']  # pylint: disable=invalid-name


@pytest.fixture
def with_backend(aiida_profile):
    """Fixture that will initialize an AiiDA backend."""
    yield


@pytest.fixture
def filepath_resources():
    """Return the filepath to the directory containing test resources."""
    return pathlib.Path(__file__).resolve().parent / 'resources'


@pytest.fixture
def get_geometry(filepath_resources):
    """Return the path to file of the requested geometry."""
    def _factory(geometry):
        """Return the filepath of the geometry with the given name.

        .. note:: The extension ``.geo`` will be automatically appended, so only the filename should be provided.

        """
        return filepath_resources / 'geometries' / f'{geometry}.geo'

    return _factory


@pytest.fixture
def get_mesh(filepath_resources):
    """Return the path to file of the requested mesh."""

    def _factory(mesh):
        """Return the filepath of the mesh with the given name."""
        return filepath_resources / 'meshes' / mesh

    return _factory
