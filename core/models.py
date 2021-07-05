from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
# from django.db.models.signals import pre_save
# from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_like')

    def likeCount(self):
        return self.likes.count()

    def __str__(self) -> str:
        return self.title

    def trimLength(self):
        return self.body[:20] + '...'






# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug == None:
#         new_slug = slug

#     qs = Blog.objects.filter(slug=slug).order_by("-id")
#     qs_exists = qs.exists();
#     if qs_exists:
#         new_slug = "%s-%s" %(slug, qs.first.id())
#         return create_slug(instance, new_slug)
#     return slug


# def pre_save_blog_reciever(sender, instance, args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)

# def pre_save_blog(sender, instance, args, **kwargs):
#     slug = slugify(instance.title)
#     instance.slug = slug


# pre_save.connect(pre_save_blog, sender=Blog)
    
    