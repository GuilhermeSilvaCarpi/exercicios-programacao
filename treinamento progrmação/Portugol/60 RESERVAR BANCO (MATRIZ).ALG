algoritmo "52 reservar banco (vetor) [aprimorar]"
var
   reservado : vetor[1..10] de logico
   resposta : caracter
   i, a : inteiro
inicio
      repita
           para i de 1 ate 10 faca
                se (reservado[i]) entao
                   escreva("[ --- ]")
                senao
                  escreva("[ B",i," ]")
                fimse
           fimpara
           escreval("")
           para i de 1 ate 10 faca
                escreva("-------")
           fimpara
           escreval("")
      
           escreva("Reservar qual banco? ")
           leia(a)
           se (reservado[a]) entao
              escreval("O ACENTO JÁ FOI RESERVADO")
           senao
                reservado[a] <- verdadeiro
                escreval("Acento",a," RESERVADO")
           fimse
           
           escreval("Quer reservar outro? [S/N]")
           leia(resposta)
           limpatela
      ate maiusc(resposta) = "N"
fimalgoritmo