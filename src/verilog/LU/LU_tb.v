`include "logicUnit.v"

module top;
	reg[31:0] X1,X2;
	reg[2:0] opcode;
	wire[31:0] Y;

	logicUnit LU_0(Y,X1,X2,opcode);

	// Setup the monitoring for the signal values
	initial
	begin
		$monitor($time," opcode = %b,  X1 = %b,  X2 = %b --- Y = %b\n",opcode,X1,X2,Y);
		$dumpfile("LU.vcd");
		$dumpvars;
	end

	// Simulate the inputs
	initial
	begin
		X1 = 0; X2 = 0; opcode = 0;

		// Bitwise AND
		#5 opcode = 0; X1 = 32'b1000_1001_1100_0011_1111_0000_1011_0101; X2 = 32'b1000_0000_1111_0000_1111_0000_0000_1111;

		// Bitwise XOR
		#5 opcode = 1; X1 = 32'b1000_1001_1100_0011_1111_0000_1011_0101; X2 = 32'b1000_0000_1111_0000_1111_0000_0000_1111;

		// Bitwise NAND
		#5 opcode = 2; X1 = 32'b1101; X2 = 32'b1010;

		// Bitwise OR
		#5 opcode = 3; X1 = 32'b1101; X2 = 32'b1010;

		// Bitwise NOT of X1
		#5 opcode = 4; X1 = 32'b11001;

		// Bitwise NOR
		#5 opcode = 5; X1 = 32'b1101; X2 = 32'b1010;

		// 2s complement of X1
		#5 opcode = 6; X1 = 32'b1100;

		// Bitwise XNOR
		#5 opcode = 7; X1 = 32'b1101; X2 = 32'b1010;

	end

endmodule


