algoritmo "49 ordenar valor (vetor)"
var
   vet : vetor[1..4] de inteiro
   i1, i2, a : inteiro
inicio
      para i1 <- 1 ate 4 faca
           escreva("digite um valor: ")
           leia(vet[i1])
      fimpara
      
      para i1 <- 1 ate 3 faca
           para i2 <- i1+1 ate 4 faca
                se (vet[i1] > vet[i2]) entao
                   a <- vet[i2]
                   vet[i2] <- vet[i1]
                   vet[i1] <- a
                fimse
           fimpara
      fimpara
      
      para i1 de 1 ate 4 faca
           escreval(vet[i1])
      fimpara
fimalgoritmo