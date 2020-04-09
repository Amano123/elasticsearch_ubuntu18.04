import elasticsearch
from elasticsearch import Elasticsearch
es = Elasticsearch("elasticsearch") #ここでどのelasticsearchを使うか決める。ローカル環境なら""ここは空白で良い。dockerの場合は""にelasticsearchが入ったコンテナ名をいれる。
print(es.indices.exists(index="aaa"))#esが起動しているか確認。辞書"aaa"が存在しているかをみるコード。
def indexcreate(dic_name):#形式を指定しない時用(es7からは自動で形式を指定してくれるので便利)
    es.indices.create(index=dic_name)
def indexcreate2(dic_name):#検索などにこだわりたい時に形式をしっかり指定する用
    mapping = {
            "mappings": {
                "my_type": {
                    "propertyies": {
                        "id": {
                            "type": "integer"
                            },
                        "title": {
                            "type": "text",
                            "analyzer": "kuromoji"
                            },
                        "text": {
                            "type": "text",
                            "analyzer": "kuromoji"
                            }
                        }
                    }
                }
            }
    es.indices.create(index=dic_name, body = mapping)
def indexdelete(dic_name):#辞書削除する
    es.indices.delete(dic_name)
def put_data(dic_name,num,title,doc):#indexに要素を挿入する
    es.index(index=dic_name,id=num,body={"title":title,"text":doc})
def searcher(dic_name,key):#検索ただし、上位１０項目がTF-IDFによって選出される。全部出力する際はまた次回
    result = es.search(
            index=dic_name,
            body = {"query": {"match": {"title": key}}})
    hits =result["hits"]
    print('ヒット数 : %s' % hits['total'])
    print('ID : %s' % first_doc['_id'])
    print('タイトル : %s' % first_doc['_source']['title'])
    print('テキスト : %s' % first_doc['_source']['text'])
#indexcreate("aaa")