import sys
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QDoubleSpinBox, 
    QPushButton, QLineEdit, QComboBox, QTextEdit, QMessageBox, QTableWidgetItem
)
from projeto_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registros = []  # Armazena registros salvos
        self.modo_edicao = False
        self.registro_selecionado = None
        
        # Inicializa a tabela de salários
        self.inicializar_tabela_salarios()
        
        # Conecta todos os botões
        self.btnNovo.clicked.connect(self.novo_registro)
        self.btnEditar.clicked.connect(self.editar_registro)
        self.btnExcluir.clicked.connect(self.excluir_registro)
        self.btnSalvar.clicked.connect(self.salvar_registro)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.btnGerarRelatorio.clicked.connect(self.gerar_relatorio)
        
        # Conecta clique na tabela de funcionários
        self.tableFuncionarios.cellClicked.connect(self.carrega_registro_da_tabela)
        
        # Estado inicial: campos desabilitados
        self.habilitar_campos(False)
        self.atualizar_tabela_funcionarios()
    
    def inicializar_tabela_salarios(self):
        """Configura a tabela com 12 colunas de meses e insere SpinBoxes"""
        self.tableSalarios.setRowCount(1)
        self.tableSalarios.setColumnCount(12)
        self.tableSalarios.setHorizontalHeaderLabels(
            ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
        )
        
        for mes in range(12):
            spinbox = QDoubleSpinBox()
            spinbox.setRange(0.0, 100000.0)
            spinbox.setDecimals(2)
            spinbox.setPrefix("R$ ")
            self.tableSalarios.setCellWidget(0, mes, spinbox)
    
    def habilitar_campos(self, habilitado: bool):
        """Habilita/desabilita campos de entrada"""
        self.lineMatricula.setEnabled(habilitado)
        self.lineNome.setEnabled(habilitado)
        self.comboGenero.setEnabled(habilitado)
        self.comboDepartamento.setEnabled(habilitado)
        
        # Habilita/desabilita spinboxes da tabela
        for mes in range(12):
            widget = self.tableSalarios.cellWidget(0, mes)
            if widget is not None:
                widget.setEnabled(habilitado)
    
    def novo_registro(self):
        """Inicia um novo registro - habilita campos e limpa"""
        self.modo_edicao = True
        self.registro_selecionado = None
        self.tableFuncionarios.clearSelection()
        self.habilitar_campos(True)
        self.limpar_campos()
        self.lineMatricula.setFocus()
    
    def editar_registro(self):
        """Habilita edição do registro atual"""
        if not self.lineMatricula.text():
            QMessageBox.warning(self, "Aviso", "Selecione um registro para editar!")
            return
        self.modo_edicao = True
        self.habilitar_campos(True)
    
    def excluir_registro(self):
        """Exclui o registro selecionado na tabela"""
        if self.tableFuncionarios.currentRow() < 0:
            QMessageBox.warning(self, "Aviso", "Selecione um funcionário para excluir!")
            return
        
        matricula = self.lineMatricula.text().strip()
        nome = self.lineNome.text().strip()
        
        if not matricula:
            QMessageBox.warning(self, "Aviso", "Nenhum funcionário selecionado!")
            return
        
        reply = QMessageBox.question(
            self, "Confirmar Exclusão", 
            f"Deseja excluir o funcionário:\n\nMatrícula: {matricula}\nNome: {nome}"
        )
        if reply == QMessageBox.Yes:
            self.registros = [r for r in self.registros if r['matricula'] != matricula]
            self.limpar_campos()
            self.atualizar_tabela_funcionarios()
            self.habilitar_campos(False)
            QMessageBox.information(self, "Sucesso", "Funcionário excluído com sucesso!")
    
    def salvar_registro(self):
        """Salva/atualiza o registro"""
        matricula = self.lineMatricula.text().strip()
        nome = self.lineNome.text().strip()
        genero = self.comboGenero.currentText()
        departamento = self.comboDepartamento.currentText()
        
        if not matricula or not nome:
            QMessageBox.warning(self, "Erro", "Matrícula e Nome são obrigatórios!")
            return
        
        # Coleta os salários
        salarios = []
        for mes in range(12):
            widget = self.tableSalarios.cellWidget(0, mes)
            if widget is not None:
                salarios.append(widget.value())
            else:
                salarios.append(0.0)
        
        # Remove registro anterior se existir
        self.registros = [r for r in self.registros if r['matricula'] != matricula]
        
        # Adiciona novo registro
        registro = {
            'matricula': matricula,
            'nome': nome,
            'genero': genero,
            'departamento': departamento,
            'salarios': salarios
        }
        self.registros.append(registro)
        
        self.modo_edicao = False
        self.registro_selecionado = None
        self.habilitar_campos(False)
        self.atualizar_tabela_funcionarios()
        self.limpar_campos()
        QMessageBox.information(self, "Sucesso", "Funcionário salvo com sucesso!")
    
    def cancelar(self):
        """Cancela a edição"""
        self.modo_edicao = False
        self.registro_selecionado = None
        self.tableFuncionarios.clearSelection()
        self.habilitar_campos(False)
        self.limpar_campos()
    
    def atualizar_tabela_funcionarios(self):
        """Atualiza a tabela com lista de funcionários"""
        self.tableFuncionarios.setRowCount(len(self.registros))
        
        for row, registro in enumerate(self.registros):
            self.tableFuncionarios.setItem(row, 0, QTableWidgetItem(registro['matricula']))
            self.tableFuncionarios.setItem(row, 1, QTableWidgetItem(registro['nome']))
            self.tableFuncionarios.setItem(row, 2, QTableWidgetItem(registro['genero']))
            self.tableFuncionarios.setItem(row, 3, QTableWidgetItem(registro['departamento']))
        
        # Ajusta tamanho das colunas
        self.tableFuncionarios.resizeColumnsToContents()
    
    def carrega_registro_da_tabela(self, row, column):
        """Carrega dados do funcionário selecionado na tabela"""
        if row < 0 or row >= len(self.registros):
            return
        
        self.registro_selecionado = self.registros[row]
        registro = self.registro_selecionado
        
        # Preenche os campos
        self.lineMatricula.setText(registro['matricula'])
        self.lineNome.setText(registro['nome'])
        self.comboGenero.setCurrentText(registro['genero'])
        self.comboDepartamento.setCurrentText(registro['departamento'])
        
        # Preenche os salários
        for mes, valor in enumerate(registro['salarios']):
            widget = self.tableSalarios.cellWidget(0, mes)
            if widget is not None:
                widget.setValue(valor)
    
    def limpar_campos(self):
        """Limpa todos os campos"""
        self.lineMatricula.clear()
        self.lineNome.clear()
        self.comboGenero.setCurrentIndex(0)
        self.comboDepartamento.setCurrentIndex(0)
        
        for mes in range(12):
            widget = self.tableSalarios.cellWidget(0, mes)
            if widget is not None:
                widget.setValue(0.0)
    
    def gerar_relatorio(self):
        """Gera um relatório com todos os registros"""
        if not self.registros:
            QMessageBox.information(self, "Relatório", "Nenhum registro salvo!")
            self.textRelatorio.setText("Nenhum registro para gerar relatório.")
            return
        
        relatorio = f"RELATÓRIO DE AUDITORIA\n"
        relatorio += f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        relatorio += "=" * 80 + "\n\n"
        
        total_geral = 0.0
        
        for idx, registro in enumerate(self.registros, 1):
            relatorio += f"{idx}. Matrícula: {registro['matricula']}\n"
            relatorio += f"   Nome: {registro['nome']}\n"
            relatorio += f"   Gênero: {registro['genero']}\n"
            relatorio += f"   Departamento: {registro['departamento']}\n"
            relatorio += "   Salários:\n"
            
            meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
            total_funcionario = 0.0
            
            for mes, valor in zip(meses, registro['salarios']):
                relatorio += f"      {mes}: R$ {valor:,.2f}\n"
                total_funcionario += valor
            
            relatorio += f"   Total Anual: R$ {total_funcionario:,.2f}\n"
            relatorio += "-" * 80 + "\n"
            total_geral += total_funcionario
        
        relatorio += f"\nTOTAL GERAL (todos os funcionários): R$ {total_geral:,.2f}\n"
        self.textRelatorio.setText(relatorio)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())