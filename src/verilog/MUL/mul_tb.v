	`include  "wallaceMult.v"

	module top;
		reg[31:0] A,B;
		wire[63:0] product;

		WM_32 wm0(product,A,B);

		initial
		begin
			$monitor($time," product = %d\n",product);
		end

		initial
		begin
			A = 0; B = 0;

			#5 A = 'd9; B = 'd6;
		end

	endmodule		