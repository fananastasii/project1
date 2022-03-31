def to_hex(n):
    lis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
    h = ''
    if n == 0:
        return('0')
    while(n>0):
        b = n%16
        h = lis[b]+ h
        n = n//16  
    return(h)

def hex_color(r,g,b):
    r = to_hex(r)
    g = to_hex(g)
    b = to_hex(b)
    if len(r) == 1:
        r = '0'+r
    if len(g) == 1:
        g = '0'+g
    if len(b) == 1:
        b = '0'+b
    return ("#"+r+g+b)