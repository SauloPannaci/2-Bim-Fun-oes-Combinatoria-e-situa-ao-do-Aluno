"""faça uma função que informe o status do aluno a partir da sua media de
 acordo com a tabela a seguir: - nota acima de 6 --> "APROVADO"
 nota entre 4 e 6 --> "VERIFICAÇAO SUPLEMENTAR"  
 nota abaixo de 4 --> "REPROVADO" """


def status_do_aluno(media):
    if media > 6:
        return "APROVADO"
    elif 4 <= media <= 6:
        return "VERIFICAÇÃO SUPLEMENTAR"
    else:
        return "REPROVADO"

media_aluno = float(input("Digite a média do aluno: "))
status = status_do_aluno(media_aluno)
print(f"Status do aluno: {status}")