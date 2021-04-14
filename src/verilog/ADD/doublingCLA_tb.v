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
		$monitor($time," A = %d,  B = %d --- Cout = %b, Sum = %d\n",A,B,Cout,Sum);
		$dumpfile("doublingCLA_32.vcd");
		$dumpvars;
	end

	// Simulate the inputs
	initial
	begin
		A = 0; B = 0; Cin = 0;

		#5 A = 'd2; B = 'd5;

		#5 A = 'd10; B = 'd21;

		#5 A = 'd127; B = 'd200;

		#5 A = 'd100; B = 'd21;

		#5 A = 'd5123; B = 'd2324;

		#5 A = 'd9999; B = 'd999;

		#5 A = 'd1147483647; B = 'd1147483648;
	 
	end

endmodule
