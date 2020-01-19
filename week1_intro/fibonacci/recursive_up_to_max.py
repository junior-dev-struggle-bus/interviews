# Question: Is this an appropriate approach
# for a solution to this particular problem 
# statement?
# Answer: No. Recursion is most useful when 
# the problem in question 

def fibonacci(max_val):
    l = []
    helper(l, max_val)
    for elem in l:
        print(elem)

def fibonacci(fib_list, max_val):
    if len(fib_list) > 1 and fib_list[-1] + fib_list[-2] > max_val: return
    
