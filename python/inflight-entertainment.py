def is_there_a_movie_pair(flight_length, movie_lengths):
    movie_lengths_seen = set()

    for movie_length in movie_lengths:
        if flight_length - movie_length in movie_lengths:
            return True

        movie_lengths_seen.add(movie_length)

    return False
