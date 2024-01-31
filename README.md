## File Structure (Only the Python files have been uploaded to GitHub.)

### `src/` (Source Code)
- `main.py`
- `todo_list.py`
- `todo.pickle`: File for storing the todo list
- `guess.py`
- `date.py`
- `forum.py`
- `word.py`

### `info/`
- `token.txt`: Contain tokens
- `extensions.txt`: Record available features

### `storage/`
- Directory for files generated during program execution

## Modules Used
- discord, pickle, requests, bs4, datetime, csv, re, asyncio, math, random, os, io

## Commands and Features

### `guess`: Number Guessing Game
- Users can play a number guessing game
- Game description: Enter a four-digit number composed of non-repeating digits from 1-9, the system will output how many A and B
    - A: Correct number and position
    - B: Correct number but wrong position
- To start: `$load guess`
- To play: `$guessnumber`
- To quit: Enter `quit`

### `todo_list`: To-Do List
- A convenient to-do list
- Commands:
    - Add: `$add <date> <label> <item>`
        - Add a new item to the list with date (MM/DD), label, and item description
    - Complete: `$done <date> <label> <item>`
        - Mark an item as completed
    - Show: `$show [label]`
        - Lists all current to-do items, sorted by date. Optional label parameter for specific items
    - Clear: `$clear`
        - Clears all items from the to-do list

### `word`: Word Translation and Image Queries
- Query translations and images for words
- Commands:
    1. Picture output: `$pic <word>`
        - Uses unsplash library for images
    2. Definition: `$definition <word>`
        - Uses urban dictionary for definitions

### `forum`: Querying Hot Posts from Dcard, ptt, Ettoday
- Commands:
    1. the top n post of Dcard: `$dcard <n>`
    2. the top n board of Dcard: `$dcc <n>`
    3. the top n board of ptt: `$ptt <n>`
    4. the top n news of Ettoday: `$ettoday <n>`

### `date`: Date Calculations
- Commands:
    1. Days between two dates: `$days <year1> <month1> <day1> <year2> <month2> <day2>`
    2. What day is that day: `$day <year> <month> <day>`
    3. How many days in that month: `$howmany <year> <month>`
