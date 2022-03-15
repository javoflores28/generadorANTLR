grammar marzo;

program : expression+ ;

expression: 
    expression '+' expression #suma
    | Numero  #numero
    | Palabra #palabra
    | expression '-' expression #resta
    | expression '*' expression #multiplicacion
    | expression '/' expression #division
    | expression '<' expression #menor
    | expression '>' expression #mayor
    | expression '=' expression #igual
    ;

statement:
    'si (' expression ')' statement #si
    | 'si (' expression ')' statement 'sino' statement #siSino
    | 'soypalabra' Palabra  #declaroPalabra
    | 'soynumero' Numero #declaroNumero
    | 'imprimir:' expression #imprimo
    ;

// A continuación los tokens (comienzan con mayúscula)
Numero : [0-9]+;
Palabra:[a-zA-Z];
WS : [ \t\n\r]+ -> skip ;




