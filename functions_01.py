# Завдання 1
# Створіть функцію(назву оберіть самі) без параметрів, котра повертає(return) рядок "Це моя перша функція". Викличте цю функцію у наступному рядку.

def first_func():
    return "This is my first function!"


print(first_func())


# Завдання 2
# Створіть функцію, котра має один параметр(число) і повертає це число у степині 2.

def square_num(num):
    return num ** 2


print(square_num(5))


# Завдання 3
# Ситворіть функцію, котра приймає список фільмів і повертає новий список з фільмами назва яких більше 8 літер.

films = ['Spider-man: No way to home',
        'Crazy Stupid Love.',
        'Die Hard',
        'Dead Poets Society',
        'Home Alone',
        'Seven',
        'Memento',
        'Harry Potter and the Prisoner of Azkaban',
        "One Flew Over the Cuckoo's Nest"
        ]


def long_title_list(movie_list):
    return [title for title in movie_list if len(title) > 8]


print("The titles of following movies are longer than 8 characters", long_title_list(films))


# Завдання 4
# Ситворіть функцію, котра приймає список чисел та повертає тупл. Перше значення тупла є середнім значенням всіх аргументів, а друге значення перше число яке більше середнього.

test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]


def average_and_next(num_list: list) -> tuple:
    x = sum(num_list) / len(num_list)
    print(f"Average num is {x}")
    for y in num_list:
        if y > x:
            print(f"The first num in list greater than average is {y}")
            return x, y


print(average_and_next(test_list))


# Завдання 5
# Створіть функцію, котра приймає 1 параметр - це cписок чисел. Функція повертає новий список, який складається лише з парних чисел що були в аргументі.

test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]


def even_num_list(num_list: list) -> list:
    return [num for num in num_list if num % 2 == 0]


print("The list of even numbers", even_num_list(test_list))


# Завдання 6
# Створіть функцію, яка приймає список туплів і повертає назву предмету з найвищою оцінкою.

grade = [('Англійська мова', 88), ('Біологія', 90), ('Математика', 97), ('Українська мова', 82)]


def highest_grade(grades_list: list) -> str:
    subject_grade = 0
    subject_title = None
    for subject in grades_list:
        if subject_grade < subject[1]:
            subject_grade = subject[1]
            subject_title = subject[0]
    return f"The subject with the highest grade is {subject_title}."


print(highest_grade(grade))


# Завдання 7
# Створіть функцію, яка приймає два параметри: перший число(назва довільна), другий параметр(step) за замовчуванням дорывнює 2.
# Функція повертає аргумент першгого параметра возведений у степінь що передається у параметрі 2.


def num_exponentiation(num, step=2):
    return num ** step


print(num_exponentiation(3, 3))
print(num_exponentiation(3))


# Завдання 8
# Створіть функцію, яка приймає один параметр imdb_id і повертає назву фільму, що відповідає цьому id зі списку films_title.

films_title = {
    "results": [
        {
            "imdb_id": "tt1201607",
            "title": "Harry Potter and the Deathly Hallows: Part 2"
        },
        {
            "imdb_id": "tt0241527",
            "title": "Harry Potter and the Sorcerer's Stone"
        },
        {
            "imdb_id": "tt0926084",
            "title": "Harry Potter and the Deathly Hallows: Part 1"
        },
        {
            "imdb_id": "tt0304141",
            "title": "Harry Potter and the Prisoner of Azkaban"
        },
        {
            "imdb_id": "tt0417741",
            "title": "Harry Potter and the Half-Blood Prince"
        },
        {
            "imdb_id": "tt0295297",
            "title": "Harry Potter and the Chamber of Secrets"
        },
        {
            "imdb_id": "tt0330373",
            "title": "Harry Potter and the Goblet of Fire"
        },
        {
            "imdb_id": "tt0373889",
            "title": "Harry Potter and the Order of the Phoenix"
        }
    ]
}


def movie_search(user_imdb_id: str) -> str:
    for movie in films_title["results"]:
        # print(movie["title"])
        if movie["imdb_id"] == user_imdb_id:
            return movie["title"]


print(movie_search("tt0295297"))
