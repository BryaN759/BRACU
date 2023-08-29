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

  MOV AH, 1
  INT 21H
  MOV BL, AL
  SUB BL, 20H          

  MOV AH, 2
  MOV DL, 0DH
  INT 21H
  MOV DL, 0AH
  INT 21H

  MOV DL, BL
  INT 21H

;exit to DOS 
               
MOV AX,4C00H
INT 21H 

MAIN ENDP
    END MAIN 




