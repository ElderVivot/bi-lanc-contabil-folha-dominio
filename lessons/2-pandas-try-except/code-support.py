# Tuplas
tupla = (1, 2, 3, 4)
# tupla[2] = 1 --> tupla não aceita alterar o valor de nenhuma posição
print(tupla)

# Listas = Array
lista = [1, 2, 3, 4]
lista[2] = 10 # --> lista aceita alteração de valor, basicamente a diferença entre ela e tupla é isso
print(lista)

# Dicionário = Objeto
objeto = {
    "nome": 'Elder',
    "idade": 25
}
objeto['idade'] = 26
objeto['nome'] = 'Elder Vivot'
print(objeto)

### ----------------- ###

# Unir lista com dicionário, ou seja, uma array de objetos
print('------------------------')
lista_pessoas = [
    {
        "nome": 'Elder Vivot',
        "idade": 25
    },
    {
        "nome": 'Augusto Mago',
        "idade": 29
    }
]
for pessoa in lista_pessoas:
    pessoa['idade'] = 30
    print(pessoa)

### ----------------- ###

# Funções
print('------------------------')
def formatName(name: str):
    return name.upper()

name = 'Elder'
print(formatName(name))