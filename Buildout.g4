grammar Buildout;

buildout: (section)+;
section: section_header (key_value)* ;
section_header: '[' section_name ']' '\n' ;
section_name: ID ;
key_value: key_value_assign | key_value_add | key_value_remove ;
key_value_assign: key '=' value '\n' ;
key_value_add: key '+=' value '\n' ;
key_value_remove: key '-=' value '\n' ;
key: ID ;
value: ID ;
ID: [a-z0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
