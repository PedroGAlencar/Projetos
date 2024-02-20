programa_usuario = list()
alunos = {'Aluno' : '','Idade' : '','notas' :({'Ciências' : '','Matemática' : '','História' : ''}) }
for _ in range(1):
    cadastrar_aluno = input('Você quer cadastrar um aluno?Digite S pra sim e N pra não:')
    while True:
        if cadastrar_aluno.lower() == 's':
            alunos['Aluno'] = input('Digite o nome do aluno:')
            alunos['Idade'] =int(input('Digite a idade do aluno:'))
            alunos['notas']['Ciências'] = float(input('Digite sua nota de Ciências:'))
            alunos['notas']['Matemática'] =float(input('Digite sua nota de Matemática:'))
            alunos['notas']['História'] =float(input('Digite sua nota de História:'))
            programa_usuario.append(alunos.copy())
            continuar = input('Deseja continuar?S/N:')
            if continuar.lower() == 's':
                continue
            else:
                for c in programa_usuario:
                    for k,i in c.items():
                        print(f'{k}:{i}')
            break
        else:
            break
