/* 2:1 Multiplexer module */
module mux_2_1(Y, X, select);

	// I/O Port Declarations
	output Y;
	input[1:0] X;
	input select;

	// NOT of select line
	wire n_select;

	not not_0(n_select, select);

	// AND gates
	wire d0, d1;

	and and_0(d0, X[0], n_select);
	and and_1(d1, X[1], select);

	or or_0(Y, d0, d1);

endmodule

/* 4:1 Multiplexer module */
module mux_4_1(Y, X, select);

	// I/O Port Declarations
	output Y;
	input[3:0] X;
	input[1:0] select;

	// Get NOT of select lines
	wire[1:0] n_select;

	not not_0(n_select[0], select[0]);
	not not_1(n_select[1], select[1]);

	// AND gates
	wire d0, d1, d2, d3;
	
	and and_0(d0, X[0], n_select[1], n_select[0]);
	and and_1(d1, X[1], n_select[1], select[0]);
	and and_2(d2, X[2], select[1], n_select[0]);
	and and_3(d3, X[3], select[1], select[0]);

	or or_0(Y, d0, d1, d2, d3);

endmodule

/* 8:1 multiplexer module */
module mux_8_1(Y, X, select);

	// I/O Port Declarations
	output Y;
	input[7:0] X;
	input[2:0] select;

	// Two 4:1 Mux
	wire[1:0] d;

	mux_4_1 mux41_0(d[1], X[7:4], select[1:0]);
	mux_4_1 mux41_1(d[0], X[3:0], select[1:0]);

	// Last layer of 2:1 Mux
	mux_2_1 mux21_0(Y, d, select[2]);

endmodule

/* 16:1 multiplexer module*/
module mux_16_1(Y,X, select);

	// I/O Port Declarations
	output Y;
	input[15:0] X;
	input[3:0] select;

	// Two 8:1 Mux
	wire[1:0] d;

	mux_8_1 mux81_0(d[1], X[15:8], select[2:0]);
	mux_8_1 mux81_1(d[0], X[7:0], select[2:0]);

	// Last layer of 2:1 Mux
	mux_2_1 mux21_0(Y, d, select[3]);

endmodule

/* 32:1 multiplexer module*/
module mux_32_1(Y,X, select);

	// I/O Port Declarations
	output Y;
	input[31:0] X;
	input[4:0] select;

	// Two 16:1 Mux
	wire[1:0] d;

	mux_16_1 mux16_0(d[1], X[31:16], select[3:0]);
	mux_16_1 mux16_1(d[0], X[15:0], select[3:0]);

	// Last layer of 2:1 Mux
	mux_2_1 mux21_0(Y, d, select[4]);

endmodule

/* 64:1 multiplexer module*/
module mux_64_1(Y,X, select);

	// I/O Port Declarations
	output Y;
	input[63:0] X;
	input[5:0] select;

	// Two 32:1 Mux
	wire[1:0] d;

	mux_32_1 mux32_0(d[1], X[63:32], select[4:0]);
	mux_32_1 mux32_1(d[0], X[31:0], select[4:0]);

	// Last layer of 2:1 Mux
	mux_2_1 mux21_0(Y, d, select[5]);

endmodule