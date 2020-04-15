algoritmo "fibonacci"
var
   c, anterior, atual, proximo : inteiro
inicio
      proximo <- 1
      escreva(atual)
      para c <- 0 ate 15 faca
           escreva(proximo)
           anterior <- atual
           atual <- proximo
           proximo <- atual + anterior
      fimpara
fimalgoritmo