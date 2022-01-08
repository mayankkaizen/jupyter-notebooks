
print("This will print in both script mode and module mode")

a = 'in module'
b = 'in script'

def FuncA(x):
    print(x)

if __name__ == "__main__":
    FuncA(b)
    print("running as script")
    print("__name__ is set to: %s" %__name__)
else:
    FuncA(a)
    print("running as module")
    print("__name__ is set to: %s" %__name__)

    
