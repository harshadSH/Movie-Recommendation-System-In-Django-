# Django Movie Recommendation System

A Django-based movie recommendation system that provides personalized movie suggestions based on user input. The system leverages a pre-built recommendation algorithm to suggest movies similar to the one entered by the user.

## Features

- **Movie Search**: Users can input a movie name to receive recommendations.
- **Autocomplete Suggestions**: While typing, users receive suggestions of movie titles.
- **Recommendations**: Get a list of recommended movies similar to the input movie.
- **Stylish UI**: A modern and responsive user interface with vibrant colors and interactive elements.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or later
- Django 4.0 or later
- `pip` for Python package management

## Installation

1. **Clone the Repository**

    ```bash
    https://github.com/harshadSH/Movie-Recommendation-System-Django.git
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run Migrations**

    ```bash
    python manage.py migrate
    ```

6. **Load Data**

    Ensure `movie_data.pkl` and `similarity_matrix.pkl` files are in the `MovieRecommendation` directory.

7. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

8. **Access the Application**

    Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Usage

1. **Input a Movie Name**

    - Type the name of a movie into the search field.
    - View suggestions as you type and select one to see recommendations.

2. **Get Recommendations**

    - After selecting a movie, click on "Get Recommendations" to view a list of similar movies.

## File Structure

- `manage.py`: Command-line utility for Django project management.
- `MovieRecommendation/`: Project directory.
  - `core/`: Contains views, models, and URL configurations.
  - `templates/`: Contains HTML templates for the application.
  - `static/`: Contains static files such as CSS, JavaScript, and images.
- `movie_data.pkl`: Pickled file containing movie data.
- `similarity_matrix.pkl`: Pickled file containing the similarity matrix.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.
