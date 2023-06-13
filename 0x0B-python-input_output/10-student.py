#!/usr/bin/python3
""""student class"""


class Student:
    """creating class called student"""
    def __init__(self, first_name, last_name, age):
        """creating an instance of class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """changes class instance to json representation"""
        if type(attrs) == list and all(type(i) == str for i in attrs):
            return {ks: getattr(self, ks) for ks in attrs if hasattr(self, ks)}
        return self.__dict__
