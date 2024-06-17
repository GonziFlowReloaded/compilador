from lexer import tokenize
from sintactico import parse
from semantico import analyze
from intermedio_code import generate_intermediate_code
from optimizer import optimize
from final_code import generate_final_code_with_printear

def compile(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    analyze(ast)
    intermediate_code, result = generate_intermediate_code(ast)
    optimized_code = optimize(intermediate_code)
    final_code = generate_final_code_with_printear(optimized_code, ast)
    return final_code

# Ejemplo de uso
if __name__ == "__main__":
    code = "PRINTEAR 3 + 5 * (2 - 8)'"
    compiled_code = compile(code)
    compiled_code_str = "\n".join(compiled_code)
    print("Código generado:")
    print(compiled_code_str)
    print("\nResultado de la ejecución:")
    exec(compiled_code_str)
