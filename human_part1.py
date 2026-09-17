"""
Part 1: basic rating statistics.

    uv run python human_part1.py

Answer the four questions below with your own code, print each answer under its label, and
explain each in one sentence in WRITEUP.md.
"""

from load_data import load_all


def human_part1(ratings, ratings_df, movies, movies_df, users, users_df):

    print("== (a) ==")
    # (a) How many ratings, users, and movies are there, and how are ratings distributed across 1-5 stars?
    number_ratings = len(ratings_df)
    number_users = len(users_df)
    number_movies = len(movies_df)
    print("There are", number_ratings, "of ratings.")
    print("There are", number_users, "of users.")
    print("There are", number_movies, "of movies.")

    print("The distribution looks like:")
    print(ratings_df['rating'].value_counts().sort_index())


    print("== (b) ==")
    # (b) What is the median number of ratings per user, and how many users have 100 or more ratings?
    user_count = ratings_df['user_id'].value_counts()
    median_user = user_count.median()
    print("The median rateings per user is:",median_user)

    m100_users = (user_count >= 100).sum()
    print("The users with 100+ ratings are this many:", m100_users)

    print("== (c) ==")
    # (c) Join ratings to titles. Which 10 movies have the most ratings?

    joined_ra_mov = ratings_df.merge(movies_df, on = 'movie_id')

    most_ratings = joined_ra_mov['title'].value_counts()
    print("The 10 movies with the most ratings are:")
    print(most_ratings.head(10))

    print("== (d) ==")
    # (d) Among movies with at least 20 ratings, which 10 have the highest mean rating?
    #     Show title, mean, and count.

    movie_mean = joined_ra_mov.groupby('title')['rating'].mean()
    counts_movies = joined_ra_mov.groupby('title')['rating'].count()

    sort_mean = movie_mean.sort_values(ascending=False)

    print("The top 10 highest-rated movies that have at least 20 reatings are:")
    shown = 0
    for title, mean_rating in sort_mean.items():
        count = counts_movies[title]
        if count >= 20:
            print(title, "mean = ", mean_rating, "count = ", count)
            shown += 1
        if shown == 10:
            break

if __name__ == "__main__":
    import pandas as pd
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part1(ratings, ratings_df, movies, movies_df, users, users_df)
