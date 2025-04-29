def test3(self):
  a = 2
  b = 4
  self.assertFalse(mystery_func(a,b),msg='Does not meet the requirements (a={}, b={}'.format(a,b))

def test4(self):
  a = 4
  b = 2
  self.assertFalse(mystery_func(a,b),msg='Does not meet the requirements (a={}, b={}'.format(a,b))