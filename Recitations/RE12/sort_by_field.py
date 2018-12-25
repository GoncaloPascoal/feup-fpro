
def sort_by_field(filename, field):
    with open(filename) as f:
        content = f.read().rstrip()

    lines = content.split("\n")

    if len(lines) < 2:
        return content

    field_names = lines[0].split(",")
    field_idx = field_names.index(field)

    sorted_lines = [lines[0]] + sorted(lines[1:], key=lambda x: x.split(",")[field_idx])

    return "\n".join(sorted_lines)