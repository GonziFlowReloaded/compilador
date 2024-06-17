from intermedio_code import generate_intermediate_code
def generate_final_code(optimized_code, result):
    final_code = []
    final_code.extend(optimized_code)
    final_code.append(f"print({result})")
    return final_code

def generate_printear_code(ast):
    if ast.type == 'PRINTEAR':
        expr_code, result = generate_intermediate_code(ast.children[0])
        return expr_code + [f"print({result})"]

def generate_final_code_with_printear(optimized_code, ast):
    final_code = []
    for line in optimized_code:
        final_code.append(line)
    printear_code = generate_printear_code(ast)
    if printear_code:
        final_code.extend(printear_code)
    return final_code
