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
from final_code import generate_final_code_with_printear

# Función Principal del Compilador

def compile(code):
    # Análisis Léxico: Convierte el código fuente en una lista de tokens.
    tokens = tokenize(code)
    
    # Análisis Sintáctico: Convierte la lista de tokens en un árbol de sintaxis abstracta (AST).
    ast = parse(tokens)
    
    # Análisis Semántico: Verifica la validez del AST desde el punto de vista semántico.
    analyze(ast)
    
    # Generación de Código Intermedio: Genera una representación intermedia del código.
    intermediate_code, result = generate_intermediate_code(ast)
    
    # Optimización: Optimiza el código intermedio para mejorar su eficiencia.
    optimized_code = optimize(intermediate_code)
    
    # Generación de Código Final: Genera el código final a partir del código intermedio optimizado.
    final_code = generate_final_code_with_printear(optimized_code, ast)
    
    # La función `compile` devuelve el código final generado.
    return final_code

# Ejemplo de uso
if __name__ == "__main__":
    # Se define una cadena de código de ejemplo.
    code = "PRINTEAR 3 + 5 * (2 - 8)'"
    
    # Se compila el código de ejemplo utilizando la función `compile`.
    compiled_code = compile(code)
    
    # El código compilado se convierte en una cadena para su visualización.
    compiled_code_str = "\n".join(compiled_code)
    
    # Se imprime el código final generado.
    print("Código generado:")
    print(compiled_code_str)
    
    # Se ejecuta el código final compilado.
    print("\nResultado de la ejecución:")
    exec(compiled_code_str)
