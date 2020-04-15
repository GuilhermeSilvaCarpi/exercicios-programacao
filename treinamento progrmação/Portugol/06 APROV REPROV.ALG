algoritmo "aprov reprov"
var
   m, n1, n2 : real
inicio
      escreva("primeira nota: ")
      leia(n1)
      escreva("segunda nota: ")
      leia(n2)
      m<- (n1 + n2)/2
      escreval("media:",m)
      se (m >= 7) entao
         escreva("aluno aprovado")
      senao
         escreva("aluno reprovado")
      fimse
fimalgoritmo