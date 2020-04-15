algoritmo "41 cronometro (para)"
var
   semanas, dias, h, m, s, c : inteiro
   verdade : logico
inicio
   verdade <- verdadeiro
   enquanto verdade faca
      para semanas <- 0 ate 3 faca
         para dias <- 0 ate 7 faca
            para h <- 0 ate 23 faca
               para m <- 0 ate 59 faca
                  para s <- 0 ate 59 faca
                     para c <- 0 ate 59 faca
                        //escreval("s:",semanas," d:",dias," h:",h," m:",m," s:",s," c:",c)
                        escreval(semanas," :",dias," :",h," :",m," :",s," :",c)
                     fimpara
                  fimpara
               fimpara
            fimpara
         fimpara
      fimpara
   fimenquanto
fimalgoritmo