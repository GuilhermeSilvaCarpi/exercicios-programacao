algoritmo "tirar carteira"
var
   nasc, atual, idade : inteiro
inicio
      escreva("ano atual: ")
      leia(atual)
      escreva("ano de nascimento: ")
      leia(nasc)
      idade <- atual - nasc
      escreval("idade:",idade)
      se (idade >=18) entao
         escreva("apto a tirar carteira")
      senao
         escreva("inapto a tirar carteira")
      fimse
fimalgoritmo