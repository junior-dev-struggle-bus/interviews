def list_demo():
    my_list = [1, 2, 3, 'a', 'b', 'c']
    for i in range(len(my_list)):
        my_list[i] *= 2
    # my_list is [2, 4, 6, ‘aa’, ‘bb’, ‘cc’]
    
    for i, elem in enumerate(my_list):
        print(i, ':', elem, 'aka', my_list[i])
    my_list.append([4, 5, 6]) # append an inner list
    print(my_list[6])         # [4, 5, 6]
    my_list.pop()             # removes last element
    my_list.extend([4, 5, 6]) # concatenates arg to my_list
    print(my_list)

if __name__=='__main__':
    list_demo()
