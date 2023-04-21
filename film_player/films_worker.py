import os


class FilmInstance:
    description = "blah-blah-blah"
    director = None
    writer = None
    actors = None
    running_time = None
    imdb_rating = None
    storage_address = None

    def __init__(self, title, year):
        self.title = title
        self.year = year

    def upload_file(self):
        # print(os.getcwd())
        os.chdir('film_storage')
        dir_list = os.listdir(os.getcwd())
        # print(dir_list)
        for directory in dir_list:
            if self.title[0].upper() == directory:
                file_path = os.path.join(os.getcwd(), directory, self.title + '.txt')
                with open(file_path, 'a') as movie_title_write:
                    movie_title_write.write(self.title + '\n')
                print(f"The title '{self.title}' is added to '{self.title}.txt' in directory '{directory}'.")

        self.storage_address = file_path

    def get_film_address(self):
        print(f"The path to movie is {self.storage_address}")
        return self.storage_address
