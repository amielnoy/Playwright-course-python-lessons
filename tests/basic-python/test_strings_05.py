test_case = "Login Test"
def test_strings():
    print(test_case.upper())  # Converts to uppercase
    print(test_case.lower())  # Converts to lowercase
    print("Test" in test_case)  # Check if substring is present

    print(test_case[4:])
    print(test_case[0:5])
    print(test_case[-4:])


# String formatting
user = "Alice"
print(f"Running tests for user: {user}")
#Exercise Questions:

#Write a script that takes a string input representing a URL and checks if it starts with "https".
#Given a string with a test case title, print the title in uppercase.


def test_loops():
        # simple loop
        for i in range(0,4):
            print('iteration==' +str(i))
        print("\n\n")

        # step step=2
        for i in range(0,2,8):
            print('iteration==' +str(i))



# Explanation: Strings are used to store textual data,
# which is often part of test data, test names, or expected outputs.

# Basic string operations
