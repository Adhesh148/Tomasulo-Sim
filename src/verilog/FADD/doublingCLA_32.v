module parallelPrefixCkt(Y,A,B);
	output reg[1:0] Y;
	input[1:0] A,B;

	always @(A or B)
	begin
		if(A == 2'b00 || A == 2'b11)
			assign Y = A;
		else
			assign Y = B;
	end
endmodule

module doublingCLA_32(Sum,Cout,A,B,Cin);

	// I/O Port Declarations
	output [31:0] Sum;
	output Cout;
	input [31:0] A;
	input [31:0] B;
	input Cin;

	// define the initial block of KGP
	wire [1:0] x_00;
	assign x_00 = {2{Cin}};

	// First let us compute the XOR-Sum of A and B
	wire [31:0] xorSum,carry;
	assign xorSum = A ^ B;

	// Define the KGP wires
	wire[1:0] x_0[31:0];
	wire[1:0] x_1[31:0];
	wire[1:0] x_2[31:0];
	wire[1:0] x_3[31:0];
	wire[1:0] x_4[31:0];
	wire[1:0] x_5[31:0];

	// Assign the first KGP values
	assign x_0[0][0] = A[0];
	assign x_0[1][0] = A[1];
	assign x_0[2][0] = A[2];
	assign x_0[3][0] = A[3];
	assign x_0[4][0] = A[4];
	assign x_0[5][0] = A[5];
	assign x_0[6][0] = A[6];
	assign x_0[7][0] = A[7];
	assign x_0[8][0] = A[8];
	assign x_0[9][0] = A[9];
	assign x_0[10][0] = A[10];
	assign x_0[11][0] = A[11];
	assign x_0[12][0] = A[12];
	assign x_0[13][0] = A[13];
	assign x_0[14][0] = A[14];
	assign x_0[15][0] = A[15];
	assign x_0[16][0] = A[16];
	assign x_0[17][0] = A[17];
	assign x_0[18][0] = A[18];
	assign x_0[19][0] = A[19];
	assign x_0[20][0] = A[20];
	assign x_0[21][0] = A[21];
	assign x_0[22][0] = A[22];
	assign x_0[23][0] = A[23];
	assign x_0[24][0] = A[24];
	assign x_0[25][0] = A[25];
	assign x_0[26][0] = A[26];
	assign x_0[27][0] = A[27];
	assign x_0[28][0] = A[28];
	assign x_0[29][0] = A[29];
	assign x_0[30][0] = A[30];
	assign x_0[31][0] = A[31];

	assign x_0[0][1] = B[0];
	assign x_0[1][1] = B[1];
	assign x_0[2][1] = B[2];
	assign x_0[3][1] = B[3];
	assign x_0[4][1] = B[4];
	assign x_0[5][1] = B[5];
	assign x_0[6][1] = B[6];
	assign x_0[7][1] = B[7];
	assign x_0[8][1] = B[8];
	assign x_0[9][1] = B[9];
	assign x_0[10][1] = B[10];
	assign x_0[11][1] = B[11];
	assign x_0[12][1] = B[12];
	assign x_0[13][1] = B[13];
	assign x_0[14][1] = B[14];
	assign x_0[15][1] = B[15];
	assign x_0[16][1] = B[16];
	assign x_0[17][1] = B[17];
	assign x_0[18][1] = B[18];
	assign x_0[19][1] = B[19];
	assign x_0[20][1] = B[20];
	assign x_0[21][1] = B[21];
	assign x_0[22][1] = B[22];
	assign x_0[23][1] = B[23];
	assign x_0[24][1] = B[24];
	assign x_0[25][1] = B[25];
	assign x_0[26][1] = B[26];
	assign x_0[27][1] = B[27];
	assign x_0[28][1] = B[28];
	assign x_0[29][1] = B[29];
	assign x_0[30][1] = B[30];
	assign x_0[31][1] = B[31];

	// 1st Stage of KGP - Recursive Doubling
	parallelPrefixCkt p0_31(x_1[31],x_0[31],x_0[30]);
	parallelPrefixCkt p0_30(x_1[30],x_0[30],x_0[29]);
	parallelPrefixCkt p0_29(x_1[29],x_0[29],x_0[28]);
	parallelPrefixCkt p0_28(x_1[28],x_0[28],x_0[27]);
	parallelPrefixCkt p0_27(x_1[27],x_0[27],x_0[26]);
	parallelPrefixCkt p0_26(x_1[26],x_0[26],x_0[25]);
	parallelPrefixCkt p0_25(x_1[25],x_0[25],x_0[24]);
	parallelPrefixCkt p0_24(x_1[24],x_0[24],x_0[23]);
	parallelPrefixCkt p0_23(x_1[23],x_0[23],x_0[22]);
	parallelPrefixCkt p0_22(x_1[22],x_0[22],x_0[21]);
	parallelPrefixCkt p0_21(x_1[21],x_0[21],x_0[20]);
	parallelPrefixCkt p0_20(x_1[20],x_0[20],x_0[19]);
	parallelPrefixCkt p0_19(x_1[19],x_0[19],x_0[18]);
	parallelPrefixCkt p0_18(x_1[18],x_0[18],x_0[17]);
	parallelPrefixCkt p0_17(x_1[17],x_0[17],x_0[16]);
	parallelPrefixCkt p0_16(x_1[16],x_0[16],x_0[15]);
	parallelPrefixCkt p0_15(x_1[15],x_0[15],x_0[14]);
	parallelPrefixCkt p0_14(x_1[14],x_0[14],x_0[13]);
	parallelPrefixCkt p0_13(x_1[13],x_0[13],x_0[12]);
	parallelPrefixCkt p0_12(x_1[12],x_0[12],x_0[11]);
	parallelPrefixCkt p0_11(x_1[11],x_0[11],x_0[10]);
	parallelPrefixCkt p0_10(x_1[10],x_0[10],x_0[9]);
	parallelPrefixCkt p0_9(x_1[9],x_0[9],x_0[8]);
	parallelPrefixCkt p0_8(x_1[8],x_0[8],x_0[7]);
	parallelPrefixCkt p0_7(x_1[7],x_0[7],x_0[6]);
	parallelPrefixCkt p0_6(x_1[6],x_0[6],x_0[5]);
	parallelPrefixCkt p0_5(x_1[5],x_0[5],x_0[4]);
	parallelPrefixCkt p0_4(x_1[4],x_0[4],x_0[3]);
	parallelPrefixCkt p0_3(x_1[3],x_0[3],x_0[2]);
	parallelPrefixCkt p0_2(x_1[2],x_0[2],x_0[1]);
	parallelPrefixCkt p0_1(x_1[1],x_0[1],x_0[0]);
	parallelPrefixCkt p0_0(x_1[0],x_0[0],x_00);


	// 2nd stage of KGP
	parallelPrefixCkt p1_31(x_2[31],x_1[31],x_1[29]);
	parallelPrefixCkt p1_30(x_2[30],x_1[30],x_1[28]);
	parallelPrefixCkt p1_29(x_2[29],x_1[29],x_1[27]);
	parallelPrefixCkt p1_28(x_2[28],x_1[28],x_1[26]);
	parallelPrefixCkt p1_27(x_2[27],x_1[27],x_1[25]);
	parallelPrefixCkt p1_26(x_2[26],x_1[26],x_1[24]);
	parallelPrefixCkt p1_25(x_2[25],x_1[25],x_1[23]);
	parallelPrefixCkt p1_24(x_2[24],x_1[24],x_1[22]);
	parallelPrefixCkt p1_23(x_2[23],x_1[23],x_1[21]);
	parallelPrefixCkt p1_22(x_2[22],x_1[22],x_1[20]);
	parallelPrefixCkt p1_21(x_2[21],x_1[21],x_1[19]);
	parallelPrefixCkt p1_20(x_2[20],x_1[20],x_1[18]);
	parallelPrefixCkt p1_19(x_2[19],x_1[19],x_1[17]);
	parallelPrefixCkt p1_18(x_2[18],x_1[18],x_1[16]);
	parallelPrefixCkt p1_17(x_2[17],x_1[17],x_1[15]);
	parallelPrefixCkt p1_16(x_2[16],x_1[16],x_1[14]);
	parallelPrefixCkt p1_15(x_2[15],x_1[15],x_1[13]);
	parallelPrefixCkt p1_14(x_2[14],x_1[14],x_1[12]);
	parallelPrefixCkt p1_13(x_2[13],x_1[13],x_1[11]);
	parallelPrefixCkt p1_12(x_2[12],x_1[12],x_1[10]);
	parallelPrefixCkt p1_11(x_2[11],x_1[11],x_1[9]);
	parallelPrefixCkt p1_10(x_2[10],x_1[10],x_1[8]);
	parallelPrefixCkt p1_9(x_2[9],x_1[9],x_1[7]);
	parallelPrefixCkt p1_8(x_2[8],x_1[8],x_1[6]);
	parallelPrefixCkt p1_7(x_2[7],x_1[7],x_1[5]);
	parallelPrefixCkt p1_6(x_2[6],x_1[6],x_1[4]);
	parallelPrefixCkt p1_5(x_2[5],x_1[5],x_1[3]);
	parallelPrefixCkt p1_4(x_2[4],x_1[4],x_1[2]);
	parallelPrefixCkt p1_3(x_2[3],x_1[3],x_1[1]);
	parallelPrefixCkt p1_2(x_2[2],x_1[2],x_1[0]);
	parallelPrefixCkt p1_1(x_2[1],x_1[1],x_00);
	parallelPrefixCkt p1_0(x_2[0],x_1[0],x_00);

	// 3rd stage of KGP
	parallelPrefixCkt p2_31(x_3[31],x_2[31],x_2[27]);
	parallelPrefixCkt p2_30(x_3[30],x_2[30],x_2[26]);
	parallelPrefixCkt p2_29(x_3[29],x_2[29],x_2[25]);
	parallelPrefixCkt p2_28(x_3[28],x_2[28],x_2[24]);
	parallelPrefixCkt p2_27(x_3[27],x_2[27],x_2[23]);
	parallelPrefixCkt p2_26(x_3[26],x_2[26],x_2[22]);
	parallelPrefixCkt p2_25(x_3[25],x_2[25],x_2[21]);
	parallelPrefixCkt p2_24(x_3[24],x_2[24],x_2[20]);
	parallelPrefixCkt p2_23(x_3[23],x_2[23],x_2[19]);
	parallelPrefixCkt p2_22(x_3[22],x_2[22],x_2[18]);
	parallelPrefixCkt p2_21(x_3[21],x_2[21],x_2[17]);
	parallelPrefixCkt p2_20(x_3[20],x_2[20],x_2[16]);
	parallelPrefixCkt p2_19(x_3[19],x_2[19],x_2[15]);
	parallelPrefixCkt p2_18(x_3[18],x_2[18],x_2[14]);
	parallelPrefixCkt p2_17(x_3[17],x_2[17],x_2[13]);
	parallelPrefixCkt p2_16(x_3[16],x_2[16],x_2[12]);
	parallelPrefixCkt p2_15(x_3[15],x_2[15],x_2[11]);
	parallelPrefixCkt p2_14(x_3[14],x_2[14],x_2[10]);
	parallelPrefixCkt p2_13(x_3[13],x_2[13],x_2[9]);
	parallelPrefixCkt p2_12(x_3[12],x_2[12],x_2[8]);
	parallelPrefixCkt p2_11(x_3[11],x_2[11],x_2[7]);
	parallelPrefixCkt p2_10(x_3[10],x_2[10],x_2[6]);
	parallelPrefixCkt p2_9(x_3[9],x_2[9],x_2[5]);
	parallelPrefixCkt p2_8(x_3[8],x_2[8],x_2[4]);
	parallelPrefixCkt p2_7(x_3[7],x_2[7],x_2[3]);
	parallelPrefixCkt p2_6(x_3[6],x_2[6],x_2[2]);
	parallelPrefixCkt p2_5(x_3[5],x_2[5],x_2[1]);
	parallelPrefixCkt p2_4(x_3[4],x_2[4],x_2[0]);
	parallelPrefixCkt p2_3(x_3[3],x_2[3],x_00);
	parallelPrefixCkt p2_2(x_3[2],x_2[2],x_00);
	parallelPrefixCkt p2_1(x_3[1],x_2[1],x_00);
	parallelPrefixCkt p2_0(x_3[0],x_2[0],x_00);

	// 4th stage of KGP
	parallelPrefixCkt p3_31(x_4[31],x_3[31],x_3[23]);
	parallelPrefixCkt p3_30(x_4[30],x_3[30],x_3[22]);
	parallelPrefixCkt p3_29(x_4[29],x_3[29],x_3[21]);
	parallelPrefixCkt p3_28(x_4[28],x_3[28],x_3[20]);
	parallelPrefixCkt p3_27(x_4[27],x_3[27],x_3[19]);
	parallelPrefixCkt p3_26(x_4[26],x_3[26],x_3[18]);
	parallelPrefixCkt p3_25(x_4[25],x_3[25],x_3[17]);
	parallelPrefixCkt p3_24(x_4[24],x_3[24],x_3[16]);
	parallelPrefixCkt p3_23(x_4[23],x_3[23],x_3[15]);
	parallelPrefixCkt p3_22(x_4[22],x_3[22],x_3[14]);
	parallelPrefixCkt p3_21(x_4[21],x_3[21],x_3[13]);
	parallelPrefixCkt p3_20(x_4[20],x_3[20],x_3[12]);
	parallelPrefixCkt p3_19(x_4[19],x_3[19],x_3[11]);
	parallelPrefixCkt p3_18(x_4[18],x_3[18],x_3[10]);
	parallelPrefixCkt p3_17(x_4[17],x_3[17],x_3[9]);
	parallelPrefixCkt p3_16(x_4[16],x_3[16],x_3[8]);
	parallelPrefixCkt p3_15(x_4[15],x_3[15],x_3[7]);
	parallelPrefixCkt p3_14(x_4[14],x_3[14],x_3[6]);
	parallelPrefixCkt p3_13(x_4[13],x_3[13],x_3[5]);
	parallelPrefixCkt p3_12(x_4[12],x_3[12],x_3[4]);
	parallelPrefixCkt p3_11(x_4[11],x_3[11],x_3[3]);
	parallelPrefixCkt p3_10(x_4[10],x_3[10],x_3[2]);
	parallelPrefixCkt p3_9(x_4[9],x_3[9],x_3[1]);
	parallelPrefixCkt p3_8(x_4[8],x_3[8],x_3[0]);
	parallelPrefixCkt p3_7(x_4[7],x_3[7],x_00);
	parallelPrefixCkt p3_6(x_4[6],x_3[6],x_00);
	parallelPrefixCkt p3_5(x_4[5],x_3[5],x_00);
	parallelPrefixCkt p3_4(x_4[4],x_3[4],x_00);
	parallelPrefixCkt p3_3(x_4[3],x_3[3],x_00);
	parallelPrefixCkt p3_2(x_4[2],x_3[2],x_00);
	parallelPrefixCkt p3_1(x_4[1],x_3[1],x_00);
	parallelPrefixCkt p3_0(x_4[0],x_3[0],x_00);

	// 5th stage of KGP
	parallelPrefixCkt p4_31(x_5[31],x_4[31],x_4[15]);
	parallelPrefixCkt p4_30(x_5[30],x_4[30],x_4[14]);
	parallelPrefixCkt p4_29(x_5[29],x_4[29],x_4[13]);
	parallelPrefixCkt p4_28(x_5[28],x_4[28],x_4[12]);
	parallelPrefixCkt p4_27(x_5[27],x_4[27],x_4[11]);
	parallelPrefixCkt p4_26(x_5[26],x_4[26],x_4[10]);
	parallelPrefixCkt p4_25(x_5[25],x_4[25],x_4[9]);
	parallelPrefixCkt p4_24(x_5[24],x_4[24],x_4[8]);
	parallelPrefixCkt p4_23(x_5[23],x_4[23],x_4[7]);
	parallelPrefixCkt p4_22(x_5[22],x_4[22],x_4[6]);
	parallelPrefixCkt p4_21(x_5[21],x_4[21],x_4[5]);
	parallelPrefixCkt p4_20(x_5[20],x_4[20],x_4[4]);
	parallelPrefixCkt p4_19(x_5[19],x_4[19],x_4[3]);
	parallelPrefixCkt p4_18(x_5[18],x_4[18],x_4[2]);
	parallelPrefixCkt p4_17(x_5[17],x_4[17],x_4[1]);
	parallelPrefixCkt p4_16(x_5[16],x_4[16],x_4[0]);
	parallelPrefixCkt p4_15(x_5[15],x_4[15],x_00);
	parallelPrefixCkt p4_14(x_5[14],x_4[14],x_00);
	parallelPrefixCkt p4_13(x_5[13],x_4[13],x_00);
	parallelPrefixCkt p4_12(x_5[12],x_4[12],x_00);
	parallelPrefixCkt p4_11(x_5[11],x_4[11],x_00);
	parallelPrefixCkt p4_10(x_5[10],x_4[10],x_00);
	parallelPrefixCkt p4_9(x_5[9],x_4[9],x_00);
	parallelPrefixCkt p4_8(x_5[8],x_4[8],x_00);
	parallelPrefixCkt p4_7(x_5[7],x_4[7],x_00);
	parallelPrefixCkt p4_6(x_5[6],x_4[6],x_00);
	parallelPrefixCkt p4_5(x_5[5],x_4[5],x_00);
	parallelPrefixCkt p4_4(x_5[4],x_4[4],x_00);
	parallelPrefixCkt p4_3(x_5[3],x_4[3],x_00);
	parallelPrefixCkt p4_2(x_5[2],x_4[2],x_00);
	parallelPrefixCkt p4_1(x_5[1],x_4[1],x_00);
	parallelPrefixCkt p4_0(x_5[0],x_4[0],x_00);

	// MSB of last stage KGP is carry
	assign carry[0] = x_5[0][0];
	assign carry[1] = x_5[1][0];
	assign carry[2] = x_5[2][0];
	assign carry[3] = x_5[3][0];
	assign carry[4] = x_5[4][0];
	assign carry[5] = x_5[5][0];
	assign carry[6] = x_5[6][0];
	assign carry[7] = x_5[7][0];
	assign carry[8] = x_5[8][0];
	assign carry[9] = x_5[9][0];
	assign carry[10] = x_5[10][0];
	assign carry[11] = x_5[11][0];
	assign carry[12] = x_5[12][0];
	assign carry[13] = x_5[13][0];
	assign carry[14] = x_5[14][0];
	assign carry[15] = x_5[15][0];
	assign carry[16] = x_5[16][0];
	assign carry[17] = x_5[17][0];
	assign carry[18] = x_5[18][0];
	assign carry[19] = x_5[19][0];
	assign carry[20] = x_5[20][0];
	assign carry[21] = x_5[21][0];
	assign carry[22] = x_5[22][0];
	assign carry[23] = x_5[23][0];
	assign carry[24] = x_5[24][0];
	assign carry[25] = x_5[25][0];
	assign carry[26] = x_5[26][0];
	assign carry[27] = x_5[27][0];
	assign carry[28] = x_5[28][0];
	assign carry[29] = x_5[29][0];
	assign carry[30] = x_5[30][0];
	assign carry[31] = x_5[31][0];

	// Compute Sum
	assign Sum[0] = xorSum[0];
	assign Sum[1] = xorSum[1] ^ carry[0];
	assign Sum[2] = xorSum[2] ^ carry[1];
	assign Sum[3] = xorSum[3] ^ carry[2];
	assign Sum[4] = xorSum[4] ^ carry[3];
	assign Sum[5] = xorSum[5] ^ carry[4];
	assign Sum[6] = xorSum[6] ^ carry[5];
	assign Sum[7] = xorSum[7] ^ carry[6];
	assign Sum[8] = xorSum[8] ^ carry[7];
	assign Sum[9] = xorSum[9] ^ carry[8];
	assign Sum[10] = xorSum[10] ^ carry[9];
	assign Sum[11] = xorSum[11] ^ carry[10];
	assign Sum[12] = xorSum[12] ^ carry[11];
	assign Sum[13] = xorSum[13] ^ carry[12];
	assign Sum[14] = xorSum[14] ^ carry[13];
	assign Sum[15] = xorSum[15] ^ carry[14];
	assign Sum[16] = xorSum[16] ^ carry[15];
	assign Sum[17] = xorSum[17] ^ carry[16];
	assign Sum[18] = xorSum[18] ^ carry[17];
	assign Sum[19] = xorSum[19] ^ carry[18];
	assign Sum[20] = xorSum[20] ^ carry[19];
	assign Sum[21] = xorSum[21] ^ carry[20];
	assign Sum[22] = xorSum[22] ^ carry[21];
	assign Sum[23] = xorSum[23] ^ carry[22];
	assign Sum[24] = xorSum[24] ^ carry[23];
	assign Sum[25] = xorSum[25] ^ carry[24];
	assign Sum[26] = xorSum[26] ^ carry[25];
	assign Sum[27] = xorSum[27] ^ carry[26];
	assign Sum[28] = xorSum[28] ^ carry[27];
	assign Sum[29] = xorSum[29] ^ carry[28];
	assign Sum[30] = xorSum[30] ^ carry[29];
	assign Sum[31] = xorSum[31] ^ carry[30];
    assign Cout = carry[31];

endmodule