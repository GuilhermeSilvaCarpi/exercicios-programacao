algoritmo "SELETOR DE PESSOAS"
var
   idade, cor, h, m : inteiro
   genero, continuar: caracter
inicio
      repita
            escreval("=======================")
            escreval("  SELETOR DE PESSOAS   ")
            escreval("=======================")
            escreva("Qual o Sexo? [f/m] ")
            leia(genero)
            escreva("Qual é a idade? ")
            leia(idade)
            escreval("qual a cor do cabelo? ")
            escreval("=======================")
            escreval("[1] preto")
            escreval("[2] castanho")
            escreval("[3] loiro")
            escreval("[4] ruivo")
            leia(cor)
            escreva("quer continuar? [s/n] ")
            leia(continuar)
            
            se genero = "m" entao
               se idade > 18 entao
                  se cor =2 entao
                     h <- h + 1
                  fimse
               fimse
            senao
                 se (idade > 25) e (idade < 30) entao
                    se cor = 3 entao
                       m <- m + 1
                    fimse
                 fimse
            fimse
            
            limpatela
      ate continuar = "n"
      
      escreval("------------------------------------------------------")
      escreval(" RESULTADO FINAL")
      escreval("------------------------------------------------------")
      escreval("total de homen com mais de 18 e cabelos castanhos:", h)
      escreval("total de mulheres entre 25 e 30 e cabelos loiros:", m)
      
fimalgoritmo