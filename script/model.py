class Model:
	def __init__(self):
		self.next_value = 0
		self.sequence = []

	def solver(self, seq):
		# Check the type of sequence => should be list of integer.
		if type(seq) != list:
			raise ValueError("A sequence's type should be list")
		if not all(isinstance(n, int) for n in seq):
			raise ValueError("The element of sequence should be integer type")

		# Simple sum algo for test
		sum = 0
		for i in seq:
			sum += i

		# save result to next_value
		self.next_value = sum

		return self.next_value