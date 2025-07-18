"""
sample_program.py
Este arquivo deve conter a criação manual de uma instância da AST
para o programa MiniJava de exemplo fornecido no enunciado da atividade.
"""

from ast_minijava import *

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