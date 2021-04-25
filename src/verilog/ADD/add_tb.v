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
			$monitor($time," C = %b,S = %b\n",Cout,Sum);
		end

		// Simulate the inputs
		initial
		begin
				A = 0; B = 0; Cin = 0;
			#5 A = 'b00000000000000000000000000001001; B = 'b11111111111111111111111111111100;
		end

	endmodule		