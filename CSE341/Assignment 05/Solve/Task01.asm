;TASK 01
.MODEL SMALL

.STACK 100H

.DATA

 A DB "Ahmad Abdur Rafi"

.CODE
MAIN PROC

;initizlize DS

MOV AX,@DATA
MOV DS,AX

; enter your code here  

  MOV CX, 16
  LEA SI, A
  ;MOV SI, Offset Array Name ; Ekhane actually A 

Start: 
  MOV AH, 2
  CMP [SI], " "
  JE  Blank
  CMP [SI], 60h
  JG  Small

;Capital Letter
  ADD [SI], 20h  
  MOV DL, [SI]
  INT 21h
  INC SI
  LOOP Start 
  JMP exit

Blank:
  MOV DL, [SI]
  INT 21h 
  INC SI
  LOOP Start
  JMP exit

Small:
  SUB [SI], 20h 
  MOV DL, [SI]
  INT 21h
  INC SI
  LOOP Start
  JMP exit

exit:

;exit to DOS
MOV AX,4C00H
INT 21H

MAIN ENDP
   END MAIN
