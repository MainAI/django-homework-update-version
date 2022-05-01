from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='Имя тега')
    article = models.ManyToManyField(Article, through='ArticleTag', related_name='article')

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=['article', 'tag'], name='some_unique_name')]
        ordering = ['-is_main', '-tag']

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return '{0}_{1}'.format(self.article, self.tag)




#
