import pandas as pd

# Load the MovieLens dataset
ratings_df = pd.read_csv('ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
users_df = pd.read_csv('ml-100k/u.user', sep='|', names=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
movies_df = pd.read_csv('ml-100k/u.item', sep='|', encoding='latin-1', names=['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url', 'unknown', 'action', 'adventure', 'animation', 'childrens', 'comedy', 'crime', 'documentary', 'drama', 'fantasy', 'film_noir', 'horror', 'musical', 'mystery', 'romance', 'sci_fi', 'thriller', 'war', 'western'])

# Merge datasets to get user demographics for each rating
merged_df = pd.merge(pd.merge(ratings_df, users_df, on='user_id'), movies_df, on='movie_id')

def get_demographics(movie_id):
    # Filter ratings for the specified movie
    movie_ratings = merged_df[merged_df['movie_id'] == movie_id]
    
    # Get demographics of users who rated the movie highly (e.g., rating >= 4)
    high_ratings = movie_ratings[movie_ratings['rating'] >= 4]
    demographics = high_ratings[['age', 'gender', 'occupation']].drop_duplicates()
    
    return demographics

def main():
    # Prompt user to enter a movie ID
    movie_id = int(input("Enter the movie ID: "))
    
    # Get demographics of users who like the specified movie
    demographics = get_demographics(movie_id)
    
    # Display demographics
    print("\nDemographics of users who like the movie:")
    print(demographics)

if __name__ == "__main__":
    main()
