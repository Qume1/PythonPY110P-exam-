import json
import random

from faker import Faker

from conf import MODEL


def pk(start=1):
    count = start
    while True:
        yield count
        count += 1


def title():
    filename = "books.txt"
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            titlist = file.read().splitlines()
            entitle_ = random.choice(titlist)
            return entitle_


def year():

    year_ = random.randint(1930, 2022)
    return year_


def pages():
    pages_ = random.randint(20, 2400)
    return pages_


def isbn13():
    fake = Faker()
    book_num = fake.isbn13()
    return book_num


def rating():

    rating_ = random.randint(0, 5)
    return rating_


def price():

    price_ = float(random.randint(200, 5000))
    return price_


def author():

    name = []
    fake = Faker(["ru_RU"])
    numerate = (random.randint(1, 3))
    for item in range(numerate):
        name.append(fake.name())
    return name


def booksgenerator():
    pk_ = pk()
    while True:
        book = {
            "model": MODEL,
            "pk": next(pk_),
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn13(),
                "rating": rating(),
                "price": price(),
                "author": author()
            }
        }
        yield book


if __name__ == "__main__":
    bookjson = "books.json"
    book_ = booksgenerator()
    booklist = [next(book_) for i in range(100)]

    with open(bookjson, "w", encoding="utf-8") as f:
        json.dump(booklist, f, indent=4, ensure_ascii=False)
