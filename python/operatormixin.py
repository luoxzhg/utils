# -*- coding: utf-8 -*-
class OrderedOperatorMixin:
    # "a > b" <=> "b < a"
    def __gt__(self, other):
        return other < self
    
    # "a >= b" <=> "not (a < b)"
    def __ge__(self, other):
        return not (self < other)

    # "a <= b" <=> "not (b < a)"
    def __le__(self, other):
        return not (other < self)

class EqualOperatorMixin:
    # " a != b" <=> "not (a == b)"
    def __ne__(self, other):
        return not (self == other)
        

class RelationalOperatorMixin(OrderedOperatorMixin, EqualOperatorMixin):
    pass
