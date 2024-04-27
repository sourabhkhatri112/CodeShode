class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def preOrderTraversal(rootNode):
        if rootNode is None:
            return
        print(rootNode.data)
        TreeNode.preOrderTraversal(rootNode.leftChild)
        TreeNode.preOrderTraversal(rootNode.rightChild)


rootNode = TreeNode("Drinks")

hotDrinks = TreeNode("HotDrinks")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")

coldDrinks = TreeNode("ColdDrinks")
cola = TreeNode("cola")
fanta = TreeNode("fanta")

rootNode.leftChild = hotDrinks
rootNode.rightChild = coldDrinks
coldDrinks.leftChild = cola
coldDrinks.rightChild = fanta
hotDrinks.leftChild = tea
hotDrinks.rightChild = coffee
TreeNode.preOrderTraversal(rootNode)
