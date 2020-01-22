def fibonacci(n, sequence):
    # because lists are zero-indexed, n + 1 elements 
    # would be produced without reducing n before 
    # beginning recursive call chains.
    helper(n - 1, sequence)

def helper(n, sequence):
    if n > 0:
        helper(n - 1, sequence)
    if n == 0: sequence.append(0)
    elif n == 1: sequence.append(1)
    else: sequence.append(sequence[n - 1] + sequence[n - 2])

if __name__=='__main__':
    s = []
    fibonacci(10, s)
    print(s)
