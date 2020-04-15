algoritmo "34 analizador de valores"
var
   c, vezes, valor, soma, div_p5, nulos, s_pares : inteiro
   media : real
inicio
      vezes <- 5
      para c <- 1 ate vezes faca
           escreva("Digite um valor: ")
           leia(valor)
           //soma
           soma <- soma + valor
           //quantos são divisiveis por 5
           se (valor % 5 = 0) entao
              div_p5 <- div_p5 + 1
           fimse
           //quantos são nulos
           se (valor = 0) entao
              nulos <- nulos + 1
           fimse
           //soma dos pares
           se (valor % 2 = 0) entao
              s_pares <- s_pares + valor
           fimse
      fimpara
      media <- soma / vezes
      escreval("---------------------------------------")
      escreval("a soma entre os valores é:",soma)
      escreval("a média entre os valores é:",media:6:2)
      escreval("valores divisiveis por 5:",div_p5)
      escreval("valores nulos:",nulos)
      escreval("a soma dos valores pares é:",s_pares)
fimalgoritmo