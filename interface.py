from sistema import sistemas
import PySimpleGUI as sg

class Interface:
	def __init__(self):
		layout = [
		[sg.Text('Nome', size=(5,0)), sg.Input(size=(20,0), key='nome')],
		[sg.Text('Telefone', size=(5,0)), sg.Input(size=(20,0), key='telefone')],
		[sg.Text('Email', size=(5,0)), sg.Input(size=(20,0), key='Email')],
		[sg.Button("Enviar dados")],
		[sg.Output(size=(30,10))]
		]
		self.janela = sg.Window('Agenda eletrônica').layout(layout)

	def Iniciar(self):
		while True:
			self.button, self.values = self.janela.Read()
			nome = self.values['nome']
			telefone = self.values['telefone']
			email = self.values['Email']
			print(f'Nome: {nome}')
			print(f'Telefone: {telefone}')
			print(f'Email: {email}')



interface = Interface()
interface.Iniciar()
