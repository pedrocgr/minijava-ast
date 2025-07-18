"""
ast_minijava.py
Este arquivo deve conter a definição das classes que representam a Árvore de Sintaxe Abstrata (AST)
para o subconjunto da linguagem MiniJava definido na Atividade da disciplina IF688.
"""

from typing import List, Optional

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, main_class: 'MainClass', classes: List['ClassDecl']):
        self.main_class = main_class
        self.classes = classes

class MainClass(ASTNode):
    def __init__(self, name: str):
        self.name = name

class ClassDecl(ASTNode):
    def __init__(self, name: str, superclass: Optional[str], members: List['MemberDecl']):
        self.name = name
        self.superclass = superclass  # pode ser None
        self.members = members  # lista de VarDecl ou MethodDecl

class MemberDecl(ASTNode):
    pass

class VarDecl(MemberDecl):
    def __init__(self, var_type: 'Type', name: str):
        self.var_type = var_type
        self.name = name

class MethodDecl(MemberDecl):
    def __init__(self, return_type: 'Type', name: str, params: List['Param']):
        self.return_type = return_type
        self.name = name
        self.params = params

class Param(ASTNode):
    def __init__(self, param_type: 'Type', name: str):
        self.param_type = param_type
        self.name = name

class Type(ASTNode):
    def __init__(self, base_type: str, is_array: bool = False):
        self.base_type = base_type  # 'int', 'float', 'boolean', ou nome da classe
        self.is_array = is_array