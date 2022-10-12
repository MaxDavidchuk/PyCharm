from config import app

from views.home import HomeViews
from views.demo import DemoViews


if __name__ == '__main__':

    views1 = HomeViews()
    views2 = DemoViews()

    app.run(debug=True)
