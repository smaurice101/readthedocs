
MAADS-VIPER Environmental Variable Configuration (Viper.env)
=============================================================

**v.5.5.90+**

.. note::

   The setting of these environmental variables are automatically set for you in the TML Solution Studio DAGs.  They are presented here for informational purposes.

   Refer to :ref:`Pre-Written 10 Apache Airflow DAGs To Speed Up TML Solution Builds`

This guide will provide common setup instructions for new users who want to run VIPER in their environment(s). For any questions, users are encouraged to email support@otics.ca .

1. **SETUP Instructions:** [**Watch the YouTube video**](https://youtu.be/b1fuIeC7d-8) **or follow instructions below.**
    A. For actual (non-Demo) use you will need:
        1. ADMIN.tok (available in ZIP for Viper on Github: https://github.com/smaurice101/transactionalmachinelearning)
            1. This allows admin users to create topics, activate/deactivate topics, produce to topics
2. Store all of the above files in the same directory you use to run VIPER
    1. VIPER will automatically create necessary directories in that folder
    2. **Note:** For Linux users File/Folder permissions may need to be adjusted for VIPER 0644 is usually fine
3. Start VIPER
    1. By default, VIPER listens on “Localhost” port=8000
    2. You can easily adjust this to whatever host/port you want by typing: \[Viper Executable\] \[host\] \[port\]
4. On Startup VIPER will check for:
    1. Valid Tokens
    2. VIPER.ENV file

**VIPER.ENV Configurations**

1. **With SSL/TLS enabled**
    1. If you have enabled SSL/TLS on Kafka brokers then you need to specify additional fields in the configuration file – for example purposes .PEM files are added to the configuration keys, but you can specify folder/file names as you wish:
        1. SSL_CLIENT_CERT_FILE=client.cer.pem
        2. SSL_CLIENT_KEY_FILE=client.key.pem
        3. SSL_SERVER_CERT_FILE=server.cer.pem

1. **No SSL/TLS Security:**
    1. Assuming you have Kafka/Zookeeper running on a broker, simply fill in the following information in the configuration file:
        1. KAFKA_ADVERTISED_HOST_NAME=kafka
        2. KAFKA_ZOOKEEPER_CONNECT=
        3. KAFKA_CONNECT_BOOTSTRAP_SERVERS=localhost:9092
    2. With HPDE:
        1. HPDE_SERVER=
        2. HPDE_PORT=
    3. With Confluent Cloud Access (If NOT using Kafka Cloud these MUST be left blank):
        1. CLOUD_USERNAME={API KEY}
        2. CLOUD_PASSWORD={API SECRET}
    
    4.  a. SSL_CLIENT_CERT_FILE=
        b. SSL_CLIENT_KEY_FILE=
        c. SSL_SERVER_CERT_FILE=

**Note:** First time the plain text values need to be entered, on start VIPER will hide these values. You can update them with plain text again if you change the key/secret then simply restart VIPER to hide the updated values again.

.. list-table::
   :widths: 25 25

   * - **Configuration Parameter**
     - **Description**
   * - KAFKA_ADVERTISED_HOST_NAME 
     - Advertised host name in Kafka server properties 
   * - KAFKA_ZOOKEEPER_CONNECT
     - Zookeeper host name and port 
   * - KAFKA_CONNECT_BOOTSTRAP_SERVERS= 
     - Kafka bootstrap servers – separate multiple servers by comma 
   * - MAADS_ALGORITHM_SERVER 
     - MAADS algorithm server host URL. This will require MAADS software installed in the host. 
       |This is needed to generate predictions from algorithms generated 
       |by MAADS.
   * - ONPREM
     - Set to 1, if running VIPER on-premise, or 0 if using Cloud 
   * - VIPERDEBUG 
     - Set to 1, if you want additional screen logging, or 0.<br><br>Set to 2, if you want additional screen **_and_** disk logging. Logs will be written to 
       ./viperlogs/viperlogs.txt\nThis is helpful if you want to see details when building TML solutions. However, for production deployments, VIPERDEBUG 
       should be set to 1 for optimized performance. 
   * - WRITETOVIPERDB 
     - Set to 1, if you want to write Egress and Ingress bytes. Set to 0 if you do not want to write to viper.db. By setting to 0 this will speed up VIPER, but 
       you will not get Egress and Ingress details in AIMS. 
   * - WRITELASTCOMMIT
     - Set to 1 if you want to record the last offset in the partition for each topic, or 0 if not. This is convenient if you do NOT want to RE-PROCESS data that 
       has already been processed. 
   * - NOWINDOWOVERLAP 
     - Set to 1, if you do NOT want sliding time windows to overlap. 
   * - NUMWINDOWSFORDUPLICATECHECK
     - This is an integer to specify how much data to retain to check for duplicates. For example, if NOWINDOWOVERLAP=0, then windows will overlap, but you do not 
       want to re-process data which may result in duplicates, so this field will save data in MySQL and check if the Partition and Offset has already been 
       processed, if so, it will not re-process it. If NUMWINDOWSFORDUPLICATECHECK=5, then the amount of data saved is 5 \*(number of partitions) \* (rollback  
       offset) per topic and cluster. 
   * - COMPRESSIONTYPE
     - You can force the producer to compress data. You can set this to: NONE, SNAPPY, GZIP, LZ4, default is NONE. |
   * - DATARETENTIONINMINUTES
     - Specify how long you want to retain the data in Topics, in minutes. This is based on your data retention policy. For example, if DATARETENTIONINMINUTES=30, 
       committed offsets will be deleted/compacted after 30 minutes. IF DATARETENTIONINMINUTES=0 or empty data is retained forever. 
   * - USEHTTP
     - Set to 1 if using HTTP to connect to VIPER. If SSL_CLIENT_CERT_FILE and SSL_CLIENT_KEY_FILE are specified then VIPER will automatically accept 
       HTTPS connections. However, if USEHTTP=1, then regardless of certificates, HTTP will be used. 
   * - LOGSTREAMTOPIC
     - Enter the name of the topic that you want to write logs to. If this field is non-empty VIPER/HPDE/VIPERVIZ will all write logging 
       information to this stream. 
   * - LOGSENDTOEMAILS
     -  Viper will send log emails to these addresses: separate multiple addresses by comma. 
   * - LOGSENDTOEMAILSSUBJECT
     - You can add a custom subject for the email. 
   * - LOGSENDTOEMAILFOOTER
     - Specify additional text to be included in the footer of your email. 
   * - KUBERNETES
     - If deploying to Kubernetes, set to 1 and VIPER will dynamically get IP address of Pod, and free port. 
   * - MAXVIPERVIZROLLBACKOFFSET
     - Sets the maximum rollback offset in VIPERVIZ. This prevents memory heap issues. 
   * - MAXVIPERVIZCONNECTIONS
     - Total number of simultaneous connections to Viperviz. For example, MAXVIPERVIZCONNECTIONS=5 
   * - SASLMECHANISM
     - Choose SASL mechanism. You can specify: PLAIN, SCRAM256, SCRAM512 
   * - LOGSTREAMTOPICPARTITIONS
     - Enter number of partitions for LOGSTREAMTOPIC, i.e. 3 
   * - LOGSTREAMTOPICREPLICATIONFACTOR
     - Enter replication factor for LOGSTREAMTOPIC, i.e. 3 
   * - LOGSENDINTERVALMINUTES
     - Specify the minutes you want Viper to check the logs – it will email you a list of logs that have been created. This is convenient when you want a batch of 
       logs to see what Viper is doing. 
   * - LOGSENDINTERVALONLYERROR
     - Set to 1 if you only want interval emails to check for ERROR or WARNING. If set to 0, all messages with ERROR, WARN, INFO will be checked, this is useful 
       for debugging. For production set to 1.
   * - MAADS_ALGORITHM_SERVER_PORT
     - MAADS algorithm server host PORT. This will require MAADS software installed in the host. This is needed to generate predictions from algorithms generated 
       by MAADS.
   * - MAXTRAININGROWS
     - Maximum number of rows for training dataset. Higher number will consumer more memory resources. 
   * - MAXOPENREQUESTS
     - How many outstanding requests a connection is allowed to have before<br><br>sending on it blocks (default 5).
   * - MAXPREDICTIONROWS
     - Maximum prediction batch size. 
   * - MINFORECASTACCURACY
     - Minimum forecast accuracy of trained TML model. Choose a number between 0-100, default is 0. A model is selected if it is greater than this value. 
   * - MAXPREPROCESSMESSAGES
     - Number of message for preprocessing. Defaults to 2000. Higher number will consume more energy. |
   * - BATCHTHREADS
     - This is used in batch functions like “viperpreprocessbatch” and indicates how many topicids to preprocess concurrently. For example, if BATCHTHREADS=5, and 
       you are preprocessing 10 topicids in batch, then 5 will be preprocessed concurrently at a time. 
   * - MAXPERCMESSAGES
     - Maximum messages when using Topicid to rollback stream. This is useful when even 1% rollbackback could result in millions of message if your total messages 
       are in the billions. Setting MAXPERCMESSAGES=1000 for example, ensures message are 1000 messages from the last message. 
   * - MAXCONSUMEMESSAGES
     - The amount of message you want Viper to consume. Note consuming a large amount will impact memory and network. 
   * - MAADS_ALGORITHM_SERVER_MICROSERVICE
     - MAADS algorithm server microservice. This will require MAADS software installed in the host. If you use a reverse proxy to access the MAADS software then 
       specify the name here.
   * - MAADS_ALGORITHM_SERVER1
     - Additional MAADS algorithm server. You can list up to 10,000 MAADS algorithm servers. Just increment the “SERVER#”, where #=1,…,10000 
   * - MAADS_ALGORITHM_SERVER1_PORT
     - Additional MAADS algorithm server port. 
   * - MAADS_ALGORITHM_SERVER1_MICROSERVICE
     - Additional MAADS algorithm server microservice. 
   * - KAFKA_ROOT
     - Kafka root folder 
   * - HPDE_IP
     - HPDE (Hyper-Predictions for Edge Devices) is another product required for **Real-Time Machine Learning.** Specify the host where it is installed. 
   * - HPDE_PORT
     - HPDE listening port. Specify port. If you specifying port range use “startport:endport”, where start port and end port are numbers 
   * - VIPER_IP
     - Specify IP for Viper, use * or leave empty for Viper to choose. 
   * - VIPER_PORT
     - Specify port. If you specifying port range use “startport:endport”, where start port and end port are numbers 
   * - VIPERVIZ_IP
     - Specify IP for Viperviz, use * or leave empty for Viper to choose. 
   * - VIPERVIZ_PORT
     - Specify port. If you specifying port range use “startport:endport”, where start port and end port are numbers 
   * - SSL_CLIENT_CERT_FILE
     - SSL certificate file needed if Kafka is SSL/TLS enabled 
   * - SSL_CLIENT_KEY_FILE
     - SSL certificate key store file needed if Kafka is SSL/TLS enabled 
   * - SSL_SERVER_CERT_FILE
     - SSL certificate server key file needed if Kafka is SSL/TLS enabled 
   * - CLOUD_USERNAME
     - SASL_PLAIN username to connect to Confluent Cloud 
   * - CLOUD_PASSWORD= 
     - SASL_PLAIN password to connect to Confluent Cloud 
   * - MAILSERVER
     - SMTP mailserver host name for sending emails. This is needed if using **AiMS Dashboard** to monitor algorithms in Kafka. 
   * - MAILPORT
     - SMTP mailserver port for sending emails. This is needed if using **AiMS Dashboard** to monitor algorithms in Kafka. 
   * - FROMADDR
     - From address to put in the emails. This is needed if using **AiMS Dashboard** to monitor algorithms in Kafka. 
   * - SMTP_USERNAME
     - SMTP username. This is needed if using **AiMS Dashboard** to monitor algorithms in Kafka. 
   * - SMTP_PASSWORD
     - SMTP password. This is needed if using **AiMS Dashboard** to monitor algorithms in Kafka and alerts are turned on.
   * - SMTP_SSLTLS
     - Mailserver SSL/TLS enabled: true of false. This is needed if using **AiMS Dashboard** to monitor algorithms in Kafka and alerts are turned on.
   * - POLLING_ALERTS
     - Polling for alerts in minutes. This is needed if using **AiMS Dashboard** and Alerts are turned on. VIPER will poll for alerts and wait in minutes for the next poll. 
   * - COMPANYNAME
     - Specify company name. This is used when sending emails from AiMS dashboard. 
   * - MYSQLDRIVERNAME
     - Enter MySQL driver name i.e. mysql 
   * - MYSQLDB
     - Enter MySQL DB name 
   * - MYSQLUSER
     - Enter MySQL username
   * - MYSQLPASS
     - Enter MySQL password 
   * -  MYSQLHOSTNAME
     -  Enter MySQL hostname – **_If using MYSQL DOCKER set this to: host.docker.internal:3306_** 
   * - MYSQLMAXLIFETIMEMINUTES
     - Enter max lifetime in minutes 
   * - MYSQLMAXCONN
     - Enter maximum connections 
   * - MYSQLMAXIDLE
     - Enter number of idle connections 
   * - MYSQL_ROOT_PASSWORD
     - MYSQL DOCKER Container: Set the Root password for MySQL 
   * - MYSQL_ROOT_HOST
     - MYSQL DOCKER Container: Set the Root host for MySQL ie. You can use % to accept connections from any host. 
   * - MYSQL_DATABASE
     - MYSQL DOCKER Container: Set the database name i.e. tmlids – **_This should match MYSQLDB_**
   * - MYSQL_USER
     - MYSQL DOCKER Container: Set the username name i.e. tmluser, avoid “root” - **_This should match MYSQLUSER_** 
   * - MYSQL_PASSWORD
     - MYSQL DOCKER Container: Set the password - **_This should match MYSQLPASS_** 
   * - MAXURLQUERYSTRINGBYTES
     - This is the size of the URL query string in bytes, if using viperhpdepredictprocess 

1. **You are done! Start VIPER.**
2. **Additional Documentation for Accessing VIPER Functionality**
3. VIPER is accessed by two methods:
    1. MAADSTML python library: <https://pypi.org/project/maadstml/>
        1. Scroll down to: **MAADS-VIPER Connector to Manage Apache KAFKA:**
    2. REST API:
        1. When starting VIPER type “Help” to see all the REST endpoints
        2. The endpoints can be called from ANY programming language.
4. Users can send an email to support@otics.ca for additional help with any of the functions.
5. OTICS provides up to **2 hours free virtual training** on an as-needed basis for clients or groups of clients.

