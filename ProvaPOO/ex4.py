#Não sei a biblioteca de DATA decorada para realizar o método da auditoria, fiz de uma forma improvisada. 

# criando as Classes
class Empresa:
    nome = ''
    cnpj = 0
    nacionalidade = ''
    nome_responsavel_empresa = ''
    paises = []
    produtos = {}
    pais = ''
    produto_novo = ''
    preco = 0
    desricao = ''

    def __init__(self, nome, cnpj, nacionalidade, nome_responsavel_empresa, paises, produtos):
        self.nome = nome
        self.cnpj = cnpj
        self.nacionalidade = nacionalidade
        self.nome_responsavel_empresa = nome_responsavel_empresa
        self.paises = paises
        self.produtos = produtos
    
    def getResponsavel(self):
        print(f'Presidente: {self.nome_responsavel_empresa}')
    
    def getPaises(self):
        print(f'Países de atuação: {self.paises}')
    
    def buscarPais(self, pais):
        if pais in self.paises:
            print(f"A {self.nome} atua no país {pais}!")
        else:
            print(f"A {self.nome} infelizmente não atua no país {pais}!")

    def AdcProduto(self, produto_novo, preco, descricao):
        self.produtos[produto_novo]=[preco, descricao]
        print(self.produtos)

    def RelatorioProdutos(self):
        print(self.produtos)
    
    def PesquisarProduto(self, produto):
        if produto in self.produtos:
            print(produto,": ", self.produtos[produto])
        else:
            print("Produto não encontrado!")

    def Vistoria(self):
        print(f"Empresa: {self.nome}")

class Area(Empresa):
    nome_area = ''
    sigla_area = ''
    funcao_area = ''
    nome_responsavel_area = ''
    lucro = 0
    inicio_auditoria = ''
    fim_auditoria = 0
    hoje = 0

    def __init__(self, nome, cnpj, nacionalidade, nome_responsavel_empresa, paises, produtos, nome_area, sigla_area, funcao_area, nome_responsavel_area,lucro, inicio_auditoria, fim_auditoria, hoje):
        super().__init__(nome, cnpj, nacionalidade, nome_responsavel_empresa, paises, produtos)
        self.nome_area = nome_area
        self.sigla_area = sigla_area
        self.funcao_area = funcao_area
        self.nome_responsavel_area = nome_responsavel_area
        self.lucro = lucro
        self.inicio_auditoria = inicio_auditoria
        self.fim_auditoria = fim_auditoria
        self.hoje = hoje

    def getResponsavel(self):
        print(f"Diretor: {self.nome_responsavel_area}")
        return super().getResponsavel()

    def RelatorioFinanceiro(self, despesas):
        print(f'\nDespesas: {despesas}')
        print(f'Receita: {self.lucro}')
        self.lucro = self.lucro - despesas
        print(f'Lucro: {self.lucro}')

    def Auditoria(self):
        print('\n',5*"-",'Auditoria',5*"-")
        if self.hoje < self.fim_auditoria and self.hoje > self.inicio_auditoria:
            print("Auditoria está sendo auditada")
        print(f'Início: dia {self.inicio_auditoria} Fim: dia {self.fim_auditoria}\n')

    def Vistoria(self):
        print(f"Setor: {self.nome_area}")
        return super().Vistoria()

