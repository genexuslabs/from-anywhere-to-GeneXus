       IDENTIFICATION DIVISION.
       PROGRAM-ID. SumProgram.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  num1          PIC S9(9) COMP-5.
       01  num2          PIC S9(9) COMP-5.
       01  sum           PIC S9(9) COMP-5.
       01  ws-return-code PIC S9(9) COMP-5 VALUE 0.
       01  ws-arg1       PIC X(10).
       01  ws-arg2       PIC X(10).

       LINKAGE SECTION.
       01  command-line-args.
           05  arg-count  PIC 9(1).
           05  arg-values OCCURS 0 TO 10 TIMES DEPENDING ON arg-count.
               10  arg-value   PIC X(100).

       PROCEDURE DIVISION USING command-line-args.
           IF arg-count < 3
               MOVE 1 TO ws-return-code
               GOBACK.

           MOVE arg-values(1) TO ws-arg1
           MOVE arg-values(2) TO ws-arg2

           IF ws-arg1 NUMERIC
               MOVE FUNCTION NUMVAL(ws-arg1) TO num1
           ELSE
               MOVE 1 TO ws-return-code
               GOBACK
           END-IF.

           IF ws-arg2 NUMERIC
               MOVE FUNCTION NUMVAL(ws-arg2) TO num2
           ELSE
               MOVE 1 TO ws-return-code
               GOBACK
           END-IF.

           ADD num1 TO num2 GIVING sum
           MOVE sum TO RETURN-CODE

           GOBACK.
