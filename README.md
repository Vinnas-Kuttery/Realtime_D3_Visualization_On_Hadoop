# Real-time-Visualization-On-Hadoop-using-D3
In this project, I have build two simple and interactive wordcloud visualization from both Hbase and Hive tables.
You can always customize the visualization as per your requirements without effecting the architecture.

# platform Requirements
1. Operating System   : Linux CentOS 6
2. Hadoop Version     : HDP2 or Above
3. Hadoop Components  : Hive, Phoenix, Hbase
4. Software/Languages : Python

# Pre Requisites
1. install all the python packages listed in the requirements.txt fil
 or
 install it by running the command 'pip install -r /requirements.txt'
2. Make sure the table 'imdb_data ' is created in both of Hive and HBase(Phoenix) databases using the source data.


# How to run the application?
1. clone or download the project.<br/> curl -L -o Visualization.zip https://github.com/Vinnas-Kuttery/Realtime_D3_Visualization_On_Hadoop/zipball/master/
2. Extract the visualization <br/> unzip Visualization.zip<br/>
3. goto 'Visualization' Directory
4. Extract and keep the given static.rar file in the same working directory (in order to avoid the upload complexity, I have just compressed and uploaded.)
3. run app.py file <br/> python app.py

# How to access the viz? <br/> 
once the application is running, you can access the visualizations by replacing server ip in the below links. <br/> 

1. Hbase Visualization - htttp://[your server IP]:5000/HBaseViz
2. Hive Visualization - htttp://[your server IP]:5000/HiveViz

# Recomendation
1. Using Hbase(Phoenix) as data source will give you the best performance.
2. User concurrency for flask can be acheive using gunicorn integration
3. for large scale application, just upgrade flask with Djang, remaining componenets are good enough as per the architecture.

*Note: refer the documentation.pdf for more details
