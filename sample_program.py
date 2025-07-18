"""
sample_program.py
Este arquivo deve conter a criação manual de uma instância da AST
para o programa MiniJava de exemplo fornecido no enunciado da atividade.
"""

from ast_minijava import *
from pprint import pprint

# MainClass (não tem membros além do nome, pois o corpo do main é fixo na sua gramática)
main_class = MainClass("Main")

# Classe Point com dois atributos inteiros
var_x = VarDecl(Type("int"), "x")
var_y = VarDecl(Type("int"), "y")
point_class = ClassDecl(
    name="Point",
    superclass=None,
    members=[var_x, var_y]
)

# Programa completo
program = Program(
    main_class=main_class,
    classes=[point_class]
)

def print_ast(node, indent=0):
    print('  ' * indent + f"{node.__class__.__name__}:")
    for k, v in node.__dict__.items():
        if isinstance(v, list):
            print('  ' * (indent + 1) + f"{k}: [")
            for item in v:
                print_ast(item, indent + 2)
            print('  ' * (indent + 1) + "]")
        elif isinstance(v, ASTNode):
            print('  ' * (indent + 1) + f"{k}:")
            print_ast(v, indent + 2)
        else:
            print('  ' * (indent + 1) + f"{k}: {v}")

print_ast(program)