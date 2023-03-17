
class BST:

    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):              
        if self.data == data:
            return
        
        if self.data > data:
            if self.lchild:
                self.lchild.insert(data)
            
            else:
                self.lchild = BST(data)

        else:
            if self.rchild:
                self.rchild.insert(data)
            
            else:
                self.rchild = BST(data)

    def search(self, data):
        if self.data == data:
            print("Node is found!")
            return
                    
        if data < self.data:
            if self.lchild:
                self.lchild.search(data)

            else:
                print("Node is not found in tree!")                

        else:
            if self.rchild:
                self.rchild.search(data)

            else:
                print("Node is not found in tree!")                
        
    def preorder(self):
        elements = []

        elements.append(self.data)

        if self.lchild:
            elements += self.lchild.preorder()
        
        if self.rchild:
            elements += self.rchild.preorder()
        
        return elements    

def build_tree(elements):
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root    


def main():

    list1 = [10, 6, 3, 1, 6, 98, 3, 7, 17, 16, 11, 20, 35]

    value = int(input("Give a value for add inside the tree: "))
    list1.append(value)
    numbers_tree = build_tree(list1)
    print(numbers_tree.preorder())

    value2 = int(input("Give a value for search inside the tree: "))
    searchvalue = numbers_tree.preorder()
    numbers_tree.search(value2)

    if value2 in numbers_tree.preorder():
        print("Node's index is:" , searchvalue.index(value2)) 
    else:
        pass
    
    value3 = int(input("Give an index for search inside the tree: "))
    
    if value3 in numbers_tree.preorder():
        print("Index of node is:" , searchvalue[value3]) 
    else:
        print("Index not exist!")
   
main()
