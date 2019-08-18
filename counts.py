'''def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
    
'print(count_upper_case("Hello World"))

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%") == 0, "Special Characters"

print("All the tests passed") '''

def count_upper_case(message):
    """
    Count the number of upper case characters in a given message
    `message` is the piece of text to be checked
    
    Returns the number of uppercase characters in a message
    """
    return sum([1 for c in message if c.isupper()])


assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One uppercase"
assert count_upper_case("a") == 0, "One lowercase"
assert count_upper_case("AA") == 2, "Two uppercase"
assert count_upper_case("£$%^&") == 0, "Special Characters"
assert count_upper_case("Hello This message HAS Uppercase Letters!") == 7, "7 Uppercase"

print("All the tests passed")