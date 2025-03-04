**Project Goal:** Adapt the existing Hangman game from "Invent with Python" into a Wordle-like game using Pygame, with external data files for words and graphics.

**I. Leveraging Existing Hangman Code:**

1.  **Code Familiarization:**
    * Thoroughly review the `hangman.py` file from the provided link.
    * Understand the game loop, input handling, and display mechanisms.
2.  **Base Structure:**
    * Utilize the existing game loop and input handling as a foundation.
    * Adapt the display logic for Pygame integration.

**II. Core Game Logic Changes (Wordle-Style Adaptation):**

1.  **Word List (External):**
    * Replace the hardcoded word list with a `words.txt` file (five-letter words, one per line).
    * Modify the word selection logic to read from this file.
2.  **Guessing Mechanism:**
    * Change the single-letter guess input to a five-letter word input.
    * Limit the number of guesses to six.
3.  **Feedback System:**
    * Remove the simple letter presence/absence feedback.
    * Implement Wordle's color-coded feedback:
        * **Green:** Correct letter, correct position.
        * **Yellow:** Correct letter, wrong position.
        * **Gray:** Letter not in the word.
4.  **Display (Pygame):**
    * Replace the text-based display with a Pygame grid.
    * Each row represents a guess, with colored letter tiles.
5.  **Win/Loss Conditions:**
    * Modify the win condition to guessing the exact word in six tries.
    * Adjust the loss condition to failing to guess within six tries.
6.  **Input Validation:**
    * Change the input validation to check for five-letter words from the word list.
7.  **Game State:**
    * Expand the game state to store the full guess history and feedback.

**III. Pygame Implementation:**

1.  **Project Setup:**
    * Create `words.txt` and `assets` folders.
    * Install Pygame.
    * Adapt the existing `hangman.py` file to `wordle_hangman.py`.
2.  **Data Loading:**
    * Functions to load words from `words.txt`.
    * Functions to load images from `assets`.
3.  **Pygame Window and Grid:**
    * Initialize Pygame.
    * Create the game window.
    * Draw the guess grid using Pygame.
4.  **Input Handling (Pygame):**
    * Adapt the existing input handling for Pygame.
    * Handle keyboard input for word guesses and "Enter" submission.
5.  **Guessing and Feedback Logic:**
    * Implement the Wordle guessing and feedback rules.
    * Generate color-coded feedback.
6.  **Game State Management:**
    * Store guess history.
    * Determine win/loss.
7.  **Visual Enhancements:**
    * Use the hangman stage progression as a base for visual assets.
    * Add fonts and text elements.
    * Refine the user interface.

**IV. Step-by-Step Development:**

1.  **Base Code Setup:**
    * Copy `hangman.py` to `wordle_hangman.py`.
    * Create `words.txt` and `assets`.
    * Install Pygame.
2.  **Word List and Graphics Loading:**
    * Implement functions to load data.
3.  **Pygame Window and Grid:**
    * Create a basic Pygame window and grid.
4.  **Input Handling:**
    * Adapt the existing input handling for Pygame.
5.  **Guessing Logic:**
    * Implement the Wordle guessing mechanism.
6.  **Feedback System:**
    * Implement the color-coded feedback.
7.  **Game State and Win/Loss Conditions:**
    * Manage the game state and determine win/loss.
8.  **Visual Enhancements:**
    * Implement hangman stages.
    * Add fonts and text.
    * Refine the user interface.
9.  **Testing and Refinement:**
    * Thoroughly test and debug.
    * Refine the user interface.
10. **Documentation:**
    * Document the code.
