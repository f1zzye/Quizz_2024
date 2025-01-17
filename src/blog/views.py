from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker

from blog.models import Entry, Blog


def create_blog(request):
    faker = Faker()
    saved = Entry(
        headline=faker.paragraph(nb_sentences=1),
        blog=[Blog(name=faker.word(), text=faker.paragraph(nb_sentences=5), author=faker.name())],
    ).save()
    return HttpResponse(f"Done: {saved}")

def all_blogs(request):
    blog_timestamps = list(Entry.objects().values_list("timestamp"))
    print(blog_timestamps)

    return HttpResponse(f"Done: {blog_timestamps}")
