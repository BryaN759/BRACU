;TASK 04
.MODEL SMALL
 
.STACK 100H

.DATA 


.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 

; 10 * 7 / (1-4) + 13 + 52 - 4 * 2 
; enter your code here

  MOV BX, 1
  MOV CX, 4
  SUB BX, CX

  MOV AX, 7
  DIV BX

  MOV BX, 10
  MUL BX

  MOV BX, 13
  ADD AX, BX

  MOV BX, 52
  ADD AX, BX
  MOV DX, AX

  MOV AX, 4
  MOV BX, 2
  MUL BX
  SUB DX, AX

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



