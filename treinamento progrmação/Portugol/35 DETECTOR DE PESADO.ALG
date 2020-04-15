algoritmo "35 detector de pesado"
var
   i : inteiro
   n, pesado : caractere
   p, mais_pesado : real
procedimento topo()
inicio
      limpatela
      escreval("-------------------------------------")
      escreval(" D E T E C T O R  D E  P E S A D O ")
      escreval(" maior peso até agora",mais_pesado,"KG")
      escreval("-------------------------------------")
fimprocedimento
inicio
      topo()
      para i <- 1 ate 5 faca
           escreva("Digite o nome: ")
           leia(n)
           escreva("Digite o peso de ",n," Kg")
           leia(p)
           
           se (p > mais_pesado) entao
              mais_pesado <- p
              pesado <- n
           fimse
           topo()
      fimpara
      limpatela
      topo()
      escreval("a pessoa mais pesada foi ",pesado,", com",mais_pesado," quilos")
fimalgoritmo