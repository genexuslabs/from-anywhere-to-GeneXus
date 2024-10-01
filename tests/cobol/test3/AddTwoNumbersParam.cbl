       IDENTIFICATION DIVISION.
       PROGRAM-ID. SumProgram.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       INPUT-OUTPUT SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  num1         PIC 9(5) VALUE 0.
       01  num2         PIC 9(5) VALUE 0.
       01  sum          PIC 9(6) VALUE 0.

       PROCEDURE DIVISION USING num1 num2.
           ACCEPT num1 FROM ARGUMENT-NUMBER 1.
           ACCEPT num2 FROM ARGUMENT-NUMBER 2.
           ADD num1 TO num2 GIVING sum.
           DISPLAY "Sum of " num1 " and " num2 " is: " sum.
           STOP RUN.
