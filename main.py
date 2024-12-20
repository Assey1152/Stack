from stack import Stack


def check_braces(string):
    st = Stack()
    for el in string:
        if el in ('(', '[', '{'):
            st.push(el)
        elif (st.peek(), el) in (('(', ')'), ('[', ']'), ('{', '}')):
            st.pop()
        else:
            return 'Несбалансированно'
    return 'Сбалансированно' if st.is_empty() else 'Несбалансированно'


if __name__ == '__main__':
    good_braces_list = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
    bad_braces_list = ['}{}', '{{[(])]}}', '[[{())}]']
    for elem in good_braces_list:
        print(check_braces(elem))
    for elem in bad_braces_list:
        print(check_braces(elem))

