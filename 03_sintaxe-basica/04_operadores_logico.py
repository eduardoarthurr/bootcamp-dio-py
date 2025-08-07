# Operadores logicos são utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica, retornando um valor booleano.

saldo = 1000
saque = 250
limite = 200
conta_especial = True


# leia-se saldo maior que ou igual a saque E saque maior que ou igual a limite .

comparacao = saldo >= saque and limite >= saque 

print(comparacao)

# o operador and para retornar true é necessario que todas expressoes forem verdadeiras

#------------------------------------------------------

# o operador or para retornar true é necessario que apenas uma das expressoes sejam verdadeiras.

comparacao_1 = saldo >= saque or limite >= saque

print(comparacao_1)

#--------------------------------------------------------

# o operador not inverte o valor retornado na comparação.

comparacao_2 = not saldo > saque

#--------------------------------------------------------

# para grandes comparações usando operadores logicos é necessario usar a precedencia de operadores para facialitar a leitura e  também se assegurar se falhas no codigo.

# esta correto mas meio confuso.
comparacao_3 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

# o mais correto a se fazer.
comparacao_4 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

# o indicado não é fazer expressões logicas muito grande.