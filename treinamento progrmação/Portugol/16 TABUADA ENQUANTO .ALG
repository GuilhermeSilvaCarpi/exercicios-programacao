algoritmo "tabuada enquanto 22"
var
   n1, n2, n3: inteiro
inicio
      escreva("a tabuada de qual numero? ")
      leia(n1)
      n2 <- 1
      n3 <- n1
      enquanto n2 <= 10 faca
               escreval(n1, " x ", n2, " = ", n3)
               n2 <- n2 + 1
               n3 <- n1 * n2
      fimenquanto
fimalgoritmo