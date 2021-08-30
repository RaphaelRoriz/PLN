import sys
import os

class FrequencySearcher:

	def __init__(self, directory_path, search_string):

		self.texts_path = directory_path
		self.search_string = search_string

		self.corpus = {}
		self.corpus['raw_texts'] = []
		
	def read_text(self,file_path):
		with open(file_path, 'r') as f:
			# print(f.read())
			self.corpus['raw_texts'].append(f.read())
	
	def read_texts(self):

		os.chdir(self.texts_path)

		print(self.texts_path)
		print(self.search_string)
		print("oh droga")

		for file in os.listdir():
			print(file)
			if file.endswith(".txt"):
				# file_path = f"{self.texts_path}/{file}"
				self.read_text(file)

		print("corpus")
		for text in self.corpus['raw_texts']:
			print('texto')
			print(text)


	# def preProcessing(self):
		
	# def log(self):

	# 	numPacotesRecebidos = len(self.rttsIndividuais)
		
	# 	if (numPacotesRecebidos != 0):
	# 		rttMedio = sum(self.rttsIndividuais) / numPacotesRecebidos 
	# 		taxaPerdaDePacotes = (1 - (numPacotesRecebidos / float(self.numPacotes))) * 100
	# 	else:
	# 		rttMedio = "indefinido"
	# 		taxaPerdaDePacotes = 100
	# 		print "Todos os pacotes foram perdidos!"

	# 	print "\nLOG"
	# 	print "--RTT medio:", rttMedio 
	# 	print"--Taxa de perda de pacotes:", taxaPerdaDePacotes, "%"  


if __name__ == "__main__":

	directory_path = sys.argv[1]
	search_string = sys.argv[2]

	# print(directory_path)
	# print(search_string)

	freq_searcher = FrequencySearcher(directory_path,search_string)
	freq_searcher.read_texts()

	# frequency_searcher = FrequencySearcher()



#fontes para o desenvolvimento do trabalho:
#   https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
#   
