
![f55e8059ea945abfd6804b887dd4a0af](https://user-images.githubusercontent.com/39152214/76674089-fb3e3000-65ee-11ea-9f52-f9efc5f6d89a.gif)

# <center>Docker + Ubuntu18.04 + Elasticsearch</center>
勉強会の準備として、Ubuntu18.04 + Elasticsearchの環境をdocker-composeを使って構築した

## ファイル構成
各サービスをわかりやすく管理するために、フォルダーを分けている。  
volumeをどの様に管理するかは後々考えて行こうと思う
```
.
├── Elasticsearch
│   └── dockerfile
├── README.md
├── Ubuntu18.04
│   └── dockerfile
├── docker-compose.yml
└── es-data
```

## 環境
docker version
```bash 
>docker -v
Docker version 19.03.5, build 633a0ea
```
docker-compose version

```bash 
>docker-compose -v 
docker-compose version 1.24.1, build 4667896b
```

## 使い方
まず、ダウンロード
```bash 
git clone https://github.com/Amano123/elasticsearch_ubuntu18.04.git
```

ダウンロードしたフォルダに入ってから
ビルドをする

```bash 
docker-compose build
```

コンテナを起動する

```bash 
docker-compose up -d
```

```bash 
Creating network "docker_es_default" with the default driver
Creating ubuntu18.04   ... done
Creating elasticsearch ... done
```
このログが出たらOK

環境を合わせるためにubuntuを入れているので  
ubuntuの中に入る
```bash 
docker exec -it ubuntu18.04 zsh
```

中に入れたら、pingでelasticsearchを探す

```bash 
ping elasticsearch
```

```log
PING elasticsearch (172.18.0.3) 56(84) bytes of data.
64 bytes from elasticsearch.docker_es_default (172.18.0.3): icmp_seq=1 ttl=64 time=0.702 ms
64 bytes from elasticsearch.docker_es_default (172.18.0.3): icmp_seq=2 ttl=64 time=0.097 ms
64 bytes from elasticsearch.docker_es_default (172.18.0.3): icmp_seq=3 ttl=64 time=0.098 ms
^C
--- elasticsearch ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2007ms
rtt min/avg/max/mdev = 0.097/0.299/0.702/0.284 ms
```
こんな感じで帰ってくればOK

ipアドレスで指定しなくてもコンテナ名で指定できるので楽ちん

## 動作確認
elasticsearchをpythonから使ってみようと思う。

```python
from elasticsearch import Elasticsearch
# hostnameはelasticsearchなのでipアドレスではなくホスト名を指定
es = Elasticsearch("elasticsearch")
# Falseが帰ってくればOK
print(es.indices.exists(index="aa"))
```

以上をvimで作成（今回は[ test.py ]とする）

```bash
python3 test.py
```
で実行する。Falseが帰ってくれば成功しているはず。