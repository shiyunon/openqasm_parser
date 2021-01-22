import numpy as np
import json
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.IntervalSet import IntervalSet
from antlr4.Token import CommonToken
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import InputMismatchException
from antlr4.tree.Tree import TerminalNodeImpl
from numpy.ma import sin, cos, sqrt, exp 

from gen4.qasm3Lexer import qasm3Lexer
from gen4.qasm3Listener import qasm3Listener
from gen4.qasm3Parser import qasm3Parser



def run_openqasm_parser(openqasm_file):
    
    # Lexing
    openqasm_stream = InputStream(openqasm_file)
    openqasm_lexer = qasm3Lexer(openqasm_stream)
    openqasm_stream = CommonTokenStream(openqasm_lexer)

    # Parsing
    openqasm_parser = qasm3Parser(openqasm_stream)
    # openqasm_parser.removeErrorListeners()
    # openqasm_parser.addErrorListener(CustomErrorListener())
    openqasm_parse_tree = openqasm_parser.program()
    
    # print([method_name for method_name in dir(openqasm_parse_tree) if callable(getattr(openqasm_parse_tree, method_name))])

    # print(openqasm_parse_tree.__repr__())

    # openqasm_listener = OpenQASMListener()

    # tree_walker = ParseTreeWalker()
    # tree_walker.walk(openqasm_listener, openqasm_parse_tree)
    
    my_dict = {}
    traverse(openqasm_parse_tree, my_dict)

    return my_dict

def traverse(tree, input_dict):

    if isinstance(tree, TerminalNodeImpl):
        token = tree.getSymbol()
        # print([method_name for method_name in dir(token) if callable(getattr(token, method_name))])
        input_dict["type"] = type(token).__name__
        input_dict["text"] = token.text

    else:
        children = []
    
        for i in range(tree.getChildCount()):
            child_dict = {}
            traverse(tree.getChild(i), child_dict)
            children.append(child_dict)

        name = type(tree).__name__.replace("Context", "")
        input_dict[name] = children

class OpenQASMListener(qasm3Listener):

    def __init__(self):
        self.js = {}

    def exitVersion(self, ctx: qasm3Parser.VersionContext) -> None:
        
        self.js['version'] = ctx.children[1].getText()

    def exitInclude(self, ctx: qasm3Parser.IncludeContext) -> None:

        if self.js.get('include') is None:
            self.js['include'] = [ctx.StringLiteral().getText().strip("\"")]



def main():
    file_name = "examples/dd.qasm"
    with open(file_name) as f:
        file_content = f.read()
    my_dict = run_openqasm_parser(file_content)
    
    print(my_dict)
    with open("output_json.txt", "w") as f_out:
        f_out.write(json.dumps(my_dict))


if __name__ == '__main__':
    main()