class Departamento(Area):
    nome_departamento = ''
    sigla_departamento = ''
    funcao_departamento = ''
    nome_responsavel_departamento = ''
    qtd_funcionarios = 0
    funcionarios = []

    def __init__(self, nome, cnpj, nacionalidade, nome_responsavel_empresa, paises, produtos, nome_area, sigla_area, funcao_area, nome_responsavel_area, lucro, inicio_auditoria, fim_auditoria, hoje, nome_departamento, sigla_departamento, funcao_departamento, nome_responsavel_departamento, qtd_funcionarios):
        super().__init__(nome, cnpj, nacionalidade, nome_responsavel_empresa, paises, produtos, nome_area, sigla_area, funcao_area, nome_responsavel_area, lucro, inicio_auditoria, fim_auditoria, hoje)
        self._nome_departamento = nome_departamento
        self._sigla_departamento = sigla_departamento
        self._funcao_departamento = funcao_departamento
        self._nome_responsavel_departamento = nome_responsavel_departamento
        self._qtd_funcionarios = qtd_funcionarios
        
    def getResponsavel(self):
        print(f"Diretor: {self._nome_responsavel_departamento}")
        return super().getResponsavel()

    def ContratarFuncionario(self,func):
        self.funcionarios.append(func)
        self._qtd_funcionarios = self._qtd_funcionarios + 1
        print(f'Funcionário(a) {func} contratado com sucesso!\nTotal de {self._qtd_funcionarios} funcionários no departamento {self._nome_departamento}')
    
    def RealizarTreinamento(self):
        print("Treinamento OK!")
        return True
    
    def Vistoria(self):
        print(f"Subsetor: {self._nome_departamento}")
        return super().Vistoria()
    

# instanciando as Classes
bosch = Empresa('Bosch',2131231231,'Alemã','Gastón',['Brasil','Alemanha','Chile','Argentina'],{'Furadeira':[1000,'Vermelho']})
pt = Area('Bosch',2131231231,'Alemã','Gastón',['Brasil','Alemanha','Chile','Argentina'],{'Furadeira':[1000,'Vermelho']}, 'Não sei', 'PT', 'Faz ferramentas', 'Jõao Pedro', 2000000, 10, 14, 12)
ets = Departamento('Bosch',2131231231,'Alemã','Gastón',['Brasil','Alemanha','Chile','Argentina'],{'Furadeira':[1000,'Vermelho']}, 'Não sei', 'PT', 'Faz ferramentas', 'Jõao Pedro', 2000000, 10, 14, 12, 'Engineering Tech School', 'ETS', 'Escola técnica', 'Fábio Siqueira', 120)

# manipulando e chamando as instancias
match int(input("\nQual classe deseja visualizar?\n1-Empresa\n2-Área\n3-Departamento\n")):
    case 1:
        print(15*"-",'EMPRESA',15*"-")
        while True:
            try:
                match int(input("\nO que deseja fazer?\n1-Ver nome do responsável\n2-Ver países de atuação\n3-Consultar país\n4-Adicionar produto\n5-Relatório de produtos\n6-Pesquisar produto\n7-Sair\n")):
                    case 1:
                        bosch.getResponsavel()
                    case 2:
                        bosch.getPaises()
                    case 3:
                        pais = input("Qual país deseja consultar?\n")
                        bosch.buscarPais(pais.title())
                    case 4:
                        produto_novo = input("Digite o nome do produto a adicionar: ")
                        preco = input("Digite o preco do produto: ")
                        descricao = input("Digite a descricao do produto: ")
                        bosch.AdcProduto(produto_novo, preco, descricao)
                    case 5:
                        bosch.RelatorioProdutos()
                    case 6:
                        produto = input("Digite o nome do produto á pesquisar: ")
                        bosch.PesquisarProduto(produto)
                    case 7:
                        print('\n',5*"-",'Vistoria',5*"-")
                        bosch.Vistoria()
                        break
            except ValueError:
                print("Digite uma opção válida! (1-7)")

    case 2:
        print(15*"-",'ÁREA',15*"-")
        pt.getResponsavel()
        pt.RelatorioFinanceiro(21239)
        pt.Auditoria()
        print('\n',5*"-",'Vistoria',5*"-")
        pt.Vistoria()

    case 3:
        print(15*"-",'DEPARTAMENTO',15*"-")
        ets.getResponsavel()
        ets.ContratarFuncionario('Mariana')
        ets.RealizarTreinamento()
        print('\n',5*"-",'Vistoria',5*"-")
        ets.Vistoria()
