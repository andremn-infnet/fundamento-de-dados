banco_tarefas = [
    {
        "id": 1, 
        "descricao": "Limpar a casa", 
        "urgencia": "Alta", 
        "status": "Concluída"
    },
    {
        "id": 2, 
        "descricao": "Levar o cachorro para passear", 
        "urgencia": "Alta", 
        "status": "Pendente"
    },
    {
        "id": 3, 
        "descricao": "Fazer o café", 
        "urgencia": "Média", 
        "status": "Pendente"
    },
    {
        "id": 4, 
        "descricao": "Fazer o almoço", 
        "urgencia": "Alta", 
        "status": "Pendente"
    },
    {
        "id": 5, 
        "descricao": "Calcular Imposto de Renda", 
        "urgencia": "Normal", 
        "status": "Pendente",
        "categoria": "IRPF"
    },
    {
        "id": 6, 
        "descricao": "Codar em produção", 
        "urgencia": "Normal", 
        "status": "Pendente"
    },
    {
        "id": 7, 
        "descricao": "Responder os amigos nas redes sociais", 
        "urgencia": "Baixa", 
        "status": "Pendente"
    }
]

contador_id = len(banco_tarefas) + 1


def adicionar_tarefa(lista: list, descricao: str, urgencia: str = "Normal", **metadados) -> bool:
    """Adiciona uma nova tarefa ao sistema.

    Argumentos posicionais:
        lista (list): A lista onde a tarefa será salva.
        descricao (str): O que precisa ser feito.

    Parâmetro padrão (Default):
        urgencia (str): 'Alta', 'Normal' ou 'Baixa'. O padrão é 'Normal'.

    Parâmetros por palavra-chave (Kwargs):
        **metadados: Qualquer informação extra.

    Retorno:
        bool: True se a tarefa foi adicionada com sucesso.
    """
    global contador_id

    nova_tarefa = {
        "id": contador_id,
        "descricao": descricao,
        "urgencia": urgencia,
        "status": "Pendente",
    }

    nova_tarefa.update(metadados)

    lista.append(nova_tarefa)
    contador_id += 1
    return True


def listar_tarefas(lista: list) -> None:
    """Percorre e exibe na tela todas as tarefas cadastradas de forma enumerada.

    Argumentos:
        lista (list): A lista de tarefas a ser lida.
    """
    if not lista:
        print("\nNenhuma tarefa cadastrada no momento.")
        return

    print("\nLISTA DE TAREFAS\n")
    for indice, tarefa in enumerate(lista, start=1):
        info = f"{indice}. [Id:{tarefa['id']}] {tarefa['descricao']} ; Urgência: {tarefa['urgencia']} ; Status: {tarefa['status']}"

        extras = [f"{k.capitalize()}: {v}" for k, v in tarefa.items() if k not in ["id", "descricao", "urgencia", "status"]]
        if extras:
            info += f" ; {' ; '.join(extras)}"

        print(info)


def marcar_concluida(lista: list, id_tarefa: int) -> bool:
    """Busca uma tarefa pelo ID e altera seu status para 'Concluída'.

    Argumentos:
        lista (list): A lista onde a busca será feita.
        id_tarefa (int): O identificador único da tarefa.

    Retorno:
        bool: True se encontrou e concluiu, False caso o ID não exista.
    """
    for tarefa in lista:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = "Concluída"
            return True
    return False


def remover_tarefa(lista: list, id_tarefa: int) -> bool:
    """Remove uma tarefa do sistema através do seu ID único.

    Argumentos:
        lista (list): A lista de onde a tarefa será deletada.
        id_tarefa (int): O identificador único da tarefa.

    Retorno:
        bool: True se a tarefa foi removida, False se não foi encontrada.
    """
    for tarefa in lista:
        if tarefa["id"] == id_tarefa:
            lista.remove(tarefa)
            return True
    return False


while True:
    print("\nSISTEMA DE GESTÃO DE TAREFAS\n")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar como Concluída")
    print("4 - Remover Tarefa")
    print("0 - Sair do Sistema")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        desc = input("Digite a descrição da tarefa: ")
        urg = input("Urgência (Alta/Normal/Baixa) [Aperte Enter para Normal]: ")

        if urg.strip() == "":
            adicionar_tarefa(banco_tarefas, descricao=desc)
        else:
            adicionar_tarefa(banco_tarefas, descricao=desc, urgencia=urg)
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        listar_tarefas(banco_tarefas)

    elif opcao == "3":
        listar_tarefas(banco_tarefas)
        if banco_tarefas:
            id_alvo = int(input("\nDigite o ID da tarefa que deseja concluir: "))
            sucesso = marcar_concluida(banco_tarefas, id_tarefa=id_alvo)
            if sucesso:
                print("Tarefa atualizada para Concluída!")
            else:
                print("ID não encontrado.")

    elif opcao == "4":
        listar_tarefas(banco_tarefas)
        if banco_tarefas:
            id_alvo = int(input("\nDigite o ID da tarefa que deseja REMOVER: "))
            sucesso = remover_tarefa(banco_tarefas, id_tarefa=id_alvo)
            if sucesso:
                print("Tarefa removida do sistema.")
            else:
                print("ID não encontrado.")

    elif opcao == "0":
        print("\nSistema Finalizado")
        break

    else:
        print("Opção inválida. Tente novamente.")
