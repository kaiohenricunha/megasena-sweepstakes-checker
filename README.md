# Requirements

* [Python 3 or above](https://www.python.org/downloads/)

# Running the project locally

1. Clone the repository
2. In the project directory, run `python3 -m venv venv`
3. Activate the virtual environment by running `source venv/bin/activate`
4. Install the requirements by running `pip3 install -r requirements.txt`. You can alternatively run `pip3 install pandas` for a slimmed down environment.
5. In the terminal, run `python3 main.py` and insert the required input

To deactivate the virtual environment just run `deactivate`.

# Betting data

* You need a .csv file in the project directory with the betting data.

If you want to add a bet, just add a new row to the .csv file.

The format is as follows:

| betcode | ownership | numbers |
|------|-----------|-----------|
... | ... | ... |
| 49 | John Doe | 1 2 3 4 5 6 |

Which translates to:

49,John Doe,1 2 3 4 5 6
