algoritmo "31 etre 0 e 10"
var
   vezes, valor, entre, quantidade, SImpares : inteiro
inicio
   escreva("quantos valores digitar? ")
   leia(quantidade)

   para vezes <- 1 ate quantidade faca
      escreva("digite um valor: ")
      leia(valor)
      se (valor >= 0) e (valor <= 10) entao
         entre <- entre + 1
         //se (valor % 2 <> 0) entao
         //SImpares <- SImpares + valor
         //fimse
      fimse

      //se (valor % 2 <> 0) entao
      //   SImpares <- SImpares + valor
      //fimse
   fimpara

      escreval("a soma dos impares é:",SImpares)
      escreva("a quantidade de valores entre 0 e 10 é:",entre)

fimalgoritmo