#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
from pymongo import MongoClient,ASCENDING
from bson.objectid import ObjectId
from flask import Flask, json, request,jsonify

from kumparan_test.model import Model


from src.kumparan_test import __version__

__author__ = "teguhcf"
__copyright__ = "teguhcf"
__license__ = "mit"

_logger = logging.getLogger(__name__)



application = Flask(__name__)


# mlab database
connection = MongoClient('ds011495.mlab.com', 11495)
db = connection['kumparan']
db.authenticate('teguhcf', '123456')

# for database lokal
# client = MongoClient('localhost', 27017)
# db = client.kumparan


model = Model()

@application.route("/api/v1/news/add", methods=['POST'])
def addNews():
    try:
        json_data = request.json['data']
        model.addNews(json_data)
        return jsonify(status='OK', message=' News inserted successfully')

    except Exception as e:
        return jsonify(status='ERROR', message="Field "+ str(e) + " not exist")


@application.route("/api/v1/news/getlist", methods=['GET'])
def getNewsList():
    try:
        status = request.args.get('status')
        topic_id = request.args.get('topic_id')
        from_date = request.args.get('from')
        to_date = request.args.get('to')
        data = model.getNewsList(status,topic_id,from_date,to_date)

    except Exception as e:
        return str(e)
    return json.dumps(data)
    # return mongo_to_jsonResponse(machines)


@application.route('/api/v1/news/get', methods=['GET'])
def getNews():
    try:
        id = request.args.get('id')
        data = model.getNews(id)
        return json.dumps(data)
        # return mongo_to_jsonResponse(machine)
    except Exception as e:
        return str(e)


@application.route("/api/v1/news/delete", methods=['DELETE'])
def deleteNews():
    try:
        id = request.args.get('id')
        res = db.news.find_one({'_id': ObjectId(id)})
        if res is None: return jsonify(status='ERROR', message="Data not exist")

        db.news.remove({'_id': ObjectId(id)})
        return jsonify(status='OK', message='deletion successful')
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))



@application.route('/api/v1/news/update', methods=['PUT'])
def updateNews():
    try:

        json_data = request.json['data']
        res = model.updateNews(json_data)
        if res is False: return jsonify(status='ERROR', message="Data not exist")
        return jsonify(status='OK', message='updated successfully')
    except Exception as e:
        return jsonify(status='ERROR', message="Field "+ str(e) + " not exist")


@application.route("/api/v1/topic/add", methods=['POST'])
def addTopic():
    try:
        json_data = request.json['data']
        model.addTopic(json_data)
        return jsonify(status='OK', message='Topic inserted successfully')

    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


@application.route('/api/v1/topic/update', methods=['PUT'])
def updateTopic():
    try:
        json_data = request.json['data']
        res = model.updateTopic(json_data)
        if res is False: return jsonify(status='ERROR', message="Data not exist")

        return jsonify(status='OK', message='updated successfully')
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))



@application.route("/api/v1/topic/getlist", methods=['GET'])
def getTopicList():
    try:
        data = model.getTopicList()
    except Exception as e:
        return str(e)
    return json.dumps(data)
    # return model.mongo_to_jsonResponse(topics)


@application.route("/api/v1/topic/get", methods=['GET'])
def getTopic():
    try:
        id = request.args.get('id')
        data= model.getTopic(id)
    except Exception as e:
        return str(e)
    return json.dumps(data)
    # return model.mongo_to_jsonResponse(data)


@application.route("/api/v1/topic/delete", methods=['DELETE'])
def deleteTopic():
    try:
        id = request.args.get('id')
        res = db.topic.find_one({'topic_id': int(id)})
        if res is None: return jsonify(status='ERROR', message="Data not exist")
        db.topic.remove({'topic_id': int(id)})
        return jsonify(status='OK', message='deletion successful')
    except Exception as e:
        return jsonify(status='ERROR', message=str(e))


if __name__ == "__main__":
    application.run(host='0.0.0.0')

