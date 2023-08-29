;TASK 04
.MODEL SMALL

.STACK 100H

.DATA

 P db "ENTER A HEX DIGIT: $"
 Q db "IN DECIMAL IT IS $"
 R db "DO YOU WANT TO DO IT AGAIN? : $" 
 S db "ILLEGAL CHARACTER, INSERT AGAIN: $"  
 T db "1$"

.CODE
MAIN PROC

;initizlize DS

MOV AX,@DATA
MOV DS,AX

; enter your code here

A: 
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, P
  MOV AH, 9
  INT 21h          
  MOV AH, 1
  INT 21h  
  MOV BL, AL
  SUB BL, 48 

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  CMP BL, 10h
  JG  B
  CMP BL, -1h
  JG  C
  JMP E
 
B: 
  ADD BL, 48
  CMP BL, 41h
  JE  D
  CMP BL, 42h
  JE  D
  CMP BL, 43h
  JE  D
  CMP BL, 44h
  JE  D
  CMP BL, 45h
  JE  D
  CMP BL, 46h
  JE  D
  JMP E

E: 
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h
  LEA DX, S
  MOV AH, 9
  INT 21h 
  JMP A

C: 
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, Q
  MOV AH, 9
  INT 21h
  MOV DL, BL
  ADD DL, 48
        
  MOV AH, 2
  INT 21h 
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, R
  MOV AH, 9
  INT 21h 
  MOV AH, 1
  INT 21h

  CMP AL, 'y'
  JE  A
  CMP AL, 'Y'
  JE  A
  CMP AL, 'n'
  JE  exit
  CMP AL, 'N'
  JE  exit 
  JMP E

D: 
  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, Q
  MOV AH, 9
  INT 21h 
  LEA DX, T
  MOV AH, 9
  INT 21h

  MOV DL, BL
  SUB DL, 11h
  MOV AH, 2
  INT 21h 

  MOV AH, 2 
  MOV DL, 0DH 
  INT 21h
  MOV DL, 0AH
  INT 21h

  LEA DX, R
  MOV AH, 9
  INT 21h 
  MOV AH, 1
  INT 21h

  CMP AL, 'y'
  JE  A
  CMP AL, 'Y'
  JE  A
  CMP AL, 'n'
  JE  exit
  CMP AL, 'N'
  JE  exit 
  JMP E

exit:

;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN