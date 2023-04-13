from mongoengine import disconnect

from models import Post, User

if __name__ == '__main__':
    user = User.objects(pk="642e8e26f5a8a8a55b8798f9")
    post = Post.objects(title='MongoEngine Documentation')

    post.update(link_url="https://docs.mongoengine.org/index.html///",
                author=user[0])

    disconnect()
