IDENTIFICATION DIVISION.
PROGRAM-ID. AddNumbers.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
    SELECT InputFile ASSIGN TO 'input.txt'
        ORGANIZATION IS LINE SEQUENTIAL.
    SELECT OutputFile ASSIGN TO 'output.txt'
        ORGANIZATION IS LINE SEQUENTIAL.

DATA DIVISION.
FILE SECTION.
FD  InputFile.
01  InputRecord.
    05  Number1      PIC 9(5).
    05  Number2      PIC 9(5).

FD  OutputFile.
01  OutputRecord     PIC X(80).

WORKING-STORAGE SECTION.
01  Sum              PIC 9(6).
01  DisplayResult    PIC X(80).

PROCEDURE DIVISION.
    OPEN INPUT InputFile
    OPEN OUTPUT OutputFile

    READ InputFile
        AT END
            DISPLAY 'End of file reached.'
            STOP RUN
    END-READ

    COMPUTE Sum = Number1 + Number2

    MOVE 'The sum of ' TO DisplayResult(1:12)
    MOVE Number1 TO DisplayResult(13:17)
    MOVE ' and ' TO DisplayResult(18:22)
    MOVE Number2 TO DisplayResult(23:27)
    MOVE ' is ' TO DisplayResult(28:32)
    MOVE Sum TO DisplayResult(33:38)

    WRITE OutputRecord FROM DisplayResult

    CLOSE InputFile
    CLOSE OutputFile

    STOP RUN.
