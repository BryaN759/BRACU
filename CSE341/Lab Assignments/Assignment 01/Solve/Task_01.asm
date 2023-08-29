;TASK 01
.MODEL SMALL
 
.STACK 100H

.DATA 


.CODE 
MAIN PROC 

;iniitialize DS

MOV AX,@DATA 
MOV DS,AX 
 
; enter your code here

  MOV AL, 30
  MOV BL, 10 
  
  SUB CL, CL
  ADD CL, AL
  
  SUB AL, AL
  ADD AL, BL
   
  SUB BL, BL 
  ADD BL, CL
 
;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 
  



