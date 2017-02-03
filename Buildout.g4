grammar Buildout;

buildout: (section)+;

section: section_header (key_value)* ;
section_header: '[' section_name ']' nl ;
section_name: ID ;

key_value: key_value_assign | key_value_add | key_value_remove ;

key_value_assign: key '=' value nl ;
key_value_add: key '+=' value nl ;
key_value_remove: key '-=' value nl ;

nl: '\n' | EOF ;

key: ID ;
value: ID ;
ID: [a-z0-9]+ ;

WS : [ \t\r\n]+ -> skip ;
