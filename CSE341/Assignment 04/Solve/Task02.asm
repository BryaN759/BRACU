;TASK 02
.MODEL SMALL
 
.STACK 100H

.DATA 


.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

  MOV AX, 0
  MOV CX, 1
    
START:
  CMP CX, 505
  JE EXIT
  
  ADD AX, CX
  ADD CX, 2
  SUB AX, CX
  ADD CX, 2
  JMP START
    
EXIT:
  ADD AX,CX 

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



