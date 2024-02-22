import time

lista_de_tarefas = list()
tarefa = dict()
lista_categorias = ['Serviço de casa','Trabalho','Procrastinar','Estudo']

def cadastrar_tarefa():
    tarefa['id'] = input('Digite o ID da tarefa:')
    tarefa['Nome']= input('Digite o nome da tarefa:')
    print(lista_categorias) 
    tarefa['Categoria'] = input('Digite a categoria:')
    tarefa['Concluída'] = bool(input('Digite False ou True se ja concluiu a tarefa:'))
    lista_de_tarefas.append(tarefa.copy())


def excluir_tarefa():
    id = input('Informe o ID da tarefa que você precisa excluir:')
    for tarefa in lista_de_tarefas:
        if id == tarefa['id']:
            lista_de_tarefas.remove(tarefa)
            print(f'A tarefa {tarefa['Nome']} foi removida do id {id}')
            break
        else:
            print('ID inválido!!')
    

def listar_tarefas():
    if lista_de_tarefas:
        for k,v in tarefa:
            print(f'{k}:{v}')
    


while True:
    print('Sistema iniciando...')
    time.sleep(1)
    menu = int(input('''Escolha a opção desejada:
                     (1) Cadastrar uma nova tarefa
                     (2) Listar Tarefas
                     (3)Excluir tarefa
                     (0 )Sair do sistema
                      :'''))
    if menu == 1:
        cadastrar_tarefa()
    elif menu == 2:
        listar_tarefas()
    elif menu == 3:
        excluir_tarefa()
    elif menu == 0:
        print('Finalizando seu sistema...')
        time.sleep(0.5)
        print('Fim do sistema!')
        break
    else:
        print('Opção inválida!Informe novamente')
        continue