from django.contrib import admin
from main import models

admin.site.register([
		models.Author,
		models.Article
	])

# Register your models here.
