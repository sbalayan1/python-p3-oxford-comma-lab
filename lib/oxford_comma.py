def oxford_comma(items):
    if (len(items) == 1): return ''.join(items)
    if (len(items) == 2): return ' and '.join(items)
    output = ''
    for item in items:
        if item == items[-1]:
            output += f"and {item}"
        else:
            output += f"{item}, "
    
    return output
