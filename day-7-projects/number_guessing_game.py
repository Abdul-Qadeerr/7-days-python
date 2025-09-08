{
 "cells": [ 
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 🎮 Number Guessing Game in Python\n",
    "This game asks the user to guess a number between 1 and 100."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "secret_number = random.randint(1, 100)\n",
    "attempts = 0\n",
    "\n",
    "print(\"Welcome to the Number Guessing Game!\")\n",
    "print(\"I have chosen a number between 1 and 100.\")\n",
    "\n",
    "while True:\n",
    "    guess = int(input(\"Enter your guess: \"))\n",
    "    attempts += 1\n",
    "\n",
    "    if guess < secret_number:\n",
    "        print(\"Too low! Try again.\")\n",
    "    elif guess > secret_number:\n",
    "        print(\"Too high! Try again.\")\n",
    "    else:\n",
    "        print(f\"🎉 Congratulations! You guessed it in {attempts} attempts.\")\n",
    "        break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
