from datetime import time
from datetime import datetime
from pony.orm import *
from settings import DATABASE_NAME, DATABASE_PASS, DATABASE_USER

db = Database("postgres",
              host="localhost",
              user=DATABASE_USER,
              password=DATABASE_PASS,
              database=DATABASE_NAME)


class Badge(db.Entity):
    _table_ = "badges"
    id = PrimaryKey(int, auto=True)
    userid = Required(int)
    name = Required(str)
    date = Required(time)


class Post(db.Entity):
    _table_ = "posts"
    id = Required(int)
    posttypeid = Required(int)
    acceptedanswerid = Optional(int)
    parentid = Optional(int)
    creationdate = Required(datetime)
    score = Optional(int)
    viewcount = Optional(int)
    body = Optional(str)
    owneruserid = Optional(int)
    lasteditoruserid = Optional(int)
    lasteditordisplayname = Optional(str)
    lasteditdate = Optional(datetime)
    lastactivitydate = Optional(datetime)
    title = Optional(str)
    tags = Optional(str)
    answercount = Optional(int)
    favoritecount = Optional(int)
    closeddate = Optional(datetime)
    communityowneddate = Optional(datetime)
    PrimaryKey(id, posttypeid)


class Tag(db.Entity):
    _table_ = "tags"
    id = PrimaryKey(int, auto=True)
    tagname = Required(str)
    count = Optional(int)
    excerptpostid = Optional(int)
    wikipostid = Optional(int)


class User(db.Entity):
    _table_ = "users"
    id = PrimaryKey(int, auto=True)
    reputation = Required(int)
    creationdate = Required(datetime)
    displayname = Required(str)
    lastaccessdate = Optional(datetime)
    websiteurl = Optional(str)
    location = Optional(str)
    aboutme = Optional(str)
    views = Required(int)
    upvotes = Required(int)
    downvotes = Required(int)
    profileimageurl = Optional(str)
    age = Optional(int)
    accountid = Optional(int)


class Vote(db.Entity):
    _table_ = "votes"
    id = PrimaryKey(int, auto=True)
    postid = Required(int)
    votetypeid = Required(int)
    userid = Optional(int)
    creationdate = Required(datetime)
    bountyamount = Optional(int)


sql_debug(False)
db.generate_mapping()

@db_session
def main():
    entries = select(e for e in Tag)
    for e in entries:
        print(e.tagname)

if __name__ == '__main__':
    main()
