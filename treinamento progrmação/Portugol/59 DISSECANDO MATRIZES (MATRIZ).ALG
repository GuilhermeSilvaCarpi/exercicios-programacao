algoritmo "59 dissecando matrizes (matriz)"
var
   m : vetor[1..4, 1..4] de inteiro
   l, c, escol :inteiro
   a : caracter
inicio
      para l de 1 ate 4 faca
           para c de 1 ate 4 faca
                escreva("Digite valor para a posição[",l,",",c,"] ")
                leia(m[l,c])
           fimpara
      fimpara
      limpatela
      //
      repita
         escreval("     MENU DE OPÇÕES")
         escreval("=======================")
         escreval("[1] Mostrar a matriz")
         escreval("[2] Diagonal principal")
         escreval("[3] Triangulo superior")
         escreval("[4] Trinangulo inferior")
         escreval("[5] Sair")
         escreval("=======================")
         leia(escol)
         escolha escol
                 //[1] Mostrar a matriz
                 caso 1
                      limpatela
                      para l de 1 ate 4 faca
                          para c de 1 ate 4 faca
                               escreva("[",m[l,c]," ]":8)
                          fimpara
                          escreval("")
                      fimpara
                      escreval("Digite qualquer coisa para continuar")
                      leia(a)
                      limpatela
                 //[2] Diagonal principal
                 caso 2
                      limpatela
                      para l de 1 ate 4 faca
                           para c de 1 ate 4 faca
                                se l = c entao
                                   escreva("[",m[l,c]," ]":5)
                                senao
                                     escreva("[ - ]":8)
                                fimse
                           fimpara
                           escreval("")
                      fimpara
                      escreval("Digite qualquer coisa para continuar")
                      leia(a)
                      limpatela
                 //[3] Triangulo superior
                 caso 3
                      limpatela
                      para l de 1 ate 4 faca
                           para c de 1 ate 4 faca
                                se (c > l) entao
                                  escreva("[",m[l,c]," ]":5)
                                senao
                                     escreva("[ - ]":8)
                                fimse
                           fimpara
                           escreval("")
                      fimpara
                      escreval("Digite qualquer coisa para continuar")
                      leia(a)
                      limpatela
                 //[4] Trinangulo inferior
                 caso 4
                      limpatela
                      para l de 1 ate 4 faca
                           para c de 1 ate 4 faca
                                se (c < l) entao
                                   escreva("[",m[l,c]," ]":5)
                                senao
                                     escreva("[ - ]":8)
                                fimse
                           fimpara
                           escreval("")
                      fimpara
                      escreval("Digite qualquer coisa para continuar")
                      leia(a)
                      limpatela
                 //
                 outrocaso
                          escol <- 5
         fimescolha
      ate escol = 5
fimalgoritmo