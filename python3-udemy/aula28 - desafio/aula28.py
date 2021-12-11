def exe1_func1(var1):
    return var1()

def exe1_func2():
    return 'qwerty'

# print(exe1_func1(exe1_func2))

def exe2_func1(var1):
    exe2_func2(1,2)
    exe2_func3(3,4,5)
    return var1()

def exe2_func2(*args):
    print(args[0],args[1])

def exe2_func3(*args):
    print(args[1],args[2], args[0])

print(exe2_func1(exe1_func2))
