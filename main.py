from sympy import *

def partials(expression, variables, **values):
    partials = {}
    for k in variables.split():
        locals()[k] = Symbol(k)  # Assign the Symbol as a local variable
    expression = eval(expression)
    partials['Equation'] = latex(expression)
    for k in expression.free_symbols:  # For all the variables in the expression
        partials[str(k)] = {}
        partials[str(k)]['Partial'] = diff(expression,
                                           k)  # Calculate the partial derivative and store it into a dictionary
    if values:
        tmpList = [x for x in expression.free_symbols]
        lambdifyFunction = lambdify(tmpList, expression)
        templist = [i for i, j in zip([str(x) for x in expression.free_symbols], values)]
        results = [values[x] for x in templist]
        partials['OriginalEvaluated'] = lambdifyFunction(*results)

    for k in partials:  # For all the variables in the dictionary
        if not k == 'Equation' and not k == 'OriginalEvaluated':
            if values:
                llist = [x for x in
                         partials[str(k)]['Partial'].free_symbols]  # Get a list of remaining variables in each partial
                tmplambdify = lambdify(llist, partials[str(k)][
                    'Partial'])  # Lambdify the partial which means create a callable function which accepts the variables in llist
                templist = [i for i, j in zip([str(x) for x in partials[str(k)]['Partial'].free_symbols],
                                              values)]  # This was one way to maintain the order, for every symbol in each partial get it's corresponding value.
                results = [values[x] for x in templist]
                partials[str(k)]['Evaluated'] = tmplambdify(*results)
            partials[str(k)]['Partial'] = latex(partials[str(k)]['Partial'])

    return partials
