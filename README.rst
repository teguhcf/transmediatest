=============
kumparan_test
=============

This project created by Teguh Chandra Febrawan
if any question please email teguhchandraf@gmail.com



Description
===========

A longer description of your project goes here...

This project has deployed in heroku

this is list of API
No	API	Methode	Keterangan
1.	http://kumparanrestapi.herokuapp.com/api/v1/topic/add	POST	Untuk save data topic
2.	http://kumparanrestapi.herokuapp.com/api/v1/topic/get?id=”news_id”	GET	Untuk mengambil data topik berdasarkan id_topik
3	http://kumparanrestapi.herokuapp.com/api/v1/topic/getlist	GET	Untuk Mengambil semua data topik
4	http://localhost:5000/api/v1/topic/update	PUT	Untuk update topik berdasarkan id topik
5	http://kumparanrestapi.herokuapp.com/api/v1/topic/delete?id=news_id	DELETE	Untuk delete topik berdasarkan id topik
6	http://localhost:5000/api/v1/news/add	POST	Untuk save data news
7	http://kumparanrestapi.herokuapp.com/api/v1/news/get?id=id	GET	Untuk mengambil News berdasarkan id news
8	http://localhost:5000/api/v1/news/getlist	GET	Untuk mengambil semua data news
9	http://kumparanrestapi.herokuapp.com/api/v1/news/getlist?status=status	GET	Untuk filter data News berdasarkan status
10	http://localhost:5000/api/v1/news/getlist?topic_id=topic_id	GET	Untuk filter data news berdasarkan id topik
11	http://kumparanrestapi.herokuapp.com/api/v1/news/getlist?from=yyyy-mm-dd&to=yyyy-mm-dd	GET	Untuk filter data news berdasarkan rentang tanggal posting.
12	http://localhost:5000/api/v1/news/update	PUT	Untuk update data berdasarkan id news
13	http://kumparanrestapi.herokuapp.com/api/v1/news/delete?id=5ad21e295a0d451b50f5a97b	DELETE	Untuk delete data berdasarkan id news



Note
====

This project has been set up using PyScaffold 3.0.2. For details and usage
information on PyScaffold see http://pyscaffold.org/.
