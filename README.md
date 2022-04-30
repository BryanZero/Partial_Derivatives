# Partial_Derivatives

This function requires sympy and takes an expression and some optional data to evaluate its partial derivatives and output latex. My use for this was to automatically calculate partial derivatives of error propagation and input to latex.

Simple case for generating latex partials is: 

INPUT:
partials('4f2D3/S', 'f2 D3 S') 
OUTPUT:
{'Equation': '\frac{4 D_{3} f_{2}}{S}', 'D3': {'Partial': '\frac{4 f_{2}}{S}'}, 'S': {'Partial': '- \frac{4 D_{3} f_{2}}{S^{2}}'}, 'f2': {'Partial': '\frac{4 D_{3}}{S}'}}

Input:
partials('4f2D3/S', 'f2 D3 S', S=6.98e-08 f2=0.256 D3=20.149) 
Output: 
{'Equation': '\frac{4 D_{3} f_{2}}{S}', 'D3': {'Partial': '\frac{4 f_{2}}{S}', 'Evaluated': 14665699.279911555}, 'S': {'Partial': '- \frac{4 D_{3} f_{2}}{S^{2}}', 'Evaluated': -4232130893501872.5}, 'f2': {'Partial': '\frac{4 D_{3}}{S}', 'Evaluated': 1154293651.5271013}, 'OriginalEvaluated': 295499174.79093796}

