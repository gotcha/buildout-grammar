from antlr4 import InputStream
from antlr4 import CommonTokenStream
from antlr4 import DiagnosticErrorListener
from BuildoutLexer import BuildoutLexer
from BuildoutParser import BuildoutParser
from rewriter import RewriteVisitor
from difflib import context_diff


data = """
[build_out]
parts = 
 test
"""


def main():
    input = InputStream(data)
    lexer = BuildoutLexer(input)
    stream = CommonTokenStream(lexer)
    parser = BuildoutParser(stream)
    tree = parser.buildout()

    visitor = RewriteVisitor()
    output = visitor.visitBuildout(tree)

    for line in context_diff(output.splitlines(), data.splitlines(), fromfile='output', tofile='data'):
        print line

if __name__ == '__main__':
    main()
