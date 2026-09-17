import numpy as np
variables = np.array(['x', 'y', 't'])
operations = ['+','-','*','/','**']
def expression_generator(n):
    """Generate an expression with n+1 operations"""
    k = 0
    v = np.size(variables)
    o = np.size(operations)
    expr = ''
    while k <= n:
        draw = np.random.randint(0,v,size=2)
        var_1,var_2= variables[draw]
        o_draw = np.random.randint(0,o)
        operation = operations[o_draw]
        if k == n:
            expr += var_1 + operation + var_2 
            break
        elif var_1 == var_2:
            expr += '2*' + var_1
        elif operation == '**':
            coin = np.random.randint(0,2)
            exponent = np.random.randint(0,10)
            pick = [var_1,var_2][coin]
            expr += pick + operation + str(exponent) 
        else:
            expr += var_1 + operation + var_2 + ' '
        expr+= '+'
        k +=1
    return expr

def make_expression_list(n,m):
    """Make a list of n expressions with m operations"""
    expr_list = []
    for i in range(n):
        expr_list.append(expression_generator(m))
    return expr_list

draw = expression_generator(2)
x = 1 
y = 1 
t = 2
#print(draw)
#print(eval(draw))



