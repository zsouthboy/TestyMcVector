import math

class Vec2(object):
	def __init__(self, x=0.0, y=0.0):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Vec2(%s, %s)" % (self.x, self.y)

	@staticmethod #first try with staticmethods, might bone this
	def from_pts(one, two): 
		"""Returns a Vec2, given two points"""
		return Vec2(two[0] - one[0], two[1] - one[1])
	
	def get_magnitude(self):
		return math.sqrt(self.x**2 + self.y**2)

	def normalize(self):
		temp = self.get_magnitude()
		try:
			self.x = self.x / temp
			self.y = self.y / temp
		except ZeroDivisionError:
			self.x = 0
			self.y = 0

	def __add__(self, other):
		return Vec2(self.x + other.x, self.y + other.y)

	def __mul__(self, scalar):
		return Vec2(self.x * scalar, self.y * scalar)

	def __div__(self, scalar):
		return Vec2(self.x / scalar, self.y / scalar)

	def __sub__(self, other):
		return Vec2(self.x - other.x, self.y - other.y)

	def __neg__(self):
		return Vector2(-self.x, -self.y)

	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)


	def __getitem__(self, index):
		if index == 1:
			return self.y
		elif index == 0:
			return self.x
		else:
			raise IndexError, "Index must be 0 or 1"

