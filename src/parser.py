import re

class myParser:

	def __init__(self, filename, mode = 'r'):
		self.filename = filename
		self.mode = mode

		# Create a file object
		self.fo = open(filename,mode)

	def getNextInstr(self,):
		return self.fo.readline().strip()

	def splitInstr(self,instr_str):
		instr_args = []						# initialize an empty list to store the instruction arguments
		eos = [" ",",",";"]					# define characters that mark end of str

		# extract the args from the instr_str into the list
		temp = ""
		for char in instr_str:
			if char not in eos:
				temp = temp + char
			else:
				if len(temp) != 0:
					instr_args.append(temp)
				temp = ""

		return instr_args

	def extractAll(self,):

		# Goto head of file
		self.fo.seek(0, 0)

		# maintain a list that stores the args from all instr
		instr_all = []

		for line in self.fo:
			instr_all.append(self.splitInstr(line.strip()))

		return instr_all



