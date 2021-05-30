import requests
import regex
a = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
b = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
A_url = requests.get(a)
pattern = r'http.*html'
match = regex.findall(pattern, A_url.text)
ans = 0
for i in match:
    C_url = requests.get(i)
    if b in C_url.text:
        ans = 1
        break
print('No') if ans == 0 else print('Yes')