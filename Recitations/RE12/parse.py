
def make_tuple(l):
    tup = ()
    depth = 0
    for i in range(len(l)):
        if l[i] == '(':
            if depth == 0:
                startpos = i
            depth += 1
        elif l[i] == ')':
            depth -= 1
            if depth == 0:
                tup += (make_tuple(l[startpos+1:i]),)
        elif depth == 0:
            tup += (int(l[i]),)
    return tup

def parse(filename):
    with open(filename) as f:
        content = f.read()
    
    content = content.replace(" ", "").split("\n")
    return make_tuple(content)