algoritmo "42 analizador de nome (funcoes)"
var
   n : caracter
   c : inteiro
inicio
   escreva("digite seu nome ")
   leia(n)
   escreval("total de letras do seu nome:",compr(n))
   escreval("seu nome em maiusculas �: ",maiusc(n))
   escreval("seu nome em mainusculas �: ",minusc(n))
   escreval("a primeira letra do seu nome �: ",maiusc(copia(n,1,1)))
   escreval("a ultima letra do seu nome �: ", maiusc(copia(n, compr(n), 1)))
   escreval("tem a letra A na posi��o:",pos("A",maiusc(n)))
   escreval("o c�digo da letra A �:",asc("A"))
   escreval("a letra de c�digo 65 �: ",carac(65))
   escreva("seu nome de tr�s pra frente �: ")
   
   para c <- 0 ate (compr(n)-1) faca
        escreva(copia(n,compr(n)-c,1))
   fimpara
   
fimalgoritmo