;TASK 04
.MODEL SMALL
 
.STACK 100H

.DATA 

 A DB 'ENTER A HEX DIGIT:$'
 B DB 'IN DECIMAL IT IS $'

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

  MOV AH, 9
  LEA DX, A
  INT 21H

  MOV AH, 1
  INT 21H
  
  MOV BL, AL
  SUB BL, 17D

  MOV AH, 2
  MOV DL, 0DH
  INT 21H
  MOV DL, 0AH
  INT 21H

  MOV AH, 9
  LEA DX, B
  INT 21H

  MOV AH, 2
  MOV DL, 31H
  INT 21H 
  
  MOV DL, BL
  INT 21H


;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 




