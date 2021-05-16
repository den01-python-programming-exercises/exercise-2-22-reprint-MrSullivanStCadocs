def main():
    #write your code below this line

    user_number = 0
    counter = 0

    print("How many times?")
    user_number = int(input())

    while True:
      print_text()
      counter = counter + 1
      if (counter == user_number):
        break

def print_text():
    print("In a hole in the ground there lived a method")

  

if __name__ == '__main__':
    main()
