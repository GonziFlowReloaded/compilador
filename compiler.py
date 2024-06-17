from lexer import tokenize
from sintactico import parse
from semantico import analyze
from intermedio_code import generate_intermediate_code
from optimizer import optimize
from final_code import generate_final_code

def compile(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    for node in ast:
        analyze(node)
    intermediate_code = []
    for node in ast:
        intermediate_part, _ = generate_intermediate_code(node)
        intermediate_code.extend(intermediate_part)
    optimized_code = optimize(intermediate_code)
    final_code = generate_final_code(ast)
    return final_code

# Ejemplo de uso
if __name__ == "__main__":
    code = 'PRINTEAR "Me pican los cocos: " PRINTEAR 3 + 5 * (2 - 8)\''
    compiled_code = compile(code)
    compiled_code_str = "\n".join(compiled_code)
    print("Código generado:")
    print(compiled_code_str)
    print("\nResultado de la ejecución:")
    exec(compiled_code_str)
