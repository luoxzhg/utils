# -*- coding: utf8 -*-
"""
Used for reference a list or part without copy.
Changes of the referenced object will reflect to the views.
View is immutable.

>>> l=[1,2,3,4]
>>> v=listview(l)
>>> v
listview([1, 2, 3, 4])
>>> v2=listview(v)
>>> v2 is v
True
>>> v3=v[:2]
>>> v3
listview([1, 2])
>>> v4=v[::2]
>>> v4
listview([1, 3])
"""
import numbers

# helper functions
def _calcindex(self, n):
    return self.start + n * self.step 

class _meta(type):
    def __call__(cls, lst, start=None, stop=None, step=None):
        ln = len(lst)
        start, stop, step = slice(start, stop, step).indices(ln)
        if isinstance(lst, cls):
            if (start, stop, step) == (0, ln, 1):
                return lst
            
            start = _calcindex(lst, start)  #lst.start + start *lst.step
            stop = _calcindex(lst, stop)    #lst.start + stop * lst.step
            step = lst.step * step
            lst = lst.lst
            
        return type.__call__(cls, lst, start, stop, step)

class listview(metaclass=_meta):
    __slots__ = ('lst', 'start', 'stop', 'step')
    
    def __init__(self, lst, start=None, stop=None, step=None):
        self.lst = lst
        self.start = start
        self.stop = stop
        self.step = step

    def __repr__(self):
        return 'listview([' + ', '.join(str(e) for e in self if e is not self else '[...]') + '])'

    def __iter__(self):
        return (self.lst[i] for i in range(self.start, self.stop, self.step))

    def __len__(self):
        return (self.stop - self.start) // self.step
    
    def __getitem__(self, n):
        if isinstance(n, numbers.Integral):
            index = _calcindex(self, n)     #self.start + n * self.step
            if index >= self.stop:
                raise IndexError("Index out of range")
            return self.lst[index]
        elif isinstance(n, slice):
            return self.__class__(self, n.start, n.stop, n.step)
        else:
            raise TypeError("index must be int")

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
