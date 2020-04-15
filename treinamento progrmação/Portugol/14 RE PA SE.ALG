algoritmo "re pa SE"
var
   gr, gp, d : inteiro
   s :caracter
inicio
      escreva("quantos gols do remo? ")
      leia(gr)
      escreva("quantos gols do paysandu? ")
      leia(gp)
      d <- abs(gr - gp)
      escreval("------")
      //
      se (d = 0) entao
         s <- "empate"
      senao
           se (d >= 1) e (d <= 3) entao
              s <- "partida normal"
           senao
                s <- "goleada"
           fimse
      fimse
      escreval("diferença: ",d)
      escreval("status: ",s)
fimalgoritmo