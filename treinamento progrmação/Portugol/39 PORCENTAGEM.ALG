algoritmo "39 porcentagem"
var
   Valor, ValorAlt : real
//
funcao porcentagem(a, b: real) : real
inicio
      retorne (Valor/100)*ValorAlt
fimfuncao
//
inicio
      escreva("digite o valor original: ")
      leia(Valor)
      escreva(" verificar quanto %")
      leia(ValorAlt)
      escreva(ValorAlt,"% de",Valor," � =",porcentagem(Valor, ValorAlt))
fimalgoritmo