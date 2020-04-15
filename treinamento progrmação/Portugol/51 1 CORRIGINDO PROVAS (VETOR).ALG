algoritmo "51 corrigindo provas (vetor)"
var
   questao2: vetor[1..5] de caracter
   questao : vetor[1..5] de caracter
   nome    : vetor[1..3] de caracter
   nota    : vetor[1..3] de real
   media_turma : real
   i, i2 : inteiro
inicio
      //gabarito
      escreval("PASSO 1 - cadastro de gabarito")
      escreval("------------------------------")
      para i de 1 ate 5 faca
           escreva("Questão",i,": ")
           leia(questao[i])
      fimpara
      limpatela
      //
      para i de 1 ate 3 faca
         escreval("------------------------------")
         escreval("ALUNO(A)",i)
         escreval("------------------------------")
         escreva("Nome: ")
         leia(nome[i])
         escreval("RESPOSTAS DADAS")
         para i2 de 1 ate 5 faca
              escreva("Questão",i2,": ")
              leia(questao2[i2])
              se (questao2[i2] = questao[i2]) entao
                nota[i] <- nota[i] + 2
              fimse
         fimpara
         limpatela
      fimpara
      //notasfinais
      escreval("NOTAS FINAIS")
      escreval("------------------------------")
      para i de 1 ate 3 faca
           escreval(nome[i]:10,": ",nota[i]:3:1)
      fimpara
      escreval("------------------------------")
      para i de 1 ate 3 faca
           media_turma <- (media_turma + nota[i])
      fimpara
      media_turma <- media_turma / 3
      escreva("média da turma: ",media_turma:3:1)
fimalgoritmo