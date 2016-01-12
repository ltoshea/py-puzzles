# Write something that makes sure all brackets in a string are balanced.
# e.g. 
# This is a {sentence}
# This is another ({sentence that is unbalance)}
import unittest

def balanced(strinput):
	stack = [];
	brackets = {'{':'}','(':')','[':']','<':'>'}
	reverse = dict((value,key) for key,value in brackets.items())

	for c in strinput:
		if c in brackets:
			stack.append(c)
		elif c in reverse:
			if len(stack) == 0:
				return ('Unbalanced')
			if stack.pop() != reverse.get(c):
				return ('Unbalanced')
	return ('Balanced')


class MyTest(unittest.TestCase):
	def test_balanced(self):
		self.assertEqual(balanced('()[]{}'),'Balanced')
		self.assertEqual(balanced('([{}])'),'Balanced')
		self.assertEqual(balanced('()[{}]'),'Balanced')
		self.assertEqual(balanced(''),'Balanced')
		self.assertEqual(balanced('({)}'),'Unbalanced')
		self.assertEqual(balanced('((())})'),'Unbalanced')


if __name__ == '__main__':
	#balanced('hello ( my ( name) )[]{} is liam')
	unittest.main()



