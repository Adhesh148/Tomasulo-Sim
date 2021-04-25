import subprocess
import re
import helper

class ADDSolve:

	def __init__(self,op, opnd1,opnd2, filename = "add_tb.v"):
		self.op = op
		self.opnd1 = opnd1
		self.opnd2 = opnd2
		self.filename = filename

	def solve(self):
		flag = 0
	
		if self.op == "SUB" or self.op == "SUBB":
			self.opnd2 = -1 * self.opnd2

		bin1 = '{:032b}'.format(self.opnd1)
		bin2 = '{:032b}'.format(self.opnd2)

		if self.opnd1 < 0 and self.opnd2 < 0:
			self.opnd1 = self.opnd1 * -1
			self.opnd2 = self.opnd2 * -1
			bin1 = '{:032b}'.format(self.opnd1)
			bin2 = '{:032b}'.format(self.opnd2)
			flag = 1

		elif self.opnd1 < 0:
			self.opnd1 = self.opnd1 * -1
			bin1 = helper.negate(self.opnd1)
			bin2 = '{:032b}'.format(self.opnd2)
			flag = 2

		elif self.opnd2 < 0:
			self.opnd2 = self.opnd2 * -1
			bin1 = '{:032b}'.format(self.opnd1)
			bin2 = helper.negate(self.opnd2)
			flag = 3

		file = self.genADDtb(bin1,bin2,self.filename)
		cmd = ["iverilog","add_tb.v"]
		p = subprocess.Popen(cmd,cwd="verilog/ADD/")
		p.wait()
		fo = open("output.txt","w")
		subprocess.call(["./a.out"],cwd="verilog/ADD/",stdout=fo)
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
		#print('res',lines)
		
		carry = result[0]
		summ = int(str(result[1]),2)
		if flag == 1:
			summ = summ *-1
		if flag == 2 or flag == 3:
			if carry == 0:
				new_result = helper.negate(summ)
				summ = -1 * int(str(new_result),2)
		#print(result)

		if self.op == "ADD":
			return summ
		elif self.op == "ADDC":
			return (summ + carry)
		elif self.op == "SUB":
			return summ
		elif self.op == "SUBB":
			return (summ + carry)

	def genADDtb(self,opnd1,opnd2,filename):
		str = '''\
	`include "doublingCLA_32.v"

	module top;
		reg[31:0] A,B;
		reg Cin;
		wire[31:0] Sum;
		wire Cout;

		doublingCLA_32 dcla_0 (Sum,Cout,A,B,Cin);

		// Setup the monitoring for the signal values
		initial
		begin
			$monitor($time," C = %b,S = %b\\n",Cout,Sum);
		end

		// Simulate the inputs
		initial
		begin
				A = 0; B = 0; Cin = 0;
			#5 A = 'b{op1}; B = 'b{op2};
		end

	endmodule\
		'''.format(op1 = opnd1, op2 = opnd2)

		filename = "verilog/ADD/" + filename
		fo = open(filename,"w")
		fo.write(str)
		fo.close()

		return filename

#genADDtb(3, 5)
#obj = ADDSolve("SUB", 3, 5)
#r = obj.solve()
#print(r)