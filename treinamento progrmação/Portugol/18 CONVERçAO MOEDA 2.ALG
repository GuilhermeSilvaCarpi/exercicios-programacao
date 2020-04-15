algoritmo "converçao moeda 2"
var
   vezes, quantidade : inteiro
   reais, dolares : real
inicio
      vezes <- 0
      escreva("quantas vezes converter? ")
      leia(quantidade)
      escreval("------------------------------")
      enquanto vezes < quantidade faca
              escreva("Quantos reais eu tenho? R$")
              leia(reais)
              dolares <- reais * 4.20
              escreval("Eu posso ter U$",dolares:9:2)
              escreval("------------------------------")
              vezes <- vezes + 1
      fimenquanto
fimalgoritmo