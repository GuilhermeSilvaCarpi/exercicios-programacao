algoritmo "54 ler matriz (Matriz)"
var
   m : vetor[1..3, 1..2] de caracter
   l, c : inteiro
inicio
      para l de 1 ate 3 faca
          para c de 1 ate 2 faca
               escreva("Digite o valor da posição",l,c," : ")
               leia(m[l,c])
          fimpara
      fimpara
      
      para l de 1 ate 3 faca
           para c de 1 ate 2 faca
                escreva("[",m[l,c],"]")
           fimpara
           escreval("")
      fimpara
fimalgoritmo