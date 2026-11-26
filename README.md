# Tic-Tac-Toe 🎮

<img width="1908" height="905" alt="2026-11-26_12-55-32" src="https://github.com/user-attachments/assets/a72b9cf1-69b3-4a63-91d8-1f3dd23f9605" />

A classic Tic-Tac-Toe (Noughts and Crosses) game that runs in the terminal,
written in pure Python — no external dependencies required.

You play as **O** against a computer opponent (**X**) on a 3×3 board whose
cells are numbered from 1 to 9. Matches are played round after round, and the
score is tracked continuously.

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## Features

- **Human vs. machine gameplay** — you enter a cell number (1–9) to place your `O`.
- **Smart-ish opponent** — the machine checks for squares that complete a line
  (winning moves) and prioritizes strategic cells (corners and center: 1, 3, 5, 7, 9).
- **Input validation** — rejects non-numeric input, out-of-range values, and
  already-occupied cells, then re-prompts.
- **Automatic win/tie detection** — rows, columns, and diagonals are checked
  after every move.
- **Persistent scoreboard** — player, machine, and tie counts accumulate
  across rounds in the same session.

## Requirements

- Python 3.x

No third-party libraries are used — only the standard library.

## How to Run

Clone the repository:

```bash
git clone https://github.com/Zyz7/tictactoe.git
cd tictactoe
```

Then run:

```bash
python main.py
```

## How to Play

1. The board is displayed with cells numbered **1** through **9**.
2. When prompted, type the number of the cell where you want to place your `O`.
3. The machine responds by placing its `X`.
4. First to align three symbols in a row, column, or diagonal wins the round.
5. If all cells are filled with no winner, the round is a tie.
6. After each round the scoreboard is shown and a new round begins.

## Project Structure

```
tictactoe/
├── main.py     # Game logic, board rendering, and game loop
└── LICENSE
```
