from pymongo import MongoClient, ASCENDING, DESCENDING
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from bson.errors import InvalidId
from sys import maxsize
from datetime import datetime
from os import environ
from pymongo.server_api import ServerApi


def get_connection():
    conection_string_to = ""
    base = ""
    with open('data/data.csv', "r") as fp:
        for m, line in enumerate(fp):
            if m == 0:
                x = line.split(';')
                conection_string_to = x[1]
            if m == 1:
                y = line.split(';')
                base = y[1]
    return conection_string_to, base


def get_meatings(page, movies_per_page):
    meating = db.WEB.find("")
    total_num_movies = meating.count()
    meating = meating.skip(movies_per_page * page) \
        .limit(movies_per_page)

    return meating, total_num_movies


def get_meating():
    try:
        id_test = '63592d93eae1c66c1e1fdb12'
        #id_test = ''
        return db.WEB.find_one({"_id": ObjectId(id_test)})
    except InvalidId:
        return None


def get_stats():
    try:
        id_test = ''
        return db.WEB.find_one({"_id": ObjectId(id_test)})
    except InvalidId:
        return None


def get_proposal():
    try:
        id_test = ''
        return db.WEB.find_one({"_id": ObjectId(id_test)})
    except InvalidId:
        return None

def put_pop():
    try:
        id_test = ''
        return db.WEB.find_one({"_id": ObjectId(id_test)})
    except InvalidId:
        return None

def get_rq():
    try:
        id_test = ''
        return db.WEB.find_one({"_id": ObjectId(id_test)})
    except InvalidId:
        return None


try:
    (conection_string, data_base) = get_connection()
    db = MongoClient(conection_string, server_api=ServerApi('1'))[data_base]
except KeyError:
    raise Exception("You haven't configured your DB_URI!")
