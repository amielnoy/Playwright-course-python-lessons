msg="Hello"


def test_printf():
    print("\n")
    print("\n\n")
    print("Hello world!ֿ")
    print("\n\n")

    print("Well we")
    print("just use more lines")
    print("of code")
    print("\n\n")

    name = "Alice"
    age = 30

    # Basic usage
    print("My name is %s and I'm %d years old." % (name, age))

def test_f_string_formatting():
        name = "Alice"
        age = 30
        expected = "My name is Alice and I'm 30 years old."
        assert f"My name is {name} and I'm {age} years old." == expected

def test_f_string_with_expressions():
        x = 10
        y = 5
        assert f"The sum of {x} and {y} is {x + y}" == "The sum of 10 and 5 is 15"

def test_f_string_formatting_options():
        pi_new = 3.14159
        name='amiel'
        age=20
        print(f"Pi is approximately {pi_new:.2f}")
        assert f"Pi is approximately {pi_new:.2f}" == "Pi is approximately 3.14"

        # Specifying width
        print("Name: %10s" % name)  # Right-aligned with width 10
        print("Age: %-10d" % age)  # Left-aligned with width 10

        # Floating-point formatting
        pi = 3.14159
        print("Pi is approximately %.2f" % pi)  # Two decimal places

        # Hexadecimal formatting
        number = 255
        print("Hexadecimal: %x" % number)
        print("Hexadecimal with 0x: %#x" % number)

        print(f"Running {msg}={msg}")



        print("""Anything that starts
        with three quotes, and ends
        in three quotes can span
        many lines and even contain " symbols
        within it without freaking anything out!""")
        print("\n\n")