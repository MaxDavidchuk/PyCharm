from config import app
from views.home import HomeViews
from views.auth import AuthViews
from views.books import BookViews


if __name__ == '__main__':

    views1 = HomeViews()
    views2 = AuthViews()
    views3 = BookViews()

    app.run(debug=True)