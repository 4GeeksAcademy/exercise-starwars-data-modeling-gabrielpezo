import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)

class Favourites(Base):
    __tablename__ = "favourites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    favourite_pokemon = relationship("Pokemon")

class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(String(100), unique=False, nullable=False)
    second_type = Column(String(100), unique=False, nullable=True) 
    height = Column(String(100), unique=False, nullable=False)
    weight = Column(String(100), unique=False, nullable=False)
    primary_ability = Column(String(100), unique=False, nullable=False)
    secondary_ability = Column(String(100), unique=False, nullable=True)
    hidden_ability = Column(String(100), unique=False, nullable=True)

class Region(Base):
    __tablename__ = "region"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    number_of_cities = Column(String(10), unique=False, nullable=False)
    professor = Column(String(100), unique=True, nullable=False)
    initials_id = Column(Integer, ForeignKey('pokemon.id'))
    initials = relationship(Pokemon)
    capital_id = Column(Integer, ForeignKey('cities.id'))
    capital = relationship("Region")
 
class Cities(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    gym_leader = Column(String(100), unique=True, nullable=False)
    city_region_id = Column(Integer, ForeignKey('region.id'))
    city_region = relationship(Region)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
