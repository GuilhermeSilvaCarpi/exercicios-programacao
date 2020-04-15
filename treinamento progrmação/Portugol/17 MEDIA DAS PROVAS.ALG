algoritmo "media das provas"
var
   vezes, quantidade :inteiro
   media, maior, menor, nota: real
inicio
      escreval("--------------------------")
      escreva("quantas provas? ")
      leia(quantidade)
      vezes <- 1
      maior <- 0
      menor <- 10
      escreval("--------------------------")
      enquanto (vezes <= quantidade) faca
               escreva("prova",vezes,": ")
               leia(nota)
               vezes <- vezes + 1
               media <- media + nota
               
               se maior < nota entao
                  maior <- nota
               fimse
               
               se menor > nota entao
                  menor <- nota
               fimse
      fimenquanto
      media <- media / quantidade
      escreval("--------------------------")
      escreval("a média das provas é:",media:3:1)
      escreval("e sua menor nota foi:",menor)
      escreval("e a maior nota foi:",maior)
      escreval("--------------------------")
fimalgoritmo