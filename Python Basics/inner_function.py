def outer_func():
    print("outer function")
    def inner_func1():
        print("inner function 1")
    
    def inner_func2():
        print("inner function 2")

        def inner_func3():
            print("inner function 3")

        inner_func3()

    inner_func1()
    inner_func2()

outer_func()

# When outer functions are called then inner functions won't be executed
# If directly any inner function is called then that inner function won't be executed. It will return function is not defined.
# Note that the order in which the inner functions are defined does not matter. Like with any other functions, the printing only happens when the inner functions are executed.
# Furthermore, the inner functions are not defined until the parent function is called.