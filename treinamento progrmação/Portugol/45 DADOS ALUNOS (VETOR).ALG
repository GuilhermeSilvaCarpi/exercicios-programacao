algoritmo "45 dados alunos (vetor)"
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
      
      repita
            escreva("ver os dados de qual aluno? ")
            leia(esc1)
            escreval("Nome: ",nome[esc1])
            escreval("Primeira nota:",n1[esc1])
            escreval("Segunda nota:",n2[esc1])
            escreval("Média:",m[esc1])
            escreval("---------------------------")
            escreval("Quer continuar? [s/n]")
            leia(esc2)
            
            limpatela
      ate esc2 = "n"
fimalgoritmo