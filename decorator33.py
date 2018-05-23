registry = []
def register(func):
    print('running register(%s)' %func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()
    
'''
o/p -
running register(<function f1 at 0x01EC7070>)
running register(<function f2 at 0x01EC70B0>)
running main()
('registry ->', [<function f1 at 0x01EC7070>, <function f2 at 0x01EC70B0>])
running f1()
running f2()
running f3()
>>> import decorator33
running register(<function f1 at 0x01EC7230>)
running register(<function f2 at 0x01EC7170>)

This example shows decorators are run right after the decorated function are
defined, that is, at import time (as against to run time).

Notice that only function which is explicitly called is 'main()' function but it
runs only after decorator function which isn't even explicitly called.Also
notice that what happens when we import 'decorator33' in interactive
shell.

The main point of this example is to emphasize that function decorators are executed
as soon as the module is imported, but the decorated functions only run when they are
explicitly invoked. This highlights the difference between what Pythonistas call import
time and run time. Refer Fluent Python Chapter 7.

Considering how decorators are commonly employed in real code, Example 7-2 is unusual
in two ways:
The decorator function is defined in the same module as the decorated functions.
A real decorator is usually defined in one module and applied to functions in other
modules.
The register decorator returns the same function passed as argument. In practice,
most decorators define an inner function and return it.
'''
