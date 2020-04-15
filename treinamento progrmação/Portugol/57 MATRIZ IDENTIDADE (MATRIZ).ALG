algoritmo "57 matriz identidade (matriz)"
var
   valor : vetor[1..3, 1..3] de inteiro
   l , c : inteiro
inicio
      para l de 1 ate 3 faca
           para c de 1 ate 3 faca
                se (l = c) entao
                   valor[l,c] <- 1
                senao
                   valor[l,c] <- 0
                fimse
           fimpara
      fimpara
      
      para l de 1 ate 3 faca
           para c de 1 ate 3 faca
                escreva(valor[l,c])
           fimpara
           escreval("")
      fimpara
fimalgoritmo