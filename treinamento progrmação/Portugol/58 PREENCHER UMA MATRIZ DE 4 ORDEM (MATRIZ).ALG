algoritmo "58 preencher uma matriz de 4 ordem (matriz)"
var
   matriz: vetor[1..4, 1..4] de inteiro
   l, c, sd_principal, p2l, m3c: inteiro
inicio
      //
      para l de 1 ate 4 faca
           para c de 1 ate 4 faca
                escreva("Digite o valor da posição [",l,",",c," ] : ")
                leia(matriz[l,c])
                se l = c entao
                   sd_principal <- sd_principal + matriz[l,c]
                fimse
           fimpara
      fimpara
      //
      escreval("")
      escreval("MATRIZ")
      para l de 1 ate 4 faca
          para c de 1 ate 4 faca
               escreva("[",matriz[l,c],"]":4)
          fimpara
          escreval("")
      fimpara
      //
      p2l <- 1
      para c de 1 ate 4 faca
           p2l <- p2l * matriz[2,c]
      fimpara
      //
      para l de 1 ate 4 faca
           se matriz[l,3] > m3c entao
              m3c <- matriz[l,3]
           fimse
      fimpara
      //
      escreval("")
      escreval("O produto dos valores da linha 2 é :",p2l)
      escreval("A soma dos valores da diagonal principal é :",sd_principal)
      escreval("O maior valor  da terceira coluna é :",m3c)
fimalgoritmo