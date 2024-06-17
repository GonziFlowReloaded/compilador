from intermedio_code import generate_intermediate_code
def generate_final_code(instructions):
    final_code = []
    for instruction in instructions:
        if instruction.type == 'PRINTEAR':
            final_code.extend(generate_printear_code(instruction))
        else:
            intermediate_code, result = generate_intermediate_code(instruction)
            final_code.extend(intermediate_code)
            final_code.append(f"print({result})")
    return final_code

def generate_printear_code(ast):
    code = []
    expr_node = ast.children[0]
    if expr_node.type == 'STRING':
        code.append(f"print({expr_node.value})")
    else:
        expr_code, result = generate_intermediate_code(expr_node)
        code.extend(expr_code)
        code.append(f"print({result})")
    return code
