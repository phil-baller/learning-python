def chop(information):
    count = 0
    for v in information:
        count = count + 1
    del information[:1]
    del information[-1:]
    return None

def middle(data_sets):
    chop(data_sets)
    print(data_sets)
    

element_values = [23, 43, 54, 34, 65, 45, 76, 345]

middle(element_values)
