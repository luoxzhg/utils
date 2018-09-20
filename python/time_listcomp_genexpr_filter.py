import timeit

TIMES = 100000

# symbols数据过小时，genexpr性能无法表现
SETUP = """
symbols = '$¢£¥€¤31456789fhdjlvruFGRJUCZKIPMSQS:{}[]()_+=-'
def non_ascii(c):
    return c > 127
"""

def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('genexpr         :', 'list(ord(s) for s in symbols if ord(s) > 127)')
clock('genexpr + func  :', 'list(ord(s) for s in symbols if non_ascii(ord(s)))')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
clock('for             :', '''
l = []
for s in symbols:
    n = ord(s);
    if n % 2:
        l.append(n)
''')
