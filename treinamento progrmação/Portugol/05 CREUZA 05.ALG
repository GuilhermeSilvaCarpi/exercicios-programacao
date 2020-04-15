algoritmo "creuza 05"
var
   emprestimo, juros, parcela : real
inicio
      escreva("qual o valor do empréstimo? ")
      leia(emprestimo)
      juros <- (emprestimo / 100) * 120
      escreva("quantas parcelas? ")
      leia(parcela)
      escreva("vou pagar",parcela, " parcelas de R$",juros / parcela)
fimalgoritmo