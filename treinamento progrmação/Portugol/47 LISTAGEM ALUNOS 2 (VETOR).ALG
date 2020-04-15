algoritmo "47 listagem alunos 2 (vetor)"
var
   nome : vetor[1..4] de caracter
   n1 : vetor[1..4] de real
   n2 : vetor[1..4] de real
   m  : vetor[1..4] de real
   esc2 : caracter
   esc1 : inteiro
   i : inteiro
inicio
      para i <- 1 ate 4 faca
           escreval("ALUNO",i)
           escreval("---------------------------")
           escreva("Nome: ")
           leia(nome[i])
           escreva("Primeira nota: ")
           leia(n1[i])
           escreva("Segunda nota : ")
           leia(n2[i])
           m[i] <- (n1[i] + n2[i]) / 2
           limpatela
      fimpara

      escreval("LISTAGEM DE ALUNOS")
      escreval("---------------------------")
      escreval("LUNOS ACIMA DA MÉDIA")

      para i <- 1 ate 4 faca
           se (m[i] >= 6) entao
              escreval(nome[i]:15,m[i]:3:1)
           fimse
      fimpara

      escreval("---------------------------")
      escreval("LUNOS ABAIXO DA MÉDIA")
      
      para i <- 1 ate 4 faca
           se (m[i] < 6) entao
              escreval(nome[i]:15,m[i]:3:1)
           fimse
      fimpara
fimalgoritmo