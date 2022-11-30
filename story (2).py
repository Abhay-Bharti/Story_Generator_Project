import random


def story():
    readername = input("Enter your name here:")
    print('Hello ' + readername)
    names = ["Kapil", "Mohit", "Abhishek", "Sumit", "Vikas", "Sachin", "Prince"]
    places = ["Delhi", "Jaipur", "Bhiwani", "Hisar", "Sikar", "Udaipur", "Mumbai", "Chennai", "Jhunjhunu", "Pilani",
              "Gurugaon", "Jalandhar", "Chandigarh"]
    quests = ["arrive to a grand building and take a photograph", "go to meet a celebraty", "drie in a large jeep",
              "Eat pizza at the Taj Hostel", "travel on the Delhi Eye in the middle of the night",
              "Buy 20 expensive things in the most extravagant shop they see along the street",
              "Go to the most beautiful area they search up in Canada"]
    roles = ["normal boy", "men", "old man", "teenager boy", "child", "secondary student",
             "worker at harrods", "university student", "intelligent boy"]
    weather = ["a sunny day", "a very humid and hot day", "a cold night", "a cloudy day", "a rainy day"]
    story = " Once upon a time a " + random.choice(roles) + " named " + random.choice(
    names) + " lived in a beautiful area called " + random.choice(places) + " where it was " + random.choice(
    weather) + " and in this place " + random.choice(names) + " will have to " + random.choice(
    quests) + " they return to their home at " + random.choice(places)

    print(story)
    return story

print("*" * 116, "\n" + "*" * 40, "Welcome to World of Filmic Stories", "*" * 40, "\n" + "*" * 37,
      "I am Jimmy, your favourite story teller", "*" * 38, "\n" + "*" * 116, "\n")


def Menu():
    print(''' Press              1 for a Mysterious story
                    2 for say goodbye to your "Jimmy" ''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        story()
        print("\n")
        Menu()
    elif choice == 2:
        exit()
    else:
        print("Enter Correct choice")
        Menu()


Menu()
