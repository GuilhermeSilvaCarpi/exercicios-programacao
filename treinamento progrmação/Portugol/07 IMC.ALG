algoritmo "imc"
var
   m, a, imc : real
inicio
      escreva("Massa (kg): ")
      leia(m)
      escreva("Altura (m): ")
      leia(a)
      imc <- m / a^2
      escreval("IMC :", imc:6:2)
      se (imc >= 18.5) e (imc < 25) entao
         escreva("você está no peso ideal")
      senao
           escreva("você não está no peso ideal")
      fimse
fimalgoritmo