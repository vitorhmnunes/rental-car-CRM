import datetime
import os
 
class Cliente(): #Class determina atributos de CLIENTE
    cpf = ''
    nome = ''
    endereco = ''
    telefone_fixo = ''
    telefone_celular = ''
    data_nascimento = ''
 
class Veiculo(): #Class determina atributos de VEICULO
    codigo = ''
    descricao = ''
    categoria = ''
    capacidade = ''
    combustivel = ''
    ano = ''
    modelo = ''
 
class Aluguel(): #Class determina atributos de ALUGUEL
    cpf_cliente = ''
    codigo_veiculo = ''
    data_entrada = ''
    data_saida = ''
 
def op_menu_principal(): #Função retorna opção para o menu principal
    print("--------------------")
    print("Clientes...........1")
    print("Veículos...........2")
    print("Aluguéis...........3")
    print("Relatórios.........4")
    print("Salvar e Sair......0")
    op = input('>> ')
    return op
 
def op_submenu(): # Função retorna opção para submenus clientes e veiculos
    print("--------------------")
    print("Listar todos.......1")
    print("Listar apenas um...2")
    print("Incluir............3")
    print("Alterar............4")
    print("Excluir............5")
    print("Menu Principal.....0")
    op = input('>> ')
    return op
 
def op_submenu_alugueis(): # Função retorna opção submenu aluguéis
    print("--------------------")
    print("Listar todos.......1")
    print("Incluir............2")
    print("Alterar............3")
    print("Excluir............4")
    print("Menu Principal.....0")
    op = input('>> ')
    return op
 
def op_submenu_relatorios(): # Função retorna opção submenu relatórios
    print("--------------------")
    print("Listar ALUGUEIS por:")
    print("CPF................1")
    print("Veiculo............2")
    print("Periodo............3")
    print("Menu Principal.....0")
    op = input('>> ')
    return op
 
def buscar_por_criterio(criterio='', lista=[], chave1='', chave2=None):
    '''Busca por criterio recebe criterio de ação, lista e até duas chaves
    e retorna os index dos objetos encontrados'''
    i = 0
    if criterio == 'cpf':
        encontrado = -1
        while i < len(lista) and encontrado == -1:
            if chave1 == lista[i].cpf:
                encontrado = i
            i += 1
        return encontrado
    elif criterio == 'codigo':
        encontrado = -1
        while i < len(lista) and encontrado == -1:
            if chave1 == lista[i].codigo:
                encontrado = i
            i += 1
        return encontrado
    elif criterio == 'clie_em_alugueis':
        encontrado = []
        while i < len(lista):
            if chave1 == lista[i].cpf_cliente:
                encontrado.append(i)
            i += 1
    elif criterio == 'veic_em_alugueis':
        encontrado = []
        while i < len(lista):
            if chave1 == lista[i].codigo_veiculo:
                encontrado.append(i)
            i += 1
    elif criterio == 'data_em_alugueis':
        encontrado = []
        while i < len(lista):
            entrada = lista[i].data_entrada
            saida = lista[i].data_saida
            if (chave1 >= entrada and chave2 <= saida) or (chave1 <= entrada and chave2 >= entrada) or (chave1 <= saida and chave2 >= saida) or (chave1 <= entrada and chave2 >= saida):
                encontrado.append(i)
            i += 1
    return encontrado
 
def existe_arquivo(): #Verificação de existência dos arquivos. Caso não existam serão criados
    if not os.path.exists('clientes.txt'):
        arq = open('clientes.txt', 'w')
        arq.close()
    if not os.path.exists('veiculos.txt'):
        arq = open('veiculos.txt', 'w')
        arq.close()
    if not os.path.exists('alugueis.txt'):
        arq = open('alugueis.txt', 'w')
        arq.close()
 
############################## C L I E N T E S ##############################
 
def imprime_cliente(c): # Função imprime dados do cliente p especificado
    print(" | CPF: " + c.cpf + " | Nome: " + c.nome + " | Endereço: " + c.endereco + " | Tel(fixo): " + c.telefone_fixo + " | Tel(celular): " + c.telefone_celular + " | Data de nascimento: " + c.data_nascimento + " | ")
 
