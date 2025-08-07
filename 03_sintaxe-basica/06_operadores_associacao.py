#Operadores de associação são utilizados para verificar se um objeto está presente em uma sequência .

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]


#retorna true,  pois a string declarada esta na variavel curso 

comparacao = "Python" in curso # é como se fosse a pergunta "Python" está na variavel curso?

print(comparacao)

#------------------------------

#retorna false, pois a string declarada nao faz parte da lista 

comparacao_1 = "banana" in frutas 

print(comparacao_1)

#-------------------------------

#neste caso vai retornar true, pois banana nao faz parte da lista frutas

comparacao_2 = "banana" not in frutas # como se estivesse perguntando "banana" não faz parte da lista frutas?

#-------------------------------

# agora com inteiro 

comparacao_3 = 200 in saques

print(comparacao_3)