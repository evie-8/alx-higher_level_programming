#!/usr/bin/python3
"""module for rectangles"""


from .base import Base as Base


class Rectangle(Base):
    """ class called rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """how to retrieve"""
        return self.__width

    @width.setter
    def width(self, value):
        """check value assigned"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """how to retrieve"""
        return self.__height

    @height.setter
    def height(self, value):
        """check value assigned"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """how to retrieve"""
        return self.__x

    @x.setter
    def x(self, value):
        """check value assigned"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """how to retrieve"""
        return self.__y

    @y.setter
    def y(self, value):
        """check value assigned"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """calculates aread of a triangle"""
        return self.width * self.height

    def display(self):
        """displaying rectangle using ##"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """printable representation of class rectangle"""
        return('[Rectangle] ({}) {}/{} - {}/{}'
               .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """updating or changing attributes of instance"""
        if args and len(args) != 0:
            k = ('id', 'x', 'y', 'width', 'height')
            new = dict(zip(k, args))
            for k, v in new.items():
                setattr(self, k, v)
        else:
            if kwargs is not None and len(kwargs) != 0:
                keys = ['id', 'x', 'y', 'width', 'height']
                for k, v in kwargs.items():
                    if k in keys:
                        setattr(self, k, v)

    def to_dictionary(self):
        """dictionary representation of rectangle"""
        keys = ['id', 'width', 'height', 'x', 'y']
        values = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(keys, values))
