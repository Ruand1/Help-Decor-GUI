import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from reportlab.pdfgen import canvas
#  from android.permissions import request_permissions, Permission  # PARA RODAR NO DESKTOP COMENTAR ESTA LINHA
import kivy
kivy.require('2.0.0')


class Telamenus(ScreenManager):  #  <---- Gerenciador das Telas
    pass


class Menu(Screen):  #<---- Tela de Menus Geral
    pass


class Menucliente(Screen):  #<---- Tela de Menu do Cadastro de Cliente

    def on_pre_enter(self):  # <----Vincula um evento de teclado em uma tela(Menucliente)
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):  # <----Se o usuário apertar ESC(27) --- Volta tela
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):  # <----Desvincula o evento de botão à tela
        Window.unbind(on_keyboard=self.voltar)


class Cadastrocliente(Screen):
    cadastrocliente = []
    path = ''

    def on_pre_enter(self):  # <----Vincula um evento de teclado em uma tela(CadastroCliente)
        self.path = App.get_running_app().user_data_dir+'/'
        self.loadData()
        Window.bind(on_keyboard=self.voltar)
        for cadastro in self.cadastrocliente:
            self.ids.boxcadcliente.add_widget(AddCadCliente(text=cadastro))

    def voltar(self, window, key, *args):  # <----Se o usuário apertar ESC(27) --- Volta tela
        if key == 27:
            App.get_running_app().root.current = 'menucliente'
            return True

    def on_pre_leave(self):  # <----Desvincula o evento de botão à tela
        Window.unbind(on_keyboard=self.voltar)
        ## <------- TENTAR ENCAIXAR A GRAVAÇÃO DA LISTA DE CADASTRO (UM POUCO ANTES DE SAIR)

    def loadData(self, *args):
        try:
            with open(self.path+'data.json', 'r') as data:
                self.cadastrocliente = json.load(data)
        except FileNotFoundError:
            pass

    def saveData(self, *args):
        with open(self.path+'data.json', 'w') as data:
            json.dump(self.cadastrocliente, data)

    def removerCadastro(self, AddCadCliente):
        texto = AddCadCliente.ids.rotulocadcliente.text
        self.ids.boxcadcliente.remove_widget(AddCadCliente)
        self.cadastrocliente.remove(texto)
        self.saveData()

    def adicionarcliente(self):  #<---- Widget que adiciona o cadastro dos clientes a tela
        cadcliente = self.ids.cadastrocli.text
        self.ids.boxcadcliente.add_widget(AddCadCliente(text=cadcliente))
        self.ids.cadastrocli.text = ''
        self.cadastrocliente.append(cadcliente)
        self.saveData()


class AddCadCliente(BoxLayout):  #<--- Widget com o cadastro do cliente
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.rotulocadcliente.text = text


class Menupeca(Screen):  #<---- Tela de Menu do Cadastro de Peças

    def on_pre_enter(self):  # <----Vincula um evento de teclado em uma tela(Menucliente)
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):  # <----Se o usuário apertar ESC(27) --- Volta tela
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def on_pre_leave(self):  # <----Desvincula o evento de botão à tela
        Window.unbind(on_keyboard=self.voltar)


