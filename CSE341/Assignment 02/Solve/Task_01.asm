;TASK 01
.MODEL SMALL
 
.STACK 100H

.DATA   

 A DB "The result is$"

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

  MOV AH, 01H
  INT 21H
  
  SUB AL, 48             
  MOV BL, AL
  MUL BL
  MOV BL, AL
  ADD BL, 48
       
  MOV AH, 2             
  MOV DL, 0AH
  INT 21H
  MOV DL, 0DH
  INT 21H
  
  LEA DX, A 
  MOV AH, 09H 
  INT 21H
  
  MOV AH, 2 
  MOV DL, 0AH 
  INT 21H 
  MOV DL, 0DH 
  INT 21H
   
  MOV DL, BL
  MOV AH, 02H 
  INT 21H 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 




