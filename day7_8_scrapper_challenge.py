from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        result = []
        companies = soup.find_all('td', class_='company')
        companies.pop(0)
        for company in companies:
            anchor = company.find('a', class_='preventLink')
            link = anchor['href']
            title = anchor.find('h2')
            companyString = company.find('h3').string.strip()
            location, income = company.find_all('div', class_='location')

            job_result = {
                'link': f"https://remoteok.com{link}",
                'title': title.string.strip(),
                'company': companyString,
                'location': location.string,
                'income': income.string
            }
            result.append(job_result)
        print(result)
    else:
        print("Can't get jobs.")

extract_jobs("rust")