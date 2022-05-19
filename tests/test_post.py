import unittest
from models import Post

class PostTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(1,'Case Study','Finance', 'Sample test case for the program')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))