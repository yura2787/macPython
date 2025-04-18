import requests

url = "https://jpeg.org/images/jpeg-home.jpg"

response = requests.get(url)
#
# with open("yura1.jpeg", mode="wb") as file:
#     content = response.content
#     content += b"23235656 Yura"
#     file.write(content)
#
# with open("spring.jpeg", mode="rb") as f:
#     print(f.read())
# pass
