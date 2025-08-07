# Estruturas de repetição são utilizadas para repetir um trecho de código um determinado numero de vezes. esse número pode ser conhcecido previamente ou determinado através de uma exoressão lógica

#O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

# Interavel
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
	if letra.upper() in VOGAIS:
		print(letra, end="")
		
print()  

#Range é uma função built-in do Python, ela é usada para produzir uma sequência de números inteiros a partir de um ínicio (inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido: 
#i, i+1, i+2, i+3, ..., j-1.
#Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

#função built-in range
for numero in range(0,51,5): # for numero in range(satart,stop, step)
	print(f"{numero}...")
	
#While é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

opcao = -1

while opcao != 0:
	opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
	if opcao == 1:
		print("Sacando...")
	elif opcao == 2:
		print("Exibindo o extrato...")
	else:
		print("Obrigado por usar nosso sistema bancário, até logo!")