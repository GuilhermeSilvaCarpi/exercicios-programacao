algoritmo "26 numero primo"
var
   c, n, divisiveis : inteiro
inicio
      escreva("digite um numero: ")
      leia(n)

      repita
            c <- c + 1
            se n % c = 0 entao
               divisiveis <- divisiveis + 1
            fimse
      ate c = n

      se divisiveis > 2 entao
         escreva("o numero n�o � primo")
      senao
           escreva("o numero � primo")
      fimse

fimalgoritmo