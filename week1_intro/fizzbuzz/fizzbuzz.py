def fizzbuzz():
    for i in range(1, 101):
        val = ''
        if i % 3 == 0: val += 'Fizz'
        if i % 5 == 0: val += 'Buzz'
        if not val: val = i
        print(val)

if __name__=='__main__':
    fizzbuzz()
