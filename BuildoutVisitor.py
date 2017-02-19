# Generated from Buildout.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by BuildoutParser.

class BuildoutVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BuildoutParser#buildout.
    def visitBuildout(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#section.
    def visitSection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#section_header.
    def visitSection_header(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#section_name.
    def visitSection_name(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#key_value.
    def visitKey_value(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#operator.
    def visitOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#assign.
    def visitAssign(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#add.
    def visitAdd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#remove.
    def visitRemove(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#values.
    def visitValues(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#key.
    def visitKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BuildoutParser#value.
    def visitValue(self, ctx):
        return self.visitChildren(ctx)


