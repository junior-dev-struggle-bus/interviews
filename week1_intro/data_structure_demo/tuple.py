def tuple_demo():
    tup = (1, 2, 3)
    print('Tuple is:', tup, 'Length:', len(tup))
    try:
        print('Attempting to reassign tuple element.')
        tup[0] = 'test'
    except TypeError:
        print('Caught TypeError because tuple is immutable; elements cannot be changed.')
    # instead of reassigning tuple elements, we can convert
    # the tuple to a list, reassign/modify as we see fit, 
    # and convert the modified list back into a tuple.
    l = list(tup)
    l[0] = 'test'
    tup = tuple(l)
    print('Tuple after conversion is:', tup, 'Length:', len(tup))

if __name__=='__main__':
    tuple_demo()