def submenu_clientes(lista_clientes): # Função recebe opção de submenu e chama funções relacionadas a clientes
    sub_op = ''
    while sub_op != '0':
        sub_op = op_submenu()
        if sub_op == '1':
            listar_todos_clientes(lista_clientes)
        elif sub_op == '2':
            listar_cliente(lista_clientes)
        elif sub_op == '3':
            inserir_cliente(lista_clientes)
        elif sub_op == '4':
            alterar_cliente(lista_clientes)
        elif sub_op == '5':
            excluir_cliente(lista_clientes)
        elif sub_op == '0':
            print('Menu Principal')
        else:
            print('Entrada invalida.')
 
def dados_cliente(c): # Função recebe cliente e insere dados da CLass Cliente
    c.nome = input("Informe o nome: ")
    c.endereco = input("Informe o endereço: ")
    c.telefone_fixo = input("Informe o telefone fixo: ")
    c.telefone_celular = input("Informe o telefone celular: ")
    c.data_nascimento = input("Informe a data de nascimento: ")
 
def inserir_cliente(lista_clientes): # Adiciona cliente na lista de clientes registrados
    p = Cliente()
    p.cpf = input("Informe o CPF do cliente: ")
    cpf_index = buscar_por_criterio('cpf',lista_clientes,p.cpf)
    if cpf_index != -1:
        print("CPF já cadastrado!")
    else:
        dados_cliente(p)
        lista_clientes.append(p)
        print("Cliente adicionado com sucesso!!!")
 
def alterar_cliente(lista_clientes): # Busca cliente e altera os atributos do cliente na lista
    cpf = input("Informe o CPF do cliente: ")
    cpf_index = buscar_por_criterio('cpf',lista_clientes,cpf)
    if cpf_index != -1:
        dados_cliente(lista_clientes[cpf_index])
        print("Cliente alterado...")
    else:
        print("Cliente inexistente...")
 
def excluir_cliente(lista_clientes): # Exclui cliente da lista com confirmação
    cpf = input("Informe o CPF do cliente: ")
    cpf_index = buscar_por_criterio('cpf',lista_clientes,cpf)
    if cpf_index != -1:
        confirm = input("Quer mesmo excluir esse registro? Digite 'SIM' ou 'NAO': ").upper()
        if confirm == 'SIM':
            del(lista_clientes[cpf_index])
            print("Cliente deletado...")
        else:
            print("PROCESSO CANCELADO!")
    else:
        print("Cliente inexistente...")
 
def listar_cliente(lista_clientes): # Busca CPF e imprime dados do respectivo cliente
    cpf = input("Informe o CPF do cliente: ")
    cpf_index = buscar_por_criterio('cpf',lista_clientes,cpf)
    if cpf_index != -1:
        imprime_cliente(lista_clientes[cpf_index])
    else:
        print("Cliente não encontrado...")
 
def listar_todos_clientes(lista_clientes): # Roda lista e imprime dados de cada cliente encontrado
    i = 0
    if len(lista_clientes) > 0:
        while i < len(lista_clientes):
            imprime_cliente(lista_clientes[i])
            i += 1
    else:
        print("Não há clientes cadastrados!")
 
def ler_clientes(nome_arquivo, lista_clientes): # Busca clientes em arquivo e os atribui a lista
    arq = open(nome_arquivo, 'r')
    for linha in arq:
        if linha.find(';'):
            dados_cliente = linha.split(';')
            c = Cliente()
            c.cpf = dados_cliente[0]
            c.nome = dados_cliente[1]
            c.endereco = dados_cliente[2]
            c.telefone_fixo = dados_cliente[3]
            c.telefone_celular = dados_cliente[4]
            c.data_de_nascimento = dados_cliente[5]
            lista_clientes.append(c)
    arq.close()
 
def armazenar_clientes(nome_arquivo, lista_clientes): # Salva clientes da lista no arquivo
    arq = open(nome_arquivo, 'w')
    i = 0
    while i < len(lista_clientes):
        c = lista_clientes[i]
        arq.write(str(c.cpf) + ';' + str(c.nome) + ';' + str(c.endereco) + ';' + str(c.telefone_fixo) + ';' + str(c.telefone_celular) +';' + str(c.data_nascimento) + ';' + '\n')
        i += 1
    arq.close()
 
