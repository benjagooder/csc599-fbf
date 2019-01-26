Set GRUN=java -cp .;C:\Users\user\antlr\antlr-4.7.1-complete.jar org.antlr.v4.gui.TestRig %*
Set ANTLR=java -jar C:\Users\user\antlr\antlr-4.7.1-complete.jar
%ANTLR% -no-listener -visitor -Dlanguage=Python3 Rome.g4
python AntlrProgram.py romeInput.txt