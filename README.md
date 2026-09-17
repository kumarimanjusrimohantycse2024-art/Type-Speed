# Type-Speed

A lightweight desktop typing-speed practice app built with Python and Tkinter.  
It helps users practice sentence typing accuracy and get instant words-per-minute (WPM) feedback.

## Features

- Random sentence prompt on each test start
- WPM calculation from typed input and elapsed time
- Accuracy feedback (`Correct` / `Incorrect`)
- Simple local GUI (no external services required)

## Tech Stack

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [unittest](https://docs.python.org/3/library/unittest.html) for tests
- [GitHub Actions](./.github/workflows/ci.yml) for CI

## Project Structure

```text
.
├── Git.py                  # Main Tkinter application
├── tests/
│   └── test_git.py         # Unit tests for WPM/result logic
└── .github/workflows/
    └── ci.yml              # CI workflow (test run)
```

## Prerequisites

- Python 3.9+ installed
- A desktop environment that supports Tkinter windows

## Installation

```bash
git clone https://github.com/kumarimanjusrimohantycse2024-art/Type-Speed.git
cd Type-Speed
```

No third-party packages are required.

## Configuration

No environment variables or secrets are needed.

To customize practice content, edit the `sentences` list in [`Git.py`](./Git.py).

## Usage

Run the app:

```bash
python Git.py
```

In the UI:
1. Click **Start Test**
2. Type the shown sentence
3. Click **Check Speed** to see WPM and accuracy

## Testing

Run unit tests:

```bash
python -m unittest discover -s tests -v
```

## Troubleshooting

- **`tkinter` import or window errors**: install Python with Tk support (system package names vary by OS).
- **Nothing happens when checking speed**: click **Start Test** first.
- **Unexpected WPM values**: ensure you type complete words separated by spaces.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add or update tests for code changes
4. Open a pull request with a clear summary

## License / Status

- **License:** No license file is currently present in this repository.
- **Project status:** Active and open to improvements.
