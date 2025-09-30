from pydantic import BaseModel


class Node(BaseModel):
    character: str
    children: dict[str, "Node"]
    # failure_link: "Node | None" = None
    is_end_of_word: bool = False


trie = Node(character="", children={})


def insert(node: Node, word: str):
    if len(word) == 0:
        node.is_end_of_word = True
        return

    first_char = word[0]
    rest_of_word = word[1 : len(word)]

    if first_char not in node.children:
        print(f"Character not in node: {first_char}")

        node.children[first_char] = Node(character=first_char, children={})

    insert(node.children[first_char], rest_of_word)


def print_node(node: Node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    print(prefix + connector + node.character)

    child_items = list(node.children.items())
    for i, (char, child) in enumerate(child_items):
        extension = f"    " if is_last else "│   "
        print_node(child, prefix + extension, i == len(child_items) - 1)


words = ("he", "she", "his", "hers", "stop", "history")

for word in words:
    insert(trie, word)

print_node(trie)
