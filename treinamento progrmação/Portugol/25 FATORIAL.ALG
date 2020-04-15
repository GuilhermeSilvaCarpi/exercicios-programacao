algoritmo "25 fatorial"
var
   r : caracter
   n, c, f : inteiro
inicio
      escreva("digite um numero: ")
      leia(n)
      c <- n + 1
      f <- 1

      repita
         repita
               c <- c - 1
               f <- c * f
         ate c = 1
         escreval("o fatorial de",n," é igual a",f)
         escreva("quer continuar? [s/n]")
         leia(r)
      ate r = "n"
fimalgoritmo