############################## V E I C U L O S ##############################
 
def imprime_veiculo(v): # Função imprime dados do veiculo v especificado
    print(" | CODIGO: " + v.codigo + " | Descrição: " + v.descricao + " | Categoria: " + v.categoria + " | Capacidade: " + v.capacidade + " | Combustivel: " + v.combustivel + " | Ano: " + v.ano + " | Modelo: " + v.modelo + " | ")
 
def submenu_veiculos(lista_veiculos): # Função recebe opção de submenu e chama funções relacionadas a veiculos
    sub_op = ''
    while sub_op !='0':
        sub_op = op_submenu()
        if sub_op == '1':
            listar_todos_veiculos(lista_veiculos)
        elif sub_op == '2':
            listar_veiculo(lista_veiculos)
        elif sub_op == '3':
            inserir_veiculo(lista_veiculos)
        elif sub_op == '4':
            alterar_veiculo(lista_veiculos)
        elif sub_op=='5':
            excluir_veiculo(lista_veiculos)
        elif sub_op=='0':
            print('Menu Principal.')
        else:
            print('Entrada invalida.')
 
def dados_veiculo(v): # Função recebe veiculo e insere dados da CLass Veiculo
    v.descricao = input("Informe a descrição: ")
    v.categoria = input("Informe a categoria: ")
    v.capacidade = input("Informe a capacidade: ")
    v.combustivel = input("Informe o tipo de combustivel: ")
    v.ano = input("Informe o ano: ")
    v.modelo = input("Informe o modelo: ")
 
def inserir_veiculo(lista_veiculos): # Adiciona veiculo na lista de veiculos registrados
    v = Veiculo()
    v.codigo = input("Informe o CÓDIGO do veiculo: ")
    codigo_index = buscar_por_criterio('codigo',lista_veiculos,v.codigo)
    if codigo_index != -1:
        print("CÓDIGO já cadastrado!")
    else:
        dados_veiculo(v)
        lista_veiculos.append(v)
        print("Veículo adicionado com sucesso!!!")
 
def alterar_veiculo(lista_veiculos): # Busca veiculo e altera os atributos do veiculo na lista
    codigo = input("Informe o CÓDIGO do veiculo: ")
    codigo_index = buscar_por_criterio('codigo',lista_veiculos,codigo)
    if codigo_index != -1:
        dados_veiculo(lista_veiculos[codigo_index])
        print("Veiculo alterado no sistema...")
    else:
        print("Veiculo inexistente no sistema...")
 
def excluir_veiculo(lista_veiculos): # Exclui veiculo da lista com confirmação
    codigo = input("Informe o CÓDIGO do veículo: ")
    codigo_index = buscar_por_criterio('codigo',lista_veiculos,codigo)
    if codigo_index != -1:
        confirm = input("Quer mesmo excluir esse registro? Digite 'SIM' ou 'NAO': ").upper()
        if confirm == 'SIM':
            del(lista_veiculos[codigo_index])
            print("Veiculo deletado...")
        else:
            print("PROCESSO CANCELADO!")
    else:
        print("Veiculo inexistente no sistema...")
 
def listar_veiculo(lista_veiculos): # Busca codigo e imprime dados do respectivo veiculo
    codigo = input("Informe o código do veículo: ")
    codigo_index = buscar_por_criterio('codigo',lista_veiculos,codigo)
    if codigo_index != -1:
        imprime_veiculo(lista_veiculos[codigo_index])
    else:
        print("Veículo não encontrado...")
 
def listar_todos_veiculos(lista_veiculos): # Roda lista e imprime dados de cada veiculo encontrado
    i = 0
    if len(lista_veiculos) > 0:
        while i < len(lista_veiculos):
            imprime_veiculo(lista_veiculos[i])
            i += 1
    else:
        print("Sem veículos registrados!")
 
def ler_veiculos(nome_arquivo, lista_veiculos): # Busca veiculos em arquivo e os atribui a lista
    arq = open(nome_arquivo, 'r')
    for linha in arq:
        if linha.find(';'):
            dados_veiculo = linha.split(';')
            v = Veiculo()
            v.codigo = dados_veiculo[0]
            v.descricao = dados_veiculo[1]
            v.categoria = dados_veiculo[2]
            v.capacidade = dados_veiculo[3]
            v.combustivel = dados_veiculo[4]
            v.ano = dados_veiculo[5]
            v.modelo = dados_veiculo[6]
            lista_veiculos.append(v)
    arq.close()
 
