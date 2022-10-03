import requests
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = requests.get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request website")
else:
    # print(response.text)
    result = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_='jobs')
    for job_section in jobs:
        jobs_posts = job_section.find_all('li')
        jobs_posts.pop(-1)
        for post in jobs_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']

            # js 의 구조 분해 할당처럼 사용함
            company, kind, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')
            # print(company, kind, region, title)
            job_data = {
                'company': company.string,
                'kind': kind.string,
                'region': region.string,
                'title': title.string,
                'link': f"https://weworkremotely.com/{link}"
            }
            result.append(job_data)

print(result)


# keyword argument
def say_hello(name, age):
    print(f"Hello {name} you are {age} years old")


say_hello(name="nico", age=12)
say_hello(age=12, name="nico")


# 구조 분해 할당
list_of_numbers = [1, 2, 3]
first, second, third = list_of_numbers
print(first, second, third)
