`include  "wallaceMult.v"

module top;
	reg[31:0] A,B;
	wire[63:0] product;

	WM_32 wm0(product,A,B);

	initial
	begin
		$monitor($time," A = %d, B = %d, product = %d",A,B,product);
		$dumpfile("wallaceMult.vcd");
		$dumpvars;
	end

	initial
	begin
		A = 0; B = 0;

		#5 A = 'd3; B = 'd7;

		#5 A = 'd13; B = 'd12;

		#5 A = 'd3123; B = 'd732;

		#5 A = 'd13; B = 'd337;

		#5 A = 'd99999; B = 'd999999;

		#5 A = 'd2147483643; B = 'd2147483643;

		 

	end

endmodule
