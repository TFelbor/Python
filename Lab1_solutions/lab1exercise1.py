def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer")

def celsius_to_fahrenheit(celsius):
    return 9 * celsius / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def to_celsius():
    target = 'X'
    while target not in ["C", "F"]:
        target = input("enter the target unit ('C' or 'F'): ").strip().upper()
    return target == "C"

def main():
    if to_celsius():
        from_unit, to_unit = "Fahrenheit", "Celsius"
        convert = fahrenheit_to_celsius
    else:
        from_unit, to_unit = "Celsius", "Fahrenheit"
        convert = celsius_to_fahrenheit
    x = read_int("enter the start value: ")
    y = read_int("enter the end value: ")
    if x <= y:
        step = 1
    else:
        step = -1
    print(from_unit, to_unit)
    for t in range(x, y + step, step):
        print(("{0:^" + str(len(from_unit)) + "d} {1:^" + str(len(to_unit)) + ".2f}").format(t, convert(t)))

if __name__ == "__main__":
    main()
