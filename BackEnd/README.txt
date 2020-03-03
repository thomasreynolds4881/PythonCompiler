The backend compiler takes input in the form of three address code and output ARM assembler code
Which can be executed in VisUAL. If your three address code file is called tac.txt, you would run
it like this:

(Mac/Linux)

cat tac.txt | python backend_starter_parser.py

or

(Windows)

type tac.txt | python starter_parser.py

To save the results to a file such as result.txt, redirect the output with a command like 

cat tac.txt | python backend_starter_parser.py > result.txt

or

type tac.txt | python backend_starter_parser.py > result.txt



If you want to combine this with the front end compiler run the following command from the parent directory of both starterFrontEnd and starterBack end. This assumes a program source file called sampleProgram.prg is in the parent folder as well:


(Mac/Linux)

cat sampleProgram.prg | python starterFrontEnd/starter_parser.py | python starterBackEnd/backend_starter_parser.py

or

(Windows)

type sampleProgram.prg | python starterFrontEnd/starter_parser.py | python starterBackEnd/backend_starter_parser.py

To save the results to a file such as result.txt, redirect the output with a command like 

cat sampleProgram.prg | python starterFrontEnd/starter_parser.py | python starterBackEnd/backend_starter_parser.py > result.txt

or

type cat sampleProgram.prg | python starterFrontEnd/starter_parser.py | python starterBackEnd/backend_starter_parser.py > result.txt