class Cadastropeca(Screen):
    teste = {}
    cadastropecadic = {}
    cadastropecalist = []
    cadpeca = []
    cadfoto = []
    cadqtd = []
    cadunique = []
    cadastrotextopeca = []
    cadastrolocalpeca = []
    cadastroqtdpeca = []
    cadastrouniquepeca = []
    path = ''
    bsobeposicao = []

    testeunique = []


    #  <----------- USAR ESC PARA VOLTAR
    def on_pre_enter(self):  # <----Vincula um evento de teclado em uma tela(CadastroPecas)
        cont = 0

        self.path = App.get_running_app().user_data_dir+"/"
        #print(self.path)  #<------ Somente testes ver caminho pastas de cadastro
        self.loadData()
        Window.bind(on_keyboard=self.voltar)
        #print(f'{self.cadastrotextopeca} On pre enter')  # APENAS PARA TESTES
        #print(self.cadastrolocalpeca)
        #print(self.cadastroqtdpeca)
        #print(self.cadastrouniquepeca)

        for peca in self.cadastrotextopeca:
            self.ids.boxcadpeca.add_widget(AddCadPeca(idpeca=self.cadastrouniquepeca[cont], text=self.cadastrotextopeca[cont], localimagem=self.cadastrolocalpeca[cont], quantidade=self.cadastroqtdpeca[cont]))
            cont += 1

    def voltar(self, window, key, *args):  # <----Se o usuário apertar ESC(27) --- Volta tela
        if key == 27:
            App.get_running_app().root.current = 'menupeca'
            return True

    def on_pre_leave(self):  # <----Desvincula o evento de botão à tela
        Window.unbind(on_keyboard=self.voltar)
        for widget in range(len(self.ids.boxcadpeca.children)):  # <----- Remove temporariamente os widgets da tela
            self.ids.boxcadpeca.remove_widget(self.ids.boxcadpeca.children[0])

    def loadData(self, *args):
        try:
            with open(self.path+'datapecatexto.json', 'r') as datatexto:
                self.cadastrotextopeca = json.load(datatexto)

            with open(self.path+'datapecalocal.json', 'r') as datalocal:
                self.cadastrolocalpeca = json.load(datalocal)

            with open(self.path+'datapecaqtd.json', 'r') as dataqtd:
                self.cadastroqtdpeca = json.load(dataqtd)

            with open(self.path+'datapecaunique.json', 'r') as dataunique:
                self.cadastrouniquepeca = json.load(dataunique)
        except FileNotFoundError:
            pass

    def saveData(self, *args):
        with open(self.path+'datapecatexto.json', 'w') as datatexto:
            json.dump(self.cadastrotextopeca, datatexto)
        with open(self.path+'datapecalocal.json', 'w') as datalocal:
            json.dump(self.cadastrolocalpeca, datalocal)
        with open(self.path+'datapecaqtd.json', 'w') as dataqtd:
            json.dump(self.cadastroqtdpeca, dataqtd)
        with open(self.path+'datapecaunique.json', 'w') as dataunique:
            json.dump(self.cadastrouniquepeca, dataunique)

    def removerCadastro(self, AddCadPeca):
        texto = AddCadPeca.ids.rotulocadpeca.text
        imagem = AddCadPeca.ids.imagem_popup.background_normal
        qtd = AddCadPeca.ids.rotuloqtdpeca.text
        uniquepeca = AddCadPeca.ids.uniquepeca.text
        self.ids.boxcadpeca.remove_widget(AddCadPeca)
        self.cadastrotextopeca.remove(texto)
        self.cadastrolocalpeca.remove(imagem)
        self.cadastroqtdpeca.remove(qtd)
        self.cadastrouniquepeca.remove(uniquepeca)  # VERIFICAR POSSIVEL ERRO
        self.saveData()

    def adicionarpeca(self):  #<---- Widget que adiciona o cadastro das peças a tela
        self.cadpeca = self.ids.cadastropec.text
        self.cadfoto = Escolherfoto().passarselecao()  # 4º Variável cadfoto recebe o caminho da imagem
        self.cadqtd = self.ids.quantidadepec.text
        if self.cadastrouniquepeca == '':
            self.cadunique = '1'
        else:
            self.cadunique = str(len(self.cadastrouniquepeca) + 1)

        self.cadastrotextopeca.append(self.cadpeca)
        self.cadastrolocalpeca.append(self.cadfoto)
        self.cadastroqtdpeca.append(self.cadqtd)
        self.cadastrouniquepeca.append(self.cadunique)

        self.ids.boxcadpeca.add_widget(AddCadPeca(idpeca=self.cadunique, text=self.cadpeca, localimagem=self.cadfoto, quantidade=self.cadqtd))  # <----Inclui texto e imagem ao widget de cadastro de peças
        self.ids.cadastropec.text = ''  #<-----TROCAR VARIÀVEL PARA descricaopec
        self.ids.quantidadepec.text = ''
        self.saveData()

    def sobeposicao(self, AddCadPeca):
        uniquepeca = int(AddCadPeca.ids.uniquepeca.text)
        for widget in range(len(self.ids.boxcadpeca.children)+1):  # <----- Remove temporariamente os widgets da tela
            if uniquepeca == widget and uniquepeca != 1:
                self.cadastrotextopeca[uniquepeca-1], self.cadastrotextopeca[uniquepeca-2] = self.cadastrotextopeca[uniquepeca-2], self.cadastrotextopeca[uniquepeca-1]
                self.cadastrolocalpeca[uniquepeca-1], self.cadastrolocalpeca[uniquepeca-2] = self.cadastrolocalpeca[uniquepeca-2], self.cadastrolocalpeca[uniquepeca-1]
                self.cadastroqtdpeca[uniquepeca-1], self.cadastroqtdpeca[uniquepeca-2] = self.cadastroqtdpeca[uniquepeca-2], self.cadastroqtdpeca[uniquepeca-1]
                self.cadastrouniquepeca[uniquepeca-1], self.cadastrouniquepeca[uniquepeca-2] = self.cadastrouniquepeca[uniquepeca-1], self.cadastrouniquepeca[uniquepeca-2]
            elif int(uniquepeca) == widget and int(uniquepeca) == 1:
                pop = Popup(title='Erro..', content=Label(text='Este cadastro esta no topo da lista'), size_hint=(None, None),
                            size=(260, 100))
                pop.open()
        self.saveData()
        self.on_pre_leave()
        self.on_pre_enter()

    def desceposicao(self, AddCadPeca):
        uniquepeca = int(AddCadPeca.ids.uniquepeca.text)
        for widget in range(len(self.ids.boxcadpeca.children)+1):  # <----- Remove temporariamente os widgets da tela
            if uniquepeca == widget and uniquepeca != len(self.ids.boxcadpeca.children):
                self.cadastrotextopeca[uniquepeca-1], self.cadastrotextopeca[uniquepeca] = self.cadastrotextopeca[uniquepeca], self.cadastrotextopeca[uniquepeca-1]
                self.cadastrolocalpeca[uniquepeca-1], self.cadastrolocalpeca[uniquepeca] = self.cadastrolocalpeca[uniquepeca], self.cadastrolocalpeca[uniquepeca-1]
                self.cadastroqtdpeca[uniquepeca-1], self.cadastroqtdpeca[uniquepeca] = self.cadastroqtdpeca[uniquepeca], self.cadastroqtdpeca[uniquepeca-1]
                self.cadastrouniquepeca[uniquepeca-1], self.cadastrouniquepeca[uniquepeca] = self.cadastrouniquepeca[uniquepeca-1], self.cadastrouniquepeca[uniquepeca]
            elif int(uniquepeca) == widget and uniquepeca == len(self.ids.boxcadpeca.children):
                pop = Popup(title='Erro..', content=Label(text='Este cadastro esta no fundo da lista'), size_hint=(None, None),
                            size=(260, 100))
                pop.open()
        self.saveData()
        self.on_pre_leave()
        self.on_pre_enter()


