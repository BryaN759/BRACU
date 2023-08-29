;TASK 02
.MODEL SMALL
 
.STACK 100H

.DATA

 A DW 2
 B DW 3
 C DW 4 

.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 

; A = C + (B-A) - 2  
; enter your code here 

  MOV AX, A  
  MOV BX, B  
  MOV CX, C
     
  SUB BX, AX
  ADD CX, BX
  MOV DX, 2
  SUB CX, DX
  
  MOV AX, CX

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



