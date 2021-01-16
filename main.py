from flask import Flask, render_template
import requests
API_URL = "https://api.npoint.io/5abcca6f4e39b4955965"

app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get(API_URL).json()
    print(posts)
    return render_template("index.html", posts=posts)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    posts = requests.get(API_URL).json()
    print(posts)
    for post in posts:
        if post["id"] == blog_id:
            post_title = post["title"]
            post_body = post["body"]
    return render_template("post.html", post_title=post_title, post_body=post_body)

if __name__ == "__main__":
    app.run(debug=True)
