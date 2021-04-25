	`include "fpAdd.v"

	module top;
		reg[31:0] X1,X2;
		wire[31:0] X3;

		fpADD_32 fp_0 (X3 ,X1, X2);

		// Setup the monitoring for the signal values
		initial
		begin
			$monitor($time," X3 = %b\n",X3);
		end

		// Simulate the inputs
		initial
		begin
			X1 = 0; X2 = 0;
			#5 X2 = 32'b01000010001000000000000000000000; X1 = 32'b11000000101000000000000000000000;
		end

	endmodule		