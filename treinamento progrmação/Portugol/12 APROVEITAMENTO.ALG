algoritmo "aproveitamento"
var
   n1, n2, m : real
   aprov : caracter
inicio
      escreva("primeira nota: ")
      leia(n1)
      escreva("segunda nota: ")
      leia(n2)
      m <- (n1 + n2)/2
      escreval("media: ",m:4:1)
      //
      se (m >= 9) entao
         aprov <- "a"
      senao
           se (m >= 8) e (m <9) entao
              aprov <- "b"
           senao
                se (m >=7) e (m<8) entao
                   aprov <- "c"
                senao
                     se (m >=6) e (m <7) entao
                        aprov <- "d"
                     senao
                          aprov <- "f"
                     fimse
                fimse
           fimse
      fimse
      //
      escreva("aproveitamento: ",aprov)
fimalgoritmo