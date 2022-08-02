name = input("What is your name? ")
age = int(input("How old are you? "))
location = input("Where are you from? ")
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

choice = input("Do you like programming?y/n ").lower()
if choice in yes:
    print("You like programming")
elif choice in no:
       print("You don't like programming")
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")

language = input("Do you speak English?y/n ").lower()
if language in yes:
    print("You speak English")
elif language in no:
       print("You don't speak English")
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")


print((f"Your name is {name}. \nYou are {age} years old. \nYou are located in {location}."))
