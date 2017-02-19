grammar Buildout;

buildout: (WS* '\n')* (section)+;

section: section_header WS* (key_value)* ;
section_header: '[' section_name ']' ('\n' | EOF ) ;
section_name: ID ;

key_value: key WS* operator values;
operator: assign | add | remove;
assign: '=';
add: '+=';
remove: '-=';

values: WS* value (WS+ value)* WS* '\n'? EOF?  ('\n' WS+ value (WS+ value)? WS* '\n'? EOF? )? ;

key: ID ;
value: ID;

ID: [a-z_0-9]+ ;
WS : [ \t\r\n]+ ;
