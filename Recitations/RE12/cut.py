

def cut(filename, delimiter, field):
    s = ""

    with open(filename) as f:
        content = f.read()
        content = content.rstrip()
        lines = content.split("\n")

        for line in lines:
            cols = line.split(delimiter)
            if type(field) is int:
                s += cols[field - 1]
            else:
                s += delimiter.join([cols[x - 1] for x in field])
            s += "\n"
    
    return s.strip()