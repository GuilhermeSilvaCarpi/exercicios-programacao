algoritmo "24 quantos negativos"
var
   r, n, menor: inteiro
inicio
      repita
            r <- r + 1
            escreva("digite um numero: ")
            leia(n)
            
            se n < 0 entao
               menor <- menor + 1
            fimse
            
      ate r = 4
      
      escolha menor
             caso 0
                  escreva("n�o h� numeros negativos")
             caso 1
                  escreva("h� um numero negativo")
             outrocaso
                  escreva("h�",menor," numeros negativos")
      fimescolha
fimalgoritmo