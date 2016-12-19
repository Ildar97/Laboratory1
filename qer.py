def MaxAndMinElement (a = []):
    if len(a) != 0:
        max = a[0]
        min = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        if a[i] < min:
            min = a[i]
    return max,min

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


def IsConsonantsLetters(word):
    ConsonantsLetters = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x",
                         "z", "б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч",
                         "ш", "щ"]
    for i in range(len(word)):
        for j in range(len(ConsonantsLetters)):
            if word[i].lower() == ConsonantsLetters[j]:
                return True
    return False
