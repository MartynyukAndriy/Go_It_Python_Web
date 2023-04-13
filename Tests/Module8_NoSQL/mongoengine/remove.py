from mongoengine import disconnect

from models import Post

if __name__ == '__main__':
    post = Post.objects(title="Fun with MongoEngine")
    post.delete()

    disconnect()
