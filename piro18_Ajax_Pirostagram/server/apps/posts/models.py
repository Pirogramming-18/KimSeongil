from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    photo = models.ImageField(blank=True, upload_to='users/%Y%m%d')


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_user')
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')

    def is_favorited(self):
        return Like.objects.filter(post=self).exists()


class Comment(models.Model):
    user = models.CharField(max_length=32)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment_post')
    content = models.TextField()


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='like_post')