def armazenar_veiculos(nome_arquivo, lista_veiculos): # Salva veiculos da lista no arquivo
    arq = open(nome_arquivo, 'w')
    i = 0
    while i < len(lista_veiculos):
        v = lista_veiculos[i]
        arq.write(str(v.codigo) + ';' + str(v.descricao) + ';' + str(v.categoria) + ';' + str(v.capacidade) + ';' + str(v.combustivel) + ';' + str(v.ano) + ';' + str(v.modelo) + ';' + '\n')
        i += 1
    arq.close()
 
############################## A L U G U E I S ##############################
 
def imprime_aluguel(a): # Função imprime dados do aluguel a especificado
    data_ent = (a.data_entrada.strftime('%d') + '/' + a.data_entrada.strftime('%m') + '/' + a.data_entrada.strftime('%G'))
    data_sai = (a.data_saida.strftime('%d') + '/' + a.data_saida.strftime('%m') + '/' + a.data_saida.strftime('%G'))
    print(" | CPF do cliente: " + a.cpf_cliente + " | Codigo do veículo: " + a.codigo_veiculo + " | Data de entrada: " + data_ent + " | Data de saída: " + data_sai + " | ")
 
def submenu_alugueis(lista_clientes, lista_veiculos, lista_alugueis): # Função recebe opção de submenu e chama funções relacionadas a alugueis
    '''Função recebe todas as listas necessárias para funções derivadas'''
    sub_op = ''
    while sub_op !='0':
        sub_op = op_submenu_alugueis()
        if sub_op == '1':
            listar_todos_alugueis(lista_alugueis)
        elif sub_op == '2':
            inserir_aluguel(lista_clientes, lista_veiculos, lista_alugueis)
        elif sub_op == "3":
            alterar_aluguel(lista_clientes, lista_veiculos, lista_alugueis)
        elif sub_op == "4":
            excluir_aluguel(lista_alugueis)
        elif sub_op == '0':
            print('Menu Principal')
        else:
            print('Entrada invalida.')  
 
def inserir_aluguel(lista_clientes, lista_veiculos, lista_alugueis): # Função verifica existência de aluguel e insere caso tudo colabore
    alugavel = True
    a = Aluguel()
    a.cpf_cliente = input('Insira o CPF do cliente: ')
    cpf_index = buscar_por_criterio('cpf',lista_clientes,a.cpf_cliente) # Busca Cliente nos registros de clientes para validar inserção
    if cpf_index == -1:
        print('Este cliente não está cadastrado no sistema...')
    else:
        a.codigo_veiculo = input('Insira o CÓDIGO do veículo: ')
        codigo_index = buscar_por_criterio('codigo',lista_veiculos,a.codigo_veiculo) # Busca Veiculo nos registros para validar inserção
        if codigo_index == -1:
            print('Este veículo não está cadastrado no sistema...')
        else:
            a.data_entrada = input('Digite a data de entrada (DD/MM/AAAA): ').split('/')
            a.data_entrada = datetime.date(int(a.data_entrada[2]), int(a.data_entrada[1]), int(a.data_entrada[0]))
            a.data_saida = input('Digite a data de saída (DD/MM/AAAA): ').split('/')
            a.data_saida = datetime.date(int(a.data_saida[2]), int(a.data_saida[1]), int(a.data_saida[0]))
            data_indexes = buscar_por_criterio('data_em_alugueis', lista_alugueis, a.data_entrada, a.data_saida) # Busca datas registradas
            i = 0
            while i < len(data_indexes) and alugavel: # Faz busca do veiculo dentro do periodo para verificar disponibilidade
                codigo_veiculo = lista_veiculos[codigo_index].codigo
                codigo_alugado = lista_alugueis[data_indexes[i]].codigo_veiculo
                if codigo_veiculo == codigo_alugado: # Compara codigo com os já alugados para verificar disponibilidade
                    alugavel = False
                    print(f'O veículo de código {lista_veiculos[codigo_index].codigo} está alugado em algum momento dentro desse periodo...')
                    return alugavel
                i += 1
            lista_alugueis.append(a)
            print('Veiculo alugado!')
            return alugavel
 
