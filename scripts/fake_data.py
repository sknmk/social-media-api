from blog.api.serializers import PostSerializer
from pprint import pprint
import requests
from faker import Faker
from django.utils.text import slugify
from django.contrib.auth.models import User
import django
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitap_pazari.settings')

django.setup()


def set_user():
   fake = Faker(['en_US'])
   f_name = fake.first_name()
   l_name = fake.last_name()
   u_name = f'{f_name.lower()}_{l_name.lower()}'
   email = f'{u_name}@{fake.domain_name()}'
   print(f_name, l_name, email)

   user_check = User.objects.filter(username=u_name)

   while user_check.exists():
      u_name = u_name + str(random.randrange(1, 99))
      user_check = User.objects.filter(username=u_name)

   user = User(
      username=u_name,
      first_name=f_name,
      last_name=l_name,
      email=email,
      is_staff=fake.boolean(chance_of_getting_true=50),
    )

   user.set_password('123456')
   # user.save()
   print(f'User {u_name} created.')


def create_post(post_title):
   fake = Faker(['en_US'])
   url = 'http://openlibrary.org/search.json'
   payload = {'q': post_title}
   response = requests.get(url, params=payload)

   if response.status_code != 200:
      print('Invalid request.', response.status_code)
      return

   jsn = response.json()

   content = jsn.get('docs')
   for item in content:
      all_authors = list(User.objects.all())
      random_author = random.choice(all_authors)
      data = dict(
            title=item.get('title'),
            slug=slugify(item.get('title')),
            text='-'.join(item.get('text'))
        )
      serializer = PostSerializer(data=data)
      if serializer.is_valid():
         serializer.save(author=random_author)
         print('Post created.')
      else:
         print(serializer.errors)
         continue

