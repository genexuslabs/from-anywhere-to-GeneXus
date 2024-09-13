IDENTIFICATION DIVISION.
PROGRAM-ID. MinOfTwoNumbers.

DATA DIVISION.
WORKING-STORAGE SECTION.
   77 num1        PIC 9(4) VALUE 0.
   77 num2        PIC 9(4) VALUE 0.
   77 minNum      PIC 9(4) VALUE 0.

PROCEDURE DIVISION.
   DISPLAY "Enter first number: " WITH NO ADVANCING.
   ACCEPT num1.
   
   DISPLAY "Enter second number: " WITH NO ADVANCING.
   ACCEPT num2.

   IF num1 < num2 THEN
       MOVE num1 TO minNum
   ELSE
       MOVE num2 TO minNum
   END-IF.

   DISPLAY "The minimum of " num1 " and " num2 " is: " minNum.

   STOP RUN.