def buscar_aluguel(lista_alugueis, cpf, codigo, entrada, saida): # Função recebe os atributos de busca e retorna indice do aluguel
    i = 0
    while i < len(lista_alugueis):
        if cpf == lista_alugueis[i].cpf_cliente and codigo == lista_alugueis[i].codigo_veiculo and entrada == lista_alugueis[i].data_entrada and saida == lista_alugueis[i].data_saida:
            return i
        i += 1
    return -1
 
def alterar_aluguel(lista_clientes, lista_veiculos, lista_alugueis): # Procura aluguel, deleta antigo e adiciona um nomo
    print('Informe os dados do aluguel que sera alterado')
    cpf = input('Digite o CPF do cliente: ')
    codigo = input('Digite o CÓDIGO do veículo: ')
    entrada = input('Digite a data de entrada (DD/MM/AAAA): ').split('/')
    entrada = datetime.date(int(entrada[2]), int(entrada[1]), int(entrada[0]))
    saida = input('Digite a data de saída (DD/MM/AAAA): ').split('/')
    saida = datetime.date(int(saida[2]), int(saida[1]), int(saida[0]))
    aluguel = buscar_aluguel(lista_alugueis, cpf, codigo, entrada, saida)
    ram = lista_alugueis[aluguel] # Aluguel que será deletado fica salvo caso alteração não permitida
    if aluguel != -1:
        del lista_alugueis[aluguel]
        print('Informe novos dados do aluguel')
        autorizado = inserir_aluguel(lista_clientes, lista_veiculos, lista_alugueis)
        if not autorizado:
            lista_alugueis.append(ram)
            print('Aluguel inalterado...')
        else:
            print('Aluguel alterado.')
    else:
        print("Aluguel inexistente...")
 
def excluir_aluguel(lista_alugueis): # Deleta aluguel com confirmação
    cpf = input('Digite o CPF do cliente: ')
    codigo = input('Digite o CÓDIGO do veículo: ')
    entrada = input('Digite a data de entrada (DD/MM/AAAA): ').split('/')
    entrada = datetime.date(int(entrada[2]), int(entrada[1]), int(entrada[0]))
    saida = input('Digite a data de saída (DD/MM/AAAA): ').split('/')
    saida = datetime.date(int(saida[2]), int(saida[1]), int(saida[0]))
    aluguel = buscar_aluguel(lista_alugueis, cpf, codigo, entrada, saida)
    if aluguel != -1:
        confirm = input("Quer mesmo excluir esse registro? Digite 'SIM' ou 'NAO': ").upper()
        if confirm == 'SIM':
            del (lista_alugueis[aluguel])
            print("Aluguel DELETADO...")
        else:
            print("PROCESSO CANCELADO!")
    else:
        print("Aluguel inexistente...")
 
def listar_todos_alugueis(lista_alugueis): # Roda lista Alugueis e imprime os dados de cada um
    i = 0
    if len(lista_alugueis) > 0:
        while i < len(lista_alugueis):
            imprime_aluguel(lista_alugueis[i])
            i += 1
    else:
        print("Sem alugueis registrados!")
 
def ler_alugueis(nome_arquivo, lista_alugueis): # Busca alugueis em arquivo e os atribui a lista
    arq = open(nome_arquivo, 'r')
    for linha in arq:
        if linha.find(';'):
            dados_aluguel = linha.split(';')
            a = Aluguel()
            a.cpf_cliente = dados_aluguel[0]
            a.codigo_veiculo = dados_aluguel[1]
            a.data_entrada = dados_aluguel[2].split('/')
            a.data_entrada = datetime.date(int(a.data_entrada[0]), int(a.data_entrada[1]), int(a.data_entrada[2]))
            a.data_saida = dados_aluguel[3].split('/')
            a.data_saida = datetime.date(int(a.data_saida[0]), int(a.data_saida[1]), int(a.data_saida[2]))
            lista_alugueis.append(a)
    arq.close()
 
