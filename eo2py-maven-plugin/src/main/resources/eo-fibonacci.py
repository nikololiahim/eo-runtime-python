from atoms import *

"""
+package sandbox

[n] > fibonacci
  if. > @
    n.less 2
    n
    add.
      fibonacci (n.sub 1)
      fibonacci (n.sub 2)
"""


# TODO: figure out type resolution
class fibonacci(EObase):
    def __init__(self, n: EObase):
        # super().__init__(0)
        self.n = n
        self.__PARENT__ = EOerror()
        self.__THIS__ = self

    @property
    def __PHI__(self):
        return EOattr(
            EOattr(self.n, 'less', EOnumber(2)),
            'If',
            self.n,
            EOattr(
                fibonacci(EOattr(self.n, 'sub', EOnumber(1))),
                   'add',
                   fibonacci(EOattr(self.n, 'sub', EOnumber(2)))
               )
            )

    def dataize(self):
        return self.__PHI__.dataize()


if __name__ == "__main__":
    res = fibonacci(EOnumber(20))
    print(res.dataize())
