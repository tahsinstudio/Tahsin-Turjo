import requests

API = "https://api.npoint.io/88c2c1f644ef334058be"
posts = requests.get(API).json()
post_objects = []
print(posts)
for post in posts:
    post_obj = (post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

print(post_objects)