class Locacao(Screen):
    def on_pre_enter(self):  # <----Vincula um evento de teclado em uma tela(CadastroPecas)
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):  # <----Se o usuário apertar ESC(27) --- Volta tela
        if key == 27:
            App.get_running_app().root.current = 'menupeca'
            return True

    def on_pre_leave(self):  # <----Desvincula o evento de botão à tela
        Window.unbind(on_keyboard=self.voltar)

    def gerarlocacao(self):  # <---- FUNÇÃO OU CLASSE
        pass


class Gerarlocacao(Screen):
    cadastrotextopeca = []
    cadastrolocalpeca = []
    cadastroqtdpeca = []
    cadastrouniquepeca = []
    cadastrocliente = []
    cadastropeca = []
    path = ''

    def on_pre_enter(self):  # <----Vincula um evento de teclado em uma tela(CadastroPecas)
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):  # <----Se o usuário apertar ESC(27) --- Volta tela
        if key == 27:
            App.get_running_app().root.current = 'menupeca'
            return True

    def on_pre_leave(self):  # <----Desvincula o evento de botão à tela
        Window.unbind(on_keyboard=self.voltar)

    def loadData(self, *args):
        try:
            with open(self.path+'datapecatexto.json', 'r') as datatexto:
                self.cadastrotextopeca = json.load(datatexto)

            with open(self.path+'datapecalocal.json', 'r') as datalocal:
                self.cadastrolocalpeca = json.load(datalocal)

            with open(self.path+'datapecaqtd.json', 'r') as dataqtd:
                self.cadastroqtdpeca = json.load(dataqtd)

            with open(self.path+'datapecaunique.json', 'r') as dataunique:
                self.cadastrouniquepeca = json.load(dataunique)

            with open(self.path+'data.json', 'r') as data:
                self.cadastrocliente = json.load(data)
        except FileNotFoundError:
            pass

    def spinner_cliente(self, value):
        self.path = App.get_running_app().user_data_dir + "/"
        self.loadData()

        self.ids.click_cliente.text = value
        print(f'{self.cadastrocliente} Cadastro Cliente')
        print(f'{self.cadastrotextopeca} Cadastro Peças')  # APENAS PARA TESTES
        print(self.cadastrolocalpeca)
        print(self.cadastroqtdpeca)
        print(self.cadastrouniquepeca)
        teste = Gerarlocacao().passarlistapeca()
        print(teste)

    def spinner_peca(self, value):
#        self.path = App.get_running_app().user_data_dir + "/"
#        self.loadData()

#        self.ids.click_peca.text = value
        self.box = BoxLayout()
        self.label = Label(text=value, font_size=13)
        self.textinput = TextInput()

        self.box.add_widget(self.label)
        self.box.add_widget(self.textinput)

        self.ids.gerapdf.add_widget(self.box)

    def gerarpdf(self):
        cont = 0
        x = 10
        y = 770
        self.path = App.get_running_app().user_data_dir + "/"
        self.loadData()

        cnv = canvas.Canvas("Locacao1.pdf")
        cnv.drawString(10, 830, f'Nome do cliente: {self.cadastrocliente}')
        cnv.drawString(10, 810, 'Endereço: Rua Lupercio de Miranda, 1776')
        cnv.drawString(10, 790, '         ID               Imagem                                        Descrição                      Qtd')

        for peca in self.cadastrotextopeca:
            cnv.drawString(x, y, f'Peça: {self.cadastrouniquepeca[cont]:<3}{self.cadastrolocalpeca[cont]:<40}{self.cadastrotextopeca[cont]:<40}{self.cadastroqtdpeca[cont]:<5}')
            cont += 1
            y -= 15
        cnv.save()
        return 0


    def passarlistacliente(self):
        self.path = App.get_running_app().user_data_dir + "/"
        self.loadData()
        self.cadastrocliente = self.cadastrocliente
        return self.cadastrocliente

    def passarlistapeca(self):
        self.path = App.get_running_app().user_data_dir + "/"
        self.loadData()
        self.cadastropeca = self.cadastrotextopeca
        return self.cadastropeca

    def adicionarlocacao(self):
        pass
#        self.spinner = Spinner(text='Peça', font_size=13, size_hint=(None, None), size=(100, 20),
#                               values=self.passarlistapeca())
#        self.ids.boxlocacao.add_widget(self.spinner)


class addlocacao(BoxLayout):
    pass


class Escolherfoto(Screen):
    listalocais = []
    imagempeca = ''
    teste = []
    localimagem = ''

# QUANDO APERTAR AQUI REMOVE OS WIDGETS DA TELA

    def on_pre_enter(self):  # <----Vincula um evento de teclado em uma tela(Menucliente)
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):  # <----Se o usuário apertar ESC(27) --- Volta tela
        if key == 27:
            App.get_running_app().root.current = 'cadastropeca'
            return True

    def on_pre_leave(self):  # <----Desvincula o evento de botão à tela
        Window.unbind(on_keyboard=self.voltar)

    def selecionar(self, filename):  # CAMINHO DA IMAGEM SÓ PASSA REFERENCIA SE FOR EM LISTA - VERIFICAR
        self.ids.imagempeca.source = filename[0]
        self.imagempeca = filename[0]
        #print(filename[0])  # TESTE 1º Variavel imagem peça - recebe o caminho do arquivo
        self.listalocais.append(filename[0])
        #print(self.listalocais)  # TESTE 2º Acrescenta o endereço em uma lista

    def passarselecao(self):  # < ------ Função para jogar o caminho da imagem para a classe adicionarpeca
        if len(self.listalocais) == 0:
            self.localimagem = ''
            return self.localimagem
        else:
            pos = len(self.listalocais) - 1
            self.localimagem = str(self.listalocais[pos])
            #print(self.localimagem)  # 3º Variavel teste recebe o caminho da imagem em uma variável
            return self.localimagem



#15/02/22
# VERIFICAR ERRO SE USUÁRIO NÃO ESCOLHER IMAGEM, NEM ESCREVER TEXTO
# verificado, foi incluido atribuições padroes, assim ao adicionar o widget sai em branco
# CRIAR UM BOTAO PARA ABRIR CAIXA DE SELEÇÃO - OK
# MODO DE ABRIR CAIXA DE SELEÇÃO - VER VÍDEO - OK, ABRIU CAIXA DE SELEÇÃO E ESCOLHEU IMAGEM - OK
# GRAVAR CAMINHO DA IMAGEM EM UMA VARIÁVEL - OK - VARIAVEL localimagem GUARDANDO CAMINHO
# MODO DE ATRIBUIR A VARIAVEL cadfoto, O CAMINHO DA FOTO ESCOLHIDO PELO USUÁRIO - OK
# NO RETORNO ESTA DUPLICANDO CADASTRO - OK
# foi acrescentado a função on_pre_leave a remoção dos widgets
# PARTE DE CADASTRO DE PEÇAS FOI FINALIZADO - VERIFICAR ERROS E MELHORAMENTOS
# ------------------------------------------------------------------------------
# 16/02/22
# PROBLEMAS NAS PERMISSOES DO ANDROID PARA ACESSAR STORAGE - OK Funcionando
# inserir permissões no .spec
# inserir android.permissions para requisitar ao usuario a permissão de acesso
# ------------------------------------------------------------------------------
# 17/02/22
# INCLUIR QUANTIDADE NAS PEÇAS - OK
# VERIFICAR MODO PARA ALTERAR DESCRIÇÃO E QTD PEÇAS - SE CONSEGUIR MUDAR POSIÇÃO NAO SERA NECESSARIO
# AUMENTAR IMAGEM AO CLICAR NO ICONE - OK
# PROBLEMAS PARA REMOVER WIDGET - OK - SEMPRE VERIFICAR SE ESTA ENTRE '' NAS LISTAS
# PROBLEMAS PARA ADICIONAR WIDGET SE USUARIO NÃO ESCOLHER IMAGEM - OK - FAZER MELHORIAS
# 18/02/22
# ARRUMAR A DISPOSIÇÃO DOS WIDGETS NO CADASTRO DAS PEÇAS - OK
# MUDAR POSIÇÃO DOS WIDGETS AO ARRASTAR
    #usuario deve clicar e arrastar widget - PROXIMA VERSÃO
    #python irá alterar a posição
    #Solução 1 - criar dois botoes ^ v onde o python refaz as posições das listas
        # FOI CRIADO ID INDIVIDUAL DAS PEÇAS ASSIM SERÁ POSSIVEL MODIFICAR POSIÇÃO - OK
