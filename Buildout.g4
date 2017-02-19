grammar Buildout;

buildout: (section)+;

section: section_header (key_value)* ;
section_header: '[' section_name ']' ('\n' | EOF ) ;
section_name: ID ;

key_value: key_value_assign | key_value_add | key_value_remove ;

key_value_assign: key WS* '=' values;
key_value_add: key WS* '+=' values;
key_value_remove: key WS* '-=' values;

values: WS* value (WS+ value)* WS* '\n'? EOF?  ('\n' WS+ value (WS+ value)? WS* '\n'? EOF? )? ;

key: ID ;
value: ID;

ID: [a-z0-9]+ ;
WS : [ \t\r\n]+ ;
