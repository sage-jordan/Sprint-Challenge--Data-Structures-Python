import time

start_time = time.time()
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if greater, go right
        if value >= self.value:
            # check if right exists
            if self.right is not None:
                # recursive
                self.right.insert(value)
            # if not, create a node with that value and set as right child
            else:
                new_node = BSTNode(value)
                self.right = new_node
        # else go left
        else:
            # check if left exists
            if self.left is not None:
                # recursive
                self.left.insert(value)
            else: 
                new_node = BSTNode(value)
                self.left = new_node
            
            

    def contains(self, target):
        # when we start searching, slef will be the root
        # compare the target against self
        if target == self.value:
            return True
        if target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            print("\nself.value: ", self.value)
            return self.right.get_max()

        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
""" Runtime 7.91s """
# for name_1 in names_1:
    # for name_2 in names_2:
    #     if name_1 == name_2:
    #         duplicates.append(name_1)

""" FINAL RUNTIME 1.11s """
# wrote BSTNode above
bst = BSTNode("empty_Node")
for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
""" Runtime 1.25s """
# duplicates = [ name for name in names_1 if name in names_2 ] 
