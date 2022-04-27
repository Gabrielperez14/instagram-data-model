import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key= True)
    email = Column(String(30), nullable = False, unique= True)
    password = Column(String(15), nullable= False, unique= True)
    name = Column(String(20), nullable= False)
    userName= Column(String(20), nullable= False, unique=True)
    post = relationship("post")
    follow = relationship("follow")
    follower = relationship("follower")

class Follower(Base):
    __tablename__= "follower"
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Follow(Base):
    __tablename__="follow"
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key = True)
    create_date = Column(Date, nullable = False)
    content = Column(String(20), nullable = False)
    comment = relationship("comment")
    like = relationship("like")
    favorite = relationship("favorite")
    user_id= Column(Integer, ForeignKey("user.id"))

class Comment(Base):
    __tablename__="comment"
    id = Column(Integer, primary_key= True)
    comment_content = Column(String(100))
    post_id = Column(Integer, ForeignKey("post.id"))
    

class Like(Base):
    __tablename__= "like"
    id = Column(Integer, primary_key= True)
    post_id = Column(Integer, ForeignKey("post.id"))
    

class Favorite(Base):
    __tablename__= "favorite"
    id = Column(Integer, primary_key= True)
    post_id = Column(Integer, ForeignKey("post.id"))
   



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e