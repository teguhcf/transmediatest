
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
from pymongo import MongoClient,DESCENDING,ASCENDING
from bson.objectid import ObjectId
from flask import Response

from bson.json_util import dumps
import datetime

# mlab database
connection = MongoClient('ds011495.mlab.com', 11495)
db = connection['kumparan']
db.authenticate('teguhcf', '123456')

# for database lokal
# client = MongoClient('localhost', 27017)
# db = client.kumparan

class Model:

    def mongo_to_jsonResponse(self,mongobj):
        # dumps function convert mongo object into json
        js = dumps(mongobj)
        resp = Response(js, status=200, mimetype='application/json')
        return resp

    def str_to_date(self,stringDate):
        from datetime import datetime
        date = datetime.strptime(stringDate,'%Y-%m-%d')
        return date


    def addNews(self,json_data):
        title = json_data['title']
        content = json_data['content']
        topic_id = json_data['topic_id']
        status = json_data['status']
        user_id = json_data['user_id']
        files_name = json_data['files_name']
        loves_count = 0;
        shared_count =0;
        comments = [];
        created_at = datetime.datetime.utcnow()
        last_modified= datetime.datetime.utcnow()

        db.news.insert_one({
            'title': title, 'content': content, 'topic_id': topic_id, 'status': status,
            'user_id': user_id, 'created_at': created_at, 'last_modified':last_modified,
            'files_name': files_name, 'loves_count': loves_count, 'shared_count': shared_count, 'comments': comments
        })


    def getNewsList(self,status,topic_id,str_from_date, str_to_date):
        if (str_from_date is not  None and str_from_date is not  None):
            from_date = self.str_to_date(str_from_date)
            to_date = self.str_to_date(str_to_date)
            print("ini from date", from_date,to_date)
            data = db.news.find({"created_at": {'$gte': from_date, '$lte': to_date}}).sort([("created_at", DESCENDING)])
            # ret = db.find({'datePeriod': {'$gte': dateStrFrom, '$lte': dateStrTo}})

        elif (status is not None):
            data = db.news.find({"status": status}).sort([("created_at", DESCENDING)])
        elif topic_id is not None:
            data = db.news.find({"topic_id": {"$in": [int(topic_id)]}}).sort([("created_at", DESCENDING)])
        else:
            data = db.news.find().sort([("created_at", DESCENDING)])

        news_list = []
        for news in data:
            topic_detail = db.topic.find({"topic_id": {"$in": news['topic_id']}})
            topicList = []
            for topic in topic_detail:
                topicItem = {
                    'topic_id': topic['topic_id'],
                    'topic': topic['topic'],
                    # 'news': machine['news']
                    'topic_desc': topic['topic_desc']
                }
                topicList.append(topicItem)

            newsItem = {
                'id': str(news['_id']),
                'title': news['title'],
                'content': news['content'],
                # 'topic_id': news['topic_id'],
                'topic_detail': topicList,
                'status': news['status'],
                'user_id': news['user_id'],
                'created_at': news['created_at'],
                'last_modified': news['last_modified'],
                'files_name': news['files_name'],
                'loves_count': news['loves_count'],
                'shared_count': news['shared_count'],
                'comments': news['comments']
            }
            news_list.append(newsItem)

        return news_list


    def getNews(self,news_id):
        news_data = db.news.find_one({'_id': ObjectId(news_id)})
        topic_detail = db.topic.find({"topic_id": {"$in": news_data['topic_id']}})
        topicList = []
        for topic in topic_detail:
            topicItem = {
                'topic_id': topic['topic_id'],
                'topic': topic['topic'],
                # 'news': topic['news']
                'topic_desc': topic['topic_desc']
            }
            topicList.append(topicItem)
        news = {
            'id': str(news_data['_id']),
            'title': news_data['title'],
            'content': news_data['content'],
            # 'topic_id': news_data['topic_id'],
            'topic_detail': topicList,
            'status': news_data['status'],
            'user_id': news_data['user_id'],
            'created_at': news_data['created_at'],
            'last_modified': news_data['last_modified'],
            'files_name': news_data['files_name'],
            'loves_count': news_data['loves_count'],
            'shared_count': news_data['shared_count'],
            'comments': news_data['comments']
        }
        return news


    def updateNews(self,json_data):
        news_id = json_data['news_id']
        # title = json_data['title']
        # content = json_data['content']
        # topic_id = json_data['topic_id']
        # status = json_data['status']
        # user_id = json_data['user_id']
        # files_name = json_data['files_name']
        # loves_count = json_data['loves_count'];
        # shared_count =json_data['shared_count'];
        # comments = json_data['files_name'];
        # last_modified = datetime.datetime.utcnow()

        res = db.news.find_one({'_id': ObjectId(news_id)})
        if res is None: return False

        # db.news.update_one({'_id': ObjectId(news_id)},
        #                    {'$set': {'title': title, 'content': content, 'topic_id': topic_id, 'status': status,
        #                              'user_id': user_id, 'last_modified': last_modified,'files_name': files_name,
        #                              'loves_count': loves_count, 'shared_count': shared_count, 'comments': comments
        #                              }})

        db.news.update_one({'_id': ObjectId(news_id)},
                           {'$set': json_data})

        return True

    def updateTopic(self,json_data):
        topic_id = json_data['topic_id']
        topic = json_data['topic']
        # news_id = json_data['news']
        topic_desc = json_data['topic_desc']
        res = db.topic.find_one({'topic_id': topic_id})
        if res is None: return False

        db.topic.update_one({'topic_id': topic_id},
                            {'$set': {'topic': topic, 'topic_desc': topic_desc
                                      }})
        return True

    def addTopic(self,json_data):
        topic_id = int(json_data['topic_id'])
        topic = json_data['topic']
        topic_desc = json_data['topic_desc']
        db.topic.insert_one({'topic_id': topic_id, 'topic': topic, 'topic_desc': topic_desc
        })


    def getTopicList(self):
        topics = db.topic.find().sort([("topic_id", ASCENDING)])

        topic_list = []
        for topic in topics:
            topicItem = {
            'topic_id': topic['topic_id'],
            'topic': topic['topic'],
            'topic_desc': topic['topic_desc'],

            }
            print("topicitem", topicItem)
            topic_list.append(topicItem)
        return  topic_list


    def getTopic(self,id):
        data = db.topic.find_one({'topic_id': int(id)})
        topic = {
            'topic_id': data['topic_id'],
            'topic': data['topic'],
            'topic_desc': data['topic_desc'],

        }
        return topic