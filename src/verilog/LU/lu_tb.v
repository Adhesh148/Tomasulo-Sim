	`include "logicUnit.v"

	module top;
		reg[31:0] X1,X2;
		reg[2:0] opcode;
		wire[31:0] Y;

		logicUnit LU_0(Y,X1,X2,opcode);

		// Setup the monitoring for the signal values
		initial
		begin
			$monitor($time,"Y = %d\n",Y);
		end

		// Simulate the inputs
		initial
		begin
			X1 = 0; X2 = 0; opcode = 0;
			#5 opcode = 4; X1 = 'd9; X2 = 'd0;
		end

	endmodule		