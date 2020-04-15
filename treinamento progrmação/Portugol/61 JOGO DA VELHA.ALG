algoritmo "61 jogo da velha"
var
   i, i2, i3, i4, a, pv: inteiro //pv = posicao_de_vitoria
   posicao : vetor[1..9] de inteiro
   ocupado : vetor[1..9] de logico
   finalizado, a2, vitoria : logico
   vez : caracter
inicio
      repita
           //preparando terreno
           limpatela
           i <- i + 1
           i4 <- 0
           //[X]ou[O]
           se (i % 2 =0) entao
              vez <- "O"
           senao
                vez <- "X"
           fimse
           //grade
            para i2 de 1 ate 7 faca
                 se (i2 % 2 <> 0) entao
                    escreva("+---+---+---+")
                 senao
                      para i3 de 1 ate 3 faca
                           //elemento da posicao
                           i4 <- i4 + 1
                           escolha posicao[i4]
                                  caso 1
                                       escreva("| X ")
                                  caso 2
                                       escreva("| O ")
                                  outrocaso
                                       escreva("|",i4," ")
                           fimescolha
                      fimpara
                      escreva("|")
                 fimse
                 escreval()
            fimpara
            //vitoria
            pv <- 1//pv = posicao_de_vitoria
            para pv de 1 ate 7 passo 3 faca//vitoria horizontal
               se (posicao[pv] <> 0) e (posicao[pv] = posicao[pv + 1]) e (posicao[pv + 1] = posicao[pv + 2]) entao
                  vitoria <- verdadeiro
                  escreva("vitoria digite algo")
                  leia(a)
                  finalizado <- verdadeiro
               fimse
               pv <- pv + 3
            fimpara
            pv <- 1//pv = posicao_de_vitoria
            para pv de 1 ate 3 passo 1 faca//vitoria vertical
               se (posicao[pv] <> 0) e (posicao[pv] = posicao[pv + 3]) e (posicao[pv + 3] = posicao[pv + 6]) entao
                  vitoria <- verdadeiro
                  escreva("vitoria digite algo")
                  leia(a)
                  finalizado <- verdadeiro
               fimse
               pv <- pv + 1
            fimpara
            pv <- 1//pv = posicao_de_vitoria

            //escolha
            se (nao vitoria) entao
               repita
                     a2 <- falso
                     escreval("Vai jogar [",vez,"] em qual posiçao?")
                     leia(a)
                     //jogada invalida
                     se ocupado[a] entao
                        escreval("JOGADA INVALIDA")

                     senao
                          se vez = "X" entao
                             a2 <- verdadeiro
                             ocupado[a] <- verdadeiro
                             posicao[a] <- 1
                          senao
                               a2 <- verdadeiro
                               ocupado[a] <- verdadeiro
                               posicao[a] <- 2
                          fimse
                     fimse
               ate a2
            fimse
      ate finalizado
fimalgoritmo