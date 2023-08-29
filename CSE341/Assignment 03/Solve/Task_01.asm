;TASK 01
.MODEL SMALL

.STACK 100H

.DATA

 L DB "1st Input: $"
 M DB "2nd Input: $"
 N DB "3rd Input: $"

.CODE
MAIN PROC

;initizlize DS

MOV AX,@DATA
MOV DS,AX 

; enter your code here

  LEA DX, L
  MOV AH, 9
  INT 21h

  MOV AH, 1
  INT 21h
  MOV BH, AL

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, M
  MOV AH, 9
  INT 21h

  MOV AH,1
  INT 21h
  MOV CH, AL

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, N
  MOV AH, 9
  INT 21h

  MOV AH, 1
  INT 21h
  MOV CL, AL 

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

;Comparison starts 

  CMP BH, CH 
  JG  E1 
  CMP CH, CL 
  JG  E3
  JMP OP1

E1:
  CMP BH, CL
  JG  E2  
  JMP OP3

E2:
  CMP CH, CL
  JG  OP1
  JMP OP2

E3:    
  CMP BH, CL
  JG  OP3
  JMP OP2

OP1:  
  MOV DL, CH
  MOV AH, 2
  INT 21h 
  JMP exit 

OP2:   
  MOV DL, CL
  MOV AH, 2
  INT 21h 
  JMP exit

OP3:   
  MOV DL, BH
  MOV AH, 2
  INT 21h 
  JMP exit

exit:

;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN



