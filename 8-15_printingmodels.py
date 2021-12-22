# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 11:00:54 2021

@author: Hank
"""

import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)