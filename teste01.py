#!/usr/bin/env python

# Usar Python3

# Rascunho do parser de planilhas de horários do Ensino Superior do IFBA
# Rafael F S Requião, Abril/Maio de 2018


# Importar bibliotecas de sempre
import os, sys, io, time, datetime, string
from datetime import date

# Usar interface gráfica com npyscreen
# > http://npyscreen.readthedocs.io/application-structure.html
import npyscreen

# Importar dados da planilha com OpenPyXL
import openpyxl

# Exportar dados... (CSV, JSON, PDF (via TeX)?)


# Definir outras funções


# Definir função principal
def main():
	# Escrever minhas funcoes depois:
	
	#importarPlanilha()
  
  
  	# Teste do npyscreen
  	
	# This application class serves as a wrapper for the initialization of curses
	# and also manages the actual forms of the application

	class MyTestApp(npyscreen.NPSAppManaged):
		def onStart(self):
			self.registerForm("MAIN", MainForm())

	# This form class defines the display that will be presented to the user.

	class MainForm(npyscreen.Form):
		def create(self):
			self.add(npyscreen.TitleText, name = "Text:", value= "Hello World!" )

		def afterEditing(self):
			self.parentApp.setNextForm(None)

	if __name__ == '__main__':
		TA = MyTestApp()
		TA.run()
  
  
  
  
  
# Executar a função principal - parece melhorar velocidade de execução
# > https://twitter.com/jeremybowers/status/984494487371239424

if __name__ == '__main__':
    main()
    exit()