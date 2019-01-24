grammar Rome;

/*
 * Parser Rules
 */

rome				: line+ EOF ;

line				: name command message NEWLINE ;

message				: (emoticon | link | color | mention | WORD)+ ;

name				: WORD ;

command				: (SAYS | SHOUTS | POST) ':' ;
					 					
emoticon			: ':' '-'? ')'
					| ':' '-'? '('
					;

link                : TEXT '(' URL ')' ;

color				: '/' WORD '/' message '/';

mention				: '@' name ;


/*
 * Lexer Rules
 */
 
fragment A          : ('A'|'a') ;
fragment S          : ('S'|'s') ;
fragment Y          : ('Y'|'y') ;
fragment H          : ('H'|'h') ;
fragment O          : ('O'|'o') ;
fragment U          : ('U'|'u') ;
fragment T          : ('T'|'t') ;
fragment P          : ('P'|'p') ;
 
fragment LOWERCASE  : [a-z] ;
fragment UPPERCASE  : [A-Z] ;
 
SAYS                : S A Y S ;
 
SHOUTS              : S H O U T S;

POST                : P O S T ;
 
WORD                : (LOWERCASE | UPPERCASE | '_' )+ ;
 
WHITESPACE          : (' ' | '\t') -> skip ;
 
NEWLINE             : ('\r'? '\n' | '\r')+ ;
 
URL					: 'http' 's'? '://' ~[ )]+ ;

TEXT                : '[' ~[\]]+ ']';