algoritmo "50 tabela de partidas (vetor)"
var
   time : vetor[1..3] de caracter
   i, i2 : inteiro
inicio
      escreval("--------------------")
      escreval("CAMPEONATO DE FUTBOL")
      escreval("--------------------")
      
      para i de 1 ate  3 faca
           escreva("O nome do",i,"o. time: ")
           leia(time[i])
      fimpara
      limpatela
      
      escreval("------------------")
      escreval("TABELA DE PARTIDAS")
      escreval("------------------")
      para i de 1 ate 9 faca
           para i2 de i+1 ate 3 faca
                escreval(time[i]:10,"[ ] X [ ] ",time[i2])
           fimpara
      fimpara
      
      para i de 1 ate 9 faca
           para i2 de i+1 ate 3 faca
                escreval(time[i2]:10,"[ ] X [ ] ",time[i])
           fimpara
      fimpara
fimalgoritmo