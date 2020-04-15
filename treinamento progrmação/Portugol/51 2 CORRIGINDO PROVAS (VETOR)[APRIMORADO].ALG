algoritmo "51 2 corrigindo provas (matriz)[aprimorado]"
var
   questao : vetor[1..20] de caracter
   valor   : vetor[1..20] de real
   nome    : vetor[1..40] de caracter
   nota    : vetor[1..40] de real
   i, i2, n_q, n_m, n_a : inteiro
   questao_a : caracter
inicio
      //pt1
      escreva("Quantas questões tem a prova? ")
      leia(n_q)
      escreva("Qual a média para passar? ")
      leia(n_m)
      escreva("Quantos alunos? ")
      leia(n_a)
      limpatela
      //pt2
      escreval("CADASTRO DE GABARITO")
      escreval("======================")
      para i de 1 ate n_q faca
           escreva("Questão",i,":        ")
           leia(questao[i])
           escreva("Valor da questao: ")
           leia(valor[i])
      fimpara
      limpatela
      //pt3
      para i de 1 ate n_a faca
          escreval("ALUNO(A)",I)
          escreval("======================")
          escreva("Nome: ")
          leia(nome[i])
          para i2 de 1 ate n_q faca
               escreva("Questão",i2,": ")
               leia(questao_a)
               se (questao_a = questao[i2]) entao
                  nota[i] <- nota[i] + valor[i]
               fimse
          fimpara
          limpatela
      fimpara
      //pt4
      escreval("NOTAS")
      escreval("======================")
      escreval("ALUNOS SEM RECUPARAÇÃO")
      escreval("======================")
      para i de 1 ate n_a faca
           se (nota[i] >= n_m) entao
              escreval(nome[i]:10,": ",nota[i]:3:1)
           fimse
      fimpara
      escreval("======================")
      escreval("ALUNOS EM RECUPARAÇÃO")
      escreval("======================")
      para i de 1 ate n_a faca
           se (nota[i] < n_m) entao
              escreval(nome[i]:10,": ",nota[i]:3:1)
           fimse
      fimpara
fimalgoritmo