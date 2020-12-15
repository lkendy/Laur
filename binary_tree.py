from node import Node

class BynaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with that value already exist')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node =self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError(f'A node with {value} was not found')


    def inorder(self):
        self._inorder_loop(self.head)

    def _inorder_loop(self, current_node):
        if not current_node:
            return
        self._inorder_loop(current_node.left)
        print(current_node)
        self._inorder_loop(current_node.right)

    def preorder(self):
        self._preorder_loop(self.head)

    def _preorder_loop(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._preorder_loop(current_node.left)
        self._preorder_loop(current_node.right)

    def main_node(self, value: int) -> Node:
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and current_node.left.value == value) or\
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

    def node_right_side(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        deleting = self.find(value)
        deletingNode = self.main_node(value)

        if deleting.left and deleting.right:
            deleting_rightmost = self.node_right_side(deleting.left)
            del_rightmost_mainnode = self.main_node(deleting_rightmost.value)

            if del_rightmost_mainnode != deleting:
                del_rightmost_mainnode.right = deleting.left
                deleting_rightmost.left = deleting.left
            deleting_rightmost.right = deleting.right

            if deleting == deletingNode.left:
                deletingNode.left = deleting_rightmost
            elif deleting == deletingNode.right:
                deletingNode.right = deleting_rightmost
            else:
                self.head = deleting_rightmost
        elif deleting.left or deleting.right:
            if deleting == deletingNode.left:
                deletingNode.left = deleting.right or deleting.left
            elif deleting == deletingNode.right:
                deletingNode.right = deleting.right or deleting.left
            else:
                self.head = deleting.right or deleting.left
        else:
            if deleting == deletingNode.left:
                deletingNode.left = None
            elif deleting == deletingNode.right:
                deletingNode.right = None
            else:
                self.head = None