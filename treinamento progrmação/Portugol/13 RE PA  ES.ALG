algoritmo "re pa"
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
      escolha d
              caso 0
                   s <- "empate"
              caso 1, 2, 3
                   s <- "partida normal"
              outrocaso
                   s <- "goleada"
      fimescolha
      //
      escreval("diferença: ",d)
      escreval("status: ",s)
fimalgoritmo