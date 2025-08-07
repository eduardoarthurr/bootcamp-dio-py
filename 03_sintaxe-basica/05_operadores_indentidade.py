#Operadores de identidade são utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.

curso = "Curso de Python"
nome_curso = curso
saldo = 200
limite = 200

#ambos na mesma região de memória 

comparacao = curso is nome_curso

print(comparacao)

#--------------------------------

#caso voce queira comparar a o contrario ou seja voce nao deseja que eles ocupem o mesmo lugar na memoria basta usar o operador logico not 

comparacao_1 = curso is not nome_curso

print(comparacao_1)

#--------------------------------

#voce pode comparar valores inteiros também

comparacao_2 = saldo is limite

print(comparacao_2)


