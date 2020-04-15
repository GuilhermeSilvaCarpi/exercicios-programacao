algoritmo "46 listagem alunos (vetor)"
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

      para i <- 1 ate 4 faca
           escreval(nome[i]:15,m[i]:4:1)
      fimpara
fimalgoritmo