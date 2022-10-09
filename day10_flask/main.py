from extractors.wwr import extract_wwr_jobs
from file import save_to_file
#
# keyword = 'python'
# jobs = extract_wwr_jobs(keyword)
# save_to_file(keyword, jobs)

from flask import Flask, render_template, request, redirect, send_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="jihee")

@app.route("/search")
def search():
    keyword = request.args.get('keyword')
    if keyword == "":
        return redirect("/")

    jobs = []
    if keyword in db:
        jobs = db[keyword]
    else:
        if keyword != None:
            jobs = extract_wwr_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")

    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run(port=3001)
