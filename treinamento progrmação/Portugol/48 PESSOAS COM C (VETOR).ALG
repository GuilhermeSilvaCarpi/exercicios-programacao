algoritmo "48 pessoas com c (vetor)"
var
   nome : caracter
   soc : vetor[1..5] de caracter
   i, i2 : inteiro
inicio
      para i <- 1 ate 5 faca
           escreva("Digite um nome: ")
           leia(nome)
           se (copia(nome,1,1) = "C") entao
              i2 <- i2 + 1
              soc[i2] <- nome
           fimse
      fimpara
      limpatela
      
      escreval("PAESSOAS Q COMEÇA COM C:",i2)
      para i <- 1 ate i2 faca
           escreval(soc[i])
      fimpara
fimalgoritmo