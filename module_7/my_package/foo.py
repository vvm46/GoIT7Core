def foo(name: str) -> str:
    return f"Hello {name}"


print(f"__name__ is {__name__}")


if __name__ == "__main__":
    print(foo("Elisabet"))
