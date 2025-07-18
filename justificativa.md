### O que você optou por representar ou omitir?

Na modelagem da AST para o subconjunto de MiniJava, criei classes Python para cada entidade relevante da gramática, como `Program`, `MainClass`, `ClassDecl`, `VarDecl`, `MethodDecl`, `Param` e `Type`. Escolhi omitir elementos sintáticos como `{}`, `;` e palavras-chave fixas, pois não agregam significado semântico à árvore e sabemos que esses detalhes são tratados separadamente na etapa de tokenização.

### Como modelou listas, herança e elementos opcionais?

As **listas** de elementos tipo declarações de variaveis ou métodos foram representandas por uma lista de Python -> `List[Type]`

**Herança**: Usei herança entre classes Python, criando uma classe abstrata(base) chamada `MemberDecl` que é herdada por `VarDecl` e `MethodDecl`, permitindo tratar dos dois em conjunto.

**Opcionais**:
Elementos que podem ou não aparecer (como a herança de uma classe, que é opcional) foram representados usando o tipo `Optional` do Python. Por exemplo, o atributo `superclass` de `ClassDecl` pode ser uma string (nome da superclasse) ou `None` caso não haja herança.

### Houve dificuldades de representar alguma parte da gramática?

A principal dificuldade foi decidir o quanto de detalhe deveria ser incluído na AST. Por exemplo, fiquei em dúvida se deveria representar o corpo do método `main`, já que na gramática ele é fixo e não tem variações. Isso gerou certa insegurança sobre o que realmente era essencial para a árvore. No fim, optei por uma abordagem mais simples, focando só nos elementos que realmente mudam de um programa para outro, para manter a AST

