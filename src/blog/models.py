from django.db import models
from pgvector.django import VectorField

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_LENGTH = 1536


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    embedding = VectorField(dimensions=EMBEDDING_LENGTH, blank=True, null=True)