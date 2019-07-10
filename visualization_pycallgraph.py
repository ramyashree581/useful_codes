def test():
    print("Hello")

def test2():
    print("Hello2")
    test()
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

with PyCallGraph(output=GraphvizOutput()):
    graphviz = GraphvizOutput()
    graphviz.output_file = 'basic.png'
    with PyCallGraph(output=graphviz):
        test2()
