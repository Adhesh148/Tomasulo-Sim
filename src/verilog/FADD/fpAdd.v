`include "doublingCLA_32.v"
`include "barrelShift_64.v"

/* A Swapper module to ensure that |X11| > |X22| */
module compareNSwap(X11, X22, X1, X2);
	
	// I/O Port Declarations
	output reg[31:0] X11, X22;
	input [31:0] X1, X2;

	// Compare n swap
	always @(X1 or X2) begin
		if(X1[30:0] > X2[30:0]) begin
			X11 <= X1;
			X22 <= X2;
		end else begin
			X11 <= X2;
			X22 <= X1;
		end
	end
endmodule

/* A module to find the amt of shift in mantissa */
module shiftMantissa(shift, D);

	// I/O Port Declarations
	output reg[5:0] shift;
	input[7:0] D;

	// If D > 24 then just set shift to 24
	always @(D) begin
		if(D <= 'd23) begin
			shift = D[5:0];
		end else begin
			shift = 'd23;
		end
	end
endmodule

/* A module to get the mantissa based on the operation performed*/
module getMantissa(M24, sum_M, flag);
	
	// I/O Port Declarations
	output reg[23:0] M24;
	input[31:0] sum_M;
	input flag;

	// Condition check
	always @(flag or sum_M) begin
		if(flag == 1'b1 && sum_M[24] == 1'b0) begin
			M24 = ~sum_M[23:0] + 1'b1;
		end else begin
			M24 = sum_M[23:0];
		end
	end
endmodule

/* Module to get the shift amt to normalize - Find leading 1*/
module normalizeMantissa(shift_1, ZF ,M24, flag, carry);

	// I/O Port Declarations
	output reg[5:0] shift_1;
	output reg ZF;
	input[23:0] M24;
	input flag, carry;

	// Condition check
	always @(flag or M24) begin
		if(flag == 1'b1) begin
			if (M24[23] == 1'b1) begin
				shift_1 = 'd0;
				ZF = 1'b0;
			end
			else if (M24[22] == 1'b1) begin
				shift_1 = 'd1;
				ZF = 1'b0;
			end
			else if (M24[21] == 1'b1) begin
				shift_1 = 'd2;
				ZF = 1'b0;
			end
			else if (M24[20] == 1'b1) begin
				shift_1 = 'd3;
				ZF = 1'b0;
			end
			else if (M24[19] == 1'b1) begin
				shift_1 = 'd4;
				ZF = 1'b0;
			end
			else if (M24[18] == 1'b1) begin
				shift_1 = 'd5;
				ZF = 1'b0;
			end
			else if (M24[17] == 1'b1) begin
				shift_1 = 'd6;
				ZF = 1'b0;
			end
			else if (M24[16] == 1'b1) begin
				shift_1 = 'd7;
				ZF = 1'b0;
			end
			else if (M24[15] == 1'b1) begin
				shift_1 = 'd8;
				ZF = 1'b0;
			end
			else if (M24[14] == 1'b1) begin
				shift_1 = 'd9;
				ZF = 1'b0;
			end
			else if (M24[13] == 1'b1) begin
				shift_1 = 'd10;
				ZF = 1'b0;
			end
			else if (M24[12] == 1'b1) begin
				shift_1 = 'd11;
				ZF = 1'b0;
			end
			else if (M24[11] == 1'b1) begin
				shift_1 = 'd12;
				ZF = 1'b0;
			end
			else if (M24[10] == 1'b1) begin
				shift_1 = 'd13;
				ZF = 1'b0;
			end
			else if (M24[9] == 1'b1) begin
				shift_1 = 'd14;
				ZF = 1'b0;
			end
			else if (M24[8] == 1'b1) begin
				shift_1 = 'd15;
				ZF = 1'b0;
			end
			else if (M24[7] == 1'b1) begin
				shift_1 = 'd16;
				ZF = 1'b0;
			end
			else if (M24[6] == 1'b1) begin
				shift_1 = 'd17;
				ZF = 1'b0;
			end
			else if (M24[5] == 1'b1) begin
				shift_1 = 'd18;
				ZF = 1'b0;
			end
			else if (M24[4] == 1'b1) begin
				shift_1 = 'd19;
				ZF = 1'b0;
			end
			else if (M24[3] == 1'b1) begin
				shift_1 = 'd20;
				ZF = 1'b0;
			end
			else if (M24[2] == 1'b1) begin
				shift_1 = 'd21;
				ZF = 1'b0;
			end
			else if (M24[1] == 1'b1) begin
				shift_1 = 'd22;
				ZF = 1'b0;
			end
			else if (M24[0] == 1'b1) begin
				shift_1 = 'd23;
				ZF = 1'b0;
			end
			else begin
				shift_1 = 'd0;
				ZF = 1'b1;
			end
		end else begin
			shift_1 = carry;
			ZF = 1'b0;
		end
	end
endmodule

/* The floating point Adder module */
module fpADD_32(X3, X1, X2);

	// I/O Port Declarations
	output [31:0] X3;
	input [31:0] X1, X2;

	/*--- Step - 1: Check if |X1| > |X2| , if not swap ---*/
	wire[31:0] X11, X22;
	compareNSwap cmp_0(X11,X22,X1,X2);

	// Get the components of the floating points
	wire S1, S2, S3;
	wire[7:0] E1, E2, E3;
	wire[22:0] M1, M2, M3;

	assign S1 = X11[31];
	assign S2 = X22[31];

	assign E1 = X11[30:23];
	assign E2 = X22[30:23];

	assign M1 = X11[22:0];
	assign M2 = X22[22:0];

	/*--- Step - 2: Set E3 and S3 ---- */
	assign S3 = S1;
	assign E3 = E1;

	/* --- Step - 3: Compute D = E1 - E2 ---*/
	wire[7:0] D;
	wire[31:0] sum_d;
	wire cout_d;
	
	doublingCLA_32 dcla_0 (sum_d,cout_d,{{24{1'b0}},E1},{{24{1'b0}},(~E2)+1'b1},1'b0);
	assign D = sum_d[7:0];

	/* -- Step - 4: Left Shift M2 by D 	---*/
	wire[23:0] M11, M21, M22;

	assign M11[22:0] = M1;
	assign M11[23] = 1'b1;

	assign M21[22:0] = M2;
	assign M21[23] = 1'b1;

	wire[63:0] temp;
	wire[5:0] shift;
	shiftMantissa sm_0(shift,D);
	barrelShift_64 bs64_0(temp,{{40{1'b0}},M21},(~shift + 1'b1));
	assign M22 = temp[23:0];

	/* ---- Step - 5: Compute the Sum/Difference of the Mantissa (24 bits) --- */
	wire[23:0] M23;
	wire flag;

	assign flag = S1 ^ S2;
	assign M23 = flag ? (~M22 + 1'b1) : M22;

	wire[31:0] sum_M;
	wire cout_M;

	// Addition/Subtraction of Mantissas
	doublingCLA_32 dcla_1 (sum_M,cout_M,{{8{1'b0}},M11},{{8{1'b0}},M23},1'b0);

	// Get the 2s complement of sum_M in M23 if the operation was subtraction and there was no overflow
	wire [23:0] M24;
	getMantissa gm_0(M24, sum_M, flag);

	// Normalize the mantissa
	wire [5:0] shift_1, shift_2;
	wire ZF;
	normalizeMantissa nm_0(shift_1, ZF, M24,flag, sum_M[24]);

	wire[63:0] temp_1;
	wire [23:0] M25;
	assign shift_2 = flag ? shift_1 : (~shift_1 + 1'b1);
	barrelShift_64 bs64_1(temp_1,{{40{1'b0}},M24}, shift_2);
	assign M25 = temp_1[23:0];

	wire[7:0] shift_3;
	assign shift_3 = flag ? (~({{2{1'b0}},shift_1}) + 1'b1) : {{2{1'b0}},shift_1};

	// Set the bits into X3
	assign X3[31] = S3;
	assign X3[22:0] = M25[22:0];
	assign X3[30:23] = ZF ? 'b0: (E3 + shift_3);

endmodule