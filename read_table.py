import pandas
url='https://roote.ekispert.net/ja/timetable/23164/3210'
table=pandas.io.html.read_html(url)
table=table[0]
table=table.drop(0,axis=1)
table.to_csv('hoge.csv',header=None,index=None)
