# DECLARATION: teach Python a new named job.
def greet():                  # FUNCTION SIGNATURE
    message = "Hello"         # BODY + LOCAL VARIABLE
    print(message)            # BODY


print("Before")
greet()                       # CALL: run the named job.
# When greet() finishes, execution returns here to its caller.
print("After")
