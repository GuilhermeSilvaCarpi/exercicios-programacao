algoritmo "21 cronometro"
var
   ativado : logico
   h, m, s : inteiro
inicio
   ativado <- verdadeiro
   enquanto ativado faca
      s <- s + 1
      se s >= 60 entao
         s <- 0
         m <- m + 1
         se m >= 60 entao
            m <- 0
            h <- h + 1
         fimse
      fimse
      
      escreval(h," :",m," :",s)
   fimenquanto
fimalgoritmo