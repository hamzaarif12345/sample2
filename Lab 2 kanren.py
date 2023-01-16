# Import the necessary functions from the kanren library
from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative
# Define values that will undertake the addition and multiplication operations
addition = 'add'
multiplication = 'mul'
# Define facts and properties of each operation
fact(commutative, multiplication)
fact(commutative, addition)
fact(associative, multiplication)
fact(associative, addition)
# Declare the variables that are going to form the expression
var_x, var_y, var_z = var('var_x'), var('var_y'), var('var_z')
# Build the correct pattern that the program needs to learn
match_pattern = (addition, (multiplication, 4, var_x, var_y), var_y, (multiplication, 6, var_z))
match_pattern = (addition, (multiplication, 3, 4), (multiplication, (addition, 1, (multiplication, 2, 4)),2))
# Build 3 distinct expressions to test if the function has learnt
test_expression_one = (addition, (multiplication, (addition, 1 , (multiplication, 2, var_x )), var_y) ,(multiplication, 3, var_z ))
test_expression_two = (addition, (multiplication, var_z, 3), (multiplication, var_y, (addition, (multiplication, 2, var_x), 1)))
test_expression_three = (addition  , (addition, (multiplication, (multiplication, 2, var_x), var_y), var_y), (multiplication, 3, var_z))
# Test the evaluations of the expression on the test expressions
print("Test expression one: ")
print(run(0,(var_x,var_y,var_z),eq(test_expression_one,match_pattern)))
print("Test expression two: ")
print(run(0,(var_x,var_y,var_z),eq(test_expression_two,match_pattern)))
print("Test expression three: ")
print(run(0,(var_x,var_y,var_z),eq(test_expression_three,match_pattern)))
