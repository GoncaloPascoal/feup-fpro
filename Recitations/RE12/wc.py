
def wc(filename):
    with open(filename) as f:
        content = f.read()

    return len(content.split("\n")), len(content.split()), len(content)