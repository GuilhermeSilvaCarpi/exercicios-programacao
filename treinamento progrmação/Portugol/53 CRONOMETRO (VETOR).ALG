algoritmo "53 cronometro (vetor)"
var
   n: vetor[1..6] de inteiro
   verdade : logico
inicio
   verdade <- verdadeiro
   enquanto verdade faca
      para n[1] <- 0 ate 3 faca
         para n[2] <- 0 ate 7 faca
            para n[3] <- 0 ate 23 faca
               para n[4] <- 0 ate 59 faca
                  para n[5] <- 0 ate 59 faca
                     para n[6] <- 0 ate 59 faca
                        //escreval("s:",semanas," d:",dias," h:",h," m:",m," s:",s," c:",c)
                        escreval(n[1]," :",n[2]," :",n[3]," :",n[4]," :",n[5]," :",n[6])
                     fimpara
                  fimpara
               fimpara
            fimpara
         fimpara
      fimpara
   fimenquanto
fimalgoritmo