def armazenar_alugueis(nome_arquivo, lista_alugueis): # Salva alugueis da lista no arquivo
    arq = open(nome_arquivo, 'w')
    i = 0
    while i < len(lista_alugueis):
        a = lista_alugueis[i]
        data_ent = (a.data_entrada.strftime('%G') + '/' + a.data_entrada.strftime('%m') + '/' + a.data_entrada.strftime('%d'))
        data_sai = (a.data_saida.strftime('%G') + '/' + a.data_saida.strftime('%m') + '/' + a.data_saida.strftime('%d'))
        arq.write(str(a.cpf_cliente) + ';' + str(a.codigo_veiculo) + ';' + str(data_ent) + ';' + str(data_sai) + ';' + '\n')
        i += 1
    arq.close()
 
############################ R E L A T O R I O S ############################
 
def submenu_relatorios(lista_alugueis): # Função recebe opção de submenu e chama funções relacionadas a relatorios
    sub_op = ''
    while sub_op !='0':
        sub_op = op_submenu_relatorios()
        if sub_op == '1':
            reservas_por_cliente(lista_alugueis)
        elif sub_op == '2':
            reservas_por_veiculo(lista_alugueis)
        elif sub_op == "3":
            reservas_por_periodo(lista_alugueis)
        elif sub_op == '0':
            print('Menu Principal')
        else:
            print('Entrada invalida.')
 
def reservas_por_cliente(lista_alugueis): # Roda lista alugueis em busca de cpf e imprime todos encontrados
    cpf = input('Digite o CPF do cliente: ')
    cpf_indexes = buscar_por_criterio('clie_em_alugueis',lista_alugueis,cpf)
    i = 0
    if len(cpf_indexes) > 0:
        while i < len(cpf_indexes):
            imprime_aluguel(lista_alugueis[i])
            i += 1
    else:
        print('Cliente sem reservas ou cliente inexistente...')
 
def reservas_por_veiculo(lista_alugueis): # Roda lista alugueis em busca de codigo de veiculo e imprime todos encontrados
    codigo = input('Digite o CODIGO do veiculo: ')
    codigo_indexes = buscar_por_criterio('veic_em_alugueis',lista_alugueis,codigo)
    i = 0
    if len(codigo_indexes) > 0:
        while i < len(codigo_indexes):
            imprime_aluguel(lista_alugueis[i])
            i += 1
    else:
        print('Veiculo sem reservas ou veiculo inexistente no sistema...')
 
def reservas_por_periodo(lista_alugueis): # Roda lista alugueis em busca de datas e imprime todos que colidam
    data_ent = input('Digite a data inicial do periodo (DD/MM/AAAA): ').split('/')
    data_ent = datetime.date(int(data_ent[2]), int(data_ent[1]), int(data_ent[0]))
    data_sai = input('Digite a data final do periodo (DD/MM/AAAA): ').split('/')
    data_sai = datetime.date(int(data_sai[2]), int(data_sai[1]), int(data_sai[0]))
    periodo_indexes = buscar_por_criterio('data_em_alugueis',lista_alugueis,data_ent,data_sai)
    i = 0
    if len(periodo_indexes) > 0:
        while i < len(periodo_indexes):
            imprime_aluguel(lista_alugueis[i])
            i += 1
    else:
        print('Sem reservas entre as datas determinadas...')
 
################################## M A I N ##################################
 
def main(): # Função principal, responsável por chamar todas as outras funções
    clientes = []
    veiculos = []
    alugueis = []
    existe_arquivo()
    ler_clientes('clientes.txt', clientes)
    ler_veiculos('veiculos.txt', veiculos)
    ler_alugueis('alugueis.txt', alugueis)
    opcao = ''
    while opcao != '0':
        opcao = op_menu_principal()
        if opcao == '1':
            submenu_clientes(clientes)
        elif opcao == '2':
            submenu_veiculos(veiculos)
        elif opcao == '3':
            submenu_alugueis(clientes, veiculos, alugueis)
        elif opcao == '4':
            submenu_relatorios(alugueis)
        elif opcao == '0':
            print("Obrigado por usar nosso sistema!")
        else:
            print('Entrada invalida.')
    armazenar_clientes('clientes.txt', clientes)
    armazenar_veiculos('veiculos.txt', veiculos)
    armazenar_alugueis('alugueis.txt', alugueis)
 
############################## P R O G R A M A ##############################
 
main() # Chamada da função principal

