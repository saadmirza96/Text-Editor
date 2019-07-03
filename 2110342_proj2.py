
import os
class Node():
    def __init__(self, data, pr = None, nxt = None):
        self.data = data
        self.pr = pr
        self.next = nxt

class DoublyLinkedList():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.pr = self.head
        self.size = 0
    def ad(self, node, data):
        addnode = Node(data)             
        if node.data == "":
            node.data = data
        else:
            self.tail.pr.next = addnode
            addnode.pr = self.tail.pr
            addnode.next = self.tail
            self.tail.pr = addnode
    def add(self, data):
        addnode = Node(data)
        if self.head.data == None:
            self.head.data = data
        else:
            self.tail.pr.next = addnode
            addnode.pr = self.tail.pr
            addnode.next = self.tail
            self.tail.pr = addnode
    def length(self):
        mainpnt = self.head
        length = 0
        while mainpnt.next.data != None:
            mainpnt = mainpnt.next
            length += 1
        return length

def Goto(mainlst, row, column):
    pointer = mainlst.head
    for e in range(row + 1):
        if pointer.next == mainlst.tail:
            mainlst.add(DoublyLinkedList())
        pointer = pointer.next
    global lst
    lst = pointer.pr.data
    pointer = pointer.pr.data.head
    for i in range(column + 1):
        if pointer.data == "":
            pass
        if pointer == lst.tail:
            addnode1 = Node("")
            lst.tail.pr.next = addnode1
            addnode1.pr = lst.tail.pr
            addnode1.next = lst.tail
            lst.tail.pr = addnode1
            pointer = addnode1
        if pointer == lst.head and pointer.data == None:
            pointer.data = ""
        pointer = pointer.next
    global x
    global y
    y = lst
    x = column
print('Welcome to our DS Text Editor')
print('Enter commands at the prompt')

text = input("")
mainLst = DoublyLinkedList()
mainpoint = mainLst.head
mainLst.head.data = DoublyLinkedList()
global txt
global ch
txt = ""
lst = None
y = None
x = None
ch = 0
if text == "Load":
    file = open('load.txt','s')
    lines = file.readlines()
    for line in lines:
        text = line
        if 'Goto' in text:
            txt = str(txt) + '\n' + str(text)
            r = int(text[5:7])
            s = int(text[7:])
            Goto(mainLst, r,s)
        if 'Forward' in text:
            yA = y.head
            if yA.next == y.tail and x > y.length():
                yA = mainLst.head.data
                x = 0
            elif x > y.length():
                yAListnode = yAListnode.next
                yA = yAListNode.data
            else:
                x +=1
        if "Back" in text:
            n = maiLst.head
            if y == y.head and x == 0: 
                pass
            else:
                x = x - 1
        if 'Insert' in text:
            txt = str(txt) + '\n' + str(text)
            text = text[7:]
            inpoint = y.head
            for u in range(x):
                inpoint = inpoint.next
            for v in text:
                y.ad(inpoint, v)
            ch = ch + len(text)
        if 'Delete' in text:
            numbr = int(text [7:])
            delPoint = y.head
            for q in range(numbr):
                delPoint.next = delPoint.next.next
                delPoint.next.pr = delPoint
                delPoint = delPoint.next
        
                
while text != "Quit":
    if 'Goto' in text:
        txt = str(txt) + '\n' + str(text)
        r = int(text[5:7])
        s = int(text[7:])
        Goto(mainLst, r,s)
        
    if 'Insert' in text:
        txt = str(txt) + '\n' + str(text)
        text = text[7:]
        inpoint = y.head
        for u in range(x):
            inpoint = inpoint.next
        for v in text:
            y.ad(inpoint, v)
        ch = ch + len(text)
    if 'Delete' in text:
        txt = str(txt) + '\n' + str(text)
        numbr = int(text [7:])
        delPoint = y.head
        for q in range(numbr):
            delPoint.next = delPoint.next.next
            delPoint.next.pr = delPoint
            delPoint = delPoint.next
    if 'CountCharacters' in text:
        chrs = 0
        yy = mainLst.head
        while yy.next != None:
            xx = yy.data.head
            while xx != None and xx.data != None:
                chrs = chrs + 1
                xx = xx.next
            yy = yy.next
        print('chrs')
    if 'CountLines' in text:
        lines = mainLst.length()
        print(lines)
    
    if 'PrintDoc' in text:
        yprnt = mainLst.head
        while yprnt.next != None:
            xprnt = yprnt.data.head
            while xprnt != None and xprnt.data != None:
                print(xprnt.data, end="")
                xprnt = xprnt.next
            print("")
            yprnt = yprnt.next
    
    if 'CC' in text:
        print(ch)
    
    if 'Forward' in text:
        txt = str(txt) + '\n' + str(text)
        yA = y.head
        if yA.next == y.tail and x > y.length():
            yA = mainLst.head.data
            x = 0
        elif x > y.length():
            yAListnode = yAListnode.next
            yA = yAListnode.data
        else:
            x += 1
    if 'Back' in text:
        txt = str(txt) + '\n' + str(text)
        n = mainLst.head
        if y == y.head and x ==0:
            pass
        else:
            x = x - 1
    if 'Save' in text:
        filename = str(input('Enter Your Filename Here:'))
        filename = filename + '.txt'
        file  = open(filename, 'w+')
        yprnt = mainLst.head
        while yprnt.next != None:
            xprnt = yprnt.data.head
            while xprnt != None and xprnt.data != None:
                file.write(xprnt.data)
                xprnt = xprnt.next
            file.write('\n')
            yprnt = yprnt.next
        file.close()
        Myfile = open('load.txt','w+')
        Myfile.write(txt)
        Myfile.close()
        file.close()


        print('______')
        print('File saved:', filename)

    print('')
    text = input('')
print('Thanks for using our Editor')
print(' ByeBye \n Regards \n Muhammad Saad & Muhammad Ali')
        
        

