# Real-time-Visualization-On-Hadoop-using-D3
In this project, I have build two simple and interactive wordcloud visualization from both Hbase and Hive tables.
You can always customize the visualization as per your requirements without effecting the architecture.

# Pre Requisites
1. install all the python packages listed in the requirements.txt fil
 or
 install it by running the command 'pip install -r /requirements.txt'
2. Make sure the table '' is created in both of Hive and HBase(Phoenix) databases using the source data.
3. extract and kepp the give static.rar file in the same working directory (in order to avoid the upload complexity, I just compressed it. it has to be available as a foler in your project.)

# How to run the application?
1. clone or download the project.
2. extract the static.rar file
3. run app.py file : python app.py

# How to access the viz?
once the application is running, you can access the visualizations by replacing server ip in the below links.
#
1. Hbase Visualization - htttp://[your server IP]:5000/HBaseViz
2. Hive Visualization - htttp://[your server IP]:5000/HiveViz

# Recomendation
1. Using Hbase(Phoenix) as data source will give you the best performance.
2. User concurrency for flask can be acheive using gunicorn integration
3. for large scale application, just upgrade flask with Djang, remaining componenets are good enough as per the architecture.

*Note: refer the document.doc for details
