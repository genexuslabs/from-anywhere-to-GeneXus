IDENTIFICATION DIVISION.
PROGRAM-ID. AddTwoNumbers.

DATA DIVISION.
WORKING-STORAGE SECTION.
   77 num1        PIC 9(4) VALUE 0.
   77 num2        PIC 9(4) VALUE 0.
   77 sum         PIC 9(5) VALUE 0.

PROCEDURE DIVISION.
   DISPLAY "Enter first number: " WITH NO ADVANCING.
   ACCEPT num1.
   
   DISPLAY "Enter second number: " WITH NO ADVANCING.
   ACCEPT num2.

   COMPUTE sum = num1 + num2.
   
   DISPLAY "The sum of " num1 " and " num2 " is: " sum.

   STOP RUN.
