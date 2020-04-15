algoritmo "40 fatorial funcao"
var
   n : inteiro

funcao fatorial(v : inteiro) : inteiro
var
   c, r : inteiro
inicio
      r <- 1
      para C <- 1 ate v faca
           r <- r * c
      fimpara

      retorne r
fimfuncao

inicio
      escreva("digite um numero: ")
      leia(n)
      escreva("o fatorial de",n," é",fatorial(n))
fimalgoritmo