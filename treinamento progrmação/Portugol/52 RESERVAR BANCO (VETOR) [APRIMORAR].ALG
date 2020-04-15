algoritmo "52.2 reservar banco (matriz) [aprimorado]"
var
   reservado : vetor[1..3, 1..9] de logico
   exist : logico
   resposta, letra, a : caracter
   i1, i2, a1, a2: inteiro
procedimento bancos()//procedimento
inicio
   para i1 de 1 ate 3 faca
        //letra fileira
        escolha i1
        caso 1
             letra <- "A"
        caso 2
             letra <- "B"
        caso 3
             letra <- "C"
        fimescolha
        //numero fileira
        para i2 de 1 ate 9 faca
             se (reservado[i1, i2]) entao
                escreva("[ --- ]")
             senao
                  escreva("[ ",letra,i2," ]")
             fimse
        fimpara
        escreval("")
   fimpara
   //grande linha
   para i1  de 1 ate 9 faca
        escreva("-------")
   fimpara
   escreval("")
fimprocedimento
inicio//algoritmo
      repita
            exist <- verdadeiro
            bancos()
           //reserva
           escreva("Reservar qual fileira? ")
           leia(a)
           
           escolha maiusc(a)
                  caso "A"
                       a1 <- 1
                  caso "B"
                       a1 <- 2
                  caso "C"
                       a1 <- 3
                  outrocaso
                  exist <- falso
           fimescolha

           se exist entao
              escreva("Reservar qual acento? ")
              leia(a2)
              se (reservado[a1,a2]) entao
                 limpatela
                 bancos()
                 escreval("O ACENTO JÁ FOI RESERVADO")
              senao
                   reservado[a1,a2] <- verdadeiro
                   limpatela
                   bancos()
                   escreval("Acento",a," RESERVADO")
              fimse
           senao
                limpatela
                bancos()
                escreval("ESSA FILEIRA NÃO EXISTE!")
           fimse

           escreval("Quer reservar outro? [S/N]")
           leia(resposta)
           limpatela
      ate maiusc(resposta) = "N"
fimalgoritmo