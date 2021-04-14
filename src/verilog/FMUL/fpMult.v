`include "wallaceMult.v"
`include "doublingCLA_32.v"

/* -- Module to combine results and handle special cases ----*/
module combineResult(X3, X1, X2, S3, E3, M33);

	// I/O Port Declarations
	output reg[31:0] X3;
	input[31:0] X1, X2;
	input S3;
	input[7:0] E3;
	input[23:0] M33;

	// Condition Check
	always @(X1, X2, S3, E3, M33) begin
		if((&(X1[30:23]) == 1'b1) || (&(X2[30:23]) == 1'b1)) begin
			// NAN Case
			if (((|X1[22:0] == 1'b1) && (&(X1[30:23]) == 1'b1)) || ((|X2[22:0] == 1'b1) && (&(X2[30:23]) == 1'b1)) || (|X1[30:0] == 1'b0) || (|X2[30:0] == 1'b0)) begin
				X3 = 32'b01111111111111111111111111111111;	
			end
			// Inf Case
			else begin 
				X3 = 32'b01111111100000000000000000000000;
			end 
		end 
		// Zero Case
		else if((|(X1[30:0]) == 1'b0) || (|(X2[30:0]) == 1'b0)) begin
			X3 = 32'b00000000000000000000000000000000;
		end
		else begin
			X3[31] = S3;
			X3[30:23] = E3;
			X3[22:0] = M33[22:0];
		end
	end
endmodule

/* --- The single percision floating point Multiplication module ---- */
module fpMult(X3, X1, X2);

	// I/O Port Declarations
	output[31:0] X3;
	input[31:0] X1, X2;

	/*--- Step - 1: Get the components of the floating points  ---- */
	wire S1, S2, S3;
	wire[7:0] E1, E2, E3;
	wire[22:0] M1, M2;

	assign S1 = X1[31];
	assign S2 = X2[31];

	assign E1 = X1[30:23];
	assign E2 = X2[30:23];

	assign M1 = X1[22:0];
	assign M2 = X2[22:0];

	/*--- Step - 2: Set sign bit ---- */
	assign S3 = S1 ^ S2;
	
	/* --- Step - 3: Multiply M1 * M2 ----*/
	wire[23:0] M11, M22;

	assign M11[22:0] = M1;
	assign M11[23] = 1'b1;
	assign M22[22:0] = M2;
	assign M22[23] = 1'b1;

	wire[63:0] M31;
	WM_32 wm32_0(M31, {{8{1'b0}},M11}, {{8{1'b0}},M22});

	wire[47:0] M32;
	assign M32 = M31[47:0];

	/* --- Step - 4: Shift to normalize if necessary and truncate the bits to get a 24 bit manitssa ----*/
	wire[23:0] M33;
	wire flag;
	assign flag = M32[47];
	assign M33 = flag  ? M32[47:24] : M32[46:23];

	/* --- Step - 5: Get the exponent: E3 = E1 + E2 - 127 + shift amt ----*/
	wire[31:0] sum_E1, sum_E2, sum_E3;
	wire cout_E1, cout_E2, cout_E3;
	doublingCLA_32 dcla_0 (sum_E1,cout_E1,{{24{1'b0}},E1},{{24{1'b0}},E2},1'b0);
	doublingCLA_32 dcla_1 (sum_E2,cout_E2,sum_E1,(~({{24{1'b0}},8'd127}) + 1'b1),1'b0);
	assign sum_E3 = sum_E2 + flag;

	assign E3 = sum_E3[7:0];

	/* --- Step - 6: Combine the components & Handle special cases ----*/
	combineResult cr_0(X3, X1, X2, S3, E3, M33);

endmodule
