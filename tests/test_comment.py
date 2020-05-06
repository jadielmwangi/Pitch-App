from app.models import Comment,User
from app import db
import unittest

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_Moringa = User(username = 'Moringa',password = 'church', email = 'jedielmwangigmail.com')
        self.new_comment = Comment(pitch_id=1111,pitch_title=' pitch review',image_path="",pitch_review='pitch review',user = self.user_Moringa) 

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_id,1111)
        self.assertEquals(self.new_comment.pitch_title,'pitch review')
        self.assertEquals(self.new_comment.image_path,"")
        self.assertEquals(self.new_comment.pitch_comment,'nice one')
        self.assertEquals(self.new_comment.user,self.user_Moringa) 

    def test_save_comment(self): 
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)