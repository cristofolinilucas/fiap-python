import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

##################################################

class View(QWidget):  ## (Complete o código que declara a View)
    __Lb_peso = None
    __Lb_altura = None
    __Lb_imc = None
    __Lb_classif = None
    __LEd_peso = None
    __LEd_altura = None
    __LEd_imc = None
    __LEd_classif = None
    __Bt_calc = None
    __Cntr = None

    def __init__(self, Cntr, Str="Janela"):
        super().__init__()
        self.__Cntr=Cntr
        self.setWindowTitle(Str)
        self.setGeometry(320, 160, 10, 10)

        self.setAutoFillBackground(True)
        p=self.palette()
        p.setColor(self.backgroundRole(), QColor('orange'))
        self.setPalette(p)

        self.inicialize()

    def closeEvent(self, event):
        print("Fechando a janela")
        self.destroy()
        sys.exit(0)

    ## Questão 10:  (Criar o método get_Peso)

    ## Questão 11:  (Criar o método get_Altura)

    ## Questão 12:  (Criar o método set_imc)

    ## Questão 13:  (Criar o método set_classif)

    def action_Bt_calc(self):
        ## Questão 14:  (Criar o evento que calcula o imc e
        ##              define a classificação de risco)

    ##def show_error(self, Erro):
        ## Questão 15:  (Criar o método que mostra uma mensagem de erro na tela com QMessageBox)

    ##def inicialize(self):
        Grid=QGridLayout()

        ## Questão 16:  (Realize a alocação dos componentes gráficos)

        self.__Bt_calc=QPushButton(self, text='Calcular')
        ## Questão 17:  (Conectar o botão Bt_adic ao evento que realiza
        ##              o cálculo do imc e define a classificação de risco)

        ############# Grid #############
        ## Questão 18:  (Acrescentar os componentes gráficos na Tela)

        self.setLayout(Grid)
        self.show()

##################################################
