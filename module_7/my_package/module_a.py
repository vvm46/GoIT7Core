import module_b


def foo():
    print("Function from module_a")

# module_b.bar()

if __name__ == "__main__":
    foo()
    # module_b.bar()