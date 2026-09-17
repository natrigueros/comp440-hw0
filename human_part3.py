"""
Part 3: the most ___ movie.

    uv run python human_part3.py

Pick an adjective. Write it on the `**My adjective:**` line of WRITEUP.md and a one-sentence
definition a classmate could code on the `**My definition:**` line. Print the top 5 movies
under it.
"""

from load_data import load_all


def top5_my_definition(ratings, ratings_df, movies, movies_df):
    print("== My definition ==")

    joined_ra_mov = ratings_df.merge(movies_df, on='movie_id')

    movie_sd = joined_ra_mov.groupby('movie_id')['rating'].std()
    counts_movies = joined_ra_mov.groupby('movie_id')['rating'].count()

    min_ratings = 50

    sort_sd = movie_sd.sort_values(ascending=False)

    shown = 0
    for movie_id, rating_sd in sort_sd.items():
        count = counts_movies[movie_id]
        if count >= min_ratings:
            title = movies_df[movies_df['movie_id'] == movie_id]['title'].iloc[0]
            print(movie_id, title, "count = ", count, " mean = ", rating_sd)
            shown += 1
        if shown == 5:
            break

def human_part3(ratings, ratings_df, movies, movies_df):
    top5_my_definition(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part3(ratings, ratings_df, movies, movies_df)
