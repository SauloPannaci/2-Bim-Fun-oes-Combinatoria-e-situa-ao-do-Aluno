""" O Professor deseja dividir uma turma com N alunos em 2 grupos:
um com M e outro com (N-M) alunos. 
Faça um programa que  lê o valor de N E M e informa o numero de combinaçoes
posiveis - Numero de combinaçoes é igaul a N!/M! * (N-M)!)
- Use funcoes para nao gerar repetiçao de codigo."""
 

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
def calcular_combinacoes(n, m):
    if n < m:
        return 0
    return fatorial(n) / (fatorial(m) * fatorial(n - m))

n = int(input("Digite o valor de N (número total de alunos): "))
m = int(input("Digite o valor de M (número de alunos em um dos grupos): "))

combinacoes = calcular_combinacoes(n, m)

print(f"O número de combinações possíveis é: {combinacoes:.0f}")