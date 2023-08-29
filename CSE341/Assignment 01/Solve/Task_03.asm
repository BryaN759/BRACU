;TASK 03
.MODEL SMALL
 
.STACK 100H

.DATA

X DB 1
Y DB 4
Z DB 2 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 

; Y * Y / (4 * X * Z) 
; enter your code here

  MOV AL, 4
  MOV BL, X
  MOV CL, Z
  MUL BL
  MUL CL
  MOV DL, AL
  MOV AL, Y
  DIV DL
  MOV DL, Y
  MUL DL

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



