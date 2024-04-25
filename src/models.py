import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    profile_name = Column(String(250))
    bio = Column(String(250))
    email = Column(String, nullable=False)

    posts = relationship("Post")
    comments = relationship("Comment")
    followers = relationship("Follower", foreign_keys='Follower.user_to_id')
    following = relationship("Follower", foreign_keys='Follower.user_from_id')

class Media(Base):
    __tablename__ = 'media'
   
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    media_type = Column(String(20), nullable=False)  
    url = Column(String(250), nullable=False)
    
    post = relationship("Post")

class Follower(Base):
    __tablename__ = 'follower'
    
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    

    user = relationship("User")
    post = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    caption = Column(String(2200))
   
    user = relationship("User")
    media = relationship("Media")
    comments = relationship("Comment")

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String(1000), nullable=False)

    user = relationship("User")
    post = relationship("Post")

 
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
  
