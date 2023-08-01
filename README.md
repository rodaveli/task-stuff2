# Flask Task Tracker

This is a simple web application built using Flask and React. It allows users to track their recurring tasks, earn points by completing tasks, and maintain a streak for continuous task completion.

## Tech Stack

- Flask: Python web framework
- PostgreSQL: Database
- React: Frontend JavaScript library

## Features

- Users can create recurring tasks that are displayed on a grid.
- Each task is worth points (1, 3, or 5), as determined by the user.
- Failing to complete a task incurs a penalty.
- Users have a streak and a point total.
- Completing two tasks per day counts towards a streak. Maintaining a streak adds 1 point per day.
- Weekends (Saturday and Sunday) do not break streaks.
- The user profile displays the user's point total.

## Installation

1. Clone this repository.
2. Install the dependencies by running `pip install -r requirements.txt`.
3. Set up the PostgreSQL database.
4. Run the Flask server with `python app.py`.
5. In a separate terminal, navigate to the `static` directory and run `npm install` to install the React dependencies.
6. Run `npm start` to start the React development server.

## Testing

Tests are located in the `tests` directory. Run them with `python -m unittest discover -s tests`.

## Files

- `app.py`: The main Flask application.
- `config.py`: Configuration for the application.
- `models.py`: Defines the database models.
- `routes.py`: Defines the routes for the Flask application.
- `templates/index.html`: The main HTML template.
- `static/css/main.css`: The main CSS file.
- `static/js/main.js`: The main JavaScript file.
- `static/js/components/`: Contains the React components.
- `migrations/versions/initial_migration.py`: The initial database migration.
- `tests/`: Contains the tests for the application.
- `package.json`: Defines the JavaScript dependencies.
- `webpack.config.js`: Configuration for Webpack.
- `.env`: Environment variables.
- `Procfile`: Used for deploying the application.
- `requirements.txt`: Defines the Python dependencies.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)