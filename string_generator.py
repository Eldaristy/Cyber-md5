def get_possibilities(lst):
    possibilities = []
    for item in lst:
        if type(item) is tuple:
            for i in range(ord(item[0]), ord(item[1]) + 1):
                possibilities.append(chr(i))
        else:
            if not type(item) is chr:
                item = str(item)
                possibilities.append(item)
    return possibilities

def print_strs(lst, str, length):
    for char in lst:
        out = str + char
        if length - 1:
            print_strs(lst, out, length - 1)
        else:
                print(out)

def main():
    pos = get_possibilities([('a','z')])
    print_strs(pos, '', 6)

if __name__ == "__main__":
    main()
