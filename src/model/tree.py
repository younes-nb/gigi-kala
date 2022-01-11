import math

r = 'right'
l = 'left'
p = 'parent'


class Pos:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"


class Tree:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f" {self.data}:<{self.left},{self.right}> "

    def draw(self):
        print(self)

    def append(self, node: Pos, position):
        node = Tree(node)
        if position == r:
            self.right = node
        else:
            self.left = node
        node.parent = self

    def clear(self):
        if self.has(p):
            if self.parent.right == self:
                self.parent.right = None
            else:
                self.parent.left = None
        else:
            self = self.__init__()

    def has(self, position):
        if position == r:
            try:
                right = self.right.data
            except:
                return False
            return True
        elif position == l:
            try:
                left = self.left.data
            except:
                return False
            return True
        else:
            try:
                parent = self.parent.data
            except:
                return False
            return True

    def insert(self, node):
        insert(self, node)

    def clean(self, node):
        clean(self, node)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def distance(p1: Pos, p2: Pos):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def insert(tree: Tree, node: Pos):
    x = node.x
    y = node.y
    z = node.z

    if x < tree.data.x:
        if not tree.has(l):
            tree.append(node, l)
            return
        if y < tree.left.data.y:
            if not tree.left.has(l):
                tree.left.append(node, l)
                return
            if z < tree.left.left.data.z:
                if not tree.left.left.has(l):
                    tree.left.left.append(node, l)
                    return
                insert(tree.left.left.left, node)
            else:
                if not tree.left.left.has(r):
                    tree.left.left.append(node, r)
                    return
                insert(tree.left.left.right, node)
        else:
            if not tree.left.has(r):
                tree.left.append(node, r)
                return
            if z < tree.left.right.data.z:
                if not tree.left.right.has(l):
                    tree.left.right.append(node, l)
                    return
                insert(tree.left.right.left, node)
            else:
                if not tree.left.right.has(r):
                    tree.left.right.append(node, r)
                    return
                insert(tree.left.right.right, node)
    else:
        if not tree.has(r):
            tree.append(node, r)
            return
        if y < tree.right.data.y:
            if not tree.right.has(l):
                tree.right.append(node, l)
                return
            if z < tree.right.left.data.z:
                if not tree.right.left.has(l):
                    tree.right.left.append(node, l)
                    return
                insert(tree.right.left.left, node)
            else:
                if not tree.right.left.has(r):
                    tree.right.left.append(node, r)
                    return
                insert(tree.right.left.right, node)
        else:
            if not tree.right.has(r):
                tree.right.append(node, r)
                return
            if z < tree.right.right.data.z:
                if not tree.right.right.has(l):
                    tree.right.right.append(node, l)
                    return
                insert(tree.right.right.left, node)
            else:
                if not tree.right.right.has(r):
                    tree.right.right.append(node, r)
                    return
                insert(tree.right.right.right, node)


def clean(tree: Tree, node: Pos, ori: Pos = None, base='pos_x'):
    if ori is None:
        ori = node
    if base == 'pos_x':
        x = tree.data.x
        base = 'y'
    elif base == 'y':
        x = tree.data.y
        base = 'z'
    else:
        x = tree.data.z
        base = 'pos_x'
    distances[tree.data] = distance(tree.data, ori)
    if node.x < x:
        if tree.has(l):
            clean(tree.left, Pos(node.y, node.z, node.x), ori, base)

        if tree.has(r):
            savageClean(tree.right, Pos(node.y, node.z, node.x), ori, base)
    else:
        if tree.has(r):
            clean(tree.right, Pos(node.y, node.z, node.x), ori, base)

        if tree.has(l):
            savageClean(tree.left, Pos(node.y, node.z, node.x), ori, base)


def savageClean(tree: Tree, node: Pos, ori: Pos = None, base='pos_x'):
    if base == 'pos_x':
        x = tree.data.x
        base = 'y'
    elif base == 'y':
        x = tree.data.y
        base = 'z'
    else:
        x = tree.data.z
        base = 'pos_x'
    distances[tree.data] = distance(tree.data, ori)
    if node.x < x:
        if tree.has(l):
            savageClean(tree.left, Pos(node.y, node.z, node.x), ori, base)

        if tree.has(r):
            killerClean(tree.right, Pos(node.y, node.z, node.x), ori, base)
    else:
        if tree.has(r):
            savageClean(tree.right, Pos(node.y, node.z, node.x), ori, base)

        if tree.has(l):
            killerClean(tree.left, Pos(node.y, node.z, node.x), ori, base)


def killerClean(tree: Tree, node: Pos, ori: Pos = None, base='pos_x'):
    if base == 'pos_x':
        x = tree.data.x
        base = 'y'
    elif base == 'y':
        x = tree.data.y
        base = 'z'
    else:
        x = tree.data.z
        base = 'pos_x'
    distances[tree.data] = distance(tree.data, ori)
    if node.x < x:
        if tree.has(l):
            killerClean(tree.left, Pos(node.y, node.z, node.x), ori, base)
    else:
        if tree.has(r):
            killerClean(tree.right, Pos(node.y, node.z, node.x), ori, base)


def nearest(tree: Tree, node: Pos):
    global distances
    distances = {}
    tree.clean(node)
    point = min(distances, key=distances.get)
    distance = distances[min(distances, key=distances.get)]
    return ((point.x, point.y, point.z), distance)
