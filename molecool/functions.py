"""
functions.py
A python package for analyzing and visualizing molecular files, For Molssi workshop.

Handles the primary functions
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""
atom_data.py
- atomic_weight
- atom_colors

visualize.py
bond_histogram
draw_molecule

measure.py
- calculate_distance
- calculate_angle


molecule.py
- build_bond_list

IO (reading and writing functions) subpackage
read and write xyz and pdb

"""

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote

def zen():
    esto="Hola"
    return esto



if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
