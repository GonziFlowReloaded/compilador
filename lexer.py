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
