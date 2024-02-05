import argparse

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    # Create an ArgumentParser ovject
    parser = argparse.ArgumentParser(description='Run the Fizzbuz program')

    # Add an argument for the number of iterations
    parser.add_argument('iterations', type=int, help='The number of iterations to run fizzbuzz')

    args = parser.parse_args()

    # Run the Fizzbuzz function with the number of interations specified on the command line.
    fizzbuzz(args.iterations)

if __name__ == "__main__":
    main()  