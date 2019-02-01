# -*- coding: utf-8 -*-
from myclass import Film


def main():
    film_1 = Film('В бой идут одни "старики".', 92, "СССР")
    print(film_1.max_recommended_duration)
    film_1.change_max_recommended_duration(95)
    print(film_1.max_recommended_duration)
    print(film_1.name)
    print(film_1.duration)
    print(film_1.country)


if __name__ == '__main__':
    main()
