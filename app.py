from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the pickle files correctly
with open(r'C:\Users\aarus\PycharmProjects\book-recommender-system\popular.pkl', 'rb') as f:
    popular_df = pickle.load(f)

with open(r'C:\Users\aarus\PycharmProjects\book-recommender-system\pt.pkl', 'rb') as f:
    pt = pickle.load(f)

with open(r'C:\Users\aarus\PycharmProjects\book-recommender-system\books.pkl', 'rb') as f:
    books = pickle.load(f)

with open(r'C:\Users\aarus\PycharmProjects\book-recommender-system\similarity_scores.pkl', 'rb') as f:
    similarity_scores = pickle.load(f)

app = Flask(__name__)

# Home page route
@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values))

# Recommend page route
@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

# The function that processes recommendations
@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input').strip()

    # Check if the input is empty or not found in the matrix
    if user_input not in pt.index:
        return render_template('recommend.html', error="Book not found. Please try again.")

    # Get index of the book from the pivot table
    index = np.where(pt.index == user_input)[0][0]

    # Get the similarity scores for that book
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]

    # Fetch book details for similar books
    data = []
    for i in similar_items:
        book_index = i[0]  # Get index of the book in the pivot table
        temp_df = books[books['Book-Title'] == pt.index[book_index]]

        # Ensure there is no empty dataframe
        if not temp_df.empty:
            item = []
            item.append(temp_df['Book-Title'].values[0])  # Book title
            item.append(temp_df['Book-Author'].values[0])  # Author name
            item.append(temp_df['Image-URL-M'].values[0])  # Image URL
            data.append(item)

    # If data is empty, no recommendations were found
    if len(data) == 0:
        return render_template('recommend.html', error="No recommendations found. Please try again.")

    # Return the data to the template
    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
