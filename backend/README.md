# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

### Documentation Example

# API Reference

## 

## Getting Started

- The backend API is hosted at [http://127.0.0.1:5000](http://127.0.0.1:5000/), it can be used as base URL.
- Authentication: This version does not require authentication or API keys.

## 

## Error Handling

Errors are returned as JSON in the following format:

`{
    "success": False,
    "error": 404,
    "message": "resource not found"
}`

The API will return three types of errors: 
- 400 – bad request
- 404 – resource not found
- 422 – unprocessable

## 

## Endpoints

### 

### GET /categories

- General: Return a list of categories
- Sample: curl [http://127.0.0.1:5000/categories](http://127.0.0.1:5000/categories)

`{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}`

### 

### GET /questions

- General:
    - Return a list of questions
    - Returned list is grouped by 10
    - Total number of questions is also included in returned json
- Sample: curl [http://127.0.0.1:5000/questions](http://127.0.0.1:5000/questions)

  `{
    "categories": {
      "1": "Science",
      "2": "Art",
      "3": "Geography",
      "4": "History",
      "5": "Entertainment",
      "6": "Sports"
    },
    "questions": [
      {
        "answer": "It's really excellent!",
        "category": 1,
        "difficulty": 3,
        "id": 58,
        "question": "How about udaicty FSND project?"
      },
      {
        "answer": "It's really excellent!",
        "category": 1,
        "difficulty": 3,
        "id": 56,
        "question": "How about udaicty FSND project?"
      },
      {
        "answer": "It's really excellent!",
        "category": 1,
        "difficulty": 3,
        "id": 54,
        "question": "How about udaicty FSND project?"
      },
      {
        "answer": "It's really excellent!",
        "category": 1,
        "difficulty": 3,
        "id": 37,
        "question": "How about udaicty FSND project?"
      },
      {
        "answer": "Blood",
        "category": 1,
        "difficulty": 4,
        "id": 22,
        "question": "Hematology is a branch of medicine involving the study of what?"
      },
      {
        "answer": "Alexander Fleming",
        "category": 1,
        "difficulty": 3,
        "id": 21,
        "question": "Who discovered penicillin?"
      },
      {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
      },
      {
        "answer": "Jackson Pollock",
        "category": 2,
        "difficulty": 2,
        "id": 19,
        "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
      },
      {
        "answer": "One",
        "category": 2,
        "difficulty": 4,
        "id": 18,
        "question": "How many paintings did Van Gogh sell in his lifetime?"
      },
      {
        "answer": "Mona Lisa",
        "category": 2,
        "difficulty": 3,
        "id": 17,
        "question": "La Giaconda is better known as what?"
      }
    ],
    "success": true,
    "total_questions": 22
  }`

### 

### DELETE /questions/<int:id>

- General: Delete a question by id, if success return deleted question's id
- Sample: curl [http://127.0.0.1:5000/questions/37](http://127.0.0.1:5000/questions/37) -X DELETE

`{
    "deleted": 37,
    "success": true
}`

### 

### POST /questions

- General: Add a new question, and return newly add new question, and list of questions
- Sample: curl [http://127.0.0.1:5000/questions](http://127.0.0.1:5000/questions) -X POST -H "Content-Type: application/json" -d '{ "question": "New
question by POST", "answer": "Answer for new question", "difficulty": 3, "category": "3" }'

`{
    "created": 67,
    "question_created": "New question by POST",
    "questions": [
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Answer for new question",
            "category": 3,
            "difficulty": 3,
            "id": 67,
            "question": "New question by POST"
        }
    ],
    "success": true,
    "total_questions": 21
}`

### 

### POST /questions with searchTerm

- General: Search questions which contains 'searchTerm' in JSON parameters
- Sample: curl [http://127.0.0.1:5000/questions](http://127.0.0.1:5000/questions) -X POST -H "Content-Type: application/json" -d '{"searchTerm": "boxer"}'

`{
  "questions": [
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    }
  ],
  "success": true,
  "total_questions": 1
}`

### 

### GET /categories/<int:id>/questions

- General: Return the list of questions which are in the category id
- Sample: curl [http://127.0.0.1:5000/categories/1/questions](http://127.0.0.1:5000/categories/1/questions)

`{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "It's really excellent!",
      "category": 1,
      "difficulty": 3,
      "id": 37,
      "question": "How about udaicty FSND project?"
    }
  ],
  "success": true,
  "total_questions": 4
}`

### 

### POST /quizzes

- General: Return a random question, however, the returned question should be not one of previous questions
- Sample:curl [http://127.0.0.1:5000/quizzes](http://127.0.0.1:5000/quizzes) -X POST -H "Content-Type: application/json" -d '{"previous_questions":
[2, 9], "quiz_category": {"type": "Science", "id": "1"}}'

`{
  "question": {
    "answer": "Alexander Fleming",
    "category": 1,
    "difficulty": 3,
    "id": 21,
    "question": "Who discovered penicillin?"
  },
  "success": true
}`

## Testing

Write at least one test for the success and at least one error behavior of each endpoint using the unittest library.

To deploy the tests, run

```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
