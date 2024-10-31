# Book Recommendation System

## Description
This Book Recommender System recommends books based on user input using collaborative filtering. The project leverages preprocessed data and similarity scores to deliver book suggestions. It includes a Flask-based backend and a user-friendly interface for book selection and recommendations.

## Project Overview
This project implements a collaborative filtering-based recommendation system with Flask as the backend and HTML/CSS for the frontend. Users can browse popular books and get personalized recommendations by entering a book title. The recommendation system utilizes a cosine similarity-based approach to match similar books.

Features:- 

**- Popular Books Display:** Displays the top-rated and most popular books.
**- Book Recommendations:** Recommends books similar to user-selected titles.
**- User-Friendly Interface:** A responsive and intuitive interface built with Bootstrap and Flask for easy navigation.

## Files and Structure
**app.py:** Main Flask application to render templates and handle requests.
**popular.pkl:** Contains data on popular books with details like title, author, image, rating, and votes.
**pt.pkl:** Pivot table used for collaborative filtering.
**books.pkl:** Complete book dataset with details for each book.
**similarity_scores.pkl:** Precomputed similarity scores used for finding similar books.
**templates/index.html:** Homepage displaying popular books.
**templates/recommend.html:** Page to accept user input and show recommended books.

## Data Requirements
The system requires preprocessed datasets in pickle format:
**popular.pkl** contains popular book data.
**pt.pkl** and **books.pkl** hold details for similarity calculation.
**similarity_scores.pkl** stores precomputed cosine similarity scores.

## Usage
**1. Homepage:**
Displays the top 50 popular books along with their author, rating, and cover image.

**2. Book Recommendation:**
-Navigate to the Recommend page.
-Enter a book title to receive a list of similar books.
-The system displays the recommended books with their title, author, and cover.

## Technical Details

**1. Backend:**
   Flask handles request routing, rendering templates, and processing recommendations.
**2. Frontend:**
   Bootstrap-based HTML/CSS for responsive pages.
**3. Recommendation Algorithm:**
   Cosine Similarity is used to compute similarity scores between books.
   Collaborative Filtering model suggests books based on user input.
**4. Data Processing:**
   The model relies on precomputed similarity scores to deliver quick recommendations.
