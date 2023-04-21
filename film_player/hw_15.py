import os
import string
import media_player as mp
import films_worker as fw

# Створюемо структуру
print(os.getcwd())
os.mkdir("film_storage")
os.chdir("film_storage")
for i in string.ascii_uppercase:
    os.mkdir(i)
os.chdir("..")

# Створюемо об'єкт класу FilmInstance
Snatch = fw.FilmInstance('Snatch', 2000)
print(Snatch.title, Snatch.year)
Snatch.upload_file()
# Snatch.get_film_address()

# Створюемо об'єкт класу MediaPlayer та передаємо як аргумент path до створенного вище об'єкта Snatch
youtube = mp.MediaPlayer(Snatch.get_film_address())

# Перевіряємо методи об'єкту youtube
youtube.play()
youtube.volume_increase()
youtube.pause()
youtube.volume_mute()
youtube.change_quality()
