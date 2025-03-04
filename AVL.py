class node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.hight = 0

class Tree:
    def __init__(self):
        self.NodeList = None

    def RightRotation(self, Node):
        Z = Node
        Y = Z.left

        T3 = Y.right

        Z.left = T3
        Y.right = Z

        Z.hight = 1 + max(self.Hight(Z.left), self.Hight(Z.right))
        Y.hight = 1 + max(self.Hight(Y.left), self.Hight(Y.right))

        return Y

    def LeftRotation(self, Node):
        Z = Node
        Y = Z.right

        T2 = Y.left

        Z.right = T2
        Y.left = Z

        Z.hight = 1 + max(self.Hight(Z.left), self.Hight(Z.right))
        Y.hight = 1 + max(self.Hight(Y.left), self.Hight(Y.right))

        return Y

    def Balance(self, Node):
        leftNode = Node.left
        rightNode = Node.right
        if not leftNode:
            hightLeft = 0
        else:
            hightLeft = leftNode.hight
        
        if not rightNode:
            hightRight = 0
        else:
            hightRight = rightNode.hight

        return hightLeft - hightRight

    def Hight(self, Node):
        if Node:
            return Node.hight
        else:
            return 0

    def insert(self, Value, Node):
        if Node == None:
            return node(Value)
        if Value < Node.value:
            Node.left = self.insert(Value, Node.left)
        elif Value > Node.value:
            Node.right = self.insert(Value, Node.right)
        
        Node.hight = 1 + max(self.Hight(Node.left), self.Hight(Node.right))

        balance = self.Balance(Node)

        print(Node.value," Balance = ",balance)

        if balance > 1 and Value < Node.left.value:
            print("Right Rotation")
            return self.RightRotation(Node)

        if balance < -1 and Value > Node.right.value:
            print("Left Rotation")
            return self.LeftRotation(Node) 

        if balance > 1 and Value > Node.left.value:
            print("Left Right Rotation")
            Node.left = self.LeftRotation(Node.left)
            return self.RightRotation(Node)

        if balance < -1 and Value < Node.right.value:
            print("Right Left Rotation")
            Node.right = self.RightRotation(Node.right)
            return self.LeftRotation(Node)        
        return Node
            
                
    
    def insert_value(self, value):
        self.NodeList = self.insert(value, self.NodeList)
        
        
    def printTree(self, Node, list2D):
        if Node:
            print(Node.value,end = "")
            Low = 0
            while 1: 

                if list2D[Low][None.hight]:
                    Low += 1
                else:
                    list2D = list2D[Low][None.hight] = Node.value
                return list2D
            self.printTree(Node.left, list2D)
            self.printTree(Node.right, list2D)
            
            

##T = Tree()
##for i in range(10, 0, -1):
##    T.insert_value(i)


##T.printTree(T.NodeList, "Root")
Low = 0

while 1: 

    if list2D[Low][0]:
        Low += 1
    else:
        list2D = list2D[Low][0] = Low
print(0-2)

