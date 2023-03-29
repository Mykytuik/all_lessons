
def calculate(string):
    wa={}
    for i in string:
        if i in wa:
            continue
        else:
            wa.update({str(i):string.count(i)})
    return wa
print(calculate("Stringg"))
    