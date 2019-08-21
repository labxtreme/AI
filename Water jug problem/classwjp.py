waste=0
def fillA(node):
    nodecpy=Node(node.x,node.y,node)
    Node.parents.append((node.x,node.y))
    nodecpy.x=4
    Node.no_of_nodes+=1
    nodecpy.addNode()
def fillB(node):
    nodecpy=Node(node.x,node.y,node)
    Node.parents.append((node.x,node.y))
    nodecpy.y=3
    Node.no_of_nodes+=1
    nodecpy.addNode()
def frAB(node):
    nodecpy=Node(node.x,node.y,node)
    Node.parents.append((node.x,node.y))
    if nodecpy.x+nodecpy.y>=3:
        r=nodecpy.x+nodecpy.y
        nodecpy.x=r-3
        nodecpy.y=3
    else:
        nodecpy.y=nodecpy.x
        nodecpy.x=0
    Node.no_of_nodes+=1
    nodecpy.addNode()
def frBA(node):
    nodecpy=Node(node.x,node.y,node)
    Node.parents.append((node.x,node.y))
    if nodecpy.x+nodecpy.y>=4:
        r=nodecpy.x+nodecpy.y
        nodecpy.y=r-4
        nodecpy.x=4
    else:
        nodecpy.x=nodecpy.y
        nodecpy.y=0
    Node.no_of_nodes+=1
    nodecpy.addNode()
def porA(node):
    global waste
    nodecpy=Node(node.x,node.y,node)
    Node.parents.append((node.x,node.y))
    waste+=nodecpy.x
    r=nodecpy.x
    nodecpy.x=0
    Node.no_of_nodes+=1
    nodecpy.addNode()
    waste-=r
def porB(node):
    nodecpy=Node(node.x,node.y,node)  
    Node.parents.append((node.x,node.y))
    global waste
    waste+=nodecpy.y
    r=nodecpy.y
    nodecpy.y=0
    Node.no_of_nodes+=1
    nodecpy.addNode()
    waste-=r
class Node:
    no_of_nodes=0 
    result=None
    waste=0
    parents=[]
    def __init__(self,x,y,par):
        self.x=x
        self.y=y
        self.parent=par
    def addNode(self):
        if Node.result!=None:
            pass
        elif (self.x,self.y) in Node.parents:
            pass
        elif self.x==0 and self.y==0:
            Node.no_of_nodes+=1
            fillA(self)
            fillB(self)
        elif self.x==2 and self.y==0:
            Node.result=self
        elif self.x==3 and self.y==0:
            fillA(self)
            fillB(self)
            frAB(self)
            porA(self)
        elif self.x==1 and self.y==0:
            fillA(self)
            fillB(self)
            frAB(self)
            porA(self)
        elif self.x==4 and self.y==0:
            fillB(self)
            frAB(self)
            porA(self)
        elif self.x==0 and self.y==1:
            fillA(self)
            fillB(self)
            frBA(self)
            porB(self)
        elif self.x==4 and self.y==1:
            fillB(self)
            frAB(self)
            porA(self)
            porB(self)
        elif self.x==0 and self.y==2:
            frBA(self)
        elif self.x==4 and self.y==2:
            fillB(self)
            frAB(self)
            porA(self)
            porB(self)
        elif self.x==0 and self.y==3:
            fillA(self)
            frBA(self)
            porB(self)
        elif self.x==1 or self.x==3 and self.y==3:
            fillA(self)
            frBA(self)
            porA(self)
            porB(self)
        elif self.x==2 and self.y==3:
            porB(self)
        elif self.x==4 and self.y==3:
            porA(self) 
            porB(self)
    def nodeshow(self):
        if self.parent!=None:
            print("({},{})".format(self.x,self.y),end='->')
            self.parent.nodeshow()
        else          :  
            print("({},{})".format(self.x,self.y),end='-> None')
    def show(self):
        print("Total Number of Nodes =",Node.no_of_nodes)
        i=0
        Node.result.nodeshow()
        print("\nTotal water wasted = {} liters".format(Node.waste))
        i+=1
A,B=0,0
root=Node(A,B,None)
root.addNode()
root.show()
