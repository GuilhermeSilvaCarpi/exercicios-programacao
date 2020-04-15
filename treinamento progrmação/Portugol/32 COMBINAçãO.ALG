algoritmo "32 combinação"
var
   c1, c2, c3, combinacoes : inteiro
inicio
   para c1 <- 1 ate 3 faca
      para c2 <- 1 ate 3 faca
         para c3 <- 1 ate 3 faca
            escreval(c1,c2,c3)
            combinacoes <- combinacoes + 1
         fimpara
      fimpara
   fimpara

   escreva("a quantidade de combinações é:",combinacoes)
   //escreva(5^5)
   //27
fimalgoritmo