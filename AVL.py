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
        #ต้องเช็คความสูงของโหนดลูกหลังการหมุน
        Z.hight = 1 + max(self.Hight(Z.left), self.Hight(Z.right))
        Y.hight = 1 + max(self.Hight(Y.left), self.Hight(Y.right))

        return Y

    def LeftRotation(self, Node):
        Z = Node
        Y = Z.right

        T2 = Y.left

        Z.right = T2
        Y.left = Z
        #ต้องเช็คความสูงของโหนดลูกหลังการหมุน
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

        if balance > 1 and Value < Node.left.value: #เช็คเงื่อนไขในการหมุนขวา คือ ความสูงของโหนดลูกมีความไม่สมดุลทางซ้าย
            print("Right Rotation")                 #          5                        4
            return self.RightRotation(Node)         #         /                        /  \
                                                    #        4            --->        3    5
                                                    #       /
                                                    #      3
        
        if balance < -1 and Value > Node.right.value: #เช็คเงื่อนไขในการหมุนซ้าย คือ ความสูงของโหนดลูกมีความไม่สมดุลทางขวา
            print("Left Rotation")                  #          3                         4
            return self.LeftRotation(Node)          #           \                       /  \
                                                    #            4         --->        3    5
                                                    #             \
                                                    #              5

        if balance > 1 and Value > Node.left.value: #เช็คเงื่อนไขในการหมุนซ้ายขวา คือ ความสูงของโหนดลูกมีความไม่สมดุลเอียงซ้ายไปขวา
            print("Left Right Rotation")                #           6                  6                   5
            Node.left = self.LeftRotation(Node.left)    #          /                  /                   / \
            return self.RightRotation(Node)             #         4        --->      5        --->       4   6
                                                        #          \                /
                                                        #            5             4
                                                        
        if balance < -1 and Value < Node.right.value: #เช็คเงื่อนไขในการหมุนขวาซ้าย คือ ความสูงของโหนดลูกมีความไม่สมดุลเอียงขวาไปซ้าย
            print("Right Left Rotation")                #     h = 2       5                   5                   6
            Node.right = self.RightRotation(Node.right) #                  \                   \                 / \
            return self.LeftRotation(Node)              #     h = 1         7    --->           6    --->       5   7
                                                        #                  /                     \
                                                        #     h = 0       6                       7
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

