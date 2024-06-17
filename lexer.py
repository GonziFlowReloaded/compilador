import re

# Definición de los Tokens Posibles
# Cada token es una tupla que contiene:
# - Un tipo de token (como "NUM" para números, "PLUS" para el símbolo '+', etc.).
# - Una expresión regular que define el patrón de ese token.
TOKENS = [
    ("NUM", r"\d+"),            # Números
    ("PLUS", r"\+"),            # Símbolo '+'
    ("MINUS", r"-"),            # Símbolo '-'
    ("MULT", r"\*"),            # Símbolo '*'
    ("DIV", r"/"),              # Símbolo '/'
    ("LPAREN", r"\("),          # Paréntesis izquierdo '('
    ("RPAREN", r"\)"),          # Paréntesis derecho ')'
    ("PRINTEAR", r"PRINTEAR"),  # Palabra clave 'PRINTEAR'
    ("END", r"\'")              # Símbolo de fin '\''
]

def tokenize(code):
    # Esta función realiza el análisis léxico del código fuente.
    tokens = []  # Lista para almacenar los tokens generados
    while code:
        match = None
        code = code.lstrip()  # Eliminar espacios en blanco al inicio
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)  # Compilar la expresión regular del token
            match = regex.match(code)    # Intentar hacer coincidir el patrón con el inicio del código
            if match:
                text = match.group(0)  # Obtener el texto que coincide con el patrón
                tokens.append((token_type, text))  # Añadir el token a la lista
                code = code[len(text):]  # Eliminar el texto coincidente del código
                break  # Salir del bucle una vez encontrado un token válido
        if not match:
            # Si no se encuentra ninguna coincidencia, se lanza una excepción indicando un carácter inesperado
            raise ValueError(f"Unexpected character: {code[0]}")
    return tokens  # Devolver la lista de tokens generados
