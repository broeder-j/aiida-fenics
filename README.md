# `aiida-fenics`

AiiDA plugin for the [FEniCS computing platform](https://fenicsproject.org/) for solving partial differential equations.


# Installation

The easiest method for installation is to download the source code and install it with `pip`:

    git clone https://github.com/sphuber/aiida-fenics
    pip install aiida-fenics

Note that on Ubuntu, one might have to install additional shared libraries that are required by `gmsh`:

    sudo apt install libglu1-mesa
