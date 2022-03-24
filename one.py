def reverse (m):
    output =[]
    x = len(m) 
    while x > 0: 
        output.append(m[x-1])
        x = x-1
    return output