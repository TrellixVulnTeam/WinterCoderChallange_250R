# to jest 1 z 10 zadań w ramach FerieChallange2021

# Napisz program, który prosi użytkownika o podanie dowolnego napisu.
# Następnie program wyświetla na ekranie to słowo wspak (od prawej do lewej)
# i wyświetla komunikat czy to wyrażenie jest palindromem
# (czyli czytane wspak daje do samo wyrażenie np. “ala”, “Kobyła ma mały bok”
# (inne przykłady: http://www.palindromy.pl/pal_kr.php).
# Podczas sprawdzania ignoruj wielkość liter oraz znaki niebędące literami.
# Następnie wywołaj dowolną stronę internetową, która pokaże anagramy oraz słowa utworzone po usunięciu liter,
# np. https://poocoo.pl/scrabble-slowa-z-liter/hardcoder

# Propozycja rozszerzenia: samodzielnie wyszukaj anagramy i słowa utworzone po usunięciu liter z podanego słowa,
# na przykład wykorzystując słownik wspomniany na stronie https://anagramy.wybornie.com/
import time
import webbrowser
word = input("Please write a word or sentence to see if it is a palindrome: ")
word_inverted = "".join(reversed(word)).lower().replace(" ", "")

if word == word_inverted:
    print("It is a palidrome")
    time.sleep(3)
    webbrowser.open("https://poocoo.pl/scrabble-slowa-z-liter/" + word)
else:
    print("It is not a palindrome.")
