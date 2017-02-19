# Generated from Buildout.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\n+\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write(u"\6\3\6\3\6\3\7\3\7\3\7\3\b\6\b#\n\b\r\b\16\b$\3\t\6\t")
        buf.write(u"(\n\t\r\t\16\t)\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write(u"\n\3\2\4\5\2\62;aac|\5\2\13\f\17\17\"\",\2\3\3\2\2\2")
        buf.write(u"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write(u"\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\25")
        buf.write(u"\3\2\2\2\7\27\3\2\2\2\t\31\3\2\2\2\13\33\3\2\2\2\r\36")
        buf.write(u"\3\2\2\2\17\"\3\2\2\2\21\'\3\2\2\2\23\24\7\f\2\2\24\4")
        buf.write(u"\3\2\2\2\25\26\7]\2\2\26\6\3\2\2\2\27\30\7_\2\2\30\b")
        buf.write(u"\3\2\2\2\31\32\7?\2\2\32\n\3\2\2\2\33\34\7-\2\2\34\35")
        buf.write(u"\7?\2\2\35\f\3\2\2\2\36\37\7/\2\2\37 \7?\2\2 \16\3\2")
        buf.write(u"\2\2!#\t\2\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3\2\2\2$%\3\2")
        buf.write(u"\2\2%\20\3\2\2\2&(\t\3\2\2\'&\3\2\2\2()\3\2\2\2)\'\3")
        buf.write(u"\2\2\2)*\3\2\2\2*\22\3\2\2\2\5\2$)\2")
        return buf.getvalue()


class BuildoutLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    ID = 7
    WS = 8

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'\n'", u"'['", u"']'", u"'='", u"'+='", u"'-='" ]

    symbolicNames = [ u"<INVALID>",
            u"ID", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"ID", u"WS" ]

    grammarFileName = u"Buildout.g4"

    def __init__(self, input=None):
        super(BuildoutLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


