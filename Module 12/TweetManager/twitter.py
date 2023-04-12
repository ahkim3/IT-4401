# Twitter (Tweet Manager)
# Andrew Kim (AHKYQX)

from Tweet import Tweet
import pickle
import os


def search_tweets(tweets: list):
    # Verify that there are tweets to search
    if len(tweets) == 0:
        print("There are no tweets to search")
        print()
        return
    else:
        # Prompt user for search term
        search_term = input("What would you like to search for? ")

        # Search tweets (case-insensitive)
        results = []
        for tweet in tweets:
            if search_term.lower() in tweet.get_text().lower():
                results.append(tweet)

        # Display results
        print()
        print("Search Results")
        print("-——————")

        if len(results) == 0:
            print("No tweets contained", search_term)
            print()
        else:
            results.reverse()  # Display most recent tweets first

            for tweet in results:
                print(tweet.get_author() + " - " + tweet.get_age())
                print(tweet.get_text())
                print()


def view_recent_tweets(tweets: list):
    print("Recent Tweets")
    print("-——————")

    # Verify that there are tweets to display
    if len(tweets) == 0:
        print("There are no recent tweets.")
        print()
    else:
        # Display five most recently created tweets
        for i in range(len(tweets) - 1, max(len(tweets) - 6, -1), -1):
            print(tweets[i].get_author() + " - " + tweets[i].get_age())
            print(tweets[i].get_text())
            print()


def make_tweet(tweets: list):
    name = input("What is your name? ")
    text = input("What would you like to tweet? ")

    # Verify that tweet is no longer than 140 characters
    if len(text) > 140:
        print("Tweets can only be 140 characters!")
        print()
    else:
        # Create tweet and update file
        tweets.append(Tweet(name, text))
        serialize(tweets)
        print(name, ", your tweet has been saved.", sep="")
        print()


def serialize(tweets: list):
    with open("tweets.dat", "wb") as f:
        pickle.dump(tweets, f)


def deserialize():
    if os.path.isfile("tweets.dat"):
        # Open file and load tweets
        with open("tweets.dat", "rb") as f:
            tweets = pickle.load(f)
    else:
        tweets = []
    return tweets


def display_menu():
    print("Tweet Menu")
    print("-—————")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")
    print()


def main():
    tweets = deserialize()

    display_menu()

    while (True):
        try:
            option = input("What would you like to do? ")

            if not option.lstrip("-").isdigit():  # Verify input is numeric
                print("Please enter a numeric value.")
                print()
                continue
            elif option == "1":
                make_tweet(tweets)
            elif option == "2":
                print()
                view_recent_tweets(tweets)
            elif option == "3":
                search_tweets(tweets)
            elif option == "4":  # Quit
                print("Thank you for using the Tweet Manager!")
                break
            else:  # Invalid option
                print("Please select a valid option")
                print()
                continue

        except ValueError:
            print("Please enter a valid numeric value.")
            print()
            continue
        except Exception as e:
            print(e)
            print("Please try again.")
            print()
            continue

        display_menu()


main()
