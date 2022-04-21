from flask import Flask, render_template
from data import test_posts
from data import test_profiles
app = Flask(__name__)

@app.route("/")
def feed():

    return render_template('feed.html', posts=test_posts, title="My Feed")

@app.route("/comments/<int:post_id>")
def comments(post_id):
    post = test_posts[post_id]
    return render_template('comments.html', title="Comments", post=post)

@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    profile = test_profiles[profile_id]
    return render_template('profile.html', title="Profile", profile=profile)