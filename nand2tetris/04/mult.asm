// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

//------------------set R2 to 0----------------------
@R2 
M = 0
//---------------------------------------------------
//------------------set i = R0-----------------------
@R0
D = M

@i
M = D                   
//---------------------------------------------------
@R1
D = M
//ADD R1 TO R2 IN EACH ROUND, THE NUMBER OF ROUNDS IS R0
(LOOP)
	@i
	M = M - 1
	@END
	M;JLT
	@R2
	M = M + D
	@LOOP
	0;JMP
(END)
@END
0;JMP