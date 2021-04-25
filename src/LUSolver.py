import subprocess
import re
import helper

class LUSolve:
	def __init__(self,opcode,opnd1,opnd2,filename="lu_tb.v"):
		self.opnd1 = opnd1
		self.opnd2 = opnd2
		self.filename = filename
		self.opcode = opcode

	def solve(self):
		opNum = 0
		if self.opcode == "AND":
			opNum = 0
		elif self.opcode == "OR":
			opNum = 3
		elif self.opcode == "NAND":
			opNum = 2
		elif self.opcode == "NOR":
			opNum = 5
		elif self.opcode == "XOR":
			opNum = 1 
		elif self.opcode == "NOT":
			opNum = 4
		elif self.opcode == "NEG":
			opNum = 6

		file = self.genLUtb(self.opnd1,self.opnd2,opNum,self.filename)
		cmd = ["iverilog","lu_tb.v"]
		p = subprocess.Popen(cmd,cwd="verilog/LU/")
		p.wait()
		fo = open("output.txt","w")
		subprocess.call(["./a.out"],cwd="verilog/LU/",stdout=fo)
		fo.close()

		fi = open("output.txt","r")
		lines = []
		for line in fi:
			lines.append(line)

		lines = [i for i in lines if len(i.strip()) > 0]
		if len(lines)>1:
			output_str = lines[1].strip()
		else:
			output_str = lines[0].strip()

		result = re.findall(r'[\w+\s+=\s+]\d+',output_str)
		result = list(map(int,result))
		#print('lu',result)

		return result[0]

	def genLUtb(self,opnd1,opnd2,opcode,filename = "lu_tb.v"):
		str = '''\
	`include "logicUnit.v"

	module top;
		reg[31:0] X1,X2;
		reg[2:0] opcode;
		wire[31:0] Y;

		logicUnit LU_0(Y,X1,X2,opcode);

		// Setup the monitoring for the signal values
		initial
		begin
			$monitor($time,"Y = %d\\n",Y);
		end

		// Simulate the inputs
		initial
		begin
			X1 = 0; X2 = 0; opcode = 0;
			#5 opcode = {opc}; X1 = 'd{op1}; X2 = 'd{op2};
		end

	endmodule\
		'''.format(op1 = opnd1, op2 = opnd2, opc = opcode)

		filename = "verilog/LU/" + filename
		fo = open(filename,"w")
		fo.write(str)
		fo.close()

		return filename

#genLUtb(3, 5, 0)