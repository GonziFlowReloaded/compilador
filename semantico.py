def analyze(ast):
    # Esta función realiza el análisis semántico del árbol de sintaxis abstracta (AST).
    if ast.type == 'DIV' and ast.children[1].type == 'NUM' and ast.children[1].value == '0':
        # Verifica si hay una división por cero en el AST.
        # Si encuentra una operación de división donde el segundo operando es el número 0,
        # lanza una excepción con el mensaje "Division by zero".
        raise ValueError("Division by zero")
    
    # Recorre recursivamente todos los hijos del nodo actual del AST para verificar otros posibles errores semánticos.
    for child in ast.children:
        analyze(child)