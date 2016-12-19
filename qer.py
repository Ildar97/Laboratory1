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

def SplitTextByPunctuationMarks (word = ""):
    punctuations = [",",".","!","?",";"," "]
    b = ""
    a = []
    c = 0
    for i in range(len(word)):
        for j in range(len(punctuations)):
            if word[i] == punctuations[j]:
                c += 1
                if len(b) != 0:
                    a.append(b)
                    b = ""
                break
        if (c == 0):
            b += word[i]
        c = 0
    return a

def CreateDictionary(l: list) -> dict:
    d = dict()
    for x in l:
        d[x] = l.count(x)
    return d

a = [1,-786,123,7565,-345,-5456456,12334]
x, y = MaxAndMinElement(a)
print("max = {0}, min = {1}".format(x,y))

print(sep="\n")
n = 6
print("{0} член Фибоначчи = {1}".format(n,Fibonacci(n)))

print(sep="\n")
IsLetter = IsConsonantsLetters("Hello my friend!")
if IsLetter == True:
    print("Есть согласная буква")
else:
    print("Согласной буквы нет")

print(sep="\n")
a = SplitTextByPunctuationMarks("Hello, my aaaee friend! hot; dog aeoyu hot www friend my hello")
print("Слова с согласными буквами :")
for i in range(len(a)):
    if IsConsonantsLetters(a[i]) == True:
        print(a[i])

print(sep="\n")
d = CreateDictionary(a)
print(d.items())