#19/02/22
# UTILIZADO SOLUÇÃO 1 PARA POSIÇÃO DOS WIDGET - OK
# os botoes de sobe e desce estão funcionando e gravando
# PROCURAR SOLUÇÃO MAIS INTELIGENTE NAS PROXIMAS VERSÕES
# ------------------------------------------------------------------------------
#21/02/22
# COMEÇAR PARTE DE GERAR RELATORIO DE LOCAÇÃO - OK
# CRIAR BOTÃO LOCAÇÃO - OK
# CRIAR TELA DE LOCAÇÃO - OK
# CRIAR ACESSO E CRIAÇÃO DE PDF - OK
# PUXAR LISTAS DE CADASTRO PRA PDF - OK
# ORGANIZAR TELA PDF - UTILIZANDO WIDGETS SPINNER -
# ------------------------------------------------------------------------------
#22/02/22
# WIDGET JA ESTA COLOCANDO NA TELA AS PEÇAS CADASTRADAS
# FALTA UM FORMA DE PASSAR PARA O PDF OS CADASTROS ESCOLHIDOS PELO USUÁRIO
# FALTA ORGANIZAR O LAYOUT DO PDF E DO BOXLAYOUT DO PDF
# DIMINUIR O TAMANHO DOS BOTÕES QUE APARECEM NO SPINNER

# FAZER CADASTRO DE CLIENTES - MELHORIA
# FAZER CADASTRO DE FORNECEDORES -

# TENTAR MUDAR OS WIDGETS DE LABEL PARA BOTÃO E MOSTRAR DETALHES DO CADASTRO
# ao inves disso fazer um botão que gera um popup com a descrição do produto
# na descrição inicial criar apenas um apelido como atalho

class AddCadPeca(BoxLayout):  #<--- Widget com o cadastro da peça
    def __init__(self,idpeca='', text='', localimagem='', quantidade='', **kwargs):
        super().__init__(**kwargs)
        self.ids.rotulocadpeca.text = str(text)  # VERIFICAR RETIRAR STR

        self.ids.rotuloqtdpeca.text = str(quantidade)

        self.ids.imagem_popup.background_normal = str(localimagem)

        self.carregaimagem = localimagem

        self.ids.uniquepeca.text = str(idpeca)

    def aumentarfoto(self, *args):
        pop = Popup(title='Imagem Peça', content=Image(source=self.carregaimagem), size_hint=(None, None), size=(300, 450))
        pop.open()


class Botao(ButtonBehavior, Label):
    cor = ListProperty([0.8, 0.6, 0.7, 1])

    def __init__(self, **kwargs):
        super(Botao, self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self, *args):
        self.atualizar()

    def on_size(self, *args):
        self.atualizar()

    def atualizar(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.cor)
            Ellipse(size=(self.height, self.height), pos=self.pos)
            Ellipse(size=(self.height, self.height), pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width-self.height, self.height), pos=(self.x+self.height/2.0, self.y))


# - PARA ATUALIZAR AO CLICAR NO BOTAO - VER VÍDEO https://www.youtube.com/watch?v=kDu1HJPruIE&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=18

class HelpDecorTest(App):
    def build(self):
        return Telamenus()
#    def on_start(self):  # PARA RODAR NO DESKTOP COMENTAR ESTA LINHA
#        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])


HelpDecorTest().run()




# - Fonte Canva - Preto e Rosa Neon Casa Noturna Logotipo


# - Utilizar esta resolução para testes python main.py -m screen:one,portrait,scale=.4