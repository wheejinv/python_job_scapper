from requests import get

websites = (
    "facebook.com",
    "https://google.com"
)

for item in websites:
    has = item.startswith("https")
    if has:
        print(f"{item}")
    else:
        print(f"https://{item}")

a = get('http://www.naver.com')
print(a)