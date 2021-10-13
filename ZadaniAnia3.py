#zad 3
#1
class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'
print('{:open-the-pod-bay-doors}'.format(HAL9000()))
#2
print('{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+'))
#3
from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))
#4
print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3'))
#5
print('{:{width}.{prec}f}'.format(2.7182, width=5, prec=2))
