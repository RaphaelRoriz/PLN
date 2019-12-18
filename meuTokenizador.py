 
class MeuTokenizador:
	def __init__(self):

		self.tokens = []
		self.numeroTokens = 0

	def tokenizar(self,texto):
		print("Tokenizar por :" + "\n" + "1 - caracteres" + "\n" + "2 - palavras ")
		resp = input()

		aux = texto.split()
		if(resp == "1"):
			indice = 0
			for x in aux:
				for k in range(len(x)):
					self.tokens.append(Token(indice,x[k]))
					indice +=1
		elif(resp == "2"):
			for i in range(len(aux)):
				self.tokens.append(Token(i,aux[i]))

	def imprimirTokens(self):
		for i in self.tokens:
			i.imprimirToken()

	def apagarTokenPorId(self,id):#corrigir para palavra
		#mudar para while
		for i in self.tokens:
			if(i.id == id):
				del i
				numeroTokens -= 1
				break
			print("ID não encontrado.")

	

	def getTamanhoToken(self , id):
		for i in self.tokens:
			if (id == i.id):
				return i.getTamanhoToken()




class Token:
	def __init__(self,id,conteudo):
		self.id = id
		self.valor = "< "+ str(self.id) + " || "  +conteudo+ " >"
		self.tamanho = len(conteudo)

	def imprimirToken(self):
		print(str(self.valor))

	def getTamanhoToken(self):#retorna tamanho de um token dado o id do mesmo.
		return self.tamanho





tokenizador =  MeuTokenizador()

teste = "exemplo a ser tokenizado por esse s1mpl3s t0k3n1z4d0r o 000 ,, /. :  22"

tokenizador.tokenizar(teste)
tokenizador.imprimirTokens()
tokenizador.apagarTokenPorId(60)
tokenizador.imprimirTokens()
print(tokenizador.getTamanhoToken(0))
