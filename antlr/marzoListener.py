# Generated from /Users/javierflores/Desktop/GeneradorANTLR/antlr/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#division.
    def enterDivision(self, ctx:marzoParser.DivisionContext):
        pass

    # Exit a parse tree produced by marzoParser#division.
    def exitDivision(self, ctx:marzoParser.DivisionContext):
        pass


    # Enter a parse tree produced by marzoParser#multiplicacion.
    def enterMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        pass

    # Exit a parse tree produced by marzoParser#multiplicacion.
    def exitMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        pass


    # Enter a parse tree produced by marzoParser#numero.
    def enterNumero(self, ctx:marzoParser.NumeroContext):
        pass

    # Exit a parse tree produced by marzoParser#numero.
    def exitNumero(self, ctx:marzoParser.NumeroContext):
        pass


    # Enter a parse tree produced by marzoParser#palabra.
    def enterPalabra(self, ctx:marzoParser.PalabraContext):
        pass

    # Exit a parse tree produced by marzoParser#palabra.
    def exitPalabra(self, ctx:marzoParser.PalabraContext):
        pass


    # Enter a parse tree produced by marzoParser#mayor.
    def enterMayor(self, ctx:marzoParser.MayorContext):
        pass

    # Exit a parse tree produced by marzoParser#mayor.
    def exitMayor(self, ctx:marzoParser.MayorContext):
        pass


    # Enter a parse tree produced by marzoParser#menor.
    def enterMenor(self, ctx:marzoParser.MenorContext):
        pass

    # Exit a parse tree produced by marzoParser#menor.
    def exitMenor(self, ctx:marzoParser.MenorContext):
        pass


    # Enter a parse tree produced by marzoParser#igual.
    def enterIgual(self, ctx:marzoParser.IgualContext):
        pass

    # Exit a parse tree produced by marzoParser#igual.
    def exitIgual(self, ctx:marzoParser.IgualContext):
        pass


    # Enter a parse tree produced by marzoParser#resta.
    def enterResta(self, ctx:marzoParser.RestaContext):
        pass

    # Exit a parse tree produced by marzoParser#resta.
    def exitResta(self, ctx:marzoParser.RestaContext):
        pass


    # Enter a parse tree produced by marzoParser#si.
    def enterSi(self, ctx:marzoParser.SiContext):
        pass

    # Exit a parse tree produced by marzoParser#si.
    def exitSi(self, ctx:marzoParser.SiContext):
        pass


    # Enter a parse tree produced by marzoParser#siSino.
    def enterSiSino(self, ctx:marzoParser.SiSinoContext):
        pass

    # Exit a parse tree produced by marzoParser#siSino.
    def exitSiSino(self, ctx:marzoParser.SiSinoContext):
        pass


    # Enter a parse tree produced by marzoParser#declaroPalabra.
    def enterDeclaroPalabra(self, ctx:marzoParser.DeclaroPalabraContext):
        pass

    # Exit a parse tree produced by marzoParser#declaroPalabra.
    def exitDeclaroPalabra(self, ctx:marzoParser.DeclaroPalabraContext):
        pass


    # Enter a parse tree produced by marzoParser#declaroNumero.
    def enterDeclaroNumero(self, ctx:marzoParser.DeclaroNumeroContext):
        pass

    # Exit a parse tree produced by marzoParser#declaroNumero.
    def exitDeclaroNumero(self, ctx:marzoParser.DeclaroNumeroContext):
        pass


    # Enter a parse tree produced by marzoParser#imprimo.
    def enterImprimo(self, ctx:marzoParser.ImprimoContext):
        pass

    # Exit a parse tree produced by marzoParser#imprimo.
    def exitImprimo(self, ctx:marzoParser.ImprimoContext):
        pass



del marzoParser