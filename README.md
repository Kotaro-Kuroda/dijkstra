# dijkstra
これは[ダイクストラ法](https://ja.wikipedia.org/wiki/%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95#:~:text=%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95%EF%BC%88%E3%81%A0%E3%81%84%E3%81%8F%E3%81%99%E3%81%A8%E3%82%89,%E3%83%95%E3%82%A9%E3%83%BC%E3%83%89%E6%B3%95%E3%81%AA%E3%81%A9%E3%81%8C%E4%BD%BF%E3%81%88%E3%82%8B%E3%80%82)を用いて、
スタート地点からゴール地点への最短経路を求めるプログラムです。

# how to use
[shortest_path.py](https://github.com/Kotaro-Kuroda/dijkstra/blob/master/shortest_path.py)を実行。
```bash
python shortest_path.py --txt path/to/text/file --start start_node --goal goal_node
```
--txt テキストファイルへのパス。テキストファイルの一行目に頂点数を、二行目以降には 「頂点1, 頂点2, 距離」を記述。\\
--start スタート地点を指定\\
--goal ゴール地点を指定\\
