algoritmo "aprov reprov 2"
var
   n1, n2, m : real
inicio
      escreva("primeira nota: ")
      leia(n1)
      escreva("segunda nota: ")
      leia(n2)
      m <- (n1 + n2)/2
      escreval("media: ",m:4:2)
      se (m >= 7) entao
         escreval("aprovado")
      senao
           se (m >= 5) e (m < 7) entao
              escreval("recuperaçao")
           senao
              escreval("reprovado")
           fimse
      fimse
fimalgoritmo