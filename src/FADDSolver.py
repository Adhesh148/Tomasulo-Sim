import subprocess
import re
import helper
import ieee2float
import float2ieee

class FADDSolve:

	def __init__(self,opcode,opnd1,opnd2,filename='fadd_tb.v'):
		self.opcode = opcode
		self.opnd1 = opnd1
		self.opnd2 = opnd2
		self.filename = filename

	def solve(self):

		if self.opcode == "FSUB":
			self.opnd2 = self.opnd2 * -1

		ie1 = float2ieee.IEEE754(self.opnd1)
		ie2 = float2ieee.IEEE754(self.opnd2)
		#print(ie1,ie2)
		
		file = self.genFADDtb(ie1,ie2,self.filename)
		cmd = ["iverilog",self.filename]
		p = subprocess.Popen(cmd,cwd="verilog/FADD/")
		p.wait()
		fo = open("output.txt","w")
		subprocess.call(["./a.out"],cwd="verilog/FADD/",stdout=fo)
		fo.close()

		fi = open("output.txt","r")
		lines = []
		for line in fi:
			lines.append(line)

		#print(lines)
		lines = [i for i in lines if len(i.strip()) > 0]
		if len(lines)>1:
			output_str = lines[1].strip()
		else:
			output_str = lines[0].strip()
		result = re.findall(r'[\w+\s+=\s+]\d+',output_str)
		result = list(map(str,result))
		result_flt = ieee2float.ieee2float(result[1].strip())

		return result_flt

	def genFADDtb(self,opnd1,opnd2,filename = 'fadd_tb.v'):
		str = '''\
	`include "fpAdd.v"

	module top;
		reg[31:0] X1,X2;
		wire[31:0] X3;

		fpADD_32 fp_0 (X3 ,X1, X2);

		// Setup the monitoring for the signal values
		initial
		begin
			$monitor($time," X3 = %b\\n",X3);
		end

		// Simulate the inputs
		initial
		begin
			X1 = 0; X2 = 0;
			#5 X2 = 32'b{op1}; X1 = 32'b{op2};
		end

	endmodule\
		'''.format(op1 = opnd1, op2 = opnd2)

		filename = "verilog/FADD/" + filename
		fo = open(filename,"w")
		fo.write(str)
		fo.close()

		return filename

#obj = FADDSolve(opcode="FADD",opnd1=13.0,opnd2=7.1)
#r = obj.solve()
#print(r)