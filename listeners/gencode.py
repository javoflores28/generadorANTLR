from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

class GenCode(marzoListener):
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    def exitNumero(self, ctx:marzoParser.NumeroContext):
        print("load $1, " + ctx.Numero().getText())

    def exitPalabra(self, ctx:marzoParser.PalabraContext):
        print("load $1, " + ctx.Palabra().getText())

    # Enter a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        print('Suma')

 
    def exitResta(self, ctx:marzoParser.RestaContext):
        print('Resta')


    # Enter a parse tree produced by marzoParser#division.
    def exitDivision(self, ctx:marzoParser.DivisionContext):
        print('Division')


    # Enter a parse tree produced by marzoParser#multiplicacion.
    def exitMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        print('Multiplicacion')

    # Enter a parse tree produced by marzoParser#numero.
    def exitNumero(self, ctx:marzoParser.NumeroContext):
        print('Numero')


    # Enter a parse tree produced by marzoParser#palabra.
    def exitPalabra(self, ctx:marzoParser.PalabraContext):
        print('Palabra')


    # Enter a parse tree produced by marzoParser#mayor.
    def exitMayor(self, ctx:marzoParser.MayorContext):
        print("Mayorque")

    # Enter a parse tree produced by marzoParser#menor.
    def exitMenor(self, ctx:marzoParser.MenorContext):
        print('Menorque')

   
    # Enter a parse tree produced by marzoParser#igual.
    def exitIgual(self, ctx:marzoParser.IgualContext):
        print('Igual')

    # Exit a parse tree produced by marzoParser#si.
    def exitSi(self, ctx:marzoParser.SiContext):
        print('Si/If')


    # Exit a parse tree produced by marzoParser#siSino.
    def exitSiSino(self, ctx:marzoParser.SiSinoContext):
        print('SiSino/IfElse')


    # Exit a parse tree produced by marzoParser#declaroPalabra.
    def exitDeclaroPalabra(self, ctx:marzoParser.DeclaroPalabraContext):
        print('Declaro Palabra')


    # Exit a parse tree produced by marzoParser#declaroNumero.
    def exitDeclaroNumero(self, ctx:marzoParser.DeclaroNumeroContext):
        print('Declaro Numero')

    # Exit a parse tree produced by marzoParser#imprimo.
    def exitImprimo(self, ctx:marzoParser.ImprimoContext):
        print('Imprimiendo')