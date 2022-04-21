from datetime import datetime


comment1 = {
    "text" : "me too!",
    "name" : "Johnny",
    "username" : "johnnydepp",
    "datetime" : datetime(2022, 5, 1, 16, 0, 0),
    "picture": "photo2.jpg"
}

comment2 = {
    "text" : "come here!",
    "name" : "Bob",
    "username" : "bob",
    "datetime" : datetime(2022, 5, 1, 16, 20, 0),
    "picture": "photo1.jpg"
}
comment3 = {
    "text" : "love it!",
    "name" : "Bob",
    "username" : "bob",
    "datetime" : datetime(2022, 5, 1, 16, 30, 0),
    "picture": "photo1.jpg"
}
post1 = {
        "post_id" : 1, 
        "profile_id" : 2,
        "text" : "I need some snacks",
        "name" : "Bob",
        "username" : "bob",
        "likes" : [],
        "comments" : [comment1, comment2],
        "datetime" : datetime(2022, 5, 1, 15, 0, 0),
        "picture": "photo1.jpg"
    }
post2 = {
        "post_id" : 2, 
        "profile_id" : 2,
        "text" : "I love my mommy",
        "name" : "Bob",
        "username" : "bob",
        "likes" : [],
        "comments" : [],
        "datetime" : datetime(2022, 5, 1, 17, 0, 0),
        "picture": "photo1.jpg"
    }

post3 = {
        "post_id" : 3, 
        "profile_id" : 1,
        "text" : "Who wants to join me today?",
        "name" : "Johnny",
        "username" : "johnnydepp",
        "likes" : [],
        "comments" : [comment3],
        "datetime" : datetime(2022, 7, 2, 14, 0, 0),
        "picture": "photo2.jpg"
    }
test_posts = {
    1 : post1,
    2 : post2,
    3 : post3
}

profile1 = {
    "posts" : [post3], 
    "profile_id" : 1,
    "name" : "Johnny",
    "username" : "johnnydepp",
    "picture": "photo2.jpg"
}
profile2 = { 
    "posts" : [post1,post2],
    "profile_id" : 2,
    "name" : "Bob",
    "username" : "bob",
    "picture": "photo1.jpg"
}
test_profiles = {
    1 : profile1,
    2 : profile2
}