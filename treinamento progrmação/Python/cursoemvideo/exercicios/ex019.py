#aula 08
from random import choice

aln1 = input('aluno(a)1: ')
aln2 = input('aluno(a)2: ')
aln3 = input('aluno(a)3: ')
aln4 = input('aluno(a)4: ')

alunos = [aln1, aln2, aln3, aln4]
alnParaApagarQuadro = choice(alunos)
print('{} foi escolhida(o) para apagar o quadro'.format(alnParaApagarQuadro))
