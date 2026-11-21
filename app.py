"""Record study sessions and total minutes by subject."""

import argparse
import sqlite3
from contextlib import closing


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("Expected an integer of at least 1")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default="study-session-log.sqlite3", help="SQLite database path")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List records")
    command = commands.add_parser("log", help="Record one session.")
    command.add_argument("subject")
    command.add_argument("minutes", type=positive)
    args = parser.parse_args()
    try:
        with closing(sqlite3.connect(args.db)) as db, db:
            db.execute("CREATE TABLE IF NOT EXISTS items (subject TEXT NOT NULL, minutes INTEGER NOT NULL)")
            if args.command == "list":
                for row in db.execute("SELECT subject, SUM(minutes) AS total_minutes FROM items GROUP BY subject ORDER BY 1, 2"):
                    print(" | ".join(map(str, row)))
            elif args.command == "log":
                db.execute("INSERT INTO items VALUES (?, ?)", (args.subject, args.minutes))
    except (ValueError, sqlite3.Error) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
