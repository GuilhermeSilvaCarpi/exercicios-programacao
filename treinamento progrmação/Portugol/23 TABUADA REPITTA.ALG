algoritmo "23 tabuada repitta"
var
   n1, multi, resultado : inteiro
inicio
      Escreva("a tabuada de que numero? ")
      leia (n1)
      
      repita
            multi <- multi + 1
            resultado <- n1 * multi
            escreval(n1, " x ", multi, " = ", resultado)
      ate multi = 10
fimalgoritmo