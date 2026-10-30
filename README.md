***
```
   ▄      ▄    ▄   ▄  ▄      ▄       ▄   
 ▄▀██▄  ▄██  ▄██ ▄██▄▀██   ▄▀██▄   ▄▀██▄ 
█▓  ▀▒█  █░   █░  █░   ▀  █░  ▀██ █░  ▀██
▓▒       ▒▓   ▒▓  ▒▓      ▒▓   ▀▀ ▒▓   ▀▀
▀▀       ▀▀▀▀▀▀▀  ▀▀▀▀▀    ▀▀      ▀▀    
░░       ░░   ░░  ░░         ▀░▄     ▀░▄ 
▒▒       ▒▒   ▒▒  ▒▒           ▒▒      ▒▒
▓▓▄  ▓▓  ▓▓   ▓▓  ▓▓▄  ▓▓ ▓▓▄  ▓▓ ▓▓▄  ▓▓
 ▀██▄▀  ▀██  ▀██   ▀██▄▀   ▀██▄▀   ▀██▄▀ 
   ▀      ▀    ▀     ▀       ▀       ▀   
```
<img src="assets\ScreenShot\game_window.png" width="300">

***

# Installation

- Create a python venv:

  ```
  python -m venv .venv
  ```

- Activate it
    - Linux / MacOs 
      ```
      source .venv/bin/activate
      ```
    - Windows
      ```
      .\.venv\Scripts\activate
      ```

- Install requirements
  ```
  pip install -r requirements.txt
  ```

# Play

Lunch the game with this command:

```
py src/main.py
```

# Features

## Gui

A pygame windows will open a display:

 - the board
 - the pieces
 - the material scores
 - turns
 - pieces taken
 - winner

## Rules

Pieces wont move if the turn is not theres or if the move is invalid.\
When picking up a piece squares will appear:

  - orange is the current position of the selected piece
  - black are the possible moves
  - red are the possible ennemie pieces to take
