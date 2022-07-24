# import module_a


def bar():
    print("Function from module_b")

    from my_package import module_a
    module_a.foo()


if __name__ == "__main__":
    bar()
