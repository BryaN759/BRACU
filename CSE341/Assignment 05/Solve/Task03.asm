;TASK 03
.MODEL SMALL
.STACK 100H
.DATA

 A DB 5 dup(?)
	
.CODE
MAIN PROC
	
;iniitialize DS

MOV AX,@DATA
MOV DS,AX 

; enter your code here
  
  MOV SI, 0
  MOV CX, 5

p:
  
  MOV AH, 1
  INT 21h
  MOV A[SI], AL
  ADD A[SI], 30h
  ADD SI, 1
  LOOP p
	
  MOV SI, 0
  MOV CX, 4

Q:
  MOV DH, 0 

R:
  CMP DH, 4
  JE  T
  MOV BH, A[SI] 	
  MOV BL, A[SI+1]
  CMP BH, BL
  JG  Larger

S:
  ADD SI, 1
  INC DH
  JMP R
	
T:
  MOV SI, 0
  LOOP Q 
  MOV SI, 0
  MOV AL, 0
	   
  MOV AH, 2
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH 
  INT 21h 
  MOV CX, 5
  JMP print
	
Larger:
  MOV A[SI], BL
  MOV A[SI+1], BH
  JMP S
	
Print:
  SUB A[SI], 30h
  MOV DL, A[SI]
  MOV AH, 2 
  INT 21h
  ADD SI, 1 
  LOOP Print
  jmp exit	
		
exit:

;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN