import words
import img
import random
def random_word(words) :
  word = random.choice(words)
  return word.upper()
def game(word) :
  guess_word = ['_']  * len(word)
  lives = 7
  wrong_guess = 0
  letter_guessed = []
  while wrong_guess < lives and '_' in guess_word :
    print(' '.join(guess_word))
    guess = input("Guess a letter: ").upper()
    if guess in letter_guessed :
      print("you already guessed this letter")
    else :
      letter_guessed.append(guess)
    if guess in word :
      for char in range (len(word)):
        if word[char] == guess:
         guess_word[char] = guess
    else :
      wrong_guess += 1
      print("you guessed a wrong letter . {} lives left.".format(lives - wrong_guess))
      print(img[lives - wrong_guess])
    if '_' not in guess_word :
      print("𝓗𝓾𝓻𝓻𝓪𝔂, 𝔂𝓸𝓾 𝔀𝓸𝓷 𝓽𝓱𝓮 𝓰𝓪𝓶𝓮!  .{}".format(word))
  if lives == wrong_guess :
      print("𝕃𝕚𝕧𝕖𝕤 𝕒𝕣𝕖 𝕠𝕧𝕖𝕣, 𝕓𝕖𝕥𝕥𝕖𝕣 𝕝𝕦𝕔𝕜 𝕟𝕖𝕩𝕥 𝕥𝕚𝕞𝕖. correct word is .{}".format(word))

word = random_word(words)
game(word)
while input("DO YOU WANT TO PLAY?(Y/N)").upper()=="Y":
    word=random_word(Words)
    print(word)
    game(word)
