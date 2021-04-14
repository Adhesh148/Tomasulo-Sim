`include "doublingCLA_64.v"

// Let's define the 32 bit Carry Save Adder Module
module CSA_64(sum,carry,A,B,C);

	// IO Port Declarations
	output[63:0] sum,carry;				// the output sum contains the sum of A,B,C without the carry bits included
	input[63:0] A,B,C;					

	// Lets compute the sum and carry -> sumi = xors of bits Ai,Bi and Ci
	assign sum = A ^ B ^ C;
	assign carry  = ((A & B) | (B & C) | (A & C))<<1;

endmodule 

// Let's define the 32 bit Carry Look Ahead Adder
module CLA_64(product,A,B);

	// IO Port Declarations
	output[63:0] product;
	input[63:0] A,B;

	// Here to do the Additions fast we shall use two doublingCLA blocks --- review this - some problem
	wire cout;
	doublingCLA_64 dcla_0 (product,cout,A,B,1'b0);

endmodule

// Finally let's define the 32 bit Wallace Multiplier using CSV and one final CLA module.
module WM_32(product,A,B);

	// IO Port Declarations
	// Review this - the number of digits in product increases.
	output[63:0] product;	
	input[31:0] A,B;

	wire[63:0] PP[31:0];				// PP here refers the partial products of the multiplications. A 32 bit multiplication would have 32 32-bit PP.

	// Calc partial products by ANDing individual bits of B with A.
	assign PP[0] =  (A & {64{B[0]}});
	assign PP[1] =  (A & {64{B[1]}}) << 1;
	assign PP[2] =  (A & {64{B[2]}}) << 2;
	assign PP[3] =  (A & {64{B[3]}}) << 3;
	assign PP[4] =  (A & {64{B[4]}}) << 4;
	assign PP[5] =  (A & {64{B[5]}}) << 5;
	assign PP[6] =  (A & {64{B[6]}}) << 6;
	assign PP[7] =  (A & {64{B[7]}}) << 7;
	assign PP[8] =  (A & {64{B[8]}}) << 8;
	assign PP[9] =  (A & {64{B[9]}}) << 9;
	assign PP[10] =  (A & {64{B[10]}}) << 10;
	assign PP[11] =  (A & {64{B[11]}}) << 11;
	assign PP[12] =  (A & {64{B[12]}}) << 12;
	assign PP[13] =  (A & {64{B[13]}}) << 13;
	assign PP[14] =  (A & {64{B[14]}}) << 14;
	assign PP[15] =  (A & {64{B[15]}}) << 15;
	assign PP[16] =  (A & {64{B[16]}}) << 16;
	assign PP[17] =  (A & {64{B[17]}}) << 17;
	assign PP[18] =  (A & {64{B[18]}}) << 18;
	assign PP[19] =  (A & {64{B[19]}}) << 19;
	assign PP[20] =  (A & {64{B[20]}}) << 20;
	assign PP[21] =  (A & {64{B[21]}}) << 21;
	assign PP[22] =  (A & {64{B[22]}}) << 22;
	assign PP[23] =  (A & {64{B[23]}}) << 23;
	assign PP[24] =  (A & {64{B[24]}}) << 24;
	assign PP[25] =  (A & {64{B[25]}}) << 25;
	assign PP[26] =  (A & {64{B[26]}}) << 26;
	assign PP[27] =  (A & {64{B[27]}}) << 27;
	assign PP[28] =  (A & {64{B[28]}}) << 28;
	assign PP[29] =  (A & {64{B[29]}}) << 29;
	assign PP[30] =  (A & {64{B[30]}}) << 30;
	assign PP[31] =  (A & {64{B[31]}}) << 31;

	// First Layer of CSAs.
	wire[63:0] sum_0[9:0];
	wire[63:0] carry_0[9:0];

	CSA_64 csa_0(sum_0[9],carry_0[9],PP[31],PP[30],PP[29]);
	CSA_64 csa_1(sum_0[8],carry_0[8],PP[28],PP[27],PP[26]);
	CSA_64 csa_2(sum_0[7],carry_0[7],PP[25],PP[24],PP[23]);
	CSA_64 csa_3(sum_0[6],carry_0[6],PP[22],PP[21],PP[20]);
	CSA_64 csa_4(sum_0[5],carry_0[5],PP[19],PP[18],PP[17]);
	CSA_64 csa_5(sum_0[4],carry_0[4],PP[16],PP[15],PP[14]);
	CSA_64 csa_6(sum_0[3],carry_0[3],PP[13],PP[12],PP[11]);
	CSA_64 csa_7(sum_0[2],carry_0[2],PP[10],PP[9],PP[8]);
	CSA_64 csa_8(sum_0[1],carry_0[1],PP[7],PP[6],PP[5]);
	CSA_64 csa_9(sum_0[0],carry_0[0],PP[4],PP[3],PP[2]);

	// assign product = carry_0[0];

	// Second Layer of CSAs
	wire[63:0] sum_1[6:0];
	wire[63:0] carry_1[6:0];

	CSA_64 csa1_0(sum_1[6],carry_1[6],sum_0[9],carry_0[9],sum_0[8]);
	CSA_64 csa1_1(sum_1[5],carry_1[5],carry_0[8],sum_0[7],carry_0[7]);
	CSA_64 csa1_2(sum_1[4],carry_1[4],sum_0[6],carry_0[6],sum_0[5]);
	CSA_64 csa1_3(sum_1[3],carry_1[3],carry_0[5],sum_0[4],carry_0[4]);
	CSA_64 csa1_4(sum_1[2],carry_1[2],sum_0[3],carry_0[3],sum_0[2]);
	CSA_64 csa1_5(sum_1[1],carry_1[1],carry_0[2],sum_0[1],carry_0[1]);
	CSA_64 csa1_6(sum_1[0],carry_1[0],sum_0[0],carry_0[0],PP[1]);

	// // Third Layer of CSAs
	wire[63:0] sum_2[4:0];
	wire[63:0] carry_2[4:0];

	CSA_64 csa2_0(sum_2[4],carry_2[4],sum_1[6],carry_1[6],sum_1[5]);
	CSA_64 csa2_1(sum_2[3],carry_2[3],carry_1[5],sum_1[4],carry_1[4]);
	CSA_64 csa2_2(sum_2[2],carry_2[2],sum_1[3],carry_1[3],sum_1[2]);
	CSA_64 csa2_3(sum_2[1],carry_2[1],carry_1[2],sum_1[1],carry_1[1]);
	CSA_64 csa2_4(sum_2[0],carry_2[0],sum_1[0],carry_1[0],PP[0]);

	// Fourth Layer of CSAs
	wire[63:0] sum_3[2:0];
	wire[63:0] carry_3[2:0];

	CSA_64 csa3_0(sum_3[2],carry_3[2],sum_2[4],carry_2[4],sum_2[3]);
	CSA_64 csa3_1(sum_3[1],carry_3[1],carry_2[3],sum_2[2],carry_2[2]);
	CSA_64 csa3_2(sum_3[0],carry_3[0],sum_2[1],carry_2[1],sum_2[0]);

	// Fifth Layer of CSAs
	wire[63:0] sum_4[1:0];
	wire[63:0] carry_4[1:0];
	CSA_64 csa4_0(sum_4[1],carry_4[1],sum_3[2],carry_3[2],sum_3[1]);
	CSA_64 csa4_1(sum_4[0],carry_4[0],carry_3[1],sum_3[0],carry_3[0]);

	// Sixth Layer of CSAs
	wire[63:0] sum_5;
	wire[63:0] carry_5;
	CSA_64 csa5_0(sum_5,carry_5,sum_4[1],carry_4[1],sum_4[0]);

	// Seventh Layer
	wire[63:0] sum_6;
	wire[63:0] carry_6;
	CSA_64 csa6_0(sum_6,carry_6,sum_5,carry_5,carry_4[0]);

	// Last CSA Layer
	wire[63:0] sum_7;
	wire[63:0] carry_7;
	CSA_64 csa7_0(sum_7,carry_7,sum_6,carry_6,carry_2[0]);

	// Now Add sum_7 and carry_7 to get the product using CLA
	CLA_64 cla_0(product,sum_7,carry_7);


endmodule
