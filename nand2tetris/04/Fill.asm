// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(BEGINNING)
    @SCREEN       
    D = A
    @8192         
    D = D + A
    @END_OF_SCREEN	  // ScreenEnd = SCREEN + 8192
    M = D
	@color
	M=0	
	
(LOOP)
	@24576
	D = M
	@SETWHITE
	D;JEQ //if D == 0 go to clean.
	@SETBLACK
	D;JNE //if D != 0 go to paint.
	@LOOP
	0;JMP

(SETWHITE)
	@color
	M=0
	@SCREEN       // pIter = SCREEN
    D = A
    @INDEX
    M=D
	@PAINT
	0;JMP
	
(SETBLACK)
	@color
	M=-1
	@SCREEN       // pIter = SCREEN
    D = A
    @INDEX
    M=D
	@PAINT
	0;JMP
	
(PAINT)
    @END_OF_SCREEN    // If ScreenEnd - pIter <= 0 GOTO END
    D = M
    @INDEX
    D = D - M
    @LOOP
    D;JLE
	@color
    D = M
    @INDEX         // M[pIter] = -1
    A = M
    M = D
    @INDEX
    M = M + 1
	@PAINT
	0;JMP // goto LOOP