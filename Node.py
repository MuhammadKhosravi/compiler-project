class Node:
    leaves = list()
    symbols = ['(', ')', '/', '*', '-', '+', '==', '<', '[', ']', ';', ':', '{', '}', '=', ',']
    file_content = ""

    def __init__(self, name, is_leaf):
        self.name = name
        self.parent = None
        self.string = name
        self.children = list()
        if is_leaf:
            Node.leaves.append(self)
            if '#' in name:
                joint = name.split('#')
                self.string = '(' + joint[0] + ', ' + joint[1] + ')'
                if joint[0] == joint[1]:
                    if joint[0] in Node.symbols:
                        self.string = '(SYMBOL, ' + joint[0] + ')'
                    else:
                        self.string = '(KEYWORD, ' + joint[0] + ')'

    def add_parent(self, parent):
        self.parent = parent

    def add_children(self, children):
        self.children.extend(children)

    def __str__(self):
        return self.string

    def traverse():
        parse_tree = ""
        max_depth = 0
        for node in Node.leaves:
            depth = 0
            node_temp = node
            while type(node_temp) == Node:
                if type(node_temp.parent) == Node:
                    root = node_temp
                node_temp = node_temp.parent
                depth += 1
            if depth > max_depth:
                max_depth = depth
        root_main = Node('program', False)
        root_main.add_children([root])
        root.add_parent(root_main)
        Node.find(root_main, 0, False, list())
        Node.file_content += '└── $'
        Node.write_to_file()

    def find(root, depth, is_only_child, index):
        index_now = 0
        string_now = list()
        if depth == 0:
            string_now.extend(list(root.string))
        elif depth == 1:
            string_now.extend(list('├── ' + root.string))
        else:
            string_now.extend(list('│' + ' ' * (depth * 4 - 5)))
            if is_only_child:
                index = [i for i in index if i < len(string_now)]
                string_now.extend(list('└── ' + root.string))
            else:
                index_now = len(string_now)
                string_now.extend(list('├── ' + root.string))
        for i in index:
            if i < len(string_now):
                if string_now[i] == ' ' and string_now[i - 1] != ',':
                    string_now[i] = '│'
        Node.file_content += ''.join(string_now) + '\n'
        children = list(root.children.__reversed__())
        if len(children) == 0:
            return
        else:
            if index_now != 0:
                index.append(index_now)
            for child, i in zip(children, range(len(children))):
                if i != len(children) - 1:
                    Node.find(child, depth + 1, False, index)
                else:
                    Node.find(child, depth + 1, True, index)

    def write_to_file(content=None):
        if content is None:
            content = Node.file_content
        with open('parse_tree.txt', 'w', encoding='utf-8') as file:
            file.write(Node.file_content)

