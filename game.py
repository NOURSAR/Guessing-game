def guessing_game():
    """A number-guessing game."""

    print("hi")
    name= input("Howdy! What's your name? ")
    name= name.capitalize()
    print(name + " I'm thinking of a number between 1 and 100.")
    number = int(input("Try to guess my number? "))
    count =0
    while True:
        count+=1
        if number < 57:
            count+=1
            print("Your guess is too low, try again.")
            number = int(input("Your guess? "))
            if number > 57:
               print("Your guess is too high, try again.")
               number = int(input("Your guess? "))
               if number == 57:
                  print("Congradulations, you guessed correct!")
                  print("Well done, "+name+"! You found my number in "+str(count)+" tries!")
                  break 
        else:
            print("Congradulations, you guessed correct!")
            print("Well done, "+name+"! You found my number in "+ str(count)+ " tries!") 
            break
guessing_game()
