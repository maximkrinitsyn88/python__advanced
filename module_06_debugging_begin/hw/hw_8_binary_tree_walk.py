"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
import re
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


def restore_tree(path_to_log_file: str):
    tree = {}
    with open(path_to_log_file, 'r') as tree_log:
        first_line = tree_log.readlines(1)
        binary_number = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(first_line))]
        main_root = BinaryTreeNode(binary_number[0])
        tree.update({main_root.val: main_root})
        for line in tree_log:
            binary_number = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
            if 'left' in line:
                root_l = BinaryTreeNode(binary_number[1])
                main_root.left = root_l
                tree.update({root_l.val: root_l})
            if 'right' in line:
                root_r = BinaryTreeNode(binary_number[1])
                main_root.right = root_r
                tree.update({root_r.val: root_r})
            if 'INFO' in line:
                main_root = BinaryTreeNode(binary_number[0])
                tree.update({main_root.val: main_root})
    return tree


print(restore_tree('hw_8_walk_log_1.txt'))
print(restore_tree('hw_8_walk_log_1.txt')[1].left)
print(restore_tree('hw_8_walk_log_1.txt')[1].right)
print(restore_tree('hw_8_walk_log_1.txt')[2].left)
print(restore_tree('hw_8_walk_log_1.txt')[2].right)

counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)

    node_right = get_tree(max_depth - 1, level=level + 1)

    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="hw_8_walk_log_5.txt",
    )

    root = get_tree(7)

    walk(root)
