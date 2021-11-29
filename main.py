balanced = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
unbalanced = ['}{}', '{{[(])]}}', '[[{())}]']
open_list = ['[', '{', '(']
close_list = [']', '}', ')']


class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.isEmpty():
            item = self[-1]
            self.__delitem__(-1)
            return item
        else:
            print('Стек пуст')

    def peek(self):
        if not self.isEmpty():
            item = self[-1]
            return item

    def size(self):
        return len(self)


def is_balanced_or_not(text):
    stack = Stack()
    for t in text:
        if t in open_list:
            stack.push(open_list.index(t))
        elif t in close_list:
            if stack.peek() == close_list.index(t):
                stack.pop()
            else:
                return 'Несбалансированно'
    if stack.size() == 0:
        return 'Balanced'
    else:
        return 'Unbalanced'


balanced_example = is_balanced_or_not('[([])((([[[]]])))]{()}')
unbalanced_example = is_balanced_or_not('{{[(])]}}')
print(balanced_example)
print(unbalanced_example)
