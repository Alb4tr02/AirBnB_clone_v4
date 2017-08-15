#!/usr/bin/python3
"""
Place Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, MetaData, Table, ForeignKey
from sqlalchemy.orm import backref

if os.environ.get('HBNB_TYPE_STORAGE') == "db":
    class PlaceAmenity(BaseModel, Base):
       """ PlaceAmenity Class """
       __tablename__ = 'place_amenity'
       metadata = Base.metadata
       place_id = Column(String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
       amenity_id = Column(String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)

#PlaceAmenity = Table('place_amenity', metadata,
#                      Column('place_id', String(60), ForeignKey('places.id'), nullable=False), 
#                      Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)
#                  )

class Place(BaseModel, Base):
    """Place class handles all application places"""
    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
       __tablename__ = 'places'
       city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
       user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
       name = Column(String(128), nullable=False)
       description = Column(String(1024), nullable=True)
       number_rooms = Column(Integer, nullable=False, default=0)
       number_bathrooms = Column(Integer, nullable=False, default=0)
       max_guest = Column(Integer, nullable=False, default=0)
       price_by_night = Column(Integer, nullable=False, default=0)
       latitude = Column(Float, nullable=True)
       longitude = Column(Float, nullable=True)

       amenities = relationship('Amenity', secondary="place_amenity", viewonly=False)
       reviews = relationship('Review', backref='place', cascade='delete')
    else:
       city_id = ''
       user_id = ''
       name = ''
       description = ''
       number_rooms = 0
       number_bathrooms = 0
       max_guest = 0
       price_by_night = 0
       latitude = 0.0
       longitude = 0.0
       amenity_ids = ['', '']

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)
