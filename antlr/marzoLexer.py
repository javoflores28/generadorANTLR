# Generated from /Users/javierflores/Desktop/GeneradorANTLR/antlr/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("j\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\6\17^\n\17\r\17\16\17_\3\20\3\20\3\21")
        buf.write("\6\21e\n\21\r\21\16\21f\3\21\3\21\2\2\22\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\2")
        buf.write("k\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5")
        buf.write("%\3\2\2\2\7\'\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2")
        buf.write("\2\17/\3\2\2\2\21\61\3\2\2\2\23\66\3\2\2\2\258\3\2\2\2")
        buf.write("\27=\3\2\2\2\31H\3\2\2\2\33R\3\2\2\2\35]\3\2\2\2\37a\3")
        buf.write("\2\2\2!d\3\2\2\2#$\7-\2\2$\4\3\2\2\2%&\7/\2\2&\6\3\2\2")
        buf.write("\2\'(\7,\2\2(\b\3\2\2\2)*\7\61\2\2*\n\3\2\2\2+,\7>\2\2")
        buf.write(",\f\3\2\2\2-.\7@\2\2.\16\3\2\2\2/\60\7?\2\2\60\20\3\2")
        buf.write("\2\2\61\62\7u\2\2\62\63\7k\2\2\63\64\7\"\2\2\64\65\7*")
        buf.write("\2\2\65\22\3\2\2\2\66\67\7+\2\2\67\24\3\2\2\289\7u\2\2")
        buf.write("9:\7k\2\2:;\7p\2\2;<\7q\2\2<\26\3\2\2\2=>\7u\2\2>?\7q")
        buf.write("\2\2?@\7{\2\2@A\7r\2\2AB\7c\2\2BC\7n\2\2CD\7c\2\2DE\7")
        buf.write("d\2\2EF\7t\2\2FG\7c\2\2G\30\3\2\2\2HI\7u\2\2IJ\7q\2\2")
        buf.write("JK\7{\2\2KL\7p\2\2LM\7w\2\2MN\7o\2\2NO\7g\2\2OP\7t\2\2")
        buf.write("PQ\7q\2\2Q\32\3\2\2\2RS\7k\2\2ST\7o\2\2TU\7r\2\2UV\7t")
        buf.write("\2\2VW\7k\2\2WX\7o\2\2XY\7k\2\2YZ\7t\2\2Z[\7<\2\2[\34")
        buf.write("\3\2\2\2\\^\t\2\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3")
        buf.write("\2\2\2`\36\3\2\2\2ab\t\3\2\2b \3\2\2\2ce\t\4\2\2dc\3\2")
        buf.write("\2\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\b\21\2")
        buf.write("\2i\"\3\2\2\2\5\2_f\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    Numero = 14
    Palabra = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", "'='", "'si ('", "')'", 
            "'sino'", "'soypalabra'", "'soynumero'", "'imprimir:'" ]

    symbolicNames = [ "<INVALID>",
            "Numero", "Palabra", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "Numero", 
                  "Palabra", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


