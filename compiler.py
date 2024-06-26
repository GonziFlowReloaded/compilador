# Importaciones de Módulos

# Estos son los módulos importados que contienen las funciones necesarias para cada etapa del proceso de compilación:
# - `tokenize`: Realiza el análisis léxico.
# - `parse`: Realiza el análisis sintáctico.
# - `analyze`: Realiza el análisis semántico.
# - `generate_intermediate_code`: Genera el código intermedio.
# - `optimize`: Optimiza el código intermedio.
# - `generate_final_code_with_printear`: Genera el código final.
from lexer import tokenize
from sintactico import parse
from semantico import analyze
from intermedio_code import generate_intermediate_code
from optimizer import optimize
from final_code import generate_final_code
from generate_exe import generate_exe
from milf_reader import milf_reader
# Función Principal del Compilador

def compile(code):
    # Análisis Léxico: Convierte el código fuente en una lista de tokens.
    tokens = tokenize(code)
    
    # Análisis Sintáctico: Convierte la lista de tokens en un árbol de sintaxis abstracta (AST).
    ast = parse(tokens)
    for node in ast:
        analyze(node)
    intermediate_code = []
    for node in ast:
        intermediate_part, _ = generate_intermediate_code(node)
        intermediate_code.extend(intermediate_part)
    optimized_code = optimize(intermediate_code)
    final_code = generate_final_code(ast)
    return final_code, optimized_code, intermediate_code

# Ejemplo de uso
if __name__ == "__main__":
    code = 'PRINTEAR "El resultado de la operación es:" 10 / (2 + 5) 5 + 3 * 2\''
    code = milf_reader("codigo.milf")
    compiled_code, optimizado, intermedio = compile(code)
    compiled_code_str = "\n".join(compiled_code)
    
    # Se imprime el código final generado.
    print("Código generado:")
    print(compiled_code_str)
    
    generate_exe(compiled_code_str)

    
    # Se ejecuta el código final compilado.
    print("\nResultado de la ejecución:")
    exec(compiled_code_str)

