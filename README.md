# Real-time-Visualization-On-Hadoop-using-D3

# Pre Requisites
Follow the below activities before you run the application,

1.install all the packages listed in the requirements.txt file
  or
  install it by running the command 'pip install -r /requirements.txt'

2.Make sure the table '' is created in both of Hive and HBase(Phoenix) databases using the source data.

3.extract and kepp the give static.rar file in the same working directory (in order to avoid the upload complexity, I just compressed it. it has to be available as a foler in your project.)

# How to run and access the viz?

1. clone or download the project.
2. extract the static.rar file
3. run app.py file
     python app.py
4. access your visualization using the below links,
     Hbase Visualization - htttp://[your server IP]:5000/HBaseViz
     Hive Visualization  - htttp://[your server IP]:5000/HiveViz

# Recomendation
1. Using Hbase(Phoenix) as data source will give you the best performance.
2. User concurrency for flask can be acheive using gunicorn integration
3. for large scale application, just upgrade flask with Djang, remaining componenets are good enough as per the architecture.

*Note: refer the document.doc for details
