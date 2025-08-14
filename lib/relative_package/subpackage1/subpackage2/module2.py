from .module1 import function1 as mod1_func
from .. import module3

def function1():
    print("Function 1 from module2")

# Example usage
if __name__ == "__main__":
    print("Running module2 directly:")
    function1()
    print("Calling module1's function:")
    mod1_func()
    print("Calling module3's function:")
    module3.function1()