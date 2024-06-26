# compilador
# Compilador Personalizado

## Descripción del Proyecto
Este proyecto es un compilador simple que procesa expresiones aritméticas y la instrucción `PRINTEAR` para imprimir cadenas de texto. El compilador sigue una serie de pasos clásicos en la compilación: análisis léxico, análisis sintáctico, análisis semántico, generación de código intermedio, optimización y generación de código final.

## Características
- Soporte para operaciones aritméticas básicas (`+`, `-`, `*`, `/`).
- Capacidad para manejar paréntesis en expresiones.
- Instrucción `PRINTEAR` para imprimir resultados numéricos y cadenas de texto.
- Manejo de errores como división por cero.
- Generación de código intermedio y final.

## Estructura del Proyecto
- `lexer.py`: Analizador léxico.
- `sintactico.py`: Analizador sintáctico.
- `semantico.py`: Analizador semántico.
- `intermedio_code.py`: Generador de código intermedio.
- `optimizer.py`: Optimizador de código intermedio.
- `final_code.py`: Generador de código final.

## Instalación
1. Clona el repositorio:
    ```bash
    git clone https://github.com/usuario/compilador-personalizado.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd compilador-personalizado
    ```
3. (Opcional) Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```
4. Instala las dependencias (si es necesario):
    ```bash
    pip install -r requirements.txt
    ```

## Uso
Ejecuta el compilador con un código de ejemplo:

```python
# Ejemplo de uso
if __name__ == "__main__":
    code = 'PRINTEAR "MILF significa Man I love frogs"\''
    compiled_code = compile(code)
    compiled_code_str = "\n".join(compiled_code)
    print("Código generado:")
    print(compiled_code_str)
    print("\nResultado de la ejecución:")
    exec(compiled_code_str)
```

## Documentación del Código

### Analizador Léxico (`lexer.py`)
```python
import re

# Tokens posibles
TOKENS = [
    ("NUM", r"\d+"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULT", r"\*"),
    ("DIV", r"/"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("PRINTEAR", r"PRINTEAR"),
    ("STRING", r"\".*?\""),  # Nueva regla para cadenas de texto
    ("END", r"\'")
]

def tokenize(code):
    tokens = []
    while code:
        match = None
        code = code.lstrip()  # Eliminar espacios en blanco al inicio
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                text = match.group(0)
                tokens.append((token_type, text))
                code = code[len(text):]
                break
        if not match:
            raise ValueError(f"Unexpected character: {code[0]}")
    return tokens
```

### Analizador Sintáctico (`sintactico.py`)
```python
class ASTNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

def parse(tokens):
    def parse_expression(index):
        return parse_add_sub(index)

    def parse_add_sub(index):
        left_node, index = parse_mul_div(index)
        while index < len(tokens) and tokens[index][0] in ('PLUS', 'MINUS'):
            operation_node = ASTNode(tokens[index][0])
            operation_node.children.append(left_node)
            right_node, index = parse_mul_div(index + 1)
            operation_node.children.append(right_node)
            left_node = operation_node
        return left_node, index

    def parse_mul_div(index):
        left_node, index = parse_primary(index)
        while index < len(tokens) and tokens[index][0] in ('MULT', 'DIV'):
            operation_node = ASTNode(tokens[index][0])
            operation_node.children.append(left_node)
            right_node, index = parse_primary(index + 1)
            operation_node.children.append(right_node)
            left_node = operation_node
        return left_node, index

    def parse_primary(index):
        if tokens[index][0] == 'NUM':
            node = ASTNode('NUM', tokens[index][1])
            return node, index + 1
        elif tokens[index][0] == 'LPAREN':
            node, index = parse_expression(index + 1)
            if tokens[index][0] != 'RPAREN':
                raise ValueError("Expected ')'")
            return node, index + 1
        elif tokens[index][0] == 'STRING':
            node = ASTNode('STRING', tokens[index][1])
            return node, index + 1
        elif tokens[index][0] == 'PRINTEAR':
            node = ASTNode('PRINTEAR')
            expr_node, index = parse_expression(index + 1)
            node.children.append(expr_node)
            return node, index
        else:
            raise ValueError(f"Unexpected token: {tokens[index]}")

    ast, index = parse_expression(0)
    if index < len(tokens) - 1:
        raise ValueError("Unexpected tokens at the end")
    return ast
```

### Analizador Semántico (`semantico.py`)
```python
def analyze(ast):
    if ast.type == 'DIV' and ast.children[1].type == 'NUM' and ast.children[1].value == '0':
        raise ValueError("Division by zero")
    for child in ast.children:
        analyze(child)
```

### Generación de Código Intermedio (`intermedio_code.py`)
```python
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
        elif node.type == 'STRING':
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
```

### Generación de Código Final (`final_code.py`)
```python
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
    elif ast.type == 'STRING':
        return [f"print({ast.value})"]

def generate_final_code_with_printear(optimized_code, ast):
    final_code = []
    for line in optimized_code:
        final_code.append(line)
    
    printear_code = generate_printear_code(ast)
    if printear_code:
        final_code.extend(printear_code)
    
    return final_code
```

## Ejemplo de Ejecución
```python
# Ejemplo de uso
if __name__ == "__main__":
    code = 'PRINTEAR "MILF significa Man I love frogs"\''
    compiled_code = compile(code)
    compiled_code_str = "\n".join(compiled_code)
    print("Código generado:")
    print(compiled_code_str)
    print("\nResultado de la ejecución:")
    exec(compiled_code_str)
```

## Contribución
Si deseas contribuir a este proyecto, por favor sigue estos pasos:
1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.