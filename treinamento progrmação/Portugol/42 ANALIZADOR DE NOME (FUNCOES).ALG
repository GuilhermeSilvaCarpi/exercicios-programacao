algoritmo "42 analizador de nome (funcoes)"
var
   n : caracter
   c : inteiro
inicio
   escreva("digite seu nome ")
   leia(n)
   escreval("total de letras do seu nome:",compr(n))
   escreval("seu nome em maiusculas é: ",maiusc(n))
   escreval("seu nome em mainusculas é: ",minusc(n))
   escreval("a primeira letra do seu nome é: ",maiusc(copia(n,1,1)))
   escreval("a ultima letra do seu nome é: ", maiusc(copia(n, compr(n), 1)))
   escreval("tem a letra A na posição:",pos("A",maiusc(n)))
   escreval("o código da letra A é:",asc("A"))
   escreval("a letra de código 65 é: ",carac(65))
   escreva("seu nome de trás pra frente é: ")
   
   para c <- 0 ate (compr(n)-1) faca
        escreva(copia(n,compr(n)-c,1))
   fimpara
   
fimalgoritmo