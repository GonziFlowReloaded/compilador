def generate_intermediate_code(ast):
    # Esta función genera el código intermedio a partir del árbol de sintaxis abstracta (AST).
    code = []  # Lista para almacenar las instrucciones del código intermedio.
    temp_counter = 0  # Contador para generar nombres únicos para los temporales.

    def new_temp():
        # Genera un nuevo nombre temporal único.
        nonlocal temp_counter
        temp = f"t{temp_counter}"
        temp_counter += 1
        return temp

    def generate(node):
        # Genera el código intermedio recursivamente para un nodo del AST.
        if node.type == 'NUM':
            # Si el nodo es un número, devuelve su valor directamente.
            return node.value
        elif node.type in ('PLUS', 'MINUS', 'MULT', 'DIV'):
            # Si el nodo es una operación aritmética, genera el código para los operandos.
            left = generate(node.children[0])
            right = generate(node.children[1])
            temp = new_temp()  # Crea un nuevo temporal para almacenar el resultado.
            op = {'PLUS': '+', 'MINUS': '-', 'MULT': '*', 'DIV': '/'}[node.type]
            code.append(f"{temp} = {left} {op} {right}")  # Añade la instrucción al código intermedio.
            return temp

    result = generate(ast)  # Inicia la generación del código intermedio desde el nodo raíz del AST.
    return code, result  # Devuelve el código intermedio generado y el resultado final.