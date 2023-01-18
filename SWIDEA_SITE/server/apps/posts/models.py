from django.db import models

# Create your models here.


class Tool(models.Model):
    name = models.CharField(max_length=64)
    kind = models.CharField(max_length=64)
    content = models.TextField()


class Idea(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey(
        Tool, on_delete=models.SET_NULL, related_name='idea_tool', null=True)

    def is_favorited(self):
        return IdeaStar.objects.filter(idea=self).exists()


class IdeaStar(models.Model):
    idea = models.ForeignKey(
        Idea, on_delete=models.CASCADE, related_name='like_idea')
