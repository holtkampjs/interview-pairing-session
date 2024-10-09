# Conway's Game of Life

Description: [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)

> The Game of Life, also known as Conway's Game of Life or simply Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

## Rules

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
1. Any live cell with two or three live neighbours lives on to the next generation.
1. Any live cell with more than three live neighbours dies, as if by overpopulation.
1. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

## Setup

It's more of a guideline, like the pirate's code.

### Virtual Environment (venv)

Create a virtual environment.

```sh
python -m venv .venv
```

Activate the virtual environment

```sh
. ./.venv/bin/activate
```

Install dependencies with `pip`

```sh
pip install --requirement requirements.txt
```

## Testing

To run the tests, execute:

```sh
pytest
```
