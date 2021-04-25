import subprocess
import re
import helper

class MULSolve:
	def __init__(self,opnd1,opnd2,filename="mul_tb.v"):
		self.opnd1 = opnd1
		self.opnd2 = opnd2
		self.filename = filename

	def solve(self):
		flag = 0

		if self.opnd1 < 0 and self.opnd2 < 0:
			self.opnd1 = self.opnd1 * -1
			self.opnd2 = self.opnd2 * -1
			flag = 1

		elif self.opnd1 < 0:
			self.opnd1 = self.opnd1 * -1
			flag = 2

		elif self.opnd2 < 0:
			self.opnd2 = self.opnd2 * -1
			flag = 3

		file = self.genMULtb(self.opnd1,self.opnd2,self.filename)
		cmd = ["iverilog","mul_tb.v"]
		p = subprocess.Popen(cmd,cwd="verilog/MUL/")
		p.wait()
		fo = open("output.txt","w")
		subprocess.call(["./a.out"],cwd="verilog/MUL/",stdout=fo)
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
		
		product = result[0]
		if flag == 2 or flag == 3:
			product = product * -1

		return product

	def genMULtb(self,opnd1,opnd2,filename = "mul_tb.v"):
		str = '''\
	`include  "wallaceMult.v"

	module top;
		reg[31:0] A,B;
		wire[63:0] product;

		WM_32 wm0(product,A,B);

		initial
		begin
			$monitor($time," product = %d\\n",product);
		end

		initial
		begin
			A = 0; B = 0;

			#5 A = 'd{op1}; B = 'd{op2};
		end

	endmodule\
		'''.format(op1 = opnd1, op2 = opnd2)

		filename = "verilog/MUL/" + filename
		fo = open(filename,"w")
		fo.write(str)
		fo.close()

		return filename

#obj = MULSolve(-3, 7)
#r = obj.solve()
#print(r)