'''
Python script to display a table of a range of Celsius (Fahrenheit) temperatures and
their Fahrenheit (Celsius) equivalents. The target scale is given by the user as the
letter 'C' or 'F'. The range is given by the user as two integers.  If the first value
is less or equal than the second, the temperatures appear in the table in increasing
order, and there are displayed in decreasing order otherwise. This is a sample log of
the execution of the program  (user input is in bold and underlined):

enter the target unit ('C' or 'F'): F
enter the start value: 50
enter the end value: 40

Celsius Fahrenheit
  50      122.00 
  49      120.20 
  48      118.40 
  47      116.60 
  46      114.80 
  45      113.00 
  44      111.20 
  43      109.40 
  42      107.60 
  41      105.80 
  40      104.00

This is another sample log of the execution of the program  (user input is in bold
and underlined):

enter the target unit ('C' or 'F'): C
enter the start value: 50
enter the end value: 60

Fahrenheit Celsius
    50      10.00
    51      10.56
    52      11.11
    53      11.67
    54      12.22
    55      12.78
    56      13.33
    57      13.89
    58      14.44
    59      15.00
    60      15.56

If the target input by the user is not correct, the program keep asking:

    enter the target unit ('C' or 'F'): X
    enter the target unit ('C' or 'F'): A
    enter the target unit ('C' or 'F'): C
    enter the start value: 100
    enter the end value: 105

    Fahrenheit Celsius
       100      37.78
       101      38.33
       102      38.89
       103      39.44
       104      40.00
       105      40.56
'''

def celsius_to_fahrenheit(c):
    return (9.0/5.0) * c + 32.0

def fahrenheit_to_celsius(f):
    return (5.0/9.0) * (f - 32.0)

def main():
    # Get valid target unit
    while True:
        target = input("enter the target unit ('C' or 'F'): ").strip().upper()
        if target in ('C', 'F'):
            break
    
    # Get range values
    start = int(input("enter the start value: "))
    end = int(input("enter the end value: "))
    
    # Determine direction
    step = 1 if start <= end else -1
    end = end + step
    
    # Print header
    source = "Celsius" if target == 'F' else "Fahrenheit"
    dest = "Fahrenheit" if target == 'F' else "Celsius"
    print(f"\n{source} {dest}")
    
    # Single loop for both conversion directions
    for temp in range(start, end, step):
        if target == 'F':
            converted = celsius_to_fahrenheit(temp)
        else:
            converted = fahrenheit_to_celsius(temp)
        print(f"  {temp}      {converted:.2f}")

if __name__ == "__main__":
    main()
