# Study Session Log

Record study sessions and total minutes by subject.

## Quick start

Use Python 3.10 or newer. All dependencies are in the standard library.

```sh
python app.py log Maths 25
python app.py log Maths 15
python app.py list
```

The example output includes `Maths | 40`.

Records are saved in `study-session-log.sqlite3` in the working directory. Use `--db PATH` before the command to choose another database. Run `python app.py --help` for the available options.
