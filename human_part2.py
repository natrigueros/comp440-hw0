"""
Part 2: the best movie.

    uv run python human_part2.py

Write your rule on the `**My rule:**` line of WRITEUP.md. Print the top 10 movies (id, title,
ratings count, mean rating) under it.
"""

from load_data import load_all


def top10_my_rule(ratings, ratings_df, movies, movies_df):
    print("== 50+ rating ranking ==")

    joined_ra_mov = ratings_df.merge(movies_df, on='movie_id')

    movie_mean = joined_ra_mov.groupby('movie_id')['rating'].mean()
    counts_movies = joined_ra_mov.groupby('movie_id')['rating'].count()

    min_ratings = 50

    sort_mean = movie_mean.sort_values(ascending=False)

    shown = 0
    for movie_id, mean_rating in sort_mean.items():
        count = counts_movies[movie_id]
        if count >= min_ratings:
            title = movies_df[movies_df['movie_id'] == movie_id]['title'].iloc[0]
            print(movie_id, title, "count = ", count, "mean = ", mean_rating)
            shown += 1
        if shown == 10:
            break


def human_part2(ratings, ratings_df, movies, movies_df):
    top10_my_rule(ratings, ratings_df, movies, movies_df)


if __name__ == "__main__":
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()
    human_part2(ratings, ratings_df, movies, movies_df)
