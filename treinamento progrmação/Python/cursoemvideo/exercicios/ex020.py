#aula 08
from random import shuffle
aln1 = str(input('aluno(a)1: '))
aln2 = str(input('aluno(a)2: '))
aln3 = str(input('aluno(a)3: '))
aln4 = str(input('aluno(a)4: '))

alunos = [aln1, aln2, aln3, aln4]
shuffle(alunos)

print('a ordem dos alunos que vão apresentar o trabalho é: \n{}'
	.format(alunos))
