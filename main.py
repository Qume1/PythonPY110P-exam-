import json
from faker import Faker
import random
from conf import MODEL


def pk(start=1):
    count = start
    while True:
        yield count
        count += 1


def title():
    filename = "books.txt"
    while True:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                titlelist = file.read().splitlines()
                randomtitle_ = random.choice(titlelist)
                yield randomtitle_


def year():
    while True:
        year_ = random.randint(1930, 2022)
        yield year_


def pages():
    while True:
        pages_ = random.randint(20, 2400)
        yield pages_


def isbn13():
    fake = Faker()
    while True:
        book_num = fake.isbn13()
        yield book_num


def rating():
    while True:
        rating_ = random.randint(0, 5)
        yield rating_


def price():
    while True:
        price_ = float(random.randint(200, 5000))
        yield price_


def author():
    while True:
        name = []
        fake = Faker(["ru_RU"])
        authornum = (random.randint(1, 3))
        for i in range(authornum):
            name.append(fake.name())
        yield name


if __name__ == "__main__":
    bookjson = "books.json"
    bookjsofull = []
    pkdict_ = pk()
    titledict_ = title()
    yeardict_ = year()
    pagesdict_ = pages()
    isbn13dict_ = isbn13()
    ratingdict_ = rating()
    pricedict_ = price()
    authordict_ = author()
    for i in range(100):
        book = {
            "model": MODEL,
            "pk": next(pkdict_),
            "fields": {
                "title": next(titledict_),
                "year": next(yeardict_),
                "pages": next(pagesdict_),
                "isbn13": next(isbn13dict_),
                "rating": next(ratingdict_),
                "price": next(pricedict_),
                "author": next(authordict_)
            }
        }
        bookjsofull.append(book)
    with open(bookjson, "w", encoding="utf-8") as f:
        json.dump(bookjsofull, f, indent=4, ensure_ascii=False)
