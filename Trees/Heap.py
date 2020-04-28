'''
'''

from Trees.BinaryTree import BinaryTree, Node

class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if i in xs:
            self.insert(i)


    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"
        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        l_satisfy=True
        r_satisfy=True
        if node.right:
            if node.value>node.right.value:
                return False
            else:
                r_satisfy=Heap._is_heap_satisfied(node.right)
        if node.left:
            if node.value>node.left.value:
                return False
            else:
                ls_satisfy=Heap._is_heap_satisfied(node.left)
        return r_satisfy and l_satisfy

    def size(self):
        'returns size of tree'
        if self.root is None:
            return 0
        stack = []
        stack.append(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            if node.right:
                size += 1
                stack.append(node.right)
        return size

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            Heap._insert(value, self.root)


    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return
        if node.left is None:
            node.left=Node(value)
            if node.left.value<node.value:
                return Heap._trickle_up(node,value)
        elif node.right is None:
            node.right=Node(value)
            if node.right.value<node.value:
                return Heap._trickle_up(node,value)
        if node.left and node.right:
            node.left=Heap._insert(node.left,value)
            if node.left.value<node.value:
                return Heap._trickle_up(node,value)


    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for i in xs:
            self.insert(i)


    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a Heap it should be easy to implement.
        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        if self.root:
            return Heap._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return
        else:
            return node.value

    @staticmethod
    def _delete_this(node):
        if node is None:
            return
        elif node.left:
            node.left=Heap._delete_this(node.left)
        elif node.right:
            node.right=Heap._delete_this(node.right)
        else:
            if node.left is None and node.right is None:
                return None
        return node


    def remove_min(self):
        '''
        Removes the minimum value from the Heap. 
        If the heap is empty, it does nothing.
        FIXME:
        Implement this function.
        '''
        if self.root is None: 
            return None
        elif self.root.right is None and self.root.left is None:
            self.root = None
        else:
            right_node = Heap._right_node(self.root)
            self.root = Heap._remove(self.root)
            if right_node == self.root.value:
                return 
            else:
                self.root.value = right_node
            if Heap._is_heap_satisfied(self.root) == False: 
                return Heap._trickle_down(self.root)

    @staticmethod
    def _right_node(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node.right is None and node.left is None:
            return node.value
        elif node.right:
            return Heap._right_node(node.right)
        elif node.left:
            return Heap._right_node(node.left)

    def trickle_up(node, value):
        '''
        FIXME:
        Implement this function.
        '''
        leaf = node
        if len(binsize) == 2:
            if binsize[-1] == '0':
                if node.value > node.left.value:
                    Heap.swap(node, node.left)
            else:
                if node.value > node.right.value:
                    Heap.swap(node, node.right)
        else:
            stack = []
            for digit in binsize[1:-1]:
                if digit == '0':
                    stack.append(node.left)
                    node = node.left
                if digit == '1':
                    stack.append(node.right)
                    node = node.right
            while len(stack) > 0:
                node = stack.pop()
                stack.append(node)
                if node.value > node.left.value:
                    stack.pop()
                    Heap.swap(node, node.left)
                    stack.append(node)
                elif node.right and node.value > node.right.value:
                    stack.pop()
                    Heap.swap(node, node.right)
                    stack.append(node)
                else:
                    stack.pop()
        if startnode.left and startnode.value > startnode.left.value:
            Heap.swap(startnode, startnode.left)
        elif startnode.right and startnode.value > startnode.right.value:
            Heap.swap(startnode, startnode.right)

    @staticmethod
    def _trickle_down(node):
        '''
        FIXME:
        Implement this function.
        '''
        if node.left is None and node.right is None: 
            return nod
        if node.right and (node.left is None or node.right.value <= node.left.value): 
            if node.right.value < node.value: 
                np = node.right.value
                nrc = node.value
                node.value = np
                node.right.value = nrc
            node.right = Heap._trickle_down(node.right)
        elif node.left and (node.right is None or node.left.value <= node.right.value): 
            if node.left.value < node.value: 
                np = node.left.value
                nlc = node.value
                node.value = np
                node.left.value = nlc
            node.left = Heap._trickle_down(node.left)
        return node

