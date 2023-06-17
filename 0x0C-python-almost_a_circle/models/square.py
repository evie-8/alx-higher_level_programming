#!/usr/bin/python3
"""sqaure module"""


from .rectangle import Rectangle as Rectangle


class Square(Rectangle):
    """class rectangle tht inherits from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """square constructor"""
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """retrieving width"""
        return self.width

    @size.setter
    def size(self, value):
        """setting values for width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """printable representation of a sqaure"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """updating or changing attributes of instance"""
        if args and len(args) != 0:
            k = ('id', 'size', 'x', 'y')
            new = dict(zip(k, args))
            for k, v in new.items():
                setattr(self, k, v)
        else:
            if kwargs is not None and len(kwargs) != 0:
                keys = ['id', 'size', 'x', 'y']
                for k, v in kwargs.items():
                    if k in keys:
                        setattr(self, k, v)

    def to_dictionary(self):
        """dictionary representation of rectangle"""
        keys = ['id', 'size', 'x', 'y']
        values = [self.id, self.width,  self.x, self.y]
        return dict(zip(keys, values))
