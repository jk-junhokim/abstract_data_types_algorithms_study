import operator

from stack import Stack
from tree_object import BinaryTree

def print_exp(tree):
    str_val = ""
    if tree:
        str_val = '(' + print_exp(tree.get_left_child())
        str_val = str_val + str(tree.get_root_val()) # 'str' is the python function to make 'root_val' string type
        str_val = str_val + print_exp(tree.get_right_child()) + ')'

    return str_val

def postorder_evaluate(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    res1 = None
    res2 = None

    if tree:
        res1 = postorder_evaluate(tree.get_left_child())
        res2 = postorder_evaluate(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_val()](res1, res2)
        else:
            return tree.get_root_val()
                              

def build_parse_tree(math_expression):
    math_expression_list = math_expression.split() # elements for tree in order
    parent_stack = Stack() # keeping track of parent
    expression_tree = BinaryTree('') # empty tree with root node (value == '')
    parent_stack.push(expression_tree) # info about the current node we are on rn
    current_tree = expression_tree
    for i in math_expression_list:
        if i == '(': # rule number 1
            current_tree.insert_left('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']: # rule number 3
            current_tree.set_root_val(int(i))
            parent = parent_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']: # rule number 2
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')': # rule number 4
            current_tree = parent_stack.pop()
        else:
            raise ValueError
    return expression_tree

test_parse_tree = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(postorder_evaluate(test_parse_tree))
print(print_exp(test_parse_tree))

