from flask import Flask, request, render_template
import requests
import smtplib

app = Flask(__name__)

my_email = "test.mail.3618@gmail.com"
password = "Aladin1845"

API = "https://api.npoint.io/88c2c1f644ef334058be"
posts = requests.get(API).json()

@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact.html", methods=["GET", "POST"])
def recieve_data():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="trturjo60@gmail.com",
                                msg=f"Subject:Contact Me Response\n\nName: {name}\nEmail: {email}\n"
                                    f"Phone {phone}\nMessage: {message}"
                                )
        return render_template("contact.html", method="post")

if __name__ == "__main__":
    app.run(debug=True)
