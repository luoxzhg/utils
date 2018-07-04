# _*_encoding: utf8 _*_
"""
Used for reference a list or part without copy.
Changes of the referenced object will reflect to the views.
View is immutable.
"""
import numbers

class listview(list):
    def __new__(cls, lst, start=None, stop=None, step=None):
        ln = len(lst)
        start, stop, step = slice(start, stop, step).indices(ln)
        if isinstance(lst, cls):
            if (start, stop, step) == (0, ln, 1):
                return lst
            
            start = lst.start + start *lst.step
            stop = lst.start + stop * lst.step
            step = lst.step * step
            lst = lst.lst
            
        self = object.__new__(listview)
        self.lst = lst
        self.start = start
        self.stop = stop
        self.step = step

        return self
    
##    def __init__(self, lst, start=None, stop=None, step=None):
##        print("----init-----")
##        start, stop, step = slice(start, stop, step).indices(len(lst))
##        
##        if isinstance(lst, listview):
##            # todo: 如果 start, stop, step 全为 None，则应该返回 lst，需要在元类中实现
##            start = lst.start + start *lst.step
##            stop = lst.start + stop * lst.step
##            step = lst.step * step
##            lst = lst.lst
##
##        self.start = start
##        self.stop = stop
##        self.step = step
##        self.lst = lst
##

    def __len__(self):
        return (self.stop - self.start) // self.step
    
    def __getitem__(self, n):
        if isinstance(n, numbers.Integral):
            index = self.start + n * self.step
            if index >= self.stop:
                raise IndexError("Index out of range")
            return self.lst[index]
        elif isinstance(n, slice):
            return self.__class__(self, n.start, n.stop, n.step)
        else:
            raise TypeError("index must be int")

    
