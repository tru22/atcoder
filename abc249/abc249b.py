target = input()

def upper(string):
    for i in range(len(string)):
        if string[i].isupper():
            return True

    return False

def lower(string):
    for i in range(len(string)):
        if string[i].islower():
            return True

    return False

def diff(string):
    appeared = []
    for i in range(len(string)):
        if string[i] in appeared:
            return False
        else:
            appeared.append(string[i])

    return True


print("Yes" if upper(target) and lower(target) and diff(target) else "No")
