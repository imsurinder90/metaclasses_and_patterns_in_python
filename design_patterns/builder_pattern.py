"""
Builder Pattern: This pattern helps building a product
usign various modules and a builder creates this product.
For example: It can create different types of social media
apps like Instagram, Twitter, Facebook etc.
Steps:
1. Create a Product class with its basic features
2. Create a Company class which delegates tasks for
building app to builder
3. Create a Builder metaclass which will be overriden
to make TwitterBuilder, InstagramBuilder with their
respective features(methods)
4. Create different features/modules class for each
product.
5. Call Company class and pass on builder object to
create a social media app
References: https://gist.github.com/pazdera/1121157
https://gist.github.com/atsuya046/8500672
"""

from abc import ABC, abstractmethod

class Company:
	def set_builder(self, builder):
		self._builder = builder

	def get_social_media(self):
		sm = SocialMedia(self._builder.name)
		sm.add_msg(self._builder.get_msg_btn())
		sm.add_post(self._builder.get_post_btn())
		sm.add_share(self._builder.get_share_btn())
		sm.add_retweet(self._builder.get_retweet_btn())
		return sm


class SocialMedia:
	def __init__(self, name):
		self.__name = name
		self.__post = None
		self.__retweet = None
		self.__share = None
		self.__like = None
		self.__msg = None

	def add_post(self, post):
		self.__post = post

	def add_retweet(self, retweet):
		self.__retweet = retweet

	def add_share(self, share):
		self.__share = share

	def add_like(self, like):
		self.__like = like

	def add_msg(self, msg):
		self.__msg = msg

	def __str__(self):
		msg ="%s with following features:" % self.__name
		if self.__post:
			msg +="\nPost with maximum chars: %d" % self.__post.max_len
		if self.__retweet:
			msg +="\nMax retweets: %d" % self.__retweet.max_retweet
		if self.__share:
			msg +="\n%s" % ("Allow Share with friends" if self.__share.friends_only else "Share not allowed")
		if self.__like:
			msg +="\nLikes with limit: %d" % self.__like.max_likes
		if self.__msg:
			msg +="\nMessage with char limit: %d" % self.__msg.max_chars
		return msg

################### Features/Modules of Product ####################
class Retweet:
	max_retweet = 0

class Post:
	max_len = None

class Share:
	friends_only = None

class Like:
	max_likes = None

class Message:
	max_chars = None

################### Builder Abstract Class ####################
class Builder(ABC):

	def get_post_btn(self):
		pass

	def get_like_btn(self):
		pass

	def get_msg_btn(self):
		pass


class TwitterBuilder(Builder):
	name = "Twitter"

	def get_retweet_btn(self):
		retweet = Retweet()
		retweet.max_retweet = 10
		return retweet

	def get_post_btn(self):
		post = Post()
		post.max_len = 1000
		return post

	def get_msg_btn(self):
		msg = Message()
		msg.max_chars = 300
		return msg

	def get_share_btn(self):
		share = Share()
		share.friends_only = True
		return share

class InstagramBuilder(Builder):
	name = "Instagram"

	def get_like_btn(self):
		like = Like()
		like.max_likes = 20
		return retweet

	def get_share_btn(self):
		share = Share()
		share.friends_only = True
		return post

	def get_msg_btn(self):
		msg = Message()
		msg.max_chars = 300
		return msg

def main():
	"""
	>>> twitter_builder = TwitterBuilder()
	>>> company = Company()
	>>> company.set_builder(twitter_builder)
	>>> social_media = company.get_social_media()
	>>> print(social_media)
	Twitter with following features:
	Post with maximum chars: 1000
	Max retweets: 10
	Allow Share with friends
	Message with char limit: 300
	"""

if __name__ == '__main__':
	import doctest
	doctest.testmod()