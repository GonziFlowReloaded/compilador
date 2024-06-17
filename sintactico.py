class ASTNode:
    def __init__(self, type, value=None):
        # Inicializa un nodo del Árbol de Sintaxis Abstracta (AST).
        # Cada nodo tiene un tipo (type) y, opcionalmente, un valor (value).
        # Los hijos del nodo se almacenan en una lista (children).
        self.type = type
        self.value = value
        self.children = []

def parse(tokens):
<<<<<<< HEAD
    # Función principal de análisis sintáctico que convierte una lista de tokens en un AST.
=======
    def parse_instructions(index):
        instructions = []
        while index < len(tokens) and tokens[index][0] != 'END':
            if tokens[index][0] == 'PRINTEAR':
                node, index = parse_printear(index)
            else:
                node, index = parse_expression(index)
            instructions.append(node)
        return instructions, index

    def parse_printear(index):
        node = ASTNode('PRINTEAR')
        if tokens[index + 1][0] == 'STRING':
            expr_node, index = parse_primary(index + 1)
        else:
            expr_node, index = parse_expression(index + 1)
        node.children.append(expr_node)
        return node, index

>>>>>>> gonsiflow
    def parse_expression(index):
        # Comienza el análisis sintáctico de una expresión.
        return parse_add_sub(index)

    def parse_add_sub(index):
        # Analiza sumas y restas, que tienen menor precedencia.
        left_node, index = parse_mul_div(index)
        while index < len(tokens) and tokens[index][0] in ('PLUS', 'MINUS'):
            operation_node = ASTNode(tokens[index][0])
            operation_node.children.append(left_node)
            right_node, index = parse_mul_div(index + 1)
            operation_node.children.append(right_node)
            left_node = operation_node
        return left_node, index

    def parse_mul_div(index):
        # Analiza multiplicaciones y divisiones, que tienen mayor precedencia.
        left_node, index = parse_primary(index)
        while index < len(tokens) and tokens[index][0] in ('MULT', 'DIV'):
            operation_node = ASTNode(tokens[index][0])
            operation_node.children.append(left_node)
            right_node, index = parse_primary(index + 1)
            operation_node.children.append(right_node)
            left_node = operation_node
        return left_node, index

    def parse_primary(index):
        # Analiza los elementos primarios de las expresiones (números, paréntesis, y la palabra clave 'PRINTEAR').
        if tokens[index][0] == 'NUM':
            node = ASTNode('NUM', tokens[index][1])
            return node, index + 1
        elif tokens[index][0] == 'STRING':
            node = ASTNode('STRING', tokens[index][1])
            return node, index + 1
        elif tokens[index][0] == 'LPAREN':
            node, index = parse_expression(index + 1)
            if tokens[index][0] != 'RPAREN':
                raise ValueError("Expected ')'")
            return node, index + 1
        else:
            raise ValueError(f"Unexpected token: {tokens[index]}")

<<<<<<< HEAD
    # Inicia el análisis sintáctico desde el primer token.
    ast, index = parse_expression(0)
    
    # Verifica si hay tokens adicionales inesperados después del análisis completo.
=======
    ast, index = parse_instructions(0)
>>>>>>> gonsiflow
    if index < len(tokens) - 1:
        raise ValueError("Unexpected tokens at the end")
    
    # Devuelve el árbol de sintaxis abstracta (AST) generado.
    return ast