programa_usuario = list()
alunos = {'Aluno' : '','Idade' : '','notas' :({'Ciências' : '','Matemática' : '','História' : ''}) }
notas = dict(alunos['notas'])
del(alunos)['notas']
media = list()
for _ in range(1):
    cadastrar_aluno = input('Você quer cadastrar um aluno?Digite S pra sim e N pra não:')
    while True:
        if cadastrar_aluno.lower() == 's':
            alunos['Aluno'] = input('Digite o nome do aluno:')
            alunos['Idade'] =int(input('Digite a idade do aluno:'))
            notas['Ciências'] = float(input('Digite sua nota de Ciências:'))
            notas['Matemática'] =float(input('Digite sua nota de Matemática:'))
            notas['História'] =float(input('Digite sua nota de História:'))
            notas['Média'] = (notas['Ciências'] + notas['História'] + notas['Matemática']) / 3
            programa_usuario.append(alunos.copy())
            programa_usuario.append(notas.copy())
            media.append(notas.copy()['Média'])
            continuar = input('Deseja continuar?S/N:')
            if continuar.lower() == 's':
                continue
            else:
                print(programa_usuario)
                melhor_media = max(media)
                for c in programa_usuario:
                    for k,i in c.items():
                        print(f'{k}:{i}')
                print(media)
                print(f'A maior média é {melhor_media}')
            break
        else:
            break
