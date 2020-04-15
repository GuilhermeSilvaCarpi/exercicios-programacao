algoritmo "44 impar ou par (vetor)"
var
   valor, pares, posicao : vetor[1..7] de inteiro
   c, c2 : inteiro
inicio
      para c <- 1 ate 7 faca
           escreva("Digite o",c,"o. um valor: ")
           leia(valor[c])
           
           se (valor[c] % 2 = 0) entao
              c2 <- c2 + 1
              pares[c2] <- valor[c]
              posicao[c2] <- c
           fimse
      fimpara
      
      escreval("o total de pares é: ",c2)
      escreva("Os valores pares são: ")
      para c <- 1 ate c2 faca
           se (c <> c2) entao
              escreva(pares[c])
           senao
                escreval(pares[c])
           fimse
      fimpara

      escreva("Os valores pares estão nas posições: ")
      para c <- 1 ate c2 faca
           escreva(posicao[c])
      fimpara
fimalgoritmo