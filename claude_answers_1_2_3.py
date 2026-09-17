"""
Claude's answers to the three questions in questions.md.

    uv run python claude_answers_1_2_3.py

Filled in by a Claude that has never seen the student's work. Kept as it was written.
"""

from load_data import load_all


def claude_answers():
    ratings, ratings_df, movies, movies_df, users, users_df = load_all()

    # ---------------------------------------------------------------
    # 1(a) Basic counts and the distribution of star ratings.
    # ---------------------------------------------------------------
    print("=" * 70)
    print("1(a) Basic rating statistics")
    print("=" * 70)
    n_ratings = len(ratings_df)
    n_users = ratings_df["user_id"].nunique()
    n_movies = ratings_df["movie_id"].nunique()
    print(f"Ratings: {n_ratings:,}")
    print(f"Users:   {n_users:,}")
    print(f"Movies:  {n_movies:,}")
    print()
    print("Distribution of ratings (1-5 stars):")
    dist = ratings_df["rating"].value_counts().sort_index()
    for stars, count in dist.items():
        pct = 100 * count / n_ratings
        print(f"  {stars} star(s): {count:6,}  ({pct:5.1f}%)")

    # ---------------------------------------------------------------
    # 1(b) Median ratings per user, and how many users hit >= 100.
    # ---------------------------------------------------------------
    print()
    print("=" * 70)
    print("1(b) Ratings per user")
    print("=" * 70)
    ratings_per_user = ratings_df.groupby("user_id").size()
    median_per_user = ratings_per_user.median()
    n_heavy_users = (ratings_per_user >= 100).sum()
    print(f"Median ratings per user: {median_per_user:.1f}")
    print(f"Users with >= 100 ratings: {n_heavy_users:,} out of {n_users:,}")

    # ---------------------------------------------------------------
    # 1(c) Join ratings to titles; the 10 most-rated movies.
    # ---------------------------------------------------------------
    print()
    print("=" * 70)
    print("1(c) 10 most-rated movies")
    print("=" * 70)
    joined = ratings_df.merge(movies_df[["movie_id", "title"]], on="movie_id")
    counts_by_title = joined.groupby("title").size().sort_values(ascending=False)
    most_rated = counts_by_title.head(10)
    for title, count in most_rated.items():
        print(f"  {count:4,}  {title}")

    # ---------------------------------------------------------------
    # 1(d) Among movies with >= 20 ratings, the 10 with the highest
    #      mean rating.
    # ---------------------------------------------------------------
    print()
    print("=" * 70)
    print("1(d) Highest mean rating (>= 20 ratings)")
    print("=" * 70)
    stats_by_title = joined.groupby("title")["rating"].agg(mean="mean", count="count")
    qualified = stats_by_title[stats_by_title["count"] >= 20]
    top_mean = qualified.sort_values("mean", ascending=False).head(10)
    for title, row in top_mean.iterrows():
        print(f"  {row['mean']:.3f}  (n={int(row['count']):4,})  {title}")

    # ---------------------------------------------------------------
    # 2. Best movie in the dataset.
    #
    # A raw average is misleading for movies with only a handful of
    # ratings (a single 5-star rating gives a "perfect" 5.0 mean with
    # n=1). So "best" here means: highest mean rating among movies
    # with a reasonably large number of ratings, so the mean is a
    # trustworthy estimate. I check a couple of thresholds to see
    # whether the answer is robust to the exact cutoff.
    # ---------------------------------------------------------------
    print()
    print("=" * 70)
    print("2. Best movie in the dataset")
    print("=" * 70)
    for min_count in (20, 50, 100):
        qualified = stats_by_title[stats_by_title["count"] >= min_count]
        best_title = qualified["mean"].idxmax()
        best_row = qualified.loc[best_title]
        print(f"  Best with >= {min_count:3} ratings: {best_title} "
              f"(mean={best_row['mean']:.3f}, n={int(best_row['count'])})")

    # ---------------------------------------------------------------
    # 3. Most polarizing movie.
    #
    # "Polarizing" means opinions are split, not just spread out: a
    # movie that gets mostly 1s and 5s (love-it-or-hate-it) is
    # polarizing, while one that gets mostly 3s is just mediocre. I
    # measure this with the standard deviation of its ratings, again
    # restricted to movies with a reasonable number of ratings so a
    # couple of oddball scores can't dominate. I also print each
    # movie's mean alongside its std so it's easy to tell "polarizing"
    # apart from merely "widely disliked or loved."
    # ---------------------------------------------------------------
    print()
    print("=" * 70)
    print("3. Most polarizing movie")
    print("=" * 70)
    stats_std = joined.groupby("title")["rating"].agg(mean="mean", std="std", count="count")
    for min_count in (20, 50, 100):
        qualified = stats_std[stats_std["count"] >= min_count]
        top_polarizing = qualified.sort_values("std", ascending=False).head(5)
        print(f"  Most polarizing with >= {min_count} ratings:")
        for title, row in top_polarizing.iterrows():
            print(f"    std={row['std']:.3f}  mean={row['mean']:.2f}  "
                  f"(n={int(row['count']):4,})  {title}")


if __name__ == "__main__":
    claude_answers()
