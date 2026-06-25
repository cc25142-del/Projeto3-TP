# 25142 - Isabella Cristine Santos Fernandes
# 25673 - Emily Taysa de Souza Alves

from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QTabWidget, QLineEdit, QComboBox, 
    QTableWidget, QTableWidgetItem, QPushButton, QTextEdit, QVBoxLayout
)


class Ui_MainWindow:
    def setupUi(self, MainWindow: QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        
        MainWindow.resize(900, 600)
        MainWindow.setWindowTitle("Sistema de Gestão Corporativa")
        
        # Widget central
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Tab Widget
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 880, 580))
        
        # ===== ABA 1: CRUD =====
        self.tabCRUD = QWidget()
        self.tabCRUD.setObjectName("tabCRUD")
        
        # Linha de Matrícula
        self.lineMatricula = QLineEdit(self.tabCRUD)
        self.lineMatricula.setObjectName("lineMatricula")
        self.lineMatricula.setGeometry(QRect(20, 20, 100, 25))
        self.lineMatricula.setPlaceholderText("Matrícula")
        
        # Linha de Nome
        self.lineNome = QLineEdit(self.tabCRUD)
        self.lineNome.setObjectName("lineNome")
        self.lineNome.setGeometry(QRect(140, 20, 300, 25))
        self.lineNome.setPlaceholderText("Nome")
        
        # Combo Gênero
        self.comboGenero = QComboBox(self.tabCRUD)
        self.comboGenero.setObjectName("comboGenero")
        self.comboGenero.setGeometry(QRect(460, 20, 120, 25))
        self.comboGenero.addItems(["Masculino", "Feminino"])
        
        # Combo Departamento
        self.comboDepartamento = QComboBox(self.tabCRUD)
        self.comboDepartamento.setObjectName("comboDepartamento")
        self.comboDepartamento.setGeometry(QRect(600, 20, 200, 25))
        
        # Tabela de Salários
        self.tableSalarios = QTableWidget(self.tabCRUD)
        self.tableSalarios.setObjectName("tableSalarios")
        self.tableSalarios.setGeometry(QRect(20, 70, 780, 120))
        self.tableSalarios.setColumnCount(12)
        self.tableSalarios.setHorizontalHeaderLabels(
            ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        )
        
        # Tabela de Funcionários Registrados
        self.tableFuncionarios = QTableWidget(self.tabCRUD)
        self.tableFuncionarios.setObjectName("tableFuncionarios")
        self.tableFuncionarios.setGeometry(QRect(20, 200, 780, 80))
        self.tableFuncionarios.setColumnCount(4)
        self.tableFuncionarios.setHorizontalHeaderLabels(
            ['Matrícula', 'Nome', 'Gênero', 'Departamento']
        )
        self.tableFuncionarios.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableFuncionarios.setSelectionMode(QTableWidget.SingleSelection)
        
        # Botões da aba CRUD
        self.btnNovo = QPushButton("Novo", self.tabCRUD)
        self.btnNovo.setObjectName("btnNovo")
        self.btnNovo.setGeometry(QRect(20, 300, 80, 30))
        
        self.btnEditar = QPushButton("Editar", self.tabCRUD)
        self.btnEditar.setObjectName("btnEditar")
        self.btnEditar.setGeometry(QRect(110, 300, 80, 30))
        
        self.btnExcluir = QPushButton("Excluir", self.tabCRUD)
        self.btnExcluir.setObjectName("btnExcluir")
        self.btnExcluir.setGeometry(QRect(200, 300, 80, 30))
        
        self.btnSalvar = QPushButton("Salvar", self.tabCRUD)
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnSalvar.setGeometry(QRect(290, 300, 80, 30))
        
        self.btnCancelar = QPushButton("Cancelar", self.tabCRUD)
        self.btnCancelar.setObjectName("btnCancelar")
        self.btnCancelar.setGeometry(QRect(380, 300, 80, 30))
        
        self.tabWidget.addTab(self.tabCRUD, "Manutenção (CRUD)")
        
        # ===== ABA 2: RELATÓRIO =====
        self.tabRelatorio = QWidget()
        self.tabRelatorio.setObjectName("tabRelatorio")
        
        # Text Edit para Relatório
        self.textRelatorio = QTextEdit(self.tabRelatorio)
        self.textRelatorio.setObjectName("textRelatorio")
        self.textRelatorio.setGeometry(QRect(20, 20, 780, 400))
        self.textRelatorio.setReadOnly(True)
        
        # Botão Gerar Relatório
        self.btnGerarRelatorio = QPushButton("Gerar Relatório de Auditoria", self.tabRelatorio)
        self.btnGerarRelatorio.setObjectName("btnGerarRelatorio")
        self.btnGerarRelatorio.setGeometry(QRect(20, 440, 200, 40))
        
        self.tabWidget.addTab(self.tabRelatorio, "Relatório Gerencial")
        
        self.retranslateUi(MainWindow)
    
    def retranslateUi(self, MainWindow: QMainWindow):
        pass
