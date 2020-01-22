def dict_demo():
    # create an empty dictionary
    d = {}
    # add some elements
    d[1] = 'a'
    keys = [2, 3, 4, 5, 6]
    vals = ['b', 'c', 'd', 'e', 'f']
    for k, v in zip(keys, vals):
        print('Adding keyval pair', k, ':', v)
        d[k] = v
    print(d)
    # remove an element
    d.pop(6)

if __name__=='__main__':
    dict_demo()
