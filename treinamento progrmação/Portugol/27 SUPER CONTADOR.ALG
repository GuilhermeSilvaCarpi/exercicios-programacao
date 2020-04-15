algoritmo "super contador"
var
   c : logico
   a, b : inteiro
inicio
      repita
         escreval("")
         escreval("=================")
         escreval("| [1] De 1 a 10 |")
         escreval("| [2] De 10 a 1 |")
         escreval("| [3] Sair      |")
         escreval("=================")
         leia(a)

         escolha a
                caso 1
                     repita
                           b <- b + 1
                           escreva(b,"..")
                     ate b = 10
                     b <- 0
                caso 2
                     b <- 11
                     repita
                           b <- b - 1
                           escreva(b,"..")
                     ate b = 1
                     b <- 11
                caso 3
                     c <- verdadeiro
         fimescolha
      ate c
      limpatela
fimalgoritmo