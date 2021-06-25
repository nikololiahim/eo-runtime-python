from eo2py.atoms import *
from functools import reduce

"""
[args...] > appArray
  stdout > @
    sprintf
      "%d"
      get.
        *
          5
          2
          4
        0
"""


class EOappArray(Object):
    def __init__(self):
        # Free attributes
        self.attributes = ["args"]
        self.application_counter = 0

    def __call__(self, arg: Object):
        if self.application_counter == 0:
            setattr(self, self.attributes[self.application_counter], [])
            self.application_counter += 1
        getattr(self, self.attributes[0]).append(arg)
        return self

    @property
    def __PHI__(self):
        return Stdout()(
                Sprintf()
                (String("%d"))
                (Attribute(reduce(lambda obj, arg: obj(arg), self.args, Array()), "Get")()(Number(3)))
                )

    def dataize(self):
        return self.__PHI__.dataize()


def test_simple_array():
    app = EOappArray()(Number(1))(Number(2))(Number(3))(Number(4))(Number(5))
    assert app.dataize()
