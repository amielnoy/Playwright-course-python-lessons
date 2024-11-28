# For loop to iterate over a list
# list
test_cases = ["Login Test", "Signup Test", "Checkout Test"]
def test_loop_foreach():
    print("\n"+test_cases)
# tuple
fruits=("Apple","Orange","banana")
print(fruits)

def test_loop_foreach():
    for case in test_cases:
        print(f"Running {case}={case}")

def test_loop_dictionary():
    # Looping through a dictionary
    test_results = {"test_1": "PASS", "test_2": "FAIL", "test_3": "PASS"}

    for test, result in test_results.items():
        print(f"{test}: {result}")
#Exercise Questions:

# Create a dictionary named http_status_codes with some status codes and their meanings,
# and print each key-value pair using a loop.

# Write a script that iterates through a set of browser names and prints each one.

def test_loop_while():
    # While loop example
    count = 0
    while count < 3:
        print(f"Test iteration {count + 1}")
        # count=count+1
        count += 1


# Write a for loop that iterates over a list of URLs and prints each one.
# Write a while loop that keeps checking a condition until it becomes True (simulate a wait scenario).



# LOOP ON STRINGS:
# Loop on Characters in Strings
# Explanation: You can loop through each character in a string, which can be helpful when you need to validate or manipulate strings in test automation.

# Examples:

# Looping through characters in a string
test_name = "LoginTest"
def test_loop_while_chars():
    for char in test_name:
        print(char)

# Write a script that iterates through a string and counts the number of vowels.
# Given a string representing a test case ID, print each character one by one.