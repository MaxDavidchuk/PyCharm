from config import app

from views.home import HomeViews
from views.task import TaskViews


if __name__ == '__main__':

    views1 = HomeViews()
    views2 = TaskViews()

    app.run(debug=True)
