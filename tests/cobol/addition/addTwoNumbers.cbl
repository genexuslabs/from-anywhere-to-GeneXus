IDENTIFICATION DIVISION.
PROGRAM-ID. AddTwoNumbersFunction.

DATA DIVISION.
LINKAGE SECTION.
01  NUM1        PIC 9(4).
01  NUM2        PIC 9(4).
01  RESULT      PIC 9(5).

PROCEDURE DIVISION USING NUM1, NUM2, RESULT.
    COMPUTE RESULT = NUM1 + NUM2.
    EXIT PROGRAM.
