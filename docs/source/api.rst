TML API
===

**Multi-Agent Accelerator for Data Science Using Transactional Machine Learning (MAADSTML)**

*Revolutionizing Data Stream Science with Transactional Machine Learning*

**Overview**

*MAADSTML combines Artificial Intelligence, ChatGPT, PrivateGPT, Auto Machine Learning with Data Streams Integrated with Apache Kafka (or Redpanda) to create frictionless and elastic machine learning solutions.*  

This library allows users to harness the power of agent-based computing using hundreds of advanced linear and non-linear algorithms. Users can easily integrate Predictive Analytics, Prescriptive Analytics, Pre-Processing, and Optimization in any data stream solution by wrapping additional code around the functions below. It connects with **Apache KAFKA brokers** for cloud based computing using Kafka (or Redpanda) as the data backbone. 

If analysing MILLIONS of IoT devices, you can easily deploy thousands of VIPER/HPDE instances in Kubernetes Cluster in AWS/GCP/Azure. 

It uses VIPER as a **KAFKA connector and seamlessly combines Auto Machine Learning, with Real-Time Machine Learning, Real-Time Optimization and Real-Time Predictions** while publishing these insights in to a Kafka cluster in real-time at scale, while allowing users to consume these insights from anywhere, anytime and in any format. 

It also HPDE as the AutoML technology for TML.  Linux/Windows/Mac versions can be downloaded from [Github](https://github.com/smaurice101/transactionalmachinelearning)

It uses VIPERviz to visualize streaming insights over HTTP(S). Linux/Windows/Mac versions can be downloaded from [Github](https://github.com/smaurice101/transactionalmachinelearning)

MAADSTML details can be found in the book: [Transactional Machine Learning with Data Streams and AutoML](https://www.amazon.com/Transactional-Machine-Learning-Streams-AutoML/dp/1484270223)


To install this library a request should be made to **support@otics.ca** for a username and a MAADSTOKEN.  Once you have these credentials then install this Python library.

**Compatibility**
    - Python 3.8 or greater
    - Minimal Python skills needed

**Copyright**
   - Author: Sebastian Maurice, PhD
   
**Installation**
   - At the command prompt write:
     **pip install maadstml**
     - This assumes you have [Downloaded Python](https://www.python.org/downloads/) and installed it on your computer.  

**MAADS-VIPER Connector to Manage Apache KAFKA:** 
  - MAADS-VIPER python library connects to VIPER instances on any servers; VIPER manages Apache Kafka.  VIPER is REST based and cross-platform that can run on windows, linux, MAC, etc.. It also fully supports SSL/TLS encryption in Kafka brokers for producing and consuming.

**TML is integrated with PrivateGPT (https://github.com/imartinez/privateGPT), which is a production ready GPT, that is 100% Local, 100% Secure and 100% FREE GPT Access.
  - Users need to PULL and RUN one of the privateGPT Docker containers:
  - 	1. Docker Hub: maadsdocker/tml-privategpt-no-gpu-amd64 (without NVIDIA GPU for AMD64 Chip)
  -     2. Docker Hub: maadsdocker/tml-privategpt-with-gpu-amd64 (with NVIDIA GPU for AMD64 Chip)
  - 	3. Docker Hub: maadsdocker/tml-privategpt-no-gpu-arm64 (without NVIDIA GPU for ARM64 Chip)
  -     4. Docker Hub: maadsdocker/tml-privategpt-with-gpu-arm64 (with NVIDIA GPU for ARM64 Chip)
  - Additional details are here: https://github.com/smaurice101/raspberrypi/tree/main/privategpt
  - TML accesses privateGPT container using REST API. 
  - For PrivateGPT production deployments it is recommended that machines have the NVIDIA GPU as this will lead to significant performance improvements.

- **pgptingestdocs**
  - Set Context for PrivateGPT by ingesting PDFs or text documents.  All responses will then use these documents for context.  

- **pgptgetingestedembeddings**
  - After documents are ingested, you can retrieve the embeddings for the ingested documents.  These embeddings allow you to filter the documents for specific context.  

- **pgptchat**
  - Send any prompt to privateGPT (with or without context) and get back a response.  

- **pgptdeleteembeddings**
  - Delete embeddings.  

- **pgpthealth**
  - Check the health of the privateGPT http server.  

- **vipermirrorbrokers**
  - Migrate data streams from (mutiple) brokers to (multiple) brokers FAST!  In one simple function you have the 
    power to migrate from hundreds of brokers with hundreds of topics and partitions to any other brokers
	with ease.  Viper ensures no duplication of messages and translates offsets from last committed.  Every transaction 
	is logged, making data validation and auditability a snap.  You can also increase or decrease partitions and 
	apply filter to topics to copy over.  
	
- **viperstreamquery**
  - Query multiple streams with conditional statements.  For example, if you preprocessed multiple streams you can 
    query them in real-time and extract powerful insights.  You can use >, <, =, AND, OR. 

- **viperstreamquerybatch**
  - Query multiple streams with conditional statements.  For example, if you preprocessed multiple streams you can 
    query them in real-time and extract powerful insights.  You can use >, <, =, AND, OR. Batch allows you to query
	multiple IDs at once.

- **viperlisttopics** 
  - List all topics in Kafka brokers
 
- **viperdeactivatetopic**
  - Deactivate topics in kafka brokers and prevent unused algorithms from consuming storage and computing resources that cost money 

- **viperactivatetopic**
  - Activate topics in Kafka brokers 

- **vipercreatetopic**
  - Create topics in Kafka brokers 
  
- **viperstats**
  - List all stats from Kafka brokers allowing VIPER and KAFKA admins with a end-end view of who is producing data to algorithms, and who is consuming the insights from the algorithms including date/time stamp on the last reads/writes to topics, and how many bytes were read and written to topics and a lot more

- **vipersubscribeconsumer**
  - Admins can subscribe consumers to topics and consumers will immediately receive insights from topics.  This also gives admins more control of who is consuming the insights and allows them to ensures any issues are resolved quickly in case something happens to the algorithms.
  
- **viperunsubscribeconsumer**
  - Admins can unsubscribe consumers from receiving insights, this is important to ensure storage and compute resources are always used for active users.  For example, if a business user leaves your company or no longer needs the insights, by unsubscribing the consumer, the algorithm will STOP producing the insights.

- **viperhpdetraining**
  - Users can do real-time machine learning (RTML) on the data in Kafka topics. This is very powerful and useful for "transactional learnings" on the fly using our HPDE technology.  HPDE will find the optimal algorithm for the data in less than 60 seconds.  

- **viperhpdetrainingbatch**
  - Users can do real-time machine learning (RTML) on the data in Kafka topics. This is very powerful and useful for "transactional learnings" on the fly using our HPDE technology. 
    HPDE will find the optimal algorithm for the data in less than 60 seconds.  Batch allows you to perform ML on multiple IDs at once.

- **viperhpdepredict**
  - Using the optimal algorithm - users can do real-time predictions from streaming data into Kafka Topics.

- **viperhpdepredictprocess**
  - Using the optimal algorithm you can determine object ranking based on input data.  For example, if you want to know which human or machine is the 
    best or worst given input data then this function will return the best or worst human or machine.

- **viperhpdepredictbatch**
  - Using the optimal algorithm - users can do real-time predictions from streaming data into Kafka Topics. Batch allows you to perform predictions
    on multiple IDs at once.
  
- **viperhpdeoptimize**
  -  Users can even do optimization to MINIMIZE or MAXIMIZE the optimal algorithm to find the BEST values for the independent variables that will minimize or maximize the dependent variable.

- **viperhpdeoptimizebatch**
  -  Users can even do optimization to MINIMIZE or MAXIMIZE the optimal algorithm to find the BEST values for the independent variables that will minimize or maximize the dependent 
     variable. Batch allows you to optimize multiple IDs at once.

- **viperproducetotopic**
  - Users can produce to any topics by injesting from any data sources.

- **viperproducetotopicbulk**
  - Users can produce to any topics by injesting from any data sources.  Use this function to write bulk transactions at high speeds.  With the right architecture and
  network you can stream 1 million transactions per second (or more).
  
- **viperconsumefromtopic**
  - Users can consume from any topic and graph the data. 

- **viperconsumefromtopicbatch**
  - Users can consume from any topic and graph the data.  Batch allows you to consume from multiple IDs at once.
  
- **viperconsumefromstreamtopic**
  - Users can consume from a multiple stream of topics at once

- **vipercreateconsumergroup**
  - Admins can create a consumer group made up of any number of consumers.  You can add as many partitions for the group in the Kafka broker as well as specify the replication factor to ensure high availaibility and no disruption to users who consume insights from the topics.

- **viperconsumergroupconsumefromtopic**
  - Users who are part of the consumer group can consume from the group topic.

- **viperproducetotopicstream**
  - Users can join multiple topic streams and produce the combined results to another topic.
  
- **viperpreprocessproducetotopicstream**
  - Users can pre-process data streams using the following functions: MIN, MAX, AVG, COUNT, COUNTSTR, DIFF, DIFFMARGIN, SUM, MEDIAN, VARIANCE, OUTLIERS, OUTLIERSX-Y,VARIED, 
    ANOMPROB,ANOMPROBX-Y,ENTROPY, AUTOCORR, TREND, CONSISTENCY, IQR (InterQuartileRange), Midhinge, GM (Geometric mean), HM (Harmonic mean), Trimean, 
	CV (coefficient of Variation),Mad (Mean absolute deviation), Skewness, Kurtosis, Spikedetect, Unique, Uniquestr, Timediff: time should be in this 
	layout:2006-01-02T15:04:05, Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
    average time in seconds between consecutive dates.. Spikedetect uses a Zscore method to detect 
	spikes in the data using lag of 5, StD of 3.5 from mean and influence of 0.5.  Geodiff (returns distance in Kilometers between two lat/long points)
	
    Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
	current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
	You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
	will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
	between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
	for data quality and data assurance programs for any number of data streams.
		
	Unique Checks numeric data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.
 
    Uniquestr Checks string data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

    Uniquecount Checks numeric data for duplication.  Returns count of unique numbers.
 
    Uniquestrcount Checks string data for duplication.  Returns count of unique strings.
	
    CONSISTENCY checks if the data all have consistent data types. Returns 1 for consistent data types, 0 otherwise.
	
	Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 

    RAW for no processing.
	
    ANOMPROB=Anomaly Probability, it will run several algorithms on the data stream window to determine a probability percentage of 
	anomalous behaviour.  This can be cross-referenced with other process types. This is very useful if you want to extract aggregate 
	values that you can then use to build TML models and/or make decisions to prevent issues.  ENTROPY will compute the amount of information
	in the data stream.  AUTOCORR will run a autocorrelation regression: Y = Y (t-1), to indicate how previous value correlates with future 
    value.  TREND will run a linear regression of Y = f(Time), to determine if the data in the stream are increasing or decreasing.	

    ANOMPROBX-Y (similar to OUTLIERSX-Y), where X and Y are numbers or "n", if "n" means examine all anomalies for recurring patterns.
	They allow you to check if the anomalies in the streams are truly anomalies and not some
    pattern.  For example, if a IoT device shuts off and turns on again routinely, this may be picked up as an anomaly when in fact
    it is normal behaviour.  So, to ignore these cases, if ANOMPROB2-5, this tells Viper, check anomalies with patterns of 2-5 peaks.
    If the stream has two classes and these two classes are like 0 and 1000, and show a pattern, then they should not be considered an anomaly.
    Meaning, class=0, is the device shutting down, class=1000 is the device turning back on.  If ANOMPROB3-10, Viper will check for 
    patterns of classes 3 to 10 to see if they recur routinely.  This is very helpful to reduce false positives and false negatives.

- **viperpreprocessbatch**
  - This function is similar to *viperpreprocessproducetotopicstream* the only difference is you can specify multiple
    tmlids in Topicid field. This allows you to batch process multiple tmlids at once.  This is very useful if using
	kubernetes architecture.

- **vipercreatejointopicstreams**
  - Users can join multiple topic streams
  
- **vipercreatetrainingdata**
  - Users can create a training data set from the topic streams for Real-Time Machine Learning (RTML) on the fly.

- **vipermodifyconsumerdetails**
  - Users can modify consumer details on the topic.  When topics are created an admin must indicate name, email, location and description of the topic.  This helps to better manage the topic and if there are issues, the admin can contact the individual consuming from the topic.
  
- **vipermodifytopicdetails**
  - Users can modify details on the topic.  When topics are created an admin must indicate name, email, location and description of the topic.  This helps to better manage the topic and if there are issues, the admin can contact the developer of the algorithm and resolve issue quickly to ensure disruption to consumers is minimal.
 
- **vipergroupdeactivate**
  - Admins can deactive a consumer group, which will stop all insights being delivered to consumers in the group.
  
- **vipergroupactivate**
  - Admins can activate a group to re-start the insights.
 
- **viperdeletetopics**
  - Admins can delete topics in VIPER database and Kafka clusters.
		
- **viperanomalytrain**
  - Perform anomaly/peer group analysis on text or numeric data stream using advanced unsupervised learning. VIPER automatically joins 
    streams, and determines the peer group of "usual" behaviours using proprietary algorithms, which are then used to predict anomalies with 
	*viperanomalypredict* in real-time.  Users can use several parameters to fine tune the peer groups.  
	
	*VIPER is one of the very few, if not only, technology to do anomaly/peer group analysis using unsupervised learning on data streams 
	with Apache Kafka.*

- **viperanomalytrainbatch**
  - Batch allows you to perform anomaly training on multiple IDs at once.

- **viperanomalypredict**
  - Predicts anomalies for text or numeric data using the peer groups found with *viperanomalytrain*.  VIPER automatically joins streams
  and compares each value with the peer groups and determines if a value is anomalous in real-time.  Users can use several parameters to fine tune
  the analysis. 
  
  *VIPER is one of the very few, if not only, technology to do anomaly detection/predictions using unsupervised learning on data streams
  with Apache Kafka.*
		
- **viperanomalypredictbatch**
  - Batch allows you to perform anomaly prediction on multiple IDs at once.
				
- **viperstreamcorr**
  - Performs streaming correlations by joining multiple data streams with 2 variables.  Also performs cross-correlations with 4 variables.
    This is a powerful function and can offer important correlation signals between variables.   Will also correlate TEXT using 
    natural language processing (NLP).	

- **viperpreprocesscustomjson**
  - Immediately start processing ANY RAW JSON data in minutes.  This is useful if you want to start processing data quickly.  

- **viperstreamcluster**
  - Perform cluster analysis on streaming data.  This uses K-Means clustering with Euclidean or EuclideanSquared algorithms to compute 
    distance.  It is a very useful function if you want to determine common behaviours between devices, patients, or other entities.
	Users can also setup email alerts if specific clusters are found.

- **vipersearchanomaly**
  - Perform advanced analysis for user search.  This function is useful if you want to monitor what people are searching for, and determine
    if the searches are anamolous and differ from the peer group of "normal" search behaviour.

- **vipernlp**
  - Perform advanced natural language summary of PDFs.

- **viperchatgpt**
  - Start a conversation with ChatGPT in real-time and stream responses.

- **viperexractpdffields**
  - Extracts fields from PDF file

- **viperexractpdffieldbylabel**
  - Extracts fields from PDF file by label name.

- **videochatloadresponse**
  - Analyse videos with video chatgpt.  This is a powerful GPT LLM that will understand and reason with videos frame by frame.  
    It will also understand the spatio-temporal frames in the video.  Video gpt runs in a container. 

- **areyoubusy**
  - If deploying thousands of VIPER/HPDE binaries in a Kubernetes cluster - you can broadcast a 'areyoubusy' message to all VIPER and HPDE
    binaries, and they will return back the HOST/PORT if they are NOT busy with other tasks.  This is very convenient for dynamically managing  
	enormous load among VIPER/HPDE and allows you to dynamically assign HOST/PORT to **non-busy** VIPER/HPDE microservices.

**First import the Python library.**

**import maadstml**


**1. maadstml.viperstats(vipertoken,host,port=-999,brokerhost='',brokerport=-999,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.


*brokerhost* : string, optional

- Address where Kafka broker is running - if none is specified, the Kafka broker address in the VIPER.ENV file will be used.


*brokerport* : int, optional

- Port on which Kafka is listenting.

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: A JSON formatted object of all the Kafka broker information.

**2. maadstml.vipersubscribeconsumer(vipertoken,host,port,topic,companyname,contactname,contactemail,
		location,description,brokerhost='',brokerport=-999,groupid='',microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required

- Topic to subscribe to in Kafka broker

*companyname* : string, required

- Company name of consumer

*contactname* : string, required

- Contact name of consumer

*contactemail* : string, required

- Contact email of consumer

*location* : string, required

- Location of consumer

*description* : string, required

- Description of why consumer wants to subscribe to topic

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*groupid* : string, optional

- Subscribe consumer to group

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Consumer ID that the user must use to receive insights from topic.


**3. maadstml.viperunsubscribeconsumer(vipertoken,host,port,consumerid,brokerhost='',brokerport=-999,
	microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*consumerid* : string, required
       
- Consumer id to unsubscribe

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

RETURNS: Success/failure 

**4. maadstml.viperproducetotopic(vipertoken,host,port,topic,producerid,enabletls=0,delay=100,inputdata='',maadsalgokey='',
	maadstoken='',getoptimal=0,externalprediction='',subtopics='',topicid=-999,identifier='',array=0,brokerhost='',
	brokerport=-999,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required

- Topic or Topics to produce to.  You can separate multiple topics by a comma.  If using multiple topics, you must 
  have the same number of producer ids (separated by commas), and same number of externalprediction (separated by
  commas).  Producing to multiple topics at once is convenient for synchronizing the timing of 
  streams for machine learning.

*subtopic* : string, optional

- Enter sub-topic streams.  This is useful if you want to reduce the number of topics/partitions in Kafka by adding
  sub-topics in the main topic.  

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, with 10 subtopic streams 
  you can assign a Topicid to each IoT device and each of the 10 subtopics will be associated to each IoT device.
  This way, you do not create 10,000 streams, but just 1 Main Topic stream, and VIPER will add the 10,000 streams
  in the one topic.  This will also drastically reduce the partition costs.  You can also create custom machine 
  learning models, predictions, and optimization for each 1000 IoT devices quickly: **It is very powerful.**

"array* : int, optional

- You can stream multiple variables at once, and use array=1 to specify that the streams are an array.
  This is similar to streaming 1 ROW in a database, and useful if you want to synchonize variables for machine learning.  
  For example, if a device produces 3 streams: stream A, stream B, stream C, and rather than streaming A, B, C separately
  you can add them to subtopic="A,B,C", and externalprediction="value_FOR_A,value_FOR_B,value_FOR_C", then specify
  array=1, then when you do machine learning on this data, the variables A, B, C are date/time synchronized
  and you can choose which variable is the depdendent variable in viperhpdetraining function.


*identifier* : string, optional

- You can add any string identifier for the device.  For examaple, DSN ID, IoT device id etc.. 

*producerid* : string, required
       
- Producer ID of topic to produce to in the Kafka broker

*enabletls* : int, optional
       
- Set to 1 if Kafka broker is enabled with SSL/TLS encryption, otherwise 0 for plaintext.

*delay*: int, optional

- Time in milliseconds from VIPER backsout from writing messages

*inputdata* : string, optional

- This is the inputdata for the optimal algorithm found by MAADS or HPDE

*maadsalgokey* : string, optional

- This should be the optimal algorithm key returned by maadstml.dotraining function.

*maadstoken* : string, optional
- If the topic is the name of the algorithm from MAADS, then a MAADSTOKEN must be specified to access the algorithm in the MAADS server

*getoptimal*: int, optional
- If you used the maadstml.OPTIMIZE function to optimize a MAADS algorithm, then if this is 1 it will only retrieve the optimal results in JSON format.

*externalprediction* : string, optional
- If you are using your own custom algorithms, then the output of your algorithm can be still used and fed into the Kafka topic.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns the value produced or results retrieved from the optimization.

**4.1. maadstml.viperproducetotopicbulk(vipertoken,host,port,topic,producerid,inputdata,partitionsize=100,enabletls=1,delay=100,
        brokerhost='',brokerport=-999,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required

- Topic or Topics to produce to.  You can separate multiple topics by a comma.  If using multiple topics, you must 
  have the same number of producer ids (separated by commas), and same number of externalprediction (separated by
  commas).  Producing to multiple topics at once is convenient for synchronizing the timing of 
  streams for machine learning.

*producerid* : string, required
       
- Producer ID of topic to produce to in the Kafka broker.  Separate multiple producer ids with comma.

*inputdata* : string, required
       
- You can write multiple transactions to each topic.  Each group of transactions must be separated by a tilde.  
  Each transaction in the group must be separate by a comma.  The number of groups must match the producerids and 
  topics.  For example, if you are writing to two topics: topic1,topic2, then the inputdata should be:
  trans1,transn2,...,transnN~trans1,transn2,...,transnN.  The number of transactions and topics can be any number.
  This function can be very powerful if you need to analyse millions or billions of transactions very quickly.

*partitionsize* : int, optional

- This is the number of partitions of the inputdata.  For example, if your transactions=10000, then VIPER will 
  create partitions of size 100 (if partitionsize=100) resulting in 100 threads for concurrency.  The higher
  the partitionsize, the lower the number of threads.  If you want to streams lots of data fast, then a 
  partitionzie of 1 is the fastest but will come with overhead because more RAM and CPU will be consumed.

*enabletls* : int, optional
       
- Set to 1 if Kafka broker is enabled with SSL/TLS encryption, otherwise 0 for plaintext.

*delay*: int, optional

- Time in milliseconds from VIPER backsout from writing messages

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: None

**5. maadstml.viperconsumefromtopic(vipertoken,host,port,topic,consumerid,companyname,partition=-1,enabletls=0,delay=100,offset=0,
	brokerhost='',brokerport=-999,microserviceid='',topicid='-999',rollbackoffsets=0,preprocesstype='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to consume from in the Kafka broker

*preprocesstype* : string, optional

- If you only want to search for record that have a particular processtype, you can enter:
  MIN, MAX, AVG, COUNT, COUNTSTR, DIFF, DIFFMARGIN, SUM, MEDIAN, VARIANCE, OUTLIERS, OUTLIERSX-Y, VARIED, ANOMPROB,ANOMPROBX-Y,ENTROPY, 
  AUTOCORR, TREND, CONSISTENCY, Unique, Uniquestr, Geodiff (returns distance in Kilometers between two lat/long points)
  IQR (InterQuartileRange), Midhinge, GM (Geometric mean), HM (Harmonic mean), Trimean, CV (coefficient of Variation), 
  Mad (Mean absolute deviation), Skewness, Kurtosis, Spikedetect, Timediff: time should be in this layout:2006-01-02T15:04:05,
  Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
  average time in seconds between consecutive dates.
  Spikedetect uses a Zscore method to detect spikes in the data using lag of 5, StD of 3.5 from mean and influence of 0.5.   

  Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
  current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
  You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
  will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
  between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
  for data quality and data assurance programs for any number of data streams.

  Unique Checks numeric data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Uniquestr Checks string data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Uniquecount Checks numeric data for duplication.  Returns count of unique numbers.
 
  Uniquestrcount Checks string data for duplication.  Returns count of unique strings.

  CONSISTENCY checks if the data all have consistent data types. Returns 1 for consistent data types, 0 otherwise.
  
  Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 

  RAW for no processing.
  
  ANOMPROB=Anomaly probability,
  it will run several algorithms on the data stream window to determine a probaility of anomalous
  behaviour.  This can be cross-refenced with OUTLIERS.  It can be very powerful way to detection
  issues with devices.
  
  ANOMPROBX-Y (similar to OUTLIERSX-Y), where X and Y are numbers, or "n".  If "n", means examine all anomalies for patterns.
  They allow you to check if the anomalies in the streams are truly anomalies and not some
  pattern.  For example, if a IoT device shuts off and turns on again routinely, this may be picked up as an anomaly when in fact
  it is normal behaviour.  So, to ignore these cases, if ANOMPROB2-5, this tells Viper, check anomalies with patterns of 2-5 peaks.
  If the stream has two classes and these two classes are like 0 and 1000, and show a pattern, then they should not be considered an anomaly.
  Meaning, class=0, is the device shutting down, class=1000 is the device turning back on.  If ANOMPROB3-10, Viper will check for 
  patterns of classes 3 to 10 to see if they recur routinely.  This is very helpful to reduce false positives and false negatives.

  
*topicid* : string, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can consume on a per device by entering
  its topicid  that you gave when you produced the topic stream. Or, you can read from multiple topicids at the same time.  
  For example, if you have 10 ids, then you can specify each one separated by a comma: 1,2,3,4,5,6,7,8,9,10
  VIPER will read topicids in parallel.  This can drastically speed up consumption of messages but will require more 
  CPU.

*rollbackoffsets* : int, optional, enter value between 0 and 100

- This will rollback the streams by this percentage.  For example, if using topicid, the main stream is rolled back by this
  percentage amount.

*consumerid* : string, required

- Consumer id associated with the topic

*companyname* : string, required

- Your company name

*partition* : int, optional

- set to Kafka partition number or -1 to autodect

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*offset*: int, optional

- Offset to start the reading from..if 0 then reading will start from the beginning of the topic. If -1, VIPER will automatically 
  go to the last offset.  Or, you can extract the LastOffet from the returned JSON and use this offset for your next call.  

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the contents read from the topic.

**5.1 maadstml.viperconsumefromtopicbatch(vipertoken,host,port,topic,consumerid,companyname,partition=-1,enabletls=0,delay=100,offset=0,
	brokerhost='',brokerport=-999,microserviceid='',topicid='-999',rollbackoffsets=0,preprocesstype='',timedelay=0,asynctimeout=120)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600
 
*topic* : string, required
       
- Topic to consume from in the Kafka broker

*preprocesstype* : string, optional

- If you only want to search for record that have a particular processtype, you can enter:
  MIN, MAX, AVG, COUNT, COUNTSTR, DIFF, DIFFMARGIN, SUM, MEDIAN, VARIANCE, OUTLIERS, OUTLIERSX-Y, VARIED, ANOMPROB,ANOMPROBX-Y,ENTROPY, AUTOCORR, TREND, 
  IQR (InterQuartileRange), Midhinge, CONSISTENCY, GM (Geometric mean), HM (Harmonic mean), Trimean, CV (coefficient of Variation), 
  Mad (Mean absolute deviation), Skewness, Kurtosis, Spikedetect, Unique, Uniquestr, Timediff: time should be in this layout:2006-01-02T15:04:05,
  Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
  average time in seconds between consecutive dates. 
  Spikedetect uses a Zscore method to detect spikes in the data using lag of 5, StD of 3.5 from mean and influence of 0.5.   
  Geodiff (returns distance in Kilometers between two lat/long points)
  Unique Checks numeric data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
  current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
  You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
  will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
  between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
  for data quality and data assurance programs for any number of data streams.

  Uniquestr Checks string data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Uniquecount Checks numeric data for duplication.  Returns count of unique numbers.
 
  Uniquestrcount Checks string data for duplication.  Returns count of unique strings.
  
  CONSISTENCY checks if the data all have consistent data types. Returns 1 for consistent data types, 0 otherwise.

  Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 

  RAW for no processing.

  ANOMPROB=Anomaly probability,
  it will run several algorithms on the data stream window to determine a probaility of anomalous
  behaviour.  This can be cross-refenced with OUTLIERS.  It can be very powerful way to detection
  issues with devices.
  
  ANOMPROBX-Y (similar to OUTLIERSX-Y), where X and Y are numbers, or "n".  If "n", means examine all anomalies for patterns.
  They allow you to check if the anomalies in the streams are truly anomalies and not some
  pattern.  For example, if a IoT device shuts off and turns on again routinely, this may be picked up as an anomaly when in fact
  it is normal behaviour.  So, to ignore these cases, if ANOMPROB2-5, this tells Viper, check anomalies with patterns of 2-5 peaks.
  If the stream has two classes and these two classes are like 0 and 1000, and show a pattern, then they should not be considered an anomaly.
  Meaning, class=0, is the device shutting down, class=1000 is the device turning back on.  If ANOMPROB3-10, Viper will check for 
  patterns of classes 3 to 10 to see if they recur routinely.  This is very helpful to reduce false positives and false negatives.

  
*topicid* : string, required

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can consume on a per device by entering
  its topicid  that you gave when you produced the topic stream. Or, you can read from multiple topicids at the same time.  
  For example, if you have 10 ids, then you can specify each one separated by a comma: 1,2,3,4,5,6,7,8,9,10
  VIPER will read topicids in parallel.  This can drastically speed up consumption of messages but will require more 
  CPU.  VIPER will consume continously from topic ids.

*rollbackoffsets* : int, optional, enter value between 0 and 100

- This will rollback the streams by this percentage.  For example, if using topicid, the main stream is rolled back by this
  percentage amount.

*consumerid* : string, required

- Consumer id associated with the topic

*companyname* : string, required

- Your company name

*partition* : int, optional

- set to Kafka partition number or -1 to autodect

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*offset*: int, optional

- Offset to start the reading from..if 0 then reading will start from the beginning of the topic. If -1, VIPER will automatically 
  go to the last offset.  Or, you can extract the LastOffet from the returned JSON and use this offset for your next call.  

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the contents read from the topic.

**6. maadstml.viperhpdepredict(vipertoken,host,port,consumefrom,produceto,companyname,consumerid,producerid,
		hpdehost,inputdata,maxrows=0,algokey='',partition=-1,offset=-1,enabletls=1,delay=1000,hpdeport=-999,brokerhost='',
		brokerport=-999,timeout=120,usedeploy=0,microserviceid='',topicid=-999, maintopic='', streamstojoin='',
		array=0,pathtoalgos='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, with 10 subtopic streams 
  you can assign a Topicid to each IoT device and each of the 10 subtopics will be associated to each IoT device.
  This way, you can do predictions for each IoT using its own custom ML model.
  
*pathtoalgos* : string, required

- Enter the full path to the root folder where the algorithms are stored.
  
*maintopic* : string, optional

-  This is the name of the topic that contains the sub-topic streams.

*array* : int, optional

- Set array=1 if you produced data (from viperproducetotopic) as an array.  

*streamstojoin* : string, optional

- These are the sub-topics you are streaming into maintopic.  To do predictions, VIPER will automatically join 
  these streams to create the input data for predictions for each Topicid.
  
*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*inputdata*: string, required

- This is a comma separated list of values that represent the independent variables in your algorithm. 
  The order must match the order of the independent variables in your algorithm. OR, you can enter a 
  data stream that contains the joined topics from *vipercreatejointopicstreams*.

*maxrows*: int, optional

- Use this to rollback the stream by maxrows offsets.  For example, if you want to make 1000 predictions
  then set maxrows=1000, and make 1000 predictions from the current offset of the independent variables.

*algokey*: string, optional

- If you know the algorithm key that was returned by VIPERHPDETRAIING then you can specify it here.
  Specifying the algokey can drastically speed up the predictions.

*partition* : int, optional

- If you know the kafka partition used to store data then specify it here.
  Most cases Kafka will dynamically store data in partitions, so you should
  use the default of -1 to let VIPER find it.
 
*offset* : int, optional

- Offset to start consuming data.  Usually you can use -1, and VIPER
  will get the last offset.
  
*hpdehost*: string, required

- Address of HPDE 

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encryted traffic, otherwise 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*hpdeport*: int, required

- Port number HPDE is listening on 

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.

*usedeploy* : int, optional

 - If 0 will use algorithm in test, else if 1 use in production algorithm. 
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the prediction.

**6.1 maadstml.viperhpdepredictbatch(vipertoken,host,port,consumefrom,produceto,companyname,consumerid,producerid,
		hpdehost,inputdata,maxrows=0,algokey='',partition=-1,offset=-1,enabletls=1,delay=1000,hpdeport=-999,brokerhost='',
		brokerport=-999,timeout=120,usedeploy=0,microserviceid='',topicid="-999", maintopic='', streamstojoin='',
		array=0,timedelay=0,asynctimeout=120,pathtoalgos='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600

*topicid* : string, required

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, with 10 subtopic streams 
  you can assign a Topicid to each IoT device and each of the 10 subtopics will be associated to each IoT device.
  This way, you can do predictions for each IoT using its own custom ML model.  Separate multiple topicids by a 
  comma.  For example, topicid="1,2,3,4,5" and viper will process at once.
    
*pathtoalgos* : string, required

- Enter the full path to the root folder where the algorithms are stored.
	
*maintopic* : string, optional

-  This is the name of the topic that contains the sub-topic streams.

*array* : int, optional

- Set array=1 if you produced data (from viperproducetotopic) as an array.  

*streamstojoin* : string, optional

- These are the sub-topics you are streaming into maintopic.  To do predictions, VIPER will automatically join 
  these streams to create the input data for predictions for each Topicid.
  
*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*inputdata*: string, required

- This is a comma separated list of values that represent the independent variables in your algorithm. 
  The order must match the order of the independent variables in your algorithm. OR, you can enter a 
  data stream that contains the joined topics from *vipercreatejointopicstreams*.

*maxrows*: int, optional

- Use this to rollback the stream by maxrows offsets.  For example, if you want to make 1000 predictions
  then set maxrows=1000, and make 1000 predictions from the current offset of the independent variables.

*algokey*: string, optional

- If you know the algorithm key that was returned by VIPERHPDETRAIING then you can specify it here.
  Specifying the algokey can drastically speed up the predictions.

*partition* : int, optional

- If you know the kafka partition used to store data then specify it here.
  Most cases Kafka will dynamically store data in partitions, so you should
  use the default of -1 to let VIPER find it.
 
*offset* : int, optional

- Offset to start consuming data.  Usually you can use -1, and VIPER
  will get the last offset.
  
*hpdehost*: string, required

- Address of HPDE 

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encryted traffic, otherwise 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*hpdeport*: int, required

- Port number HPDE is listening on 

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.

*usedeploy* : int, optional

 - If 0 will use algorithm in test, else if 1 use in production algorithm. 
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the prediction.

**6.2. maadstml.viperhpdepredictprocess(vipertoken,host,port,consumefrom,produceto,companyname,consumerid,producerid,hpdehost,inputdata,processtype,maxrows=0,
                     algokey='',partition=-1,offset=-1,enabletls=1,delay=1000,hpdeport=-999,brokerhost='',brokerport=9092,
                     timeout=120,usedeploy=0,microserviceid='',topicid=-999, maintopic='',
                     streamstojoin='',array=0,pathtoalgos='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, with 10 subtopic streams 
  you can assign a Topicid to each IoT device and each of the 10 subtopics will be associated to each IoT device.
  This way, you can do predictions for each IoT using its own custom ML model.
  
*pathtoalgos* : string, required

- Enter the full path to the root folder where the algorithms are stored.
  
*maintopic* : string, optional

-  This is the name of the topic that contains the sub-topic streams.

*array* : int, optional

- Set array=1 if you produced data (from viperproducetotopic) as an array.  

*streamstojoin* : string, optional

- These are the sub-topics you are streaming into maintopic.  To do predictions, VIPER will automatically join 
  these streams to create the input data for predictions for each Topicid.
  
*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*inputdata*: string, required

- This is a comma separated list of values that represent the independent variables in your algorithm. 
  The order must match the order of the independent variables in your algorithm. OR, you can enter a 
  data stream that contains the joined topics from *vipercreatejointopicstreams*.

*processtype*: string, required

- This must be: max, min, avg, median, trend, all.  For example, to find the maximum or the best human or machine.
  Trend will compute the predictions are trending.  Avg is the average of all predictions.  Median is the median of
  predictions.  All will produce all predictions.  

*maxrows*: int, optional

- Use this to rollback the stream by maxrows offsets.  For example, if you want to make 1000 predictions
  then set maxrows=1000, and make 1000 predictions from the current offset of the independent variables.

*algokey*: string, optional

- If you know the algorithm key that was returned by VIPERHPDETRAIING then you can specify it here.
  Specifying the algokey can drastically speed up the predictions.

*partition* : int, optional

- If you know the kafka partition used to store data then specify it here.
  Most cases Kafka will dynamically store data in partitions, so you should
  use the default of -1 to let VIPER find it.
 
*offset* : int, optional

- Offset to start consuming data.  Usually you can use -1, and VIPER
  will get the last offset.
  
*hpdehost*: string, required

- Address of HPDE 

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encryted traffic, otherwise 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*hpdeport*: int, required

- Port number HPDE is listening on 

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.

*usedeploy* : int, optional

 - If 0 will use algorithm in test, else if 1 use in production algorithm. 
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the prediction.

**7. maadstml.viperhpdeoptimize(vipertoken,host,port,consumefrom,produceto,companyname,consumerid,producerid,
		hpdehost,partition=-1,offset=-1,enabletls=0,delay=100,hpdeport=-999,usedeploy=0,ismin=1,constraints='best',
		stretchbounds=20,constrainttype=1,epsilon=10,brokerhost='',brokerport=-999,timeout=120,microserviceid='',topicid=-999)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can perform
  mathematical optimization for each of the 1000 IoT devices using their specific algorithm.
  
*produceto* : string, required

- Topic to produce results of the prediction to

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*partition* : int, optional

- If you know the kafka partition used to store data then specify it here.
  Most cases Kafka will dynamically store data in partitions, so you should
  use the default of -1 to let VIPER find it.
 
*offset* : int, optional

- Offset to start consuming data.  Usually you can use -1, and VIPER
  will get the last offset.
  
*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*hpdeport*: int, required

- Port number HPDE is listening on 

*usedeploy* : int, optional
 - If 0 will use algorithm in test, else if 1 use in production algorithm. 

*ismin* : int, optional
- If 1 then function is minimized, else if 0 the function is maximized

*constraints*: string, optional

- If "best" then HPDE will choose the best values of the independent variables to minmize or maximize the dependent variable.  
  Users can also specify their own constraints for each variable and must be in the following format: varname1:min:max,varname2:min:max,...

*stretchbounds*: int, optional

- A number between 0 and 100, this is the percentage to stretch the bounds on the constraints.

*constrainttype*: int, optional

- If 1 then HPDE uses the min/max of each variable for the bounds, if 2 HPDE will adjust the min/max by their standard deviation, 
  if 3 then HPDE uses stretchbounds to adjust the min/max for each variable.  

*epsilon*: int, optional

- Once HPDE finds a good local minima/maxima, it then uses this epsilon value to find the Global minima/maxima to ensure 
  you have the best values of the independent variables that minimize or maximize the dependent variable.
					 
*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.

 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the optimization details and optimal values.

**7.1 maadstml.viperhpdeoptimizebatch(vipertoken,host,port,consumefrom,produceto,companyname,consumerid,producerid,
		hpdehost,partition=-1,offset=-1,enabletls=0,delay=100,hpdeport=-999,usedeploy=0,ismin=1,constraints='best',
		stretchbounds=20,constrainttype=1,epsilon=10,brokerhost='',brokerport=-999,timeout=120,microserviceid='',topicid="-999",
		timedelay=0,asynctimeout=120)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*topicid* : string, required

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can perform
  mathematical optimization for each of the 1000 IoT devices using their specific algorithm.  Separate 
  multiple topicids by a comma.
  
*produceto* : string, required

- Topic to produce results of the prediction to

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*partition* : int, optional

- If you know the kafka partition used to store data then specify it here.
  Most cases Kafka will dynamically store data in partitions, so you should
  use the default of -1 to let VIPER find it.
 
*offset* : int, optional

- Offset to start consuming data.  Usually you can use -1, and VIPER
  will get the last offset.
  
*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*hpdeport*: int, required

- Port number HPDE is listening on 

*usedeploy* : int, optional
 - If 0 will use algorithm in test, else if 1 use in production algorithm. 

*ismin* : int, optional
- If 1 then function is minimized, else if 0 the function is maximized

*constraints*: string, optional

- If "best" then HPDE will choose the best values of the independent variables to minmize or maximize the dependent variable.  
  Users can also specify their own constraints for each variable and must be in the following format: varname1:min:max,varname2:min:max,...

*stretchbounds*: int, optional

- A number between 0 and 100, this is the percentage to stretch the bounds on the constraints.

*constrainttype*: int, optional

- If 1 then HPDE uses the min/max of each variable for the bounds, if 2 HPDE will adjust the min/max by their standard deviation, 
  if 3 then HPDE uses stretchbounds to adjust the min/max for each variable.  

*epsilon*: int, optional

- Once HPDE finds a good local minima/maxima, it then uses this epsilon value to find the Global minima/maxima to ensure 
  you have the best values of the independent variables that minimize or maximize the dependent variable.
					 
*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.

 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the optimization details and optimal values.

**8. maadstml.viperhpdetraining(vipertoken,host,port,consumefrom,produceto,companyname,consumerid,producerid,
                 hpdehost,viperconfigfile,enabletls=1,partition=-1,deploy=0,modelruns=50,modelsearchtuner=80,hpdeport=-999,
				 offset=-1,islogistic=0,brokerhost='', brokerport=-999,timeout=120,microserviceid='',topicid=-999,maintopic='',
                 independentvariables='',dependentvariable='',rollbackoffsets=0,fullpathtotrainingdata='',processlogic='',
				 identifier='',array=0,transformtype='',sendcoefto='',coeftoprocess='',coefsubtopicnames='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*transformtype* : string, optional

- You can transform the dependent and independent variables using: log-log, log-lin, lin-log, lin=linear, log=natural log 
  This may be useful if you want to compute price or demand elasticities.

*sendcoefto* : string, optional
 
- This is the name of the kafka topic that you want to stream the estimated parameters to.

*coeftoprocess* : string, optional

- This is the indexes of the estimated parameters.  For example, if the ML model has a constant and two estimated
  parameters, then coeftoprocess="0,1,2" means stream constant term (at index 0) and the two estmiated parameters at
  index 1, and 2.

*coefsubtopicnames* : string, optional

- This is the names for the estimated parameters.  For example, "constant,elasticity,elasticity2" would be streamed
  as kafka topics for *coeftoprocess*

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can create individual 
  Machine Learning models for each IoT device in real-time.  This is a core functionality of TML solutions.
  
*array* : int, optional

- Set array=1 if the data you are consuming from is an array of multiple streams that you produced from 
  viperproducetotopic in an effort to synchronize data for training.

*maintopic* : string, optional

- This is the maintopic that contains the sub-topc streams.

*independentvariables* : string, optional

- These are the independent variables that are the subtopics.  

*dependentvariable* : string, optional

- This is the dependent variable in the subtopic streams.  

*rollbackoffsets*: int, optional

- This is the rollback percentage to create the training dataset.  VIPER will automatically create a training dataset
  using the independent and dependent variable streams.  

*fullpathtotrainingdata*: string, optional

- This is the FULL path where you want to store the training dataset.  VIPER will write file to disk. Make sure proper
  permissions are granted to VIPER.   For example, **c:/myfolder/mypath**

*processlogic* : string, optional

- You can dynamically build a classification model by specifying how you want to classify the dependent variable by
  indicating your conditions in the processlogic variable (this will take effect if islogistic=1). For example: 
  
  **processlogic='classification_name=my_prob:temperature=20.5,30:humidity=50,55'**, means the following:
   
   1. The name of the dependent variable is specified by **classification_name**
   2. Then you can specify the conditions on the streams. If your stream is Temperature and humidity,
      if Temperature is between 20.5 and 30, then my_prob=1, otherwise my_prob=0, and
	  if Humidity is between 50 and 55, then my_prob=1, otherwise my_prob=0
   3.  If you want to specify no upperbound you can use *n*, or *-n* for no lowerbound.
       For example, if **temperature=20.5,n**, means temperature >=20.5 then my_prob=1
	   If **humidity=-n,55**, means humidity<=55 then my_prob=1 

- This allows you to classify the dependent with any number of variables all in real-time!

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*companyname* : string, required

- Your company name

*consumerid*: string, required

*identifier*: string, optional

- You can add any name or identifier like DSN ID

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*viperconfigfile* : string, required

- Full path to VIPER.ENV configuration file on server.

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*partition*: int, optional

- Partition used by kafka to store data. NOTE: Kafka will dynamically store data in partitions.
  Unless you know for sure the partition, you should use the default of -1 to let VIPER
  determine where your data is.

*deploy*: int, optional

- If deploy=1, this will deploy the algorithm to the Deploy folder.  This is useful if you do not
  want to use this algorithm in production, and just testing it.  If just testing, then set deploy=0 (default).  

*modelruns*: int, optional

- Number of iterations for model training

*modelsearchtuner*: int, optional

- An integer between 0-100, this variable will attempt to fine tune the model search space.  A number close to 0 means you will 
  have lots of models but their quality may be low, a number close to 100 (default=80) means you will have fewer models but their 
  quality will be higher

*hpdeport*: int, required

- Port number HPDE is listening on 

*offset* : int, optional

 - If 0 will use the training data from the beginning of the topic
 
*islogistic*: int, optional

- If is 1, the HPDE will switch to logistic modeling, else continous.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the optimal algorithm that best fits your data.

**8.1 maadstml.viperhpdetrainingbatch(vipertoken,host,port,consumefrom,produceto,companyname,consumerid,producerid,
                 hpdehost,viperconfigfile,enabletls=1,partition=-1,deploy=0,modelruns=50,modelsearchtuner=80,hpdeport=-999,
				 offset=-1,islogistic=0,brokerhost='', brokerport=-999,timeout=120,microserviceid='',topicid="-999",maintopic='',
                 independentvariables='',dependentvariable='',rollbackoffsets=0,fullpathtotrainingdata='',processlogic='',
				 identifier='',array=0,timedelay=0,asynctimeout=120)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600

*topicid* : string, required

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can create individual 
  Machine Learning models for each IoT device in real-time.  This is a core functionality of TML solutions.
  Separate multiple topic ids by comma.
  
*array* : int, optional

- Set array=1 if the data you are consuming from is an array of multiple streams that you produced from 
  viperproducetotopic in an effort to synchronize data for training.

*maintopic* : string, optional

- This is the maintopic that contains the sub-topc streams.

*independentvariables* : string, optional

- These are the independent variables that are the subtopics.  

*dependentvariable* : string, optional

- This is the dependent variable in the subtopic streams.  

*rollbackoffsets*: int, optional

- This is the rollback percentage to create the training dataset.  VIPER will automatically create a training dataset
  using the independent and dependent variable streams.  

*fullpathtotrainingdata*: string, optional

- This is the FULL path where you want to store the training dataset.  VIPER will write file to disk. Make sure proper
  permissions are granted to VIPER.   For example, **c:/myfolder/mypath**

*processlogic* : string, optional

- You can dynamically build a classification model by specifying how you want to classify the dependent variable by
  indicating your conditions in the processlogic variable (this will take effect if islogistic=1). For example: 
  
  **processlogic='classification_name=my_prob:temperature=20.5,30:humidity=50,55'**, means the following:
   
   1. The name of the dependent variable is specified by **classification_name**
   2. Then you can specify the conditions on the streams. If your stream is Temperature and humidity,
      if Temperature is between 20.5 and 30, then my_prob=1, otherwise my_prob=0, and
	  if Humidity is between 50 and 55, then my_prob=1, otherwise my_prob=0
   3.  If you want to specify no upperbound you can use *n*, or *-n* for no lowerbound.
       For example, if **temperature=20.5,n**, means temperature >=20.5 then my_prob=1
	   If **humidity=-n,55**, means humidity<=55 then my_prob=1 

- This allows you to classify the dependent with any number of variables all in real-time!

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*companyname* : string, required

- Your company name

*consumerid*: string, required

*identifier*: string, optional

- You can add any name or identifier like DSN ID

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*viperconfigfile* : string, required

- Full path to VIPER.ENV configuration file on server.

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*partition*: int, optional

- Partition used by kafka to store data. NOTE: Kafka will dynamically store data in partitions.
  Unless you know for sure the partition, you should use the default of -1 to let VIPER
  determine where your data is.

*deploy*: int, optional

- If deploy=1, this will deploy the algorithm to the Deploy folder.  This is useful if you do not
  want to use this algorithm in production, and just testing it.  If just testing, then set deploy=0 (default).  

*modelruns*: int, optional

- Number of iterations for model training

*modelsearchtuner*: int, optional

- An integer between 0-100, this variable will attempt to fine tune the model search space.  A number close to 0 means you will 
  have lots of models but their quality may be low, a number close to 100 (default=80) means you will have fewer models but their 
  quality will be higher

*hpdeport*: int, required

- Port number HPDE is listening on 

*offset* : int, optional

 - If 0 will use the training data from the beginning of the topic
 
*islogistic*: int, optional

- If is 1, the HPDE will switch to logistic modeling, else continous.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the optimal algorithm that best fits your data.

**9. maadstml.viperproducetotopicstream(vipertoken,host,port,topic,producerid,offset,maxrows=0,enabletls=0,delay=100,
	brokerhost='',brokerport=-999,microserviceid='',topicid=-999,mainstreamtopic='',streamstojoin='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topics to produce to in the Kafka broker - this is a topic that contains multiple topics, VIPER will consume from each topic and 
  write results to the produceto topic

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can join these streams
  and produce it to one stream,

*mainstreamtopic*: string, optional

- This is the main stream topic that contain the subtopic streams.

*streamstojoin*: string, optional

- These are the streams you want to join and produce to mainstreamtopic.

*producerid* : string, required

- Producerid of the topic producing to  

*offset* : int
 
 - If 0 will use the stream data from the beginning of the topics, -1 will automatically go to last offset

*maxrows* : int, optional
 
 - If offset=-1, this number will rollback the streams by maxrows amount i.e. rollback=lastoffset-maxrows
 
*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise 0 for plaintext

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the optimal algorithm that best fits your data.

**10. maadstml.vipercreatetrainingdata(vipertoken,host,port,consumefrom,produceto,dependentvariable,
		independentvariables,consumerid,producerid,companyname,partition=-1,enabletls=0,delay=100,
		brokerhost='',brokerport=-999,microserviceid='',topicid=-999)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*consumefrom* : string, required
       
- Topic to consume from 

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, with 10 subtopic streams 
  you can assign a Topicid to each IoT device and each of the 10 subtopics will be associated to each IoT device.
  You can create training dataset for each device.

*produceto* : string, required
       
- Topic to produce to 

*dependentvariable* : string, required
       
- Topic name of the dependentvariable 
 
*independentvariables* : string, required
       
- Topic names of the independentvariables - VIPER will automatically read the data streams.  
  Separate multiple variables by comma. 

*consumerid* : string, required

- Consumerid of the topic to consume to  

*producerid* : string, required

- Producerid of the topic producing to  
 
*partition* : int, optional

- This is the partition that Kafka stored the stream data.  Specifically, the streams you joined 
  from function *viperproducetotopicstream* will be stored in a partition by Kafka, if you 
  want to create a training dataset from these data, then you should use this partition.  This
  ensures you are using the right data to create a training dataset.
    
*companyname* : string, required

- Your company name  

*enabletls*: int, optional

- Set to 1 if Kafka broker is enabled for SSL/TLS encrypted traffic, otherwise set to 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backout from reading messages

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the training data set.

**11. maadstml.vipercreatetopic(vipertoken,host,port,topic,companyname,contactname,contactemail,location,
description,enabletls=0,brokerhost='',brokerport=-999,numpartitions=1,replication=1,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to create 

*companyname* : string, required

- Company name of consumer

*contactname* : string, required

- Contact name of consumer

*contactemail* : string, required

- Contact email of consumer

*location* : string, required

- Location of consumer

*description* : string, required

- Description of why consumer wants to subscribe to topic

*enabletls* : int, optional

- Set to 1 if Kafka is SSL/TLS enabled for encrypted traffic, otherwise 0 for no encryption (plain text)

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*numpartitions*: int, optional

- Number of the parititons to create in the Kafka broker - more parititons the faster Kafka will produce results.

*replication*: int, optional

- Specificies the number of brokers to replicate to - this is important for failover
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the producer id for the topic.

**12. maadstml.viperconsumefromstreamtopic(vipertoken,host,port,topic,consumerid,companyname,partition=-1,
        enabletls=0,delay=100,offset=0,brokerhost='',brokerport=-999,microserviceid='',topicid=-999)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to consume from 

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can consume 
  for each device.

*consumerid* : string, required

- Consumerid associated with topic

*companyname* : string, required

- Your company name

*partition*: int, optional

- Set to a kafka partition number, or -1 to autodetect partition.

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*offset* : int, optional

- Offset to start reading from ..if 0 VIPER will read from the beginning

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the contents of all the topics read


**13. maadstml.vipercreatejointopicstreams(vipertoken,host,port,topic,topicstojoin,companyname,contactname,contactemail,
		description,location,enabletls=0,brokerhost='',brokerport=-999,replication=1,numpartitions=1,microserviceid='',
		topicid=-999)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to consume from 

*topicid* : int, optional

- Topicid represents an id for some entity.  Create a joined topic stream per topicid.

*topicstojoin* : string, required

- Enter two or more topics separated by a comma and VIPER will join them into one topic

*companyname* : string, required

- Company name of consumer

*contactname* : string, required

- Contact name of consumer

*contactemail* : string, required

- Contact email of consumer

*location* : string, required

- Location of consumer

*description* : string, required

- Description of why consumer wants to subscribe to topic

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled, otherwise set to 0 for plaintext.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*numpartitions* : int, optional

- Number of partitions

*replication* : int, optional

- Replication factor

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the producerid of the joined streams
								
**14. maadstml.vipercreateconsumergroup(vipertoken,host,port,topic,groupname,companyname,contactname,contactemail,
		description,location,enabletls=1,brokerhost='',brokerport=-999,microserviceid='')**
		
**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to dd to the group, multiple (active) topics can be separated by comma 

*groupname* : string, required

- Enter the name of the group

*companyname* : string, required

- Company name of consumer

*contactname* : string, required

- Contact name of consumer

*contactemail* : string, required

- Contact email of consumer

*location* : string, required

- Location of consumer

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled, otherwise set to 0 for plaintext.

*description* : string, required

- Description of why consumer wants to subscribe to topic

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the groupid of the group.
								
**15. maadstml.viperconsumergroupconsumefromtopic(vipertoken,host,port,topic,consumerid,groupid,companyname,
		partition=-1,enabletls=0,delay=100,offset=0,rollbackoffset=0,brokerhost='',brokerport=-999,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to dd to the group, multiple (active) topics can be separated by comma 

*consumerid* : string, required

- Enter the consumerid associated with the topic

*groupid* : string, required

- Enter the groups id

*companyname* : string, required

- Enter the company name

*partition*: int, optional

- set to Kakfa partition number or -1 to autodetect

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled, otherwise set to 0 for plaintext.

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*offset* : int, optional

- Offset to start reading from.  If 0, will read from the beginning of topic, or -1 to automatically go to end of topic.

*rollbackoffset* : int, optional

- The number of offsets to rollback the data stream.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the contents of the group.
    
**16. maadstml.vipermodifyconsumerdetails(vipertoken,host,port,topic,companyname,consumerid,contactname='',
contactemail='',location='',brokerhost='',brokerport=9092,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to dd to the group, multiple (active) topics can be separated by comma 

*consumerid* : string, required

- Enter the consumerid associated with the topic

*companyname* : string, required

- Enter the company name

*contactname* : string, optional

- Enter the contact name 

*contactemail* : string, optional
- Enter the contact email

*location* : string, optional

- Enter the location

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns success/failure

**17. maadstml.vipermodifytopicdetails(vipertoken,host,port,topic,companyname,partition=0,enabletls=1,
          isgroup=0,contactname='',contactemail='',location='',brokerhost='',brokerport=9092,microserviceid='')**
     
**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to dd to the group, multiple (active) topics can be separated by comma 

*companyname* : string, required

- Enter the company name

*partition* : int, optional

- You can change the partition in the Kafka topic.

*enabletls* : int, optional

- If enabletls=1, then SSL/TLS is enables in Kafka, otherwise if enabletls=0 it is not.

*isgroup* : int, optional

- This tells VIPER whether this is a group topic if isgroup=1, or a normal topic if isgroup=0

*contactname* : string, optional

- Enter the contact name 

*contactemail* : string, optional
- Enter the contact email

*location* : string, optional

- Enter the location

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns success/failure

**18. maadstml.viperactivatetopic(vipertoken,host,port,topic,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to activate

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns success/failure
    
**19. maadstml.viperdeactivatetopic(vipertoken,host,port,topic,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to deactivate

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns success/failure

**20. maadstml.vipergroupactivate(vipertoken,host,port,groupname,groupid,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*groupname* : string, required
       
- Name of the group

*groupid* : string, required
       
- ID of the group

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns success/failure
   
**21.  maadstml.vipergroupdeactivate(vipertoken,host,port,groupname,groupid,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*groupname* : string, required
       
- Name of the group

*groupid* : string, required
       
- ID of the group

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns success/failure
   
**22. maadstml.viperdeletetopics(vipertoken,host,port,topic,enabletls=1,brokerhost='',brokerport=9092,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topic to delete.  Separate multiple topics by a comma.

*enabletls* : int, optional

- If enabletls=1, then SSL/TLS is enable on Kafka, otherwise if enabletls=0, it is not.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*microserviceid* : string, optional

- microservice to access viper
   
**23.  maadstml.balancebigdata(localcsvfile,numberofbins,maxrows,outputfile,bincutoff,distcutoff,startcolumn=0)**

**Parameters:**	

*localcsvfile* : string, required

- Local file, must be CSV formatted.

*numberofbins* : int, required

- The number of bins for the histogram. You can set to any value but 10 is usually fine.

*maxrows* :  int, required

- The number of rows to return, which will be a subset of your original data.

*outputfile* : string, required

- Your new data will be writted as CSV to this file.

*bincutoff* : float, required. 

-  This is the threshold percentage for the bins. Specifically, the data in each variable is allocated to bins, but many 
   times it will not fall in ALL of the bins.  By setting this percentage between 0 and 1, MAADS will choose variables that
   exceed this threshold to determine which variables have data that are well distributed across bins.  The variables
   with the most distributed values in the bins will drive the selection of the rows in your dataset that give the best
   distribution - this will be very important for MAADS training.  Usually 0.7 is good.

*distcutoff* : float, required. 

-  This is the threshold percentage for the distribution. Specifically, MAADS uses a Lilliefors statistic to determine whether 
   the data are well distributed.  The lower the number the better.  Usually 0.45 is good.
   
*startcolumn* : int, optional

- This tells MAADS which column to start from.  If you have DATE in the first column, you can tell MAADS to start from 1 (columns are zero-based)

RETURNS: Returns a detailed JSON object and new balaced dataset written to outputfile.

**24. maadstml.viperanomalytrain(vipertoken,host,port,consumefrom,produceto,producepeergroupto,produceridpeergroup,consumeridproduceto,
                      streamstoanalyse,companyname,consumerid,producerid,flags,hpdehost,viperconfigfile,
                      enabletls=1,partition=-1,hpdeport=-999,topicid=-999,maintopic='',rollbackoffsets=0,fullpathtotrainingdata='',
					  brokerhost='',brokerport=9092,delay=1000,timeout=120,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can perform anomaly detection/predictions
  for each device.

*maintopic* : string, optional

- This is the maintopic that contains the subtopic streams.

*rollbackoffsets*: int, optional

- This is the percentage to rollback the streams that you are analysing: streamstoanalyse

*fullpathtotrainingdata*: string, optional

- This is the full path to the training dataset to use to find peer groups.

*producepeergroupto* : string, required

- Topic to produce the peer group for anomaly comparisons 

*produceridpeergroup* : string, required

- Producerid for the peer group topic

*consumeridproduceto* : string, required

- Consumer id for the Produceto topic 

*streamstoanalyse* : string, required

- Comma separated list of streams to analyse for anomalies

*flags* : string, required

- These are flags that will be used to select the peer group for each stream.  The flags must have the following format:
  *topic=[topic name],topictype=[numeric or string],threshnumber=[a number between 0 and 10000, i.e. 200],
  lag=[a number between 1 and 20, i.e. 5],zthresh=[a number between 1 and 5, i.e. 2.5],influence=[a number between 0 and 1 i.e. 0.5]*
  
  *threshnumber*: decimal number to determine usual behaviour - only for numeric streams, numbers are compared to the centroid number, 
  a standardized distance is taken and all numbers below the thresholdnumeric are deemed as usual i.e. thresholdnumber=200, any value 
  below is close to the centroid  - you need to experiment with this number.
  
  *lag*: number of lags for the moving mean window, works to smooth the function i.e. lag=5
  
  *zthresh*: number of standard deviations from moving mean i.e. 3.5
  
  *influence*: strength in identifying outliers for both stationary and non-stationary data, i.e. influence=0 ignores outliers 
  when recalculating the new threshold, influence=1 is least robust.  Influence should be between (0,1), i.e. influence=0.5
  
  Flags must be provided for each topic.  Separate multiple flags by ~

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*viperconfigfile* : string, required

- Full path to VIPER.ENV configuration file on server.

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*partition*: int, optional

- Partition used by kafka to store data. NOTE: Kafka will dynamically store data in partitions.
  Unless you know for sure the partition, you should use the default of -1 to let VIPER
  determine where your data is.

*hpdeport*: int, required

- Port number HPDE is listening on 

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*delay* : int, optional

- delay parameter to wait for Kafka to respond - in milliseconds.

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the peer groups for all the streams.

**24.1 maadstml.viperanomalytrainbatch(vipertoken,host,port,consumefrom,produceto,producepeergroupto,produceridpeergroup,consumeridproduceto,
                      streamstoanalyse,companyname,consumerid,producerid,flags,hpdehost,viperconfigfile,
                      enabletls=1,partition=-1,hpdeport=-999,topicid="-999",maintopic='',rollbackoffsets=0,fullpathtotrainingdata='',
					  brokerhost='',brokerport=9092,delay=1000,timeout=120,microserviceid='',timedelay=0,asynctimeout=120)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*topicid* : string, required

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can perform anomaly detection/predictions
  for each device.  Separate multiple topicids by a comma.

*maintopic* : string, optional

- This is the maintopic that contains the subtopic streams.

*rollbackoffsets*: int, optional

- This is the percentage to rollback the streams that you are analysing: streamstoanalyse

*fullpathtotrainingdata*: string, optional

- This is the full path to the training dataset to use to find peer groups.

*producepeergroupto* : string, required

- Topic to produce the peer group for anomaly comparisons 

*produceridpeergroup* : string, required

- Producerid for the peer group topic

*consumeridproduceto* : string, required

- Consumer id for the Produceto topic 

*streamstoanalyse* : string, required

- Comma separated list of streams to analyse for anomalies

*flags* : string, required

- These are flags that will be used to select the peer group for each stream.  The flags must have the following format:
  *topic=[topic name],topictype=[numeric or string],threshnumber=[a number between 0 and 10000, i.e. 200],
  lag=[a number between 1 and 20, i.e. 5],zthresh=[a number between 1 and 5, i.e. 2.5],influence=[a number between 0 and 1 i.e. 0.5]*
  
  *threshnumber*: decimal number to determine usual behaviour - only for numeric streams, numbers are compared to the centroid number, 
  a standardized distance is taken and all numbers below the thresholdnumeric are deemed as usual i.e. thresholdnumber=200, any value 
  below is close to the centroid  - you need to experiment with this number.
  
  *lag*: number of lags for the moving mean window, works to smooth the function i.e. lag=5
  
  *zthresh*: number of standard deviations from moving mean i.e. 3.5
  
  *influence*: strength in identifying outliers for both stationary and non-stationary data, i.e. influence=0 ignores outliers 
  when recalculating the new threshold, influence=1 is least robust.  Influence should be between (0,1), i.e. influence=0.5
  
  Flags must be provided for each topic.  Separate multiple flags by ~

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*viperconfigfile* : string, required

- Full path to VIPER.ENV configuration file on server.

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*partition*: int, optional

- Partition used by kafka to store data. NOTE: Kafka will dynamically store data in partitions.
  Unless you know for sure the partition, you should use the default of -1 to let VIPER
  determine where your data is.

*hpdeport*: int, required

- Port number HPDE is listening on 

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*delay* : int, optional

- delay parameter to wait for Kafka to respond - in milliseconds.

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the peer groups for all the streams.


**25. maadstml.viperanomalypredict(vipertoken,host,port,consumefrom,produceto,consumeinputstream,produceinputstreamtest,produceridinputstreamtest,
                      streamstoanalyse,consumeridinputstream,companyname,consumerid,producerid,flags,hpdehost,viperconfigfile,
                      enabletls=1,partition=-1,hpdeport=-999,topicid=-999,maintopic='',rollbackoffsets=0,fullpathtopeergroupdata='',
					  brokerhost='',brokerport=9092,delay=1000,timeout=120,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*consumeinputstream* : string, required

- Topic of the input stream to test for anomalies

*produceinputstreamtest* : string, required

- Topic to store the input stream data for analysis

*produceridinputstreamtest* : string, required

- Producer id for the produceinputstreamtest topic 

*streamstoanalyse* : string, required

- Comma separated list of streams to analyse for anomalies

*flags* : string, required

- These are flags that will be used to select the peer group for each stream.  The flags must have the following format:
  *riskscore=[a number between 0 and 1]~complete=[and, or, pvalue i.e. p50 means streams over 50% that have an anomaly]~type=[and,or this will 
  determine what logic to apply to v and sc],topic=[topic name],topictype=[numeric or string],v=[v>some value, v<some value, or valueany],
  sc=[sc>some number, sc<some number - this is the score for the anomaly test]
  
  if using strings, the specify flags: type=[and,or],topic=[topic name],topictype=string,stringcontains=[0 or 1 - 1 will do a substring test, 
  0 will equate the strings],v2=[any text you want to test - use | for OR or ^ for AND],sc=[score value, sc<some value, sc>some value]
 
  *riskscore*: this the riskscore threshold.  A decimal number between 0 and 1, use this as a threshold to flag anomalies.

  *complete* : If using multiple streams, this will test each stream to see if the computed riskscore and perform an AND or OR on each risk value
  and take an average of the risk scores if using AND.  Otherwise if at least one stream exceeds the riskscore it will return.
  
  *type*: AND or OR - if using v or sc, this is used to apply the appropriate logic between v and sc.  For example, if type=or, then VIPER 
  will see if a test value is less than or greater than V, OR, standarzided value is less than or greater than sc.  
  
  *sc*: is a standarized variavice between the peer group value and test value.
  
  *v1*: is a user chosen value which can be used to test for a particular value.  For example, if you want to flag values less then 0, 
  then choose v<0 and VIPER will flag them as anomolous.

  *v2*: if analysing string streams, v2 can be strings you want to check for. For example, if I want to check for two
  strings: Failed and Attempt Failed, then set v2=Failed^Attempt Failed, where ^ tells VIPER to perform an AND operation.  
  If I want either to exist, 2=Failed|Attempt Failed, where | tells VIPER to perform an OR operation.

  *stringcontains* : if using string streams, and you want to see if a particular text value exists and flag it - then 
  if stringcontains=1, VIPER will test for substrings, otherwise it will equate the strings. 
  
  
  Flags must be provided for each topic.  Separate multiple flags by ~

*consumeridinputstream* : string, required

- Consumer id of the input stream topic: consumeinputstream

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*viperconfigfile* : string, required

- Full path to VIPER.ENV configuration file on server.

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*partition*: int, optional

- Partition used by kafka to store data. NOTE: Kafka will dynamically store data in partitions.
  Unless you know for sure the partition, you should use the default of -1 to let VIPER
  determine where your data is.

*hpdeport*: int, required

- Port number HPDE is listening on 

*topicid* : int, optional

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can perform anomaly 
  prediction for each device.

*maintopic* : string, optional

- This is the maintopic that contains the subtopic streams.

*rollbackoffsets*: int, optional

- This is the percentage to rollback the streams that you are analysing: streamstoanalyse

*fullpathtopeergroupdata*: string, optional

- This is the full path to the peer group you found in viperanomalytrain; this will be used for anomaly detection.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*delay* : int, optional

- delay parameter to wait for Kafka to respond - in milliseconds.

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the peer groups for all the streams.

**25.1 maadstml.viperanomalypredictbatch(vipertoken,host,port,consumefrom,produceto,consumeinputstream,produceinputstreamtest,produceridinputstreamtest,
                      streamstoanalyse,consumeridinputstream,companyname,consumerid,producerid,flags,hpdehost,viperconfigfile,
                      enabletls=1,partition=-1,hpdeport=-999,topicid="-999",maintopic='',rollbackoffsets=0,fullpathtopeergroupdata='',
					  brokerhost='',brokerport=9092,delay=1000,timeout=120,microserviceid='',timedelay=0,asynctimeout=120)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600

*consumefrom* : string, required
       
- Topic to consume from in the Kafka broker

*produceto* : string, required

- Topic to produce results of the prediction to

*consumeinputstream* : string, required

- Topic of the input stream to test for anomalies

*produceinputstreamtest* : string, required

- Topic to store the input stream data for analysis

*produceridinputstreamtest* : string, required

- Producer id for the produceinputstreamtest topic 

*streamstoanalyse* : string, required

- Comma separated list of streams to analyse for anomalies

*flags* : string, required

- These are flags that will be used to select the peer group for each stream.  The flags must have the following format:
  *riskscore=[a number between 0 and 1]~complete=[and, or, pvalue i.e. p50 means streams over 50% that have an anomaly]~type=[and,or this will 
  determine what logic to apply to v and sc],topic=[topic name],topictype=[numeric or string],v=[v>some value, v<some value, or valueany],
  sc=[sc>some number, sc<some number - this is the score for the anomaly test]
  
  if using strings, the specify flags: type=[and,or],topic=[topic name],topictype=string,stringcontains=[0 or 1 - 1 will do a substring test, 
  0 will equate the strings],v2=[any text you want to test - use | for OR or ^ for AND],sc=[score value, sc<some value, sc>some value]
 
  *riskscore*: this the riskscore threshold.  A decimal number between 0 and 1, use this as a threshold to flag anomalies.

  *complete* : If using multiple streams, this will test each stream to see if the computed riskscore and perform an AND or OR on each risk value
  and take an average of the risk scores if using AND.  Otherwise if at least one stream exceeds the riskscore it will return.
  
  *type*: AND or OR - if using v or sc, this is used to apply the appropriate logic between v and sc.  For example, if type=or, then VIPER 
  will see if a test value is less than or greater than V, OR, standarzided value is less than or greater than sc.  
  
  *sc*: is a standarized variavice between the peer group value and test value.
  
  *v1*: is a user chosen value which can be used to test for a particular value.  For example, if you want to flag values less then 0, 
  then choose v<0 and VIPER will flag them as anomolous.

  *v2*: if analysing string streams, v2 can be strings you want to check for. For example, if I want to check for two
  strings: Failed and Attempt Failed, then set v2=Failed^Attempt Failed, where ^ tells VIPER to perform an AND operation.  
  If I want either to exist, 2=Failed|Attempt Failed, where | tells VIPER to perform an OR operation.

  *stringcontains* : if using string streams, and you want to see if a particular text value exists and flag it - then 
  if stringcontains=1, VIPER will test for substrings, otherwise it will equate the strings. 
  
  
  Flags must be provided for each topic.  Separate multiple flags by ~

*consumeridinputstream* : string, required

- Consumer id of the input stream topic: consumeinputstream

*companyname* : string, required

- Your company name

*consumerid*: string, required

- Consumerid associated with the topic to consume from

*producerid*: string, required

- Producerid associated with the topic to produce to

*hpdehost*: string, required

- Address of HPDE 

*viperconfigfile* : string, required

- Full path to VIPER.ENV configuration file on server.

*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise set to 0 for plaintext.

*partition*: int, optional

- Partition used by kafka to store data. NOTE: Kafka will dynamically store data in partitions.
  Unless you know for sure the partition, you should use the default of -1 to let VIPER
  determine where your data is.

*hpdeport*: int, required

- Port number HPDE is listening on 

*topicid* : string, required

- Topicid represents an id for some entity.  For example, if you have 1000 IoT devices, you can perform anomaly 
  prediction for each device. Separate  multiple topic ids by a comma.

*maintopic* : string, optional

- This is the maintopic that contains the subtopic streams.

*rollbackoffsets*: int, optional

- This is the percentage to rollback the streams that you are analysing: streamstoanalyse

*fullpathtopeergroupdata*: string, optional

- This is the full path to the peer group you found in viperanomalytrain; this will be used for anomaly detection.

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file

*delay* : int, optional

- delay parameter to wait for Kafka to respond - in milliseconds.

*timeout* : int, optional

 - Number of seconds that VIPER waits when trying to make a connection to HPDE.
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: Returns a JSON object of the peer groups for all the streams.

**26. maadstml.viperpreprocessproducetotopicstream(VIPERTOKEN,host,port,topic,producerid,offset,maxrows=0,enabletls=0,delay=100,
                brokerhost='',brokerport=-999,microserviceid='',topicid=-999,streamstojoin='',preprocesslogic='',
				preprocessconditions='',identifier='',preprocesstopic='',array=0,saveasarray=0,rawdataoutput=0)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topics to produce to in the Kafka broker - this is a topic that contains multiple topics, VIPER will consume from each 
   topic and write the aggregated results back to this stream.

*array* : int, optional

- Set array=1 if you produced data (from viperproducetotopic) as an array.  

*rawdataoutput* : int, optional

- Set rawdataoutput=1 and the raw data used for preprocessing will be added to the output json.  

*preprocessconditions* : string, optional

- You can set conditions to aggregate functions: MIN, MAX, AVG, COUNT, COUNTSTR, DIFF, DIFFMARGIN, SUM, MEDIAN, VARIANCE, OUTLIERS, OUTLIERSX-Y, VARIED, 
  ANOMPROB,ANOMPROBX-Y, CONSISTENCY,
  ENTROPY, AUTOCORR, TREND, IQR (InterQuartileRange), Midhinge, GM (Geometric mean), HM (Harmonic mean), Trimean, CV (coefficient of Variation), 
  Mad (Mean absolute deviation),Skewness, Kurtosis, Spikedetect, Unique, Uniquestr, Timediff: time should be in this layout:2006-01-02T15:04:05,
  Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
  average time in seconds between consecutive dates.
  Spikedetect uses a Zscore method to detect spikes in the data using lag of 5, StD of 3.5 from mean and influence of 0.5.
  Geodiff (returns distance in Kilometers between two lat/long points)
  Unique Checks numeric data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
  current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
  You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
  will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
  between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
  for data quality and data assurance programs for any number of data streams.

  Uniquestr Checks string data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Uniquecount Checks numeric data for duplication.  Returns count of unique numbers.
 
  Uniquestrcount Checks string data for duplication.  Returns count of unique strings.
  
  CONSISTENCY checks if the data all have consistent data types. Returns 1 for consistent data types, 0 otherwise.

  Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 
  
  RAW for no processing.
  
  ANOMPROB=Anomaly Probability, it will run several algorithms on the data stream window to determine a probaility of anomalous
  behaviour.  This can be cross-refenced with OUTLIERS.  It can be very powerful way to detection
  issues with devices. VARIED will determine if the values in the window are all the same, or varied: it will return 1 for varied,
  0 if values are all the same.  This is useful if you want to know if something changed in the stream.
  
  ANOMPROBX-Y (similar to OUTLIERSX-Y), where X and Y are numbers or "n".  If "n" means examine all anomalies for patterns.
  They allow you to check if the anomalies in the streams are truly anomalies and not some
  pattern.  For example, if a IoT device shuts off and turns on again routinely, this may be picked up as an anomaly when in fact
  it is normal behaviour.  So, to ignore these cases, if ANOMPROB2-5, this tells Viper, check anomalies with patterns of 2-5 peaks.
  If the stream has two classes and these two classes are like 0 and 1000, and show a pattern, then they should not be considered an anomaly.
  Meaning, class=0, is the device shutting down, class=1000 is the device turning back on.  If ANOMPROB3-10, Viper will check for 
  patterns of classes 3 to 10 to see if they recur routinely.  This is very helpful to reduce false positives and false negatives.
  
  For example, preprocessconditions='humidity=55,60:temperature=34,n', and preprocesslogic='max,count', means
  Get the MAX value of values in humidity if humidity is between [55,60], and Count values in
  temperature if temperature >=34.  
  
*preprocesstopic* : string, optional

- You can specify a topic for the preprocessed message.  VIPER will automatically dump the preprocessed results to this topic. 
  
*identifier* : string, optional 

- Add any identifier like DSN ID. 

*producerid* : string, required

- Producerid of the topic producing to  

*offset* : int, optional
 
 - If 0 will use the stream data from the beginning of the topics, -1 will automatically go to last offset

*saveasarray* : int, optional

- Set to 1, to save the preprocessed jsons as a json array.  This is very helpful if you want to do machine learning
  or further query the preprocessed json because each processed json are time synchronized.  For example, if you want to compare
  different preprocessed streams the date/time of the data is synchronized to give you impacts of one
  stream on another.

*maxrows* : int, optional
 
 - If offset=-1, this number will rollback the streams by maxrows amount i.e. rollback=lastoffset-maxrows
 
*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise 0 for plaintext

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

*topicid* : int, optional

- This represents the IoT device number or any entity

*streamstojoin* : string, optional

- If you entered topicid, you need to enter the streams you want to pre-process

*preprocesslogic* : string, optional

- Here you need to specify how you want to pre-process the streams.  You can perform the following operations:
  MAX, MIN, AVG, COUNT, COUNTSTR, SUM, DIFF, DIFFMARGIN, VARIANCE, MEDIAN, OUTLIERS, OUTLIERSX-Y, VARIED, ANOMPROB, ANOMPROBX-Y, ENTROPY, 
  AUTOCORR, TREND, CONSISTENCY, Unique, Uniquestr, Geodiff (returns distance in Kilometers between two lat/long points),
  IQR (InterQuartileRange), Midhinge, GM (Geometric mean), HM (Harmonic mean), Trimean, CV (coefficient of Variation), 
  Mad (Mean absolute deviation), Skewness, Kurtosis, Spikedetect, Timediff: time should be in this layout:2006-01-02T15:04:05,
  Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
  average time in seconds between consecutive dates.
  Uniquecount Checks numeric data for duplication.  Returns count of unique numbers.

  Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
  current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
  You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
  will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
  between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
  for data quality and data assurance programs for any number of data streams.
 
  Uniquestrcount Checks string data for duplication.  Returns count of unique strings.
  
  Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 

  RAW for no processing.
  
  Spikedetect uses a Zscore method to detect spikes in the data using lag of 5, StD of 3.5 from mean and influence of 0.5.

  The order of the operation must match the 
  order of the stream.  If you specified topicid, you can perform TML on the new preprocessed stream append appending: 
  _preprocessed_processlogic
  For example, if streamstojoin="stream1,stream2,streams3", and preprocesslogic="min,max,diff", the new streams will be:
  stream1_preprocessed_Min, stream2_preprocessed_Max, stream3_preprocessed_Diff.

RETURNS: Returns preprocessed JSON.

**27. maadstml.areyoubusy(host,port)**

**Parameters:**	

*host* : string, required
 
- You can get the host by determining all the hosts that are listening in your machine.   
  You use this code: https://github.com/smaurice101/transactionalmachinelearning/blob/main/checkopenports


*port* : int, required
 
- You can get the port by determining all the ports that are listening in your machine. 
  You use this code: https://github.com/smaurice101/transactionalmachinelearning/blob/main/checkopenports 
  
RETURNS: Returns a list of available VIPER and HPDE with their HOST and PORT.

**28. maadstml.viperstreamquery(VIPERTOKEN,host,port,topic,producerid,offset=-1,maxrows=0,enabletls=1,delay=100,brokerhost='',
                                          brokerport=-999,microserviceid='',topicid=-999,streamstojoin='',preprocessconditions='',
                                          identifier='',preprocesstopic='',description='',array=0)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*topic* : string, required
       
- Topics to produce to in the Kafka broker - this is a topic that contains multiple topics, VIPER will consume from each 
   topic and write the aggregated results back to this stream.

*producerid* : string, required
       
- Producer id of topic


*offset* : int, optional
 
 - If 0 will use the stream data from the beginning of the topics, -1 will automatically go to last offset

*maxrows* : int, optional
 
 - If offset=-1, this number will rollback the streams by maxrows amount i.e. rollback=lastoffset-maxrows
 
*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise 0 for plaintext

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

*topicid* : int, optional

- This represents the IoT device number or any entity

*streamstojoin* : string, required

- Identify multiple streams to join, separate by comma.  For example, if you preprocessed Power, Current, Voltage:
 **streamstojoin="Power_preprocessed_Avg,Current_preprocessed_Min,Voltage_preprocessed_Avg,Current_preprocessed_Trend"**

*preprocessconditions* : string, required

 - You apply strict conditions to a MAX of 3 streams.  You can use >, <, =, AND, OR.  You can add as many conditions as you like.
   Separate multiple conditions by semi-colon. You **cannot mix** AND and OR.  For example, 
  **preprocessconditions='Power_preprocessed_Avg > 139000:Power_preprocessed_Avg < 1000 or Voltage_preprocessed_Avg > 120000 
  or Current_preprocessed_Min=0:Voltage_preprocessed_Avg > 120000 and Current_preprocessed_Trend>0'**
  
*identifier*: string, optional
 
 - Add an identifier text to the result.  This is a label, and useful if you want to identify the result for some IOT device.  
 
*preprocesstopic* : string, optional

 - The topic to produce the query results to.  
 
*description* : string, optional

 - You can give each query condition a description.  Separate multiple desction by semi-colon.  
 
*array* : int, optional

 - Set to 1 if you are reading a JSON ARRAY, otherwise 0.
 
RETURNS: 1 if the condition is TRUE (condition met), 0 if false (condition not met)

**28.1 maadstml.viperstreamquerybatch(VIPERTOKEN,host,port,topic,producerid,offset=-1,maxrows=0,enabletls=1,delay=100,brokerhost='',
                                          brokerport=-999,microserviceid='',topicid="-999",streamstojoin='',preprocessconditions='',
                                          identifier='',preprocesstopic='',description='',array=0,timedelay=0,asynctimeout=120)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600

*topic* : string, required
       
- Topics to produce to in the Kafka broker - this is a topic that contains multiple topics, VIPER will consume from each 
   topic and write the aggregated results back to this stream.

*producerid* : string, required
       
- Producer id of topic


*offset* : int, optional
 
 - If 0 will use the stream data from the beginning of the topics, -1 will automatically go to last offset

*maxrows* : int, optional
 
 - If offset=-1, this number will rollback the streams by maxrows amount i.e. rollback=lastoffset-maxrows
 
*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise 0 for plaintext

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

*topicid* : string, required

- This represents the IoT device number or any entity.  Separate multiple topic ids by a comma.

*streamstojoin* : string, required

- Identify multiple streams to join, separate by comma.  For example, if you preprocessed Power, Current, Voltage:
 **streamstojoin="Power_preprocessed_Avg,Current_preprocessed_Min,Voltage_preprocessed_Avg,Current_preprocessed_Trend"**

*preprocessconditions* : string, required

 - You apply strict conditions to a MAX of 3 streams.  You can use >, <, =, AND, OR.  You can add as many conditions as you like.
   Separate multiple conditions by semi-colon. You **cannot mix** AND and OR.  For example, 
  **preprocessconditions='Power_preprocessed_Avg > 139000:Power_preprocessed_Avg < 1000 or Voltage_preprocessed_Avg > 120000 
  or Current_preprocessed_Min=0:Voltage_preprocessed_Avg > 120000 and Current_preprocessed_Trend>0'**
  
*identifier*: string, optional
 
 - Add an identifier text to the result.  This is a label, and useful if you want to identify the result for some IOT device.  
 
*preprocesstopic* : string, optional

 - The topic to produce the query results to.  
 
*description* : string, optional

 - You can give each query condition a description.  Separate multiple desction by semi-colon.  
 
*array* : int, optional

 - Set to 1 if you are reading a JSON ARRAY, otherwise 0.
 
RETURNS: 1 if the condition is TRUE (condition met), 0 if false (condition not met)

**29. maadstml.viperpreprocessbatch(VIPERTOKEN,host,port,topic,producerid,offset,maxrows=0,enabletls=0,delay=100,
                brokerhost='',brokerport=-999,microserviceid='',topicid="-999",streamstojoin='',preprocesslogic='',
				preprocessconditions='',identifier='',preprocesstopic='',array=0,saveasarray=0,timedelay=0,asynctimeout=120,rawdataoutput=0)**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*asynctimeout* : int, optional
 
  -This is the timeout in seconds for the Python library async function.

*rawdataoutput* : int, optional
 
  -Set rawdataoutput=1 to output the raw preprocessing data to the Json.

*timedelay* : int, optional

 - Timedelay is in SECONDS. Because batch runs continuously in the background, this will cause Viper to pause 
   *timedelay* seconds when reading and writing to Kafka.  For example, if the raw data is being generated
   every 3600 seconds, it may make sense to set timedelay=3600

*topic* : string, required
       
- Topics to produce to in the Kafka broker - this is a topic that contains multiple topics, VIPER will consume from each 
   topic and write the aggregated results back to this stream.

*array* : int, optional

- Set array=1 if you produced data (from viperproducetotopic) as an array.  

*preprocessconditions* : string, optional

- You can set conditions to aggregate functions: MIN, MAX, AVG, COUNT, COUNTSTR, DIFF, SUM, MEDIAN, VARIANCE, OUTLIERS, OUTLIERSX-Y, VARIED, ANOMPROB,ANOMPROBX-Y,
  ENTROPY, AUTOCORR, TREND, IQR (InterQuartileRange), Midhinge, GM (Geometric mean), HM (Harmonic mean), Trimean, CV (coefficient of Variation), 
  Mad (Mean absolute deviation),Skewness, Kurtosis, Spikedetect, Unique, Uniquestr, Timediff: time should be in this layout:2006-01-02T15:04:05,
  Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
  average time in seconds between consecutive dates.  Spikedetect uses a Zscore method to detect spikes in the data using lag of 5, 
  StD of 3.5 from mean and influence of 0.5.  Geodiff (returns distance in Kilometers between two lat/long points).

  Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
  current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
  You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
  will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
  between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
  for data quality and data assurance programs for any number of data streams.
  
  Unique Checks numeric data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Uniquestr Checks string data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.
  Uniquecount Checks numeric data for duplication.  Returns count of unique numbers. 
  Uniquestrcount Checks string data for duplication.  Returns count of unique strings.
  
  Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 

  ANOMPROB=Anomaly Probability, it will run several algorithms on the data stream window to determine a probaility of anomalous
  behaviour.  This can be cross-refenced with OUTLIERS.  It can be very powerful way to detection
  issues with devices. VARIED will determine if the values in the window are all the same, or varied: it will return 1 for varied,
  0 if values are all the same.  This is useful if you want to know if something changed in the stream.
  
  ANOMPROBX-Y (similar to OUTLIERSX-Y), where X and Y are numbers or "n".  If "n" means examine all anomalies for patterns.
  They allow you to check if the anomalies in the streams are truly anomalies and not some
  pattern.  For example, if a IoT device shuts off and turns on again routinely, this may be picked up as an anomaly when in fact
  it is normal behaviour.  So, to ignore these cases, if ANOMPROB2-5, this tells Viper, check anomalies with patterns of 2-5 peaks.
  If the stream has two classes and these two classes are like 0 and 1000, and show a pattern, then they should not be considered an anomaly.
  Meaning, class=0, is the device shutting down, class=1000 is the device turning back on.  If ANOMPROB3-10, Viper will check for 
  patterns of classes 3 to 10 to see if they recur routinely.  This is very helpful to reduce false positives and false negatives.
  
  For example, preprocessconditions='humidity=55,60:temperature=34,n', and preprocesslogic='max,count', means
  Get the MAX value of values in humidity if humidity is between [55,60], and Count values in
  temperature if temperature >=34.  
  
*preprocesstopic* : string, optional

- You can specify a topic for the preprocessed message.  VIPER will automatically dump the preprocessed results to this topic. 
  
*identifier* : string, optional 

- Add any identifier like DSN ID. Note, for multiple identifiers per topicid, you can separate by pipe "|".

*producerid* : string, required

- Producerid of the topic producing to  

*offset* : int, optional
 
 - If 0 will use the stream data from the beginning of the topics, -1 will automatically go to last offset

*saveasarray* : int, optional

- Set to 1, to save the preprocessed jsons as a json array.  This is very helpful if you want to do machine learning
  or further query the preprocessed json because each processed json are time synchronized.  For example, if you want to compare
  different preprocessed streams the date/time of the data is synchronized to give you impacts of one
  stream on another.

*maxrows* : int, optional
 
 - If offset=-1, this number will rollback the streams by maxrows amount i.e. rollback=lastoffset-maxrows
 
*enabletls*: int, optional

- Set to 1 if Kafka broker is SSL/TLS enabled for encrypted traffic, otherwise 0 for plaintext

*delay*: int, optional

- Time in milliseconds before VIPER backsout from reading messages

*brokerhost* : string, optional

- Address of Kafka broker - if none is specified it will use broker address in VIPER.ENV file

*brokerport* : int, optional

- Port Kafka is listening on - if none is specified it will use port in the VIPER.ENV file
 
*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

*topicid* : string, required

- This represents the IoT device number or any entity.  You can specify multiple ids 
  separated by a comma: topicid="1,2,4,5". 

*streamstojoin* : string, optional

- If you entered topicid, you need to enter the streams you want to pre-process

*preprocesslogic* : string, optional

- Here you need to specify how you want to pre-process the streams.  You can perform the following operations:
  MAX, MIN, AVG, COUNT, COUNTSTR, SUM, DIFF, VARIANCE, MEDIAN, OUTLIERS, OUTLIERSX-Y, VARIED, ANOMPROB, ANOMPROBX-Y, ENTROPY, AUTOCORR, TREND,
  IQR (InterQuartileRange), Midhinge, CONSISTENCY, GM (Geometric mean), HM (Harmonic mean), Trimean, CV (coefficient of Variation), 
  Mad (Mean absolute deviation), Skewness, Kurtosis, Spikedetect, Unique, Uniquestr, Timediff: time should be in this layout:2006-01-02T15:04:05,
  Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
  average time in seconds between consecutive dates. 
  Geodiff (returns distance in Kilometers between two lat/long points).
  Spikedetect uses a Zscore method to detect spikes in the data using lag of 5, StD of 3.5 from mean and influence of 0.5.
  Uniquecount Checks numeric data for duplication.  Returns count of unique numbers.
  Uniquestrcount Checks string data for duplication.  Returns count of unique strings.

  Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
  current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
  You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
  will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
  between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
  for data quality and data assurance programs for any number of data streams.

  Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 

  The order of the operation must match the 
  order of the stream.  If you specified topicid, you can perform TML on the new preprocessed stream append appending: 
  _preprocessed_processlogic
  For example, if streamstojoin="stream1,stream2,streams3", and preprocesslogic="min,max,diff", the new streams will be:
  stream1_preprocessed_Min, stream2_preprocessed_Max, stream3_preprocessed_Diff.

RETURNS: None.

**30. maadstml.viperlisttopics(vipertoken,host,port=-999,brokerhost='', brokerport=-999,microserviceid='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.


*brokerhost* : string, optional

- Address where Kafka broker is running - if none is specified, the Kafka broker address in the VIPER.ENV file will be used.


*brokerport* : int, optional

- Port on which Kafka is listenting.

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: A JSON formatted object of all the topics in the Kafka broker.


**31. maadstml.viperpreprocesscustomjson(VIPERTOKEN,host,port,topic,producerid,offset,jsoncriteria='',rawdataoutput=0,maxrows=0,
                   enabletls=0,delay=100,brokerhost='',brokerport=-999,microserviceid='',topicid=-999,streamstojoin='',preprocesslogic='',
                   preprocessconditions='',identifier='',preprocesstopic='',array=0,saveasarray=0,timedelay=0,asynctimeout=120,
                   usemysql=0,tmlfilepath='',pathtotmlattrs='')**

**Parameters:**	

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*topic* : string, required

- Topic containing the raw data to consume.

*producerid* : string, required

- Id of the Topic.

*offset* : int, required

- Offset to consume from.  Set to -1 if consuming the last offset of topic.

*jsoncriteria* : string, required

- This is the JSON path to the data you want to consume . It must be the following format: 

            *UID* is path to the main id. For example, Patient ID
			
			*filter* is the path to something that filter the jsons 
			
			*subtopic* is the path to the subtopics in the json (several paths can be specified)
			
			*values* is the path to the Values of the subtopics - Subtopic and Value must have 1-1 match
			
			*identifiers* is the path to any special identifiers for the subtopics
			
			*datetime* is the path to the datetime of the message
			
			*msgid* is the path to any msg id

*For example:*

     jsoncriteria='uid=subject.reference,filter:resourceType=Observation~\
                   subtopics=code.coding.0.code,component.0.code.coding.0.code,component.1.code.coding.0.code~\
                   values=valueQuantity.value,component.0.valueQuantity.value,component.1.valueQuantity.value~\
                   identifiers=code.coding.0.display,component.0.code.coding.0.display,component.1.code.coding.0.display~\
                   datetime=effectiveDateTime~\
                   msgid=id'

*rawdataoutput* : int, optional

- set to 1 if you want to output the raw data.  Note: This could involve a lot of data and Kafka may refuse to write to the topic.

*maxrows* : int, optional

- Number of offsets or percentage to roll back the data stream

*enabletls* : int, optional

- Set to 1 for TLS encrpyted traffic

*delay* : int, optional

- Delay to wait for Kafka to finish writing to topic

*topicid* : int, optional

- Since you are consuming raw data, this is not needed.  Topicid will be set for you.

*streamstojoin* : string, optional

- This is ignored for raw data.

*preprocesslogic* : string, optional

- Specify your preprocess algorithms. For example, You can set conditions to aggregate functions: MIN, MAX, AVG, COUNT, COUNTSTR, DIFF, 
  DIFFMARGIN, SUM, MEDIAN, VARIANCE, OUTLIERS, OUTLIERSX-Y, VARIED, 
  ANOMPROB,ANOMPROBX-Y, CONSISTENCY,
  ENTROPY, AUTOCORR, TREND, IQR (InterQuartileRange), Midhinge, GM (Geometric mean), HM (Harmonic mean), Trimean, CV (coefficient of Variation), 
  Mad (Mean absolute deviation),Skewness, Kurtosis, Spikedetect, Unique, Uniquestr, Timediff: time should be in this layout:2006-01-02T15:04:05,
  Timediff returns the difference in seconds between the first date/time and last datetime. Avgtimediff returns the 
  average time in seconds between consecutive dates.
  Spikedetect uses a Zscore method to detect spikes in the data using lag of 5, StD of 3.5 from mean and influence of 0.5.
  Geodiff (returns distance in Kilometers between two lat/long points)
  Unique Checks numeric data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Dataage_[UTC offset]_[timetype], dataage can be used to check the last update time of the data in the data stream from
  current local time.  You can specify the UTC offset to adjust the current time to match the timezone of the data stream.
  You can specify timetype as millisecond, second, minute, hour, day.  For example, if Dataage_1_minute, then this processtype
  will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference
  between the data stream timestamp and current local time and return the difference in minutes.  This is a very powerful processtype
  for data quality and data assurance programs for any number of data streams.

  Uniquestr Checks string data for duplication.  Returns 1 if no data duplication (unique), 0 otherwise.

  Uniquecount Checks numeric data for duplication.  Returns count of unique numbers.
 
  Uniquestrcount Checks string data for duplication.  Returns count of unique strings.
  
  CONSISTENCY checks if the data all have consistent data types. Returns 1 for consistent data types, 0 otherwise.

  Meanci95 or Meanci99 - returns a 95% or 99% confidence interval: mean, low, high 
  
  RAW for no processing.

*preprocessconditions* : string, optional

- Specify any preprocess conditions

*identifier* : string, optional

- Specify any text identifier

*preprocesstopic* : string, optional

- Specify the name of the topic to write preprocessed results.

*array* : int, optional

- Ignored for raw data - as jsoncriteria specifies json path

*saveasarray* : int, optional

- Set to 1 to save as json array

*timedelay* : int, optional

- Delay to wait for response from Kafka.

*asynctimeout* : int, optional

- Maximum delay for asyncio in Python library

*usemysql* : int, optional

- Set to 1 to specify whether MySQL is used to store TMLIDs.  This will be needed to track individual objects.

*tmlfilepath* : string, optional

- Ignored. 

*pathtotmlattrs* : string, optional

- Specifiy any attributes for the TMLID.  Here you can specify OEM, Latitude, Longitude, and Location JSON paths:

     pathtotmlattrs='oem=id,lat=subject.reference,long=component.0.code.coding.0.display,location=component.1.valueQuantity.value'

*port* : int, required

- Port on which VIPER is listenting.

*brokerhost* : string, optional

- Address where Kafka broker is running - if none is specified, the Kafka broker address in the VIPER.ENV file will be used.


*brokerport* : int, optional

- Port on which Kafka is listenting.

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: null

**32. maadstml.viperstreamcorr(vipertoken,host,port,topic,producerid,offset=-1,maxrows=0,enabletls=1,delay=100,brokerhost='',
                                 brokerport=-999,microserviceid='',topicid=-999,streamstojoin='',
                                 identifier='',preprocesstopic='',description='',array=0, wherecondition='',
                                 wheresearchkey='PreprocessIdentifier',rawdataoutput=1,threshhold=0,pvalue=0,
                                 identifierextractpos="",topcorrnum=5,jsoncriteria='',tmlfilepath='',usemysql=0,
                                 pathtotmlattrs='',mincorrvectorlen=5,writecorrstotopic='',outputtopicnames=0,nlp=0,
                                 correlationtype='',docrosscorr=0)**

**Parameters:**	Perform Stream correlations

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*topic* : string, required

- Topic containing the raw data to consume.

*producerid* : string, required

- Id of the Topic.

*wherecondition* : string, optional

- Specify the where condition.  For example, if you want to filter the data on "males", enter males.  You can
  specify exact match by using [males], or substring by using (males), or "not" includes by using {males}  

*correlationtype* : string, optional

-  Specify type of correlation you want to do.  Valid values are: kendall,spearman,pearson,ks
   You can specify some, or all (leave blank and ALL will be done), separated by comma. ks=kolmogorov-Smirnov test.

*docrosscorr* : int, optional

- Set to 1 if you want to do cross-correlations with 4 variables, not the normal 2-variable. 

*wheresearchkey* : string, optional

- Specify the where search key.  This key will be searched for "males".  

*description* : string, optional

- Specify a text description for this correlation.  

*identifierextractpos* : string, optional

- If doing correlation on data you have already preprocessed, you can extract the identifier from the identifier field
  in the preprocessed json. 

*offset* : int, required

- Offset to consume from.  Set to -1 if consuming the last offset of topic.

*mincorrvectorlen* : int, optional

- Minimum length of the data variables you are correlating.

*topcorrnum* : int, optional

- Top number of sorted correlations to output

*threshhold* : int, optional

- Threshold for the correlation coefficient.  Must range from 0-100.  All correlations will be greater than this number.

*pvalue* : int, optional

- Pvalue threshold for the p-values.  Must range from 0-100.  All p-values will be below this number.

*writecorrstotopic* : string, optional

- This is the name of the topic that Viper will write "individual" correlation results to.  

*outputtopicnames* : int, optional

- Set to 1 if you want to write out topic names.

*nlp* : int, optional

- Set to 1 if you want to correlate TEXT data by using natural language processing (NLP).

*jsoncriteria* : string, required

- This is the JSON path to the data you want to consume . It must be the following format: 

            *UID* is path to the main id. For example, Patient ID
			
			*filter* is the path to something that filter the jsons 
			
			*subtopic* is the path to the subtopics in the json (several paths can be specified)
			
			*values* is the path to the Values of the subtopics - Subtopic and Value must have 1-1 match
			
			*identifiers* is the path to any special identifiers for the subtopics
			
			*datetime* is the path to the datetime of the message
			
			*msgid* is the path to any msg id

*For example:*

     jsoncriteria='uid=subject.reference,filter:resourceType=Observation~\
                   subtopics=code.coding.0.code,component.0.code.coding.0.code,component.1.code.coding.0.code~\
                   values=valueQuantity.value,component.0.valueQuantity.value,component.1.valueQuantity.value~\
                   identifiers=code.coding.0.display,component.0.code.coding.0.display,component.1.code.coding.0.display~\
                   datetime=effectiveDateTime~\
                   msgid=id'

*rawdataoutput* : int, optional

- set to 1 if you want to output the raw data.  Note: This could involve a lot of data and Kafka may refuse to write to the topic.

*maxrows* : int, optional

- Number of offsets or percentage to roll back the data stream

*enabletls* : int, optional

- Set to 1 for TLS encrpyted traffic

*delay* : int, optional

- Delay to wait for Kafka to finish writing to topic

*topicid* : int, optional

- Since you are consuming raw data, this is not needed.  Topicid will be set for you.

*streamstojoin* : string, optional

- This is ignored for raw data.

*preprocesslogic* : string, optional

- Specify your preprocess algorithms. For example, min, max, variance, trend, anomprob, outliers, etc..

*preprocessconditions* : string, optional

- Specify any preprocess conditions

*identifier* : string, optional

- Specify any text identifier

*preprocesstopic* : string, optional

- Specify the name of the topic to write preprocessed results.

*array* : int, optional

- Ignored for raw data - as jsoncriteria specifies json path

*saveasarray* : int, optional

- Set to 1 to save as json array

*timedelay* : int, optional

- Delay to wait for response from Kafka.

*asynctimeout* : int, optional

- Maximum delay for asyncio in Python library

*usemysql* : int, optional

- Set to 1 to specify whether MySQL is used to store TMLIDs.  This will be needed to track individual objects.

*tmlfilepath* : string, optional

- Ignored. 

*pathtotmlattrs* : string, optional

- Specifiy any attributes for the TMLID.  Here you can specify OEM, Latitude, Longitude, and Location JSON paths:

     pathtotmlattrs='oem=id,lat=subject.reference,long=component.0.code.coding.0.display,location=component.1.valueQuantity.value'

*port* : int, required

- Port on which VIPER is listenting.

*brokerhost* : string, optional

- Address where Kafka broker is running - if none is specified, the Kafka broker address in the VIPER.ENV file will be used.


*brokerport* : int, optional

- Port on which Kafka is listenting.

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

RETURNS: null

**33. maadstml.viperstreamcluster(vipertoken,host,port,topic,producerid,offset=-1,maxrows=0,enabletls=1,delay=100,brokerhost='',
                                          brokerport=-999,microserviceid='',topicid=-999,iterations=1000, numclusters=8,
                                          distancealgo=1,description='',rawdataoutput=0,valuekey='',filterkey='',groupkey='',
                                          identifier='',datetimekey='',valueidentifier='',msgid='',valuecondition='',
                                          identifierextractpos='',preprocesstopic='',
                                          alertonclustersize=0,alertonsubjectpercentage=50,sendalertemailsto='',emailfrequencyinseconds=0,
                                          companyname='',analysisdescription='',identifierextractposlatitude=-1,
                                          identifierextractposlongitude=-1,identifierextractposlocation=-1,
                                          identifierextractjoinedidentifiers=-1,pdfformat='',minimumsubjects=2)**


**Parameters:**	Perform Stream correlations

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*topic* : string, required

- Topic containing the raw data to consume.

*port* : int, required

- Port on which VIPER is listenting.

*brokerhost* : string, optional

- Address where Kafka broker is running - if none is specified, the Kafka broker address in the VIPER.ENV file will be used.

*brokerport* : int, optional

- Port on which Kafka is listenting.

*alertonsubjectpercentage* : int, optional

- Set a value between 0-100 that specifies the percentage of subjects that exceed a threshold. 

*identifierextractjoinedidentifiers* : int, optional

 - Position of additional text in identfier field.

*pdfformat* : string, optional

- Speficy format text of the PDF to generate and emailed to users.  You can set title, signature, showpdfemaillist, and charttitle.

     pdfformat="title=This is a Transactional Machine Learning Auto-Generated PDF for Cluster Analysis For OTICS|signature=\
     Created by: OTICS, Toronto|showpdfemaillist=1|charttitle=Chart Shows Clusters of Patients with Similar Symptoms"

*minimumsubjects* : int, optional

- Sepecify minimum subjects in the cluster analysis.

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

*maxrows* : int, optional

- Number of offsets or percentage to roll back the data stream

*enabletls* : int, optional

- Set to 1 for TLS encrpyted traffic

*delay* : int, optional

- Delay to wait for Kafka to finish writing to topic

*producerid* : string, required

- Id of the Topic.

*topicid* : int, optional

- Ignored

*iterations* : int, optional

 - Number of iterations to compute clusters

*numclusters* : int, optional

 - Number of clusters you want.  Maximum is 20.

*distancealgo* : int, optional

 - Set to 1 for Euclidean, or 2 for EuclideanSquared.

*valuekey* : string, required

- JSON path to the value to cluster on 

*filterkey* : string, optional
 
 - JSON path to filter on.  Ex. Preprocesstype=Pearson, gets value from Key=Preprocesstype, and checks for value=Pearson

*groupkey* : string, optional
 
 - JSON path to group on a key.  Ex. Topicid, to group on TMLIDs

*valueidentifier* : string, optional
 
 - JSON path to text value IDs you correlated.

*msgid* : string, optional

 - JSON path for a unique message id
 
*valuecondition* : string, optional
 
 - A condition to filter numeric values on.  Ex. valuecondition="> .5", if valuekey is correlations, then all correlation > 0.5 are taken.
  
*identifierextractpos* : string, optional

 - The location of data to extract from the Identifier field.  Ex. identifierextractpos="1,2", will extract data from position 1 and 2.
 
*preprocesstopic* : string, required

 - Topic to produce results to 
 
*alertonclustersize* : int, optional

 - Size of the cluster to alert on.  Ex.  if this is 100, then when any cluster has more than 100 elements an email is sent.

*sendalertemailsto*: string, optional
 
 - List of email addresses to send alert to
 
*emailfrequencyinseconds* : int, optional

 - Seconds between emails. Ex. set to 3600, so emails will be sent every 1 hour if alert condition met.

*companyname* : string, optional
 
 - Your company name
 
*analysisdescription* : string, optional

 - A detailed description of the analysis.  This will be added to the PDF.

*identifierextractposlatitude* : int, optional

- Position for latitude in the Identifier field  

*identifierextractposlongitude* : int, optional

- Position for longitude in the Identifier field  

*identifierextractposlocation* : int, optional

- Position for location in the Identifier field  

RETURNS: null

**34. maadstml.vipersearchanomaly(vipertoken,host,port,topic,producerid,offset,jsoncriteria='',rawdataoutput=0,maxrows=0,enabletls=0,delay=100,
                       brokerhost='',brokerport=-999,microserviceid='',topicid=-999,identifier='',preprocesstopic='',
                       timedelay=0,asynctimeout=120,searchterms='',entitysearch='',tagsearch='',checkanomaly=1,testtopic='',
                       includeexclude=1,anomalythreshold=0,sendanomalyalertemail='',emailfrequency=3600)**

**Parameters:**	Perform Stream correlations

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*topic* : string, required

- Topic containing the raw data to consume.

*port* : int, required

- Port on which VIPER is listenting.

*brokerhost* : string, optional

- Address where Kafka broker is running - if none is specified, the Kafka broker address in the VIPER.ENV file will be used.

*brokerport* : int, optional

- Port on which Kafka is listenting.

*jsoncriteria* : string, optional

- Enter the JSON path to the search fields

*anomalythreshold* : int, optional

 - Threshold to meet to determine if search differs from the peer group.  This is a number between 0-100.  The lower the number
   the "more" this search differs from the peer group and likely anomalous.

*includeexclude* : int, optional

- Set to 1 if you want the search terms included in the user searches, 0 otherwise.

*sendanomalyalertemail* : string, optional

- List of email addresses to send alerts to: separate list by comma.

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

*maxrows* : int, optional

- Number of offsets or percentage to roll back the data stream

*enabletls* : int, optional

- Set to 1 for TLS encrpyted traffic

*delay* : int, optional

- Delay to wait for Kafka to finish writing to topic

*producerid* : string, required

- Id of the Topic.

*emailfrequency* : int, optional

- Frequency in seconds, between alert emails.

*testtopic* : string, optional

 - ignored 

*preprocesstopic* : string, required

 - Topic to produce results to 
 
*sendalertemailsto*: string, optional
 
 - List of email addresses to send alert to

*tagsearch* : string, optional

 - Search for tags in the search.  You can enter: 'superlative,noun,interjection,verb,pronoun'

*entitysearch* : string, optional

 - Search for entities in the search.  You can enter: 'person,gpe', where gpe=Geo-political entity
 
*searchterms* : string, optional

 - You can specify your own search terms.  Separate list by comma.
 
*emailfrequencyinseconds* : int, optional

 - Seconds between emails. Ex. set to 3600, so emails will be sent every 1 hour if alert condition met.

*companyname* : string, optional
 
 - Your company name
 
*topicid* : int, optional

 - ignored
 
*identifier* : string, optional

- identifier text

*checkanomaly* : int, optional

- Set to 1 to check for search anomaly.

*rawdataoutput* : int, optional

- ignored

RETURNS: null

**35. maadstml.vipermirrorbrokers(VIPERTOKEN,host,port,brokercloudusernamepassfrom,brokercloudusernamepassto,
         enabletlsfrom,enabletlsto,
         replicationfactorfrom,replicationfactorto,compressionfrom,compressionto,
         saslfrom,saslto,partitions,brokerlistfrom,brokerlistto,                                         
         topiclist,asynctimeout=300,microserviceid="",servicenamefrom="broker",
  		 servicenameto="broker",partitionchangeperc=0,replicationchange=0,filter="",rollbackoffset=0)**

**Parameters:**	Perform Data Stream migration across brokers - fast and simple.

*VIPERTOKEN* : string, required

- A token given to you by VIPER administrator.

*host* : string, required
       
- Indicates the url where the VIPER instance is located and listening.

*port* : int, required

- Port on which VIPER is listenting.

*brokercloudusernamepassfrom* : string, required

- This is a comma separated list of source broker username:password. For multiple brokers separate with comma, for example for 3 brokers:
  username:password,username:password,username:password

*brokercloudusernamepassto* : string, required

- This is a comma separated list of destination broker username:password. For multiple brokers separate with comma, for example for 3 brokers:
  username:password,username:password,username:password.  The number of source and destination brokers must match.

*enabletlsfrom* : string, required

- This is a colon separated list of whether source brokers require TLS: 1=TLS, 0=NoTLS. For multiple brokers separate with colon, 
  for example for 3 brokers: 1:0:1.  Some brokers may be On-Prem and do not need TLS.
  
*enabletlsto* : string, required

- This is a colon separated list of whether destination brokers require TLS: 1=TLS, 0=NoTLS. For multiple brokers separate with colon, 
  for example for 3 brokers: 1:0:1.  Some brokers may be On-Prem and do not need TLS.

*replicationfactorfrom* : string, optional

- This is a colon separated list of the replication factor of source brokers. For multiple brokers separate with colon, 
  for example for 3 brokers: 3:4:3, or leave blank to let VIPER decide.  
  
*replicationfactorto* : string, optional

- This is a colon separated list of the replication factor of destination brokers. For multiple brokers separate with colon, 
  for example for 3 brokers: 3:4:3, or leave blank to let VIPER decide.

*compressionfrom* : string, required

- This is a colon separated list of the compression type of source brokers: snappy, gzip, lz4. For multiple brokers separate with colon, 
  for example for 3 brokers: snappy:snappy:gzip.  
  
*compressionto* : string, required

- This is a colon separated list of the compression type of destination brokers: snappy, gzip, lz4. For multiple brokers separate with colon, 
  for example for 3 brokers: snappy:snappy:gzip.  

*saslfrom* : string, required

- This is a colon separated list of the SASL type: None, Plain, SCRAM256, SCRAM512 of source brokers. For multiple brokers separate with colon, 
  for example for 3 brokers: PLAIN:SCRAM256:SCRAM512.  
  
*saslto* : string, required

- This is a colon separated list of the SASL type: None, Plain, SCRAM256, SCRAM512 of destination brokers. For multiple brokers separate with colon, 
  for example for 3 brokers: PLAIN:SCRAM256:SCRAM512.  

*partitions* : string, optional

- If you are manually migrating topics you will need to specify the partitions of the topics in *topiclist*.  Otherwise, VIPER
  will automatically find topics and their partitions on the broker for you - this is recommended.

*brokerlistfrom* : string, required

- This is a list of source brokers: host:port. For multiple brokers separate with comma, for example for 3 brokers: host:port,host:port,host:port.  

*brokerlistto* : string, required

- This is a list of destination brokers: host:port. For multiple brokers separate with comma, for example for 3 brokers: host:port,host:port,host:port.  

*topiclist* : string, optional

- You can manually specify topics to migrate, separate multiple topics with a comma. Otherwise, Viper will automatically find topics
  on the broker for you - this is recommended.

*partitionchangeperc* : number, optional

- You can increase or decrease partitions on destination broker by specifying a percentage between 0-100, or -100-0.
  Minimum partition will always be 1.

*replicationchange* : ignored for now

- You can increase or decrease replication factor on destination broker by specifying a positive or negative number.
  Minimum partition will always be 2.

*filter* : string, optional

- You can specify a filter to choose only those topics that satisfy the filter.  Filters must have the 
  following format: "searchstring1,searchstring2,searchstring3,..:Logic=0 or 1:search position: 0,1,2".  For example, 
  Logic 0=AND, 1=OR, search position: 0=BeginsWith, 1=Any, 2=EndsWith

*asynctimeout* : number, optional

- This specifies the timeout in seconds for the python connection.

*microserviceid* : string, optional

- If you are routing connections to VIPER through a microservice then indicate it here.

*servicenamefrom* : string, optional

- You can specify the name of the source brokers.

*servicenameto* : string, optional

- You can specify the name of the destination brokers.

*rollbackoffset*: ignored

**36. maadstml.vipernlp(filename,maxsummarywords,maxkeywords)**

**Parameters:**	Perform NLP summarization of PDFs

*filename* : string, required

- Filename of PDF to summarize.

*maxsummarywords* : int, required
       
- Maximum amount of words in the summary.

*maxkeywords* : int, required

- Maximum amount of keywords to extract.

RETURNS: JSON string of summary.

**37. maadstml.viperchatgpt(openaikey,texttoanalyse,query, temperature,modelname)**

**Parameters:**	Start a conversation with ChatGPT

*openaikey* : string, required

- OpenAI API key

*texttoanalyse* : string, required
       
- Text you want ChatGPT to analyse

*query* : string, required

- Prompts for chatGPT.  For example, "What are key points in this text? What are the concerns or issues?"

*temperature* : float, required

- Temperature for chatgpt, must be between 0-1 i.e. 0.7

*modelname* : string, required

- ChatGPT model to use.  For example, text-davinci-002, text-curie-001, text-babbage-001.

RETURNS: ChatGPT response.

**38. maadstml.viperexractpdffields(pdffilename)**

**Parameters:**	Extract data from PDF

*pdffilename* : string, required

- PDF filename

RETURNS: JSON of PDF and writes JSON and XML files of PDF to disk.

**39. maadstml.viperexractpdffieldbylabel(pdffilename,labelname,arcotype)**

**Parameters:**	Extract data from PDF by PDF labels

*pdffilename* : string, required

- PDF filename

*labelname* : string, required

- Label name in the PDF filename to search for.

*pdffilename,labelname,arcotype* : string, required

- Acrobyte tag in PDF i.e. LTTextLineHorizontal

RETURNS: Value of the labelname - if any.

**40. maadstml.pgptingestdocs(docname,doctype, pgptip,pgptport,pgptendpoint)**

**Parameters:**	

*docname* : string, required

- A full-path to a PDF, or text file.

*doctype* : string, required
       
- This can be: binary, or text.

*pgptip* : string, required

- Your container IP - this is usually: http://127.0.0.1

*pgptport* : string, required

- Your container Port - this is usually: 8001.  This will be dependent on the docker run port forwarding command. See: https://github.com/smaurice101/raspberrypi/tree/main/privategpt

*pgptendpoint* : string, required

- This must be: /v1/ingest

RETURNS: JSON containing Document details, or ERROR. 

**41. maadstml.pgptgetingestedembeddings(docname,ip,port,endpoint)**

**Parameters:**	

*docname* : string, required

- A full-path to a PDF, or text file.

*ip* : string, required

- Your container IP - this is usually: http://127.0.0.1

*port* : string, required

- Your container Port - this is usually: 8001.  This will be dependent on the docker run port forwarding command. See: https://github.com/smaurice101/raspberrypi/tree/main/privategpt

*endpoint* : string, required

- This must be: /v1/ingest/list

RETURNS: Three variables: docids,docstr,docidsstr; these are the embeddings related to docname. Or, ERROR. 

**42. maadstml.pgptchat(prompt,context,docfilter,port,includesources,ip,endpoint)**

**Parameters:**	

*prompt* : string, required

- A prompt for privateGPT.

*context* : bool, required

- This can be True or False. If True, privateGPT will use context, if False, it will not.

*docfilter* : string array, required

- This is docidsstr, and can be retrieved from pgptgetingestedembeddings.  If context=True, and dockfilter is empty, then ALL documents are used for context. 

*port* : string, required

- Your container Port - this is usually: 8001.  This will be dependent on the docker run port forwarding command. See: https://github.com/smaurice101/raspberrypi/tree/main/privategpt

*includesources* : bool, required

- This can be True or False. If True, with context, privateGPT will return the sources in the response.

*ip* : string, required

- Your container IP - this is usually: http://127.0.0.1

*endpoint* : string, required

- This must be: /v1/completions

RETURNS: The response from privateGPT, or ERROR. 

**43. maadstml.pgptdeleteembeddings(docids, ip,port,endpoint)**

**Parameters:**	

*docids* : string array, required

- An array of doc ids.  This can be retrieved from  pgptgetingestedembeddings.

*port* : string, required

- Your container Port - this is usually: 8001.  This will be dependent on the docker run port forwarding command. See: https://github.com/smaurice101/raspberrypi/tree/main/privategpt

*ip* : string, required

- Your container IP - this is usually: http://127.0.0.1

*endpoint* : string, required

- This must be: /v1/ingest/

RETURNS: Null if successful, or ERROR. 

**44. maadstml.pgpthealth(ip,port,endpoint)**

**Parameters:**	

*port* : string, required

- Your container Port - this is usually: 8001.  This will be dependent on the docker run port forwarding command. See: https://github.com/smaurice101/raspberrypi/tree/main/privategpt

*ip* : string, required

- Your container IP - this is usually: http://127.0.0.1

*endpoint* : string, required

- This must be: /health

RETURNS: This will return a JSON of OK if the privateGPT server is running, or ERROR. 

**45. maadstml.videochatloadresponse(url,port,filename,prompt,responsefolder='videogpt_response',temperature=0.2,max_output_tokens=512)**

**Parameters:**	

*url* : string, required

- IP video chatgpt is listening on in the container - this is usually: http://127.0.0.1

*port* : string, required

- Port video chat gpt is listening on in the container i.e. 7800

*filename* : string, required

- This is the video filename to analyse i.e. with mp4 extension

*prompt* : string, required

- This is the prompt for video chat gpt. i.e. "what is the video about? Is there anaything strange in the video?"

*responsefolder* : string, optional

- This is the folder you want video chatgpt to write responses to 

*temperature* : float, optional

- Temperature determines how conservative video chat gpt is i.e. closer to 0 very conservative in responses

*max_output_tokens* : int, optional

- max_output_tokens determines tokens to return

RETURNS: The file name the response was written to by video chatgpt. 

.. autosummary::
   :toctree: generated

   lumache
