#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author : Teguh Chandra Febriawan
email : teguhchandraf@gmail.com
"""


from __future__ import division, print_function, absolute_import


import logging
from pymongo import MongoClient,ASCENDING
from flask import Flask, json, request,jsonify
from src.kumparan_test.dataEmployee import DataEmployee
from flask_cors import CORS

from src.kumparan_test import __version__

__author__ = "teguhcf"
__copyright__ = "teguhcf"
__license__ = "mit"

_logger = logging.getLogger(__name__)

application = Flask(__name__)

cors = CORS(application)


# mlab database
connection = MongoClient('ds011495.mlab.com', 11495)
db = connection['kumparan']
db.authenticate('teguhcf', '123456')

# for database lokal
# client = MongoClient('localhost', 27017)
# db = client.kumparan

@application.route("/api/v1/cluster/getAge", methods=['GET'])
def getClusterAge():
    try:

        dataEmployee = DataEmployee()

        dataName = dataEmployee.getEmployee()

        #
        # for index in dataName:
        #     print(index)

        print("ini class employee cluster age")
        clusterAge = dataEmployee.getEmployeeClusteringAge()
        # print(clusterAge)

        return jsonify(clusterAge)

    except Exception as e:
        # return str(e)
        return jsonify(status='ERROR', message=str(e))

@application.route("/api/v1/cluster/getAllAge", methods=['GET'])
def getClusterAgeAll():
    try:

        dataEmployee = DataEmployee()

        # dataName = dataEmployee.getEmployee()

        #
        # for index in dataName:
        #     print(index)

        print("ini class employee cluster age")
        clusterAge = dataEmployee.getEmployeeClusteringAgeAll()
        # print(clusterAge)

        return jsonify(clusterAge)

    except Exception as e:
        # return str(e)
        return jsonify(status='ERROR', message=str(e))

@application.route("/api/v1/employee/get", methods=['GET'])
def getEmp():
    try:

        dataEmployee = DataEmployee()

        dataName = dataEmployee.getEmployee()

        #
        # for index in dataName:
        #     print(index)

        print("ini class employee cluster age")
        # clusterAge = dataEmployee.getEmployeeClusteringAge()
        # print(clusterAge)

        return jsonify(dataName)

    except Exception as e:
        # return str(e)
        return jsonify(status='ERROR', message=str(e))


if __name__ == "__main__":
    application.run(host='0.0.0.0')

