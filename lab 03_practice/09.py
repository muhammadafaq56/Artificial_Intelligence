def fibonacci_series(limit):
    a = 1  # First number in Fibonacci series
    b = 1  # Second number in Fibonacci series
    
    # Continue printing numbers while 'a' is less than or equal to the limit
    while a <= limit:
        print(a, end=" ")  # Print the current Fibonacci number
        temp = a  # Store the current value of 'a'
        a = b  # Set 'a' to 'b' (next Fibonacci number)
        b = temp + b  # Calculate the next Fibonacci number by adding 'a' and 'b'

fibonacci_series(50)  # Call the function with limit 50
