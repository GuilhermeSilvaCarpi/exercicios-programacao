algoritmo "38 par ou impar funcao"
var
   n1, n2: inteiro
//
funcao ParOuImpar(a: inteiro) : caracter
inicio
      se (a % 2 = 0) entao
         retorne "par"
      senao
         retorne "impar"
      fimse
fimfuncao
//
inicio
      escreva("digite um numero: ")
      leia(n1)
      escreval("o numero digitedo é ",ParOuImpar(n1))
      escreva("digite outro numero: ")
      leia(n2)
      escreval("esse numero é ",ParOuImpar(n2))
fimalgoritmo