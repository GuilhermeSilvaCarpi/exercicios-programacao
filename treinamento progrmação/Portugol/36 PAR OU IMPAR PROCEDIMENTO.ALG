algoritmo "36 par ou impar procedimento"
var
   n : inteiro
procedimento parouimpar (a : inteiro)
inicio

se (a % 2 = 0) entao
   escreva("o numero � par")
senao
   escreva("o numero � impar")
fimse

fimprocedimento
inicio
      escreva("digite um numero: ")
      leia(n)
      parouimpar(n)
fimalgoritmo