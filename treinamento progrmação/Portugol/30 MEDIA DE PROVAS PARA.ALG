algoritmo "30 media de provas para"
var
   vezes, quantidade : inteiro
   nota, menor, maior, media : real
inicio
      escreva("quantas provas? ")
      leia(quantidade)
      menor <- 10
      para vezes <- 1 ate quantidade faca
           escreva("prova",vezes,": ")
           leia(nota)
           media <- media + nota
           
           se maior < nota entao
              maior <- nota
           fimse
           se menor > nota entao
           menor <- nota
           fimse
      fimpara
      media <- media / quantidade
      escreval("a media é :",media)
      escreval("a maior nota é :",maior)
      escreval("a menor nota é :",menor)
      
fimalgoritmo