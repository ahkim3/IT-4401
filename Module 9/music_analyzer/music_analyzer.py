# IT 4401: Midterm Project
#
# Name: Andrew Kim
# Pawprint: AHKYQX
# Description: Reads a playlist export from Apple Music or iTunes and provides an analysis to the user


class EmptyFileError(Exception):
    pass


class BadFileFormatError(Exception):
    pass


class Colors:
    # ANSI color codes
    CYAN = "\033[0;36m"
    LIGHT_GREEN = "\033[1;32m"
    LIGHT_BLUE = "\033[1;34m"
    BOLD = "\033[1m"
    NEGATIVE = "\033[7m"
    END = "\033[0m"


def check_validity(headers, songs):
    # Ensure that the headers are formatted as an Apple Music or iTunes playlist export
    if headers != [
        "Name", "Artist", "Composer", "Album", "Grouping", "Work", "Movement Number",
        "Movement Count", "Movement Name", "Genre", "Size", "Time", "Disc Number",
        "Disc Count", "Track Number", "Track Count", "Year", "Date Modified",
        "Date Added", "Bit Rate", "Sample Rate", "Volume Adjustment", "Kind",
        "Equalizer", "Comments", "Plays", "Last Played", "Skips", "Last Skipped",
        "My Rating", "Location"
    ]:
        raise ValueError()

    # Ensure that the playlist isn't empty
    if (len(songs) == 0):
        raise EmptyFileError()


def read_file(filename):
    songs = []

    with open(filename, 'r', encoding="utf-16") as file:
        # Read the first line and split to get list of headers
        headers = file.readline().rstrip('\n').split("\t")

        # Scan rest of file for songs
        while line := file.readline():
            line = line.rstrip('\n')
            song = line.split("\t")
            songs.append(song)
    return headers, songs


def find_longest_and_shortest_songs(songs):
    longest = []
    shortest = []

    # Create list of all song lengths
    song_lengths = []
    for song in songs:
        time = song[11]
        if time.isdigit():
            song_lengths.append(int(time))

    # Determine shortest and longest song lengths
    shortest_song_length = min(song_lengths)
    longest_song_length = max(song_lengths)

    for song in songs:
        # Ensure that the song length exists and is a number
        if not song[11].isdigit():
            continue

        time = int(song[11])

        if int(time) == longest_song_length:
            songInfo = {}

            if not song[0] or song[0] == "":  # If song name is empty
                songInfo["name"] = "Unknown Artist"
            else:
                songInfo["name"] = song[0]

            if not song[1] or song[1] == "":  # If artist name is empty
                songInfo["artist"] = "Unknown Artist"
            else:
                songInfo["artist"] = song[1]

            songInfo["length"] = int(time)
            longest.append(songInfo)

        if int(song[11]) == shortest_song_length:
            songInfo = {}
            songInfo["name"] = song[0]
            songInfo["artist"] = song[1]
            songInfo["length"] = int(song[11])
            shortest.append(songInfo)

    return longest, shortest


def analyze(songs):
    results = {}

    # Determine total number of songs in the playlist
    results["total_songs"] = len(songs)

    # Determine the number of songs that were released each year
    results["songs_per_year"] = {}
    for song in songs:
        year = song[16]
        if year.isdigit():
            if year in results["songs_per_year"]:
                results["songs_per_year"][year] += 1
            else:
                results["songs_per_year"][year] = 1

    # Determine the song(s) by Name and Artist with the longest and shortest length
    results["longest_songs"], results["shortest_songs"] = find_longest_and_shortest_songs(
        songs)

    # Determine for each genre the number of songs and the longest/shortest song(s)
    genres = {}

    for song in songs:  # Sort each song by genre
        genre = song[9]

        if not genre or genre == "":  # If genre is empty
            continue
        if genre in genres:
            genres[genre].append(song)
        else:
            genres[genre] = [song]

    results["genre_analysis"] = {}

    for genre in genres:  # Determine results for each genre
        results["genre_analysis"][genre] = {}

        results["genre_analysis"][genre]["longest_in_genre"], results["genre_analysis"][
            genre]["shortest_in_genre"] = find_longest_and_shortest_songs(genres[genre])
        results["genre_analysis"][genre]["total_in_genre"] = len(
            genres[genre])  # Number of songs in genre

    # Determine number of songs that have been played/not been played
    results["played_songs"] = 0
    results["unplayed_songs"] = 0
    for song in songs:
        if not song[25] or song[25] == "0":
            results["unplayed_songs"] += 1
        else:
            results["played_songs"] += 1

    return results


def display_results(filename, results):
    print("\n\n------------------------------------------------------")
    print(Colors.NEGATIVE, "Analysis of ", filename + ":", Colors.END, sep="")
    print("------------------------------------------------------\n")

    print(Colors.LIGHT_BLUE, "Total number of songs: ",
          Colors.END, results["total_songs"], "\n", sep="")

    print(Colors.LIGHT_BLUE,
          "Number of songs released each year in the playlist:", Colors.END, sep="")
    for year in results["songs_per_year"]:
        print('  ', Colors.CYAN, year + ": ", Colors.END,
              results["songs_per_year"][year], sep="")

    print(Colors.LIGHT_BLUE, "\nLongest song(s):", Colors.END, sep="")
    for song in results["longest_songs"]:
        print(' ', song["name"], "by", song["artist"],
              "(" + str(song["length"]) + " seconds)")

    print(Colors.LIGHT_BLUE, "\nShortest song(s):", Colors.END, sep="")
    for song in results["shortest_songs"]:
        print(' ', song["name"], "by", song["artist"],
              "(" + str(song["length"]) + " seconds)")

    print(Colors.LIGHT_BLUE, "\n\nGenre Analysis:", sep="")
    print("------------------------------------------------------")
    for genre in results["genre_analysis"]:
        print(Colors.CYAN, "\nGenre: ", Colors.LIGHT_GREEN,
              genre, Colors.END, sep="")
        print(Colors.BOLD, "  Total number of songs in this genre: ", Colors.END,
              results["genre_analysis"][genre]["total_in_genre"], sep="")

        # Check if artist is unknown
        if results["genre_analysis"][genre]["longest_in_genre"][0]["artist"] == "Unknown Artist" or results["genre_analysis"][genre]["longest_in_genre"][0]["artist"] == "":
            print(Colors.BOLD, "  Longest song(s) in this genre:",
                  Colors.END, sep="")
            for song in results["genre_analysis"][genre]["longest_in_genre"]:
                print('    ', song["name"], " by Unknown Artist",
                      " (" + str(song["length"]) + " seconds)", sep="")
        else:
            print(Colors.BOLD,
                  "  Longest song(s) in this genre:", Colors.END, sep="")
            for song in results["genre_analysis"][genre]["longest_in_genre"]:
                print('    ', song["name"], " by ", song["artist"],
                      " (" + str(song["length"]) + " seconds)", sep="")

        # Check if artist is unknown
        if results["genre_analysis"][genre]["shortest_in_genre"][0]["artist"] == "Unknown Artist" or results["genre_analysis"][genre]["shortest_in_genre"][0]["artist"] == "":
            print(Colors.BOLD, "  Shortest song(s) in this genre:",
                  Colors.END, sep="")
            for song in results["genre_analysis"][genre]["shortest_in_genre"]:
                print('    ', song["name"], " by Unknown Artist",
                      " (" + str(song["length"]) + " seconds)", sep="")
        else:
            print(Colors.BOLD,
                  "  Shortest song(s) in this genre:", Colors.END, sep="")
            for song in results["genre_analysis"][genre]["shortest_in_genre"]:
                print('    ', song["name"], " by ", song["artist"],
                      " (" + str(song["length"]) + " seconds)", sep="")

    print("------------------------------------------------------\n")

    print(Colors.LIGHT_BLUE, "Total number of played songs: ",
          Colors.END, results["played_songs"], sep="")
    print(Colors.LIGHT_BLUE, "Total number of unplayed songs: ", Colors.END,
          results["unplayed_songs"], sep="")


def main():
    repeat = 'y'

    # Loop until the user wants to quit
    while repeat == 'y':
        print()
        filename = input("Enter the name of the playlist data file to read: ")

        try:
            with open(filename, "r") as file:
                try:
                    # Parse data and ensure integrity
                    headers, songs = read_file(filename)
                    check_validity(headers, songs)

                    # Analyze data and display results
                    results = analyze(songs)
                    display_results(filename, results)

                except (BadFileFormatError):
                    print("Error: The file", filename,
                          "is not a valid Apple Music or iTunes playlist export.")
                except (EmptyFileError):
                    print("Error: No data could be found in file " + filename + ".")
                except (OSError, IOError):
                    print("Error reading from file " + filename + ".")
        except (FileNotFoundError, PermissionError, OSError):
            print("Error opening file " + filename + ".")
        except Exception as e:
            print("An error occurred:", e)

        # Ask the user if they want to repeat the program
        print()
        repeat = input("Would you like to evaluate another file? (y/n) ")


main()
