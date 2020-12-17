class Node:
    def show(self):
        print(self.__value)
        if self.__children:
            for child in self.__children:
                print("-"*child.getDepth(), end="")
                child.show()

    def addChild(self, node):
        assert isinstance(node, Node), f"node={node} is not a Node"
        node.updateDepth(self.__depth+1)
        self.__children.append(node)

    def updateDepth(self, depth):
        self.__depth = depth

    def getDepth(self):
        return self.__depth

    def __init__(self, value):
        self.__value = value
        self.__children = []
        self.__depth = 0


if __name__ == "__main__":
    root = Node(10)
    n1 = Node(20)
    root.addChild(n1)
    root.addChild(Node(22))
    n1.addChild(Node(30))
    n1.addChild(Node(31))
    root.show()
