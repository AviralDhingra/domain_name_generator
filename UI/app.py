from flask import Flask, redirect, render_template, request, session, url_for

from main import *

# keywords = sys.argv

app = Flask(__name__)

# global v
# v = 6 + 1


@app.route('/', methods=['GET', 'POST'])
def index():
    # keywords = 'testing domain dev'
    print(keywords)
    keyw = keywords.split(' ')
    print(keyw)
    print(type(keyw))
    name_wanted_opt = main(keyw)

    if request.method == 'POST':
        req = request.form
        name = req.get('name_chosen')
        domain = req.get('domain')
        redirectLink = godaddy_redirect(name, domain)
        # return render_template("output.html",
        #                        name=name,
        #                        domain=domain,
        #                        link=redirectLink)
        return redirect(redirectLink)

    return render_template("index.html", listOfNames=name_wanted_opt)


# @app.route('/domainSt')


@app.route('/domainStarter', methods=['GET', 'POST'])
def domainStarter():
    if request.method == 'POST':
        req = request.form
        print(req)
        req = dict(req)
        print(req)
        req = req['keyowords']
        print(req)
        global keywords
        keywords = req
        return redirect(url_for('.index', keywords=keywords, code=302))
        # return redirect(domainGenerator, name_wanted_opt=name_wanted_opt)

    return render_template("domainStarter.html")


@app.route('/domainGenerator', methods=['GET', 'POST'])
def domainGenerator():
    # request.method = 'GET /domainGenerator'
    # name_wanted_opt = session
    # print(name_wanted_opt)
    # name_wanted_opt = session['name_wanted_opt']
    keywords = request.args['keywords']
    print(keywords)
    name_wanted_opt = main(keywords)
    if request.method == 'POST':
        req = request.form
        req = dict(req)
        print(req)
        name = req['name_chosen']
        print(name)
        domain = req['domain']
        print(domain)

        redirectLink = godaddy_redirect(name, domain)
        return render_template("output.html",
                               name=name,
                               domain=domain,
                               link=redirectLink)
    return render_template("domainGenerator.html", listOfNames=name_wanted_opt)


@app.route("/sign-up", methods=["GET", "POST"])  ## To understand forms and GET
def sign_up():
    if request.method == "POST":  ## To Get Information From A Form
        req = request.form
        print(req)
        print(type(req))
        # username = req.get("username")
        email = req["email"]
        password = request.form["password"]
        return render_template(
            "sign_up_conn.html",
            full_dict_form=req,
            # username=username,
            email=email,
            password=password
        )  ## 'info=req' to give variables.info to the html page
        # return redirect(request.url)
    return render_template("sign_up.html")


if __name__ == '__main__':
    app.run(debug=True)
