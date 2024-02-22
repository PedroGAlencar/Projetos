programa_usuario = list()
alunos = {'Aluno' : '','Idade' : '','notas' :({'Ciências' : '','Matemática' : '','História' : ''}) }
medias = list()
for _ in range(1):
    cadastrar_aluno = input('Você quer cadastrar um aluno?Digite S pra sim e N pra não:')
    while True:
        if cadastrar_aluno.lower() == 's':
            # alunos['Aluno'] = input('Digite o nome do aluno:')
            # alunos['Idade'] =int(input('Digite a idade do aluno:'))
            # alunos['notas']['Ciências'] = float(input('Digite sua nota de Ciências:'))
            # alunos['notas']['Matemática'] =float(input('Digite sua nota de Matemática:'))
            # alunos['notas']['História'] =float(input('Digite sua nota de História:'))
            # alunos['notas']['Média'] = (alunos['notas']['Ciências'] + alunos['notas']['História'] + alunos['notas']['Matemática']) / 3
            # programa_usuario.append(alunos.copy())

            aluno_nome = input('Digite o nome do aluno:')
            aluno_idade =int(input('Digite a idade do aluno:'))
            aluno_nota_ciencia = float(input('Digite sua nota de Ciências:'))
            aluno_nota_matematica =float(input('Digite sua nota de Matemática:'))
            aluno_nota_historia =float(input('Digite sua nota de História:'))
            aluno = {'Aluno' : aluno_nome,'Idade' : aluno_idade,'notas' :({'Ciências' : aluno_nota_ciencia,'Matemática' : aluno_nota_matematica,'História' : aluno_nota_historia}) }
            programa_usuario.append(aluno)

            continuar = input('Deseja continuar?S/N:')
            if continuar.lower() == 's':
                continue
            else:
                for usuario in programa_usuario:
                    usuario_media = (usuario['notas']['Ciências'] + usuario['notas']['Matemática'] + usuario['notas']['História']) / 3
                    medias.append({'Aluno':usuario['Aluno'],'Média' : usuario_media})
                for c in programa_usuario:
                    for k,i in c.items():
                        print(f'{k}:{i}')
                print(medias)
                maior = 0
                for media in medias:
                    if media['Média'] > maior:
                        maior = media['Média']

                for media in medias:
                    if media['Média'] == maior:
                        print(f'Nome é {media['Aluno']} e a media {media['Média']}')
                        break
        else:
            break
