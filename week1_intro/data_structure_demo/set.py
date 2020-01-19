def set_demo():
    # create an empty set
    s = set()
    # add some elements
    s.add('a')              # single element
    s.update(['b', 'c'])    # multiple elements in iterable
    s.add('c')              # does nothing; unique elements only
    if 'a' in s:
        print('s contains \'a\'. s:', s)
    # we can create a set from other data structures
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    alphabet = set(l)
    t = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    alpha2 = set(t)
    shared = alpha2.intersection(alphabet)
    print('Intersection of alphabet sets:', shared)

if __name__=='__main__':
    set_demo()
