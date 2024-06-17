class ASTNode:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

def parse(tokens):
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

    ast, index = parse_instructions(0)
    if index < len(tokens) - 1:
        raise ValueError("Unexpected tokens at the end")
    return ast
