class Facebook():
	def __init__(self,list_of_users):
		self.list_of_users = list_of_users

	def add_user(self,user):
		self.list_of_users.append(user)

	def remove_user(self,user):
		self.list_of_users.remove(user)

	def find_user(self,user):
		if user in self.list_of_users:
			return user
		else:
			return None

	def send_personal_info_to_companies(self):
		out = {}
		for user in self.list_of_users:
			out[user] = user.post
		return out

class User():
	def __init__(self,name,age,gender,hometown,state):
		self.name = name
		self.age = age
		self.gender = gender
		self.hometown = hometown
		self.state = state
		self.friends = []
		self.wall = []

	def make_friend(self,friend):
		self.friends.append(friend)

	def unfriend(self,friend):
		self.friends.remove(friend)

	def add_post(self,post):
		self.wall.append(post)

	def tag_friend(self, post,friend):
		if friend in self.friends:
			post.tags.append(friend)
			friend.wall.append(post)

	def like(self,post,friend):
		if friend in self.friends:
			post.likes.append(friend)

	def look_at_friends_wall(self,friend):
		if friend in self.friends:
			return friend.wall


class Post():
	def __init__(self,post_type,post_text):
		self.post_type = post_type
		self.post_text = post_text
		self.tags = []
		self.likes = []
