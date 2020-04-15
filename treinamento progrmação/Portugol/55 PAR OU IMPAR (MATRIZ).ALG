algoritmo "55 par ou impar (matriz)"
var
   matriz: vetor[1..3, 1..3] de inteiro
   l, c  : inteiro
inicio
      para l de 1 ate 3 faca
           para c de 1 ate 3 faca
                escreva("Digite um valor da posição",l,c,": ")
                leia(matriz[l,c])
           fimpara
      fimpara
      
      para l de 1 ate 3 faca
           para c de 1 ate 3 faca
                se (matriz[l,c] % 2 = 0) entao
                   escreva("[p]")
                senao
                     escreva("[i]")
                fimse
           fimpara
           escreval("")
      fimpara
fimalgoritmo