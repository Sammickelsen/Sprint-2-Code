import pandas as pd
import os

# Create dataframe by reading the csv dataset
df = pd.read_csv("movie_data.csv", index_col=False)

def search_by_genre(title, limit):
    # Clear screen
    os.system('cls')
    
    # Create dataframe and filter it to the title given by the user.
    # Select only the text within the 'genres' column
    genre = df.loc[df['name'] == title]["genres"]

    # Cast the dataframe value into the string, while also chopping off the index.
    genre = genre.to_string(index=False)

    # Create a new dataframe, filtering it by the genre given and making sure it was made in the US.
    # Sort the values by their votecount and only pass back the values in the 'name' column.
    show_list = df.loc[(df['genres'] == genre) \
                        & (df['origin_country'] == 'US')]\
                        .sort_values('vote_count', ascending=False)['name']
    
    # Get the length of the show_list and show user
    count = len(show_list)
    print(f"There are {count} similar shows to {title}.")

    # Shorten the dataframe to the user's input + 1 since the user's show is included in the query
    # Cast the smaller dataframe into a list
    smaller_list = show_list[:limit + 1]
    read_list = smaller_list.to_list()
    print(f"\nHere are a list of {limit} titles you may like, based on the genres and rating of the show you selected:\n")
    
    # For each item in the list print them to the screen, unless it is the show the user typed out
    for item in read_list:
        if item != title:
            print(f"    {item}")
    
    # Give the user however much time they need to read the data before continuing
    print("\nPress any key to continue.")
    input()

def show_by_rating(rating):
    # Clear screen
    os.system('cls')

    # Filter the dataframe by the given vote_average and limit it to only shows in the US
    # Sort by highest vote_count and return the only the 'name' column
    show_list = df.loc[(df['vote_average'] == rating) \
                    & (df['origin_country'] == 'US')]\
                    .sort_values('vote_count', ascending= False)['name']
    
    # Get the length of the list and share with user
    count = len(show_list)
    print(f"There are {count} shows in the dataset with a rating of {rating}.")

    # Limit the list to 10 entries and print them to the user
    read_list = show_list[:10]
    print(f"\nHere are the most rated show with the rating of {rating}:\n")
    for item in read_list:
        print(f"    {item}")

    # Give the user as much time as they need before continuing
    print("\nPress any key to continue")
    input()

def show_by_name(title):
    # Clear screen
    os.system('cls')

    # Allow the dataframe to pull out larger sets of data for when we grab the overview text
    pd.set_option('display.max_colwidth', 1000000)
    
    # Filter the dataframe to only the show with the title given by the user and print out info
    show = df.loc[df['name'] == title]
    print(f'''
    Title: {title}

    Overview: {show['overview'].to_string(index=False)}

    Viewer Rating: {show['vote_count'].to_string(index=False)} users voted, giving this show a {\
        show['vote_average'].to_string(index=False)}/10

    Genres: {show['genres'].to_string(index=False)}

    Networks: {show['networks'].to_string(index=False)}
    
    ''')

    # Give the user as much time as they need before continuing
    print("\nPress any key to continue.")
    input()


# Set sentinal and Create While-Loop
loop = True

while loop == True:
    # Welcome User and collect user input
    print("""
    Welcome!  What would you like to search?

          1. Recommend Me Something
          2. Show Highest in Rating
          3. Search For Show By Name
          4. Quit
    """)
    response = input("> ")

    # Collect arguments and send them to the search_by_genre function
    if response == '1':
        os.system('cls')
        print("Please type a TV show you like below:")
        title = input("> ")
        print("How many suggestions would you like?")
        limit = int(input("> "))
        search_by_genre(title, limit)
    
    # Collect arguments and send them to the show_by_rating function
    elif response == '2':
        os.system('cls')
        print("What rating (0.0 - 10.0) would you like to view?")
        rating = round(float(input("> ")), 1)
        show_by_rating(rating)

    # Collect arguments and send them to the show_by_name function
    elif response == '3':
        os.system('cls')
        print('What show would you like to know more about?')
        title = input("> ")
        show_by_name(title)
    
    # Exit loop and close program
    elif response == '4':
        loop = False
    
    # Catch any outliers
    else:
        print('Not a valid answer')