import requests
from bs4 import BeautifulSoup

def replace_comma(string):
    if string != None:
        return string.replace(",", " ")
    return string

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="

    response = requests.get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("Can't request website")
    else:
        # print(response.text)
        results = []
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
                    'company': replace_comma(company.string),
                    'kind': replace_comma(kind.string),
                    'location': replace_comma(region.string),
                    'title': replace_comma(title.string),
                    'link': f"https://weworkremotely.com/{link}"
                }
                results.append(job_data)

        return results
