# Generated from /Users/javierflores/Desktop/GeneradorANTLR/antlr/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete generic visitor for a parse tree produced by marzoParser.

class marzoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by marzoParser#program.
    def visitProgram(self, ctx:marzoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#suma.
    def visitSuma(self, ctx:marzoParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#division.
    def visitDivision(self, ctx:marzoParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#multiplicacion.
    def visitMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#numero.
    def visitNumero(self, ctx:marzoParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#palabra.
    def visitPalabra(self, ctx:marzoParser.PalabraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#mayor.
    def visitMayor(self, ctx:marzoParser.MayorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#menor.
    def visitMenor(self, ctx:marzoParser.MenorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#igual.
    def visitIgual(self, ctx:marzoParser.IgualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#resta.
    def visitResta(self, ctx:marzoParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#si.
    def visitSi(self, ctx:marzoParser.SiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#siSino.
    def visitSiSino(self, ctx:marzoParser.SiSinoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaroPalabra.
    def visitDeclaroPalabra(self, ctx:marzoParser.DeclaroPalabraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#declaroNumero.
    def visitDeclaroNumero(self, ctx:marzoParser.DeclaroNumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by marzoParser#imprimo.
    def visitImprimo(self, ctx:marzoParser.ImprimoContext):
        return self.visitChildren(ctx)



del marzoParser