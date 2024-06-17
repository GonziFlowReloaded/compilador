def analyze(ast):
    if ast.type == 'DIV' and ast.children[1].type == 'NUM' and ast.children[1].value == '0':
        raise ValueError("Division by zero")
    for child in ast.children:
        analyze(child)

