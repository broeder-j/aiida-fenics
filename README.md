# `aiida-fenics`

AiiDA plugin for the [FEniCS computing platform](https://fenicsproject.org/) for solving partial differential equations.


# Installation

The easiest method for installation is to download the source code and install it with `pip`:

    git clone https://github.com/sphuber/aiida-fenics
    pip install aiida-fenics

Note that on Ubuntu, one might have to install additional shared libraries that are required by `gmsh`:

    sudo apt install libglu1-mesa


# Example

## Solving Poisson equation for geometry

To solve the Poisson equation for a particular geometry, one can use the `GeometryPoisson` work chain:

```python
from aiida.engine import run
from aiida.orm import Int, SinglefileData

cls = WorkflowFactory('fenics.geometry_poisson')
geometry = SinglefileData('/path/to/geometry.geo')
inputs = {
    'geometry': geometry,
    'dimension': Int(2),
}
results = run(cls, **inputs)
```
