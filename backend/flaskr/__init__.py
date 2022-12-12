import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def pagination(request, select):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in select]
    pg = questions[start:end]
    return pg


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        response.headers.add("Access-Control-Allow-Credentials", "true")

        return response

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.

    """

    @app.get("/categories")
    def category():
        try:
            category = Category.query.all()
            if category is None:
                abort(404)
            list_cat = {}
            for categ in category:
                list_cat[categ.id] = categ.type
            return {"success": True, "categories": list_cat}
        except:
            abort(404)

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.get("/questions")
    def quest():
        try:
            questions = Question.query.order_by(Question.id).all()
            total_questions = len(questions)
            pg = pagination(request, questions)

            category = Category.query.all()
            if category is None:
                abort(404)
            list_cat = {}
            for categ in category:
                list_cat[categ.id] = categ.type

            return {
                "success": True,
                "questions": pg,
                "total_questions": total_questions,
                "categories": list_cat,
                "current_category": None,
            }

        except:
            pass

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.delete("/questions/<int:question_id>")
    def deletequestion(question_id):
        removeid = Question.query.filter_by(id=question_id).first()
        if removeid is None:
            abort(422)

        try:
            removeid.delete()
            questions = Question.query.order_by(Question.id).all()
            pg = pagination(request, questions)
            return {"success": True}
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.post("/questions")
    def insert_new_one():
        body = request.get_json()
        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_category = body.get("category", None)
        new_difficulty = body.get("difficulty", None)
        try:
            record = Question(
                question=new_question,
                answer=new_answer,
                category=new_category,
                difficulty=new_difficulty,
            )
            record.insert()
            questions = Question.query.order_by(Question.id).all()
            total_questions = len(questions)
            pg = pagination(request, questions)
            return {"success": True}

        except:
            abort(400)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    @app.post("/search")
    def search_quest():
        body = request.get_json()
        new_search = body.get("searchTerm")
        questions = Question.query.filter(
            Question.question.ilike("%" + new_search + "%")
        ).all()
        if questions:
            total_questions = len(questions)

            pg = pagination(request, questions)
            return {
                "success": True,
                "questions": pg,
                "total_questions": total_questions,
                "current_category": None,
            }
        else:
            abort(404)

    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """

    @app.get("/categories/<int:catigory_id>/questions")
    def get_id(catigory_id):
        get_catigory = Category.query.filter_by(id=catigory_id).first()
        try:
            if get_catigory:
                questions = Question.query.filter_by(category=get_catigory.id).all()
                total_questions = len(questions)

                pg = pagination(request, questions)
                return {
                    "success": True,
                    "questions": pg,
                    "total_questions": total_questions,
                    "current_category": get_catigory.type,
                }
        except:
            abort(404)

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """

    @app.post("/quizzes")
    def quiz():
        body = request.get_json()
        new_c = body.get("quiz_category")
        privious_q = body.get("privious_question")
        quest_by_category = (
            Question.query.all()
            if new_c.get("id") == 0
            else Question.query.filter_by(category=new_c.get("id")).all()
        )

        random_index = random.randint(0, len(quest_by_category) - 1)
        question = None
        if quest_by_category:
            question = quest_by_category[random_index]

        return {"question": question.format()}

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "error": 404, "message": "not found"}), 404

    @app.errorhandler(422)
    def unprocesable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    return app
