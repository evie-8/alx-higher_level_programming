#!/usr/bin/python3
"""first module"""


import json
import csv


class Base:
    """creating a new class called Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor for class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """change dictionary to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write('[]')
            else:
                lists = [objs.to_dictionary() for objs in list_objs]
                f.write(Base.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """change to python reprsentation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """change dictionary to instance"""
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 2, 3, 5, 4)
        else:
            new_obj = cls(1, 3, 1, 1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """files to instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                lists = Base.from_json_string(f.read())
                return [cls.create(**dicts) for dicts in lists]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save objects to csv file in csv format"""
        filename = cls.__name__ + '.csv'
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    fields = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Square":
                    fields = ['id', 'size', 'x', 'y']
                writing_to = csv.DictWriter(f, fieldnames=fields)
                for objs in list_objs:
                    writing_to.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """convert csv to python object"""
        filename = cls.__name__ + '.csv'
        try:
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
            if cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            with open(filename) as f:
                dicts = csv.DictReader(f, fieldnames=fields)
                objs = []
                for d in dicts:
                    for k, v in d.items():
                        if k in ['width', 'height', 'size', 'x', 'y']:
                            d[k] = int(v)
                    objs.append(cls.create(**d))
                return objs
        except FileNotFoundError:
            return []
