## TIPOS DE DADOS

POR QUE USAMOS?? 

Os tipos servem para definir as características e comportamentos de um valor (objeto) para o interpretador. Por exemplo:

Com esse tipo eu sou capaz de realizar operações matemáticas.

Esse tipo para ser armazenado em memória irá consumir 24 bytes.

``` bash
int – Números inteiros (ex: 1, 42, -10)

float – Números de ponto flutuante (ex: 3.14, -0.001)

complex – Números complexos (ex: 2 + 3j)

bool – Booleano (ex: True, False)

str – Cadeia de caracteres (ex: "Olá", 'Python')

bytes – Sequência de bytes imutáveis (ex: b"abc")

bytearray – Sequência de bytes mutáveis

memoryview – Visão de um buffer de memória
```
---

## Modo Interativo

Modo interativo nada mais é que a abertura do terminal dentro da pasta ou arquivo .py, onde voce pode interagir com o arquivo com resposta imediata, a partir disso temos algumas funções que podem nos ajudar elas são:

Funções **dir()** e **help()**

**DIR**

Sem argumentos ,retorna a lista de nomes no escopo local atual .Com um argumento ,retorna uma lista de atributos válidos para o objeto. Exemplo:
dir()
dir(100)


**HELP**

É literalmente um guia interativo que voce pode invocar a partir do modo interativo, onde basta colocar o seu objeto de duvida após o comando que vai ser retornado uma explicação sobre o que o método faz e etc. Resumindo é uma documentação **off-line**. Exemplo:
help()
help(100)


---

## Variáveis e Constantes

**O que são variáveis e constantes?** 

**VARIAVEIS**

Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.

**CONSTANTES** 

Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é [[Imutável]].

**PYTHON NAO TEM CONTANTES !!!**

**Não existe uma palavra reservada para informar ao interpretador que o valor é constante**. Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.

Em Python usamos a [[convenção]] que diz ao programador  que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas:



```
ABS_PATH = '/home/guilherme/Documents/python_course/'
DEBUG = TrueSTATES = [    
'SP',    
'RJ',    
'MG',  
]  
AMOUNT = 30.2
```


nesse exemplo todos os objetos são exemplos de valores imutáveis com isso considerados **constantes**.


---

## Conversão de tipos 

Em alguns momentos é necessário será necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:

Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

Exemplo de como isso pode ser feito:

```
age = 19

name = "dudu"

(float(age))

# Nem sempre é possivel converter tipos por exemplo:

(int(name)) # Não é possivel converter uma string em um numero inteiro.
 
# Se quiser transformar um valor inteiro para ponto flutuante ou float para int pode usar a divisao também


print(100 / 2)  #inteiro para ponto flutuante

print(100 // 2) #float para int
```

Em momentos em que você quer [[Concatenar]] sua variável com mensagem para ser exibido ao seu usuário, pra isso e necessário transformar valores int ou float em strings ou então usar outro método para concatenar. Exemplo dos dois métodos:

```
1ª (str(age))
-----------------------------------------------------------
2ª print(f"Minha idade é {age} e meu nome é {name}")
```

O segundo método você está formatando, ou seja o ato de [[Concatenar]] uma string com variáveis


---

## Funções de entrada e saída

**ENTRADA (Input)**

A função builtin input é utilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

```

name = input("Digite seu nome: ")

```

**SAIDA(Print)**

A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

```
nome = "Guilherme"  
sobrenome = "Carvalho"  
  
print(nome, sobrenome)  
print(nome, sobrenome, end="...\n")  
print(nome, sobrenome, sep="#")  
  
>>> Guilherme Carvalho  
>>> Guilherme Carvalho...  
>>> Guilherme#Carvalho

```


---
