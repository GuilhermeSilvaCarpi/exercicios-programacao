algoritmo "escolha"
var
   nome : caracter
   sal, nsal  : real
   dep  : inteiro
inicio
      escreva("qual o nome do funcionario? ")
      leia(nome)
      escreva("qual p salario do funcionario? R$")
      leia(sal)
      escreva("qual a quantidade de dependentes? ")
      leia(dep)
      escolha dep
             caso 0
                  nsal <- sal + (sal/100*5)
             caso 1, 2, 3
                  nsal <- sal + (sal/100*10)
             caso 4, 5, 6
                  nsal <- sal + (sal/100*15)
             outrocaso
                      nsal <- sal + (sal/100*18)
      fimescolha
      escreva(nsal)
fimalgoritmo