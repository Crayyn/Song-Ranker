# started by Crayyn on 18/07/24
import spotipy
import random

number_of_songs = 0
rank_up_to = 1
winning_song_order = []


def order_songs(number_of_songs, rank_up_to):
    list_of_songs = []
    has_song_been_shown = []
    passed_songs = []
    eliminated_songs = []
    current_rank = 1

    for i in range(number_of_songs):
        song_name = input("enter the name of song " + str(i + 1) + ": ")
        list_of_songs.append(song_name)
        has_song_been_shown.append(0)

    rank_songs(list_of_songs, passed_songs, eliminated_songs, rank_up_to, current_rank, has_song_been_shown)


def rank_songs(list_of_songs, passed_songs, eliminated_songs, rank_up_to, current_rank, has_song_been_shown):
    if len(passed_songs) != 0:
        list_of_songs = passed_songs
    number_of_songs = len(list_of_songs)
    number_of_matchups = number_of_songs * (number_of_songs - 1) // 2
    passed_songs = []
    previous_matchups = [""]

    for _ in range(number_of_matchups):
        song1 = ""
        song2 = ""

        while song1 == song2:
            song1 = random.choice(list_of_songs)
            song2 = random.choice(list_of_songs)
            if [song1, song2] in previous_matchups or [song2, song1] in previous_matchups:
                song1 = ""
                song2 = ""

        song1_position = list_of_songs.index(song1)
        song2_position = list_of_songs.index(song2)
        previous_matchups.append([song1, song2])

        while True:
            choice = int(input("which song do you prefer: \n\t1: " + song1 + "\n\t2: " + song2 + "\n1 or 2? "))
            if choice == 1:
                print(song1 + " wins the round!")
                passed_songs.append(song1)
                eliminated_songs.append(song2)
                has_song_been_shown[song1_position] += 1
                break
            elif choice == 2:
                print(song2 + " wins the round!")
                passed_songs.append(song2)
                eliminated_songs.append(song1)
                has_song_been_shown[song2_position] += 1
                break
            else:
                print("well you must have goofed up somehow so try again")

    print(list_of_songs)
    print(has_song_been_shown)


'''
    if len(passed_songs) == 1:
        print("Your No. " + str(current_rank) + " favourite song in this playlist is " + passed_songs[0] + "!")
        winning_song_order.append(passed_songs[0])
        passed_songs.pop(0)
        if current_rank == rank_up_to:
            print("You have now ranked your playlist!")
            print("Here are your top " + str(rank_up_to) + " songs!")
            for i in range(rank_up_to):
                print(i + 1, ": " + winning_song_order[i])
            exit()
        else:
            current_rank += 1
            print("NEXT ROUND")
            list_of_songs = eliminated_songs
            passed_songs = []
            rank_songs(list_of_songs, passed_songs, eliminated_songs, rank_up_to, current_rank, has_song_been_shown)

    rank_songs(list_of_songs, passed_songs, eliminated_songs, rank_up_to, current_rank, has_song_been_shown)
'''

while rank_up_to > number_of_songs:
    number_of_songs = int(input("please enter the number of songs you'd like to enter: "))
    rank_up_to = int(input("please enter the number of places you'd like to rank your songs to: "))
    if rank_up_to > number_of_songs:
        print("songs entered cannot exceed songs to be ranked")
order_songs(number_of_songs, rank_up_to)
