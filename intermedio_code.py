def generate_intermediate_code(ast):
    code = []
    temp_counter = 0

    def new_temp():
        nonlocal temp_counter
        temp = f"t{temp_counter}"
        temp_counter += 1
        return temp

    def generate(node):
        if node.type == 'NUM':
            return node.value
        elif node.type in ('PLUS', 'MINUS', 'MULT', 'DIV'):
            left = generate(node.children[0])
            right = generate(node.children[1])
            temp = new_temp()
            op = {'PLUS': '+', 'MINUS': '-', 'MULT': '*', 'DIV': '/'}[node.type]
            code.append(f"{temp} = {left} {op} {right}")
            return temp

    result = generate(ast)
    return code, result
