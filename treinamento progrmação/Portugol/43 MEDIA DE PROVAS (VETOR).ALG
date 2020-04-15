algoritmo "media de provas (vetor)"
var
   maior, menor, media : real
   c, v  : inteiro
   nota : vetor[1..9] de real
inicio
      escreva("quantas provas? ")
      leia(v)
      menor <- 10
      
      para c <- 1 ate v faca
           escreva("nota",c,": ")
           leia(nota[c])
           se (menor > nota[c]) entao
              menor <- nota[c]
           fimse
           se (maior < nota[c]) entao
              maior <- nota[c]
           fimse
           media <- media + nota[c]
      fimpara
      
      escreval("a menor nota é:",menor)
      escreval("a maior nota é:",maior)
      escreval("a media é: ",media/v:4:2)

      para c <- 1 ate v faca
           escreva(nota[c])
      fimpara
fimalgoritmo