# -*- coding: utf-8 -*-


class Film:
    min_recommended_duration = 10  # class attribute #1
    max_recommended_duration = 60  # class attribute #1

    def __init__(self, name: str, duration: int, country: str):
        """
        The constructor method to initialize the attributes of the class
        Args:
            name: film name
            duration: film duration in minutes
            country: producing country
        """
        self.name = name
        self.duration = duration
        self.country = country

    def change_max_recommended_duration(self, max_recommended_duration):
        """
        Inner methods for change variables
        Returns:

        """
        self.max_recommended_duration = max_recommended_duration
