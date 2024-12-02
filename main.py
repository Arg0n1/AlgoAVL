from collections import deque

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Балансировка
        # Левое левое
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        # Правое правое
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        # Левое правое
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # Правое левое
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # Обходы
    def dfs_in_order(self, node, result): #Симметричный обход
        if node:
            self.dfs_in_order(node.left, result)
            result.append(node.key)
            self.dfs_in_order(node.right, result)

    def dfs_pre_order(self, node, result): #Прямой обход
        if node:
            result.append(node.key)
            self.dfs_pre_order(node.left, result)
            self.dfs_pre_order(node.right, result)

    def dfs_post_order(self, node, result): #Обратный обход
        if node:
            self.dfs_post_order(node.left, result)
            self.dfs_post_order(node.right, result)
            result.append(node.key)

    def bfs(self, root): #Обход в ширину
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

avl = AVLTree()
root = None

for key in [1, 12, 4, 7, 32, 23, 15, 2, 17]:
    root = avl.insert(root, key)

in_order_result = []
avl.dfs_in_order(root, in_order_result)
print("Симметричный обход:", in_order_result)

pre_order_result = []
avl.dfs_pre_order(root, pre_order_result)
print("Прямой обход:", pre_order_result)

post_order_result = []
avl.dfs_post_order(root, post_order_result)
print("Обратный обход:", post_order_result)

bfs_result = avl.bfs(root)
print("Обход в ширину:", bfs_result)

root = avl.delete(root, 12)
print("\nПосле удаления 12:")

in_order_result = []
avl.dfs_in_order(root, in_order_result)
print("Симметричный обход:", in_order_result)

pre_order_result = []
avl.dfs_pre_order(root, pre_order_result)
print("Прямой обход:", pre_order_result)

post_order_result = []
avl.dfs_post_order(root, post_order_result)
print("Обратный обход:", post_order_result)

bfs_result = avl.bfs(root)
print("Обход в ширину:", bfs_result)

print("\nПосле добавления 3")
root = avl.insert(root, 3)

in_order_result = []
avl.dfs_in_order(root, in_order_result)
print("Симметричный обход:", in_order_result)

pre_order_result = []
avl.dfs_pre_order(root, pre_order_result)
print("Прямой обход:", pre_order_result)

post_order_result = []
avl.dfs_post_order(root, post_order_result)
print("Обратный обход:", post_order_result)

bfs_result = avl.bfs(root)
print("Обход в ширину:", bfs_result)