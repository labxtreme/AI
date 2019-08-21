import numpy
import copy
import sys
sys.setrecursionlimit(3000)
sup=0
Notval=0
def moveleft(obj):
        frame=Block(obj.Mat,obj,'left')
        index=ndindex(frame.Mat,0)
        frame.Mat[index[0]][index[1]]=frame.Mat[index[0]][index[1]-1]
        frame.Mat[index[0]][index[1]-1]=0
        frame.hue=frame.calcheuristic()
        return frame
def moveright(obj):
        frame=Block(obj.Mat,obj,'right')
        index=ndindex(frame.Mat,0)
        frame.Mat[index[0]][index[1]]=frame.Mat[index[0]][index[1]+1]
        frame.Mat[index[0]][index[1]+1]=0
        frame.hue=frame.calcheuristic()
        return frame
def moveup(obj):
        frame=Block(obj.Mat,obj,'up')
        index=ndindex(frame.Mat,0)
        frame.Mat[index[0]][index[1]]=frame.Mat[index[0]-1][index[1]]
        frame.Mat[index[0]-1][index[1]]=0
        frame.hue=frame.calcheuristic()
        return frame
def movedown(obj):
        frame=Block(obj.Mat,obj,'down')
        index=ndindex(frame.Mat,0)
        frame.Mat[index[0]][index[1]]=frame.Mat[index[0]+1][index[1]]
        frame.Mat[index[0]+1][index[1]]=0
        frame.hue=frame.calcheuristic()
        return frame
def ndindex(ndarray, item):
    if len(ndarray.shape) == 1:
        try:
            return [ndarray.tolist().index(item)]
        except:
            pass
    else:
        for i, subarray in enumerate(ndarray):
            try:
                return [i] + ndindex(subarray, item)
            except:
                pass
def solvable_or_not(mat):
    k=mat.flatten()
    index=numpy.argwhere(k==0)
    k=numpy.delete(k,index)
    count=0
    i=0
    while i<8:
        j=i
        while j<8:
            if k[i]>k[j]:
                count+=1
            j+=1
        i+=1
    if count%2==0:
        return mat
    else:
        a = numpy.arange(9)
        numpy.random.shuffle(a)
        a=numpy.reshape(a,(3,3))
        a=solvable_or_not(a)
        return a
class Block:
    result=None
    checklist=[]
    Thematrix = numpy.arange(9)
    Thematrix=numpy.reshape(Thematrix,(3,3))
    NOT=0
    selected=[]
    theway=[]
    direction=[]
    def __init__(self,Matrix,par,last):
        self.Mat=copy.deepcopy(Matrix)
        self.parent=par
        self.last=last
        self.hue=None
    def calcheuristic(self):
        heu=0
        for var in self.Mat:
            for ele in var:
                   x=ndindex(Block.Thematrix,ele)
                   y=ndindex(self.Mat,ele) 
                   total=abs((x[0]-y[0]))+abs((x[1]-y[1]))
                   heu+=total
        return heu
    def heudecider(self):
        global sup
        global Notval
        minvalue=1000
        Block.NOT+=1
        list=copy.deepcopy(Block.checklist)
        for var in list:
            for varvar in var:
                if varvar.check_parent(varvar.Mat):
                    Block.checklist=[]
                    pass
                elif varvar==None:
                    pass
                elif (varvar.hue) < (minvalue):
                    for per in Block.selected:
                        del per
                    Block.selected=[]
                    Block.selected.append(varvar)
                    minvalue=varvar.hue
                    Block.checklist=[]
                elif (varvar.hue) == (minvalue):
                        Block.selected.append(varvar) 
        for var in Block.selected:
            if var.hue==0:
                Block.result=var
                return
            else:
                    var.Decider()
        self.heudecider()
    def check_parent(self,mat):
        if self.parent!=None:
            if (mat == self.parent.Mat).all():
                return 1
            else:
                if(self.parent.check_parent(mat)):
                    return 1
                else:
                    return 0
        else:
            return 0
    def path(self):
        Block.theway.append(self.Mat)
        Block.direction.append(self.last)
        if self.parent==None:
            return
        else:    
            self.parent.path()
    def show(self):        
        Block.direction.reverse()
        Block.theway.reverse()
        for var in range(len(Block.theway)):
            print(Block.direction[var])
            print(Block.theway[var])
        print("No. Of Steps",len(Block.theway))
    def Decider(self):
        listdec=[]
        if ndindex(self.Mat,0)==[0,0]:
            listdec.append(movedown(self))
            listdec.append(moveright(self))
        elif ndindex(self.Mat,0)==[0,1]:
            listdec.append(movedown(self))
            listdec.append(moveright(self))
            listdec.append(moveleft(self))
        elif ndindex(self.Mat,0)==[0,2]:
            listdec.append(movedown(self))
            listdec.append(moveleft(self))
        elif ndindex(self.Mat,0)==[1,0]:
            listdec.append(movedown(self))
            listdec.append(moveup(self))
            listdec.append(moveright(self))
        elif ndindex(self.Mat,0)==[1,1]:
            listdec.append(movedown(self))
            listdec.append(moveup(self))
            listdec.append(moveright(self))
            listdec.append(moveleft(self))
        elif ndindex(self.Mat,0)==[1,2]:
            listdec.append(movedown(self))
            listdec.append(moveup(self))
            listdec.append(moveleft(self))
        elif ndindex(self.Mat,0)==[2,0]:
            listdec.append(moveup(self))
            listdec.append(moveright(self))
        elif ndindex(self.Mat,0)==[2,1]:
            listdec.append(moveup(self))
            listdec.append(moveright(self))
            listdec.append(moveleft(self))
        elif ndindex(self.Mat,0)==[2,2]:
            listdec.append(moveup(self))
            listdec.append(moveleft(self))
        Block.checklist.append(listdec)
        if Block.NOT==0:
            self.heudecider()
a = numpy.arange(9)
numpy.random.shuffle(a)
a=numpy.reshape(a,(3,3))
a=solvable_or_not(a)
start=Block(a,None,'none')
start.Decider()
k=Block.result
Block.result.path()
Block.result.show()
