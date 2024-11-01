def decision_maker():
    print("Welcome to the Decision Maker!")
    print("Choose one of the following options:")
    print("1: Make a career choice")
    print("2: Decide on a meal")
    print("3: Plan a weekend activity")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        career_choice = input("Are you interested in tech, healthcare, or finance? ").lower()
        if career_choice == "tech":
            print("Consider roles in software engineering, data science, or cybersecurity!")
        elif career_choice == "healthcare":
            print("You might enjoy careers in nursing, medicine, or public health.")
        elif career_choice == "finance":
            print("Look into roles in accounting, investment banking, or financial analysis.")
        else:
            print("That's an interesting field! Research some roles in that area.")
    
    elif choice == "2":
        meal_choice = input("Do you feel like eating something light or heavy? ").lower()
        if meal_choice == "light":
            print("How about a salad or a sandwich?")
        elif meal_choice == "heavy":
            print("Maybe a pasta dish or a hearty stew would be good.")
        else:
            print("Try something new! Look up recipes online.")
    
    elif choice == "3":
        activity_choice = input("Do you prefer indoor or outdoor activities? ").lower()
        if activity_choice == "indoor":
            print("Consider going to a movie, visiting a museum, or trying a new recipe at home.")
        elif activity_choice == "outdoor":
            print("How about hiking, biking, or a picnic in the park?")
        else:
            print("Explore some unique ideas based on what interests you!")
    
    else:
        print("Invalid choice. Please choose a number between 1 and 3.")

# Run the decision maker function
decision_maker()
