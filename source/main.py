import numpy as np
import matplotlib.pyplot as plt
import generate
import bootstrap
import visual
import retrieve

"""
The final script will retrieve the array instead of generating it
"""
arr = retrieve.func_retrieve()

visual.func_visual(arr)

second_arr = bootstrap.func_bootstrap(arr)

visual.func_visual(second_arr)