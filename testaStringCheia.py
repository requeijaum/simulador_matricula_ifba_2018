import io, sys, string

def testaStringCheia(string, modo):  # (string, 1) é meu preferido
	
	teste = None
	lista_teste = []
	
	print(type(string))

	if isinstance(string, str): #saber se tá vazio
		for letra in string:
			lista_teste.append(bool(letra))
			
			if letra != " ":
				teste = True
			
			if modo == 1 : # limitar string apenas a segurar letras, sem numeros
				
				if letra.isnumeric() == True :
					#print(letra.isnumeric)
					teste = False
					
			else:
				teste = False
				
		
		print(lista_teste)
		#for booleano in lista_teste:
		#	if booleano == True:
		#		print(booleano + " não é vazio.")
					
		
				
	else:
		print("[DEBUG] testeStringCheia diz que você entrou com:")
		print(type(string))		
		
		
	if teste == True :
		print("[DEBUG] testaStringCheia() = True")
		return True
		
		
	else:
		print("[DEBUG] testaStringCheia() = False")
		return False	



def main():
	testaStringCheia(input("Entre com uma string:\n   --> ") , 1)			


			
if __name__ == '__main__':
    main()





