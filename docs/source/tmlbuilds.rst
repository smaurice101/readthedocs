TML Solution Building In 10 Steps Using Pre-Written DAGs (Directed Acyclic Graphs)
======================

Where Do I Start?
----------

The fastest way to build TML solutions with your real-time data is to use the :ref:`TML Solution Studio Container`

.. important::

   **The following prerequisites MUST be met before you run the TML Solution Studio Container:**

   1. You MUST Install Docker - in Ubuntu run: sudo apt install docker.io

   2. You MUST have a Github Account

   3. You MUST Clone Github Repo: https://github.com/smaurice101/raspberrypi.git

   4. You MUST Create Github **Personal Access Token** (Refer to Docker section)

   5. You MUST have a Docker Hub account

   FOLLOW THE :ref:`How To Use the TML Solution Container` SECTION.

Pre-Written 10 Apache Airflow DAGs To Speed Up TML Solution Builds
-------------------

The TML solution process with DAGS (explained in detail below).  **The entire TML solution build process is highly efficient; advanced, scalable, real-time TML solutions can be built in few hours with GenAI integrations!**

.. figure:: tsol1.png

DAGs (Directed Acyclic Graphs) are a powerful and easy way to build powerful (real-time) TML solutions quickly.  Users are provided with the following DAGs:

.. note::
   
   The numbers in the DAGs indicate solution process step.  For example, step 2 is dependent on step 1.

DAG Table
-------------------

.. list-table::
   :widths: 20 50

   * - **DAG Name**
     - **Description**
   * - tml_system_step_1_getparams_dag
     - This DAG will get the core TML connection and tokens needed for operations.
   * - tml_system_step_2_kafka_createtopic_dag
     - This DAG will create all the necessary topics in Kafka (on-prem or Cloud) for your TML solution. 
   * - tml-read-MQTT-step-3-kafka-producetotopic-dag.py
     - This DAG is an MQTT server and will listen for a connection from a client.  You use this if your TML solution ingests data from MQTT system like HiveMQ and 
       stream it to Kafka.
   * - tml-read-LOCALFILE-step-3-kafka-producetotopic-dag.py
     - This DAG will read a local CSV file for data and stream it to Kafka.
   * - tml-read-gRPC-step-3-kafka-producetotopic-dag
     - This DAG is an gRPC server and will listen for a connection from a gRPC client.  You use this if your TML solution ingests data from devices and you want to 
       leverage a gRPC connection and stream the data to Kafka.
   * - tml-read-RESTAPI-step-3-kafka-producetotopic-dag
     - This DAG is an RESTAPI server and will listen for a connection from a REST client.  You use this if your TML solution ingests data from devices and you want 
       to leverage a rest connection and stream the data to Kafka.
   * - tml-system-step-4-kafka-preprocess-dag
     - This DAG perform entity level preprocessing on the real-time data.  There are over 35 different preprocessing types in TML. 
   * - tml-system-step-5-kafka-machine-learning-dag
     - This DAG perform entity level machine learning on the real-time data.
   * - tml-system-step-6-kafka-predictions-dag
     - This DAG performs predictions using the trained algorithms for every entity.
   * - tml-system-step-7-kafka-visualization-dag
     - This DAG streams the output to a real-time dashboard.
   * - tml_system_step_8_deploy_solution_to_docker_dag
     - This DAG automatically deploys the entire TML solution to Docker container - and pushes it to Dockerhub.
   * - tml_system_step_9_privategpt_qdrant_dag
     - This DAG configures your solution to access the privateGPT and Qdrant containers.
   * - tml_system_step_10_documentation_dag
     - This DAG will automatically create the documentation for your solution on readthedocs.io.

STEP 1: Get TML Core Params: tml_system_step_1_getparams_dag
-----------------

Below is the complete definition of the **tml_system_step_1_getparams_dag**.  Users only need to configure the code highlighted in the **USER CHOSEN PARAMETERS**.

.. code-block::
   :emphasize-lines: 10,11,12,13,14,15,16,17,18,19
 
   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from airflow.operators.bash import BashOperator
   import datetime
   from airflow.decorators import dag, task
   import os 
   import sys
  
   sys.dont_write_bytecode = True
   ######################################################USER CHOSEN PARAMETERS ###########################################################
   default_args = {
   'owner': 'Sebastian Maurice',  # <<< ******** change as needed 
   'start_date': datetime.datetime (2024, 6, 29),
   'brokerhost' : '127.0.0.1',  # <<<<***************** THIS WILL ACCESS LOCAL KAFKA - YOU CAN CHANGE TO CLOUD KAFKA HOST
   'brokerport' : '9092',     # <<<<***************** LOCAL AND CLOUD KAFKA listen on PORT 9092
   'cloudusername' : '',  # <<<< --------FOR KAFKA CLOUD UPDATE WITH API KEY  - OTHERWISE LEAVE BLANK
   'cloudpassword' : '',  # <<<< --------FOR KAFKA CLOUD UPDATE WITH API SECRET - OTHERWISE LEAVE BLANK   
   'retries': 1,
   }
  
  
   ############################################################### DO NOT MODIFY BELOW ####################################################
   # Instantiate your DAG
   @dag(dag_id="tml_system_step_1_getparams_dag", default_args=default_args, tags=["tml-system-step-1-getparams"], schedule=None, 
    start_date=datetime.datetime(2022, 3, 4), catchup=False)
   def tmlparams():
      # Define tasks
    basedir = "/"
    viperconfigfile=basedir + "/Viper-produce/viper.env"
  
    def updateviperenv():
    # update ALL
      filepaths = ['/Viper-produce/viper.env','/Viper-preprocess/viper.env','/Viper-preprocess2/viper.env','/Viper-ml/viper.env','/Viperviz/viper.env']
      for mainfile in filepaths:
          with open(mainfile, 'r', encoding='utf-8') as file: 
            data = file.readlines() 
          r=0 
          for d in data:
             if 'KAFKA_CONNECT_BOOTSTRAP_SERVERS' in d: 
               data[r] = "KAFKA_CONNECT_BOOTSTRAP_SERVERS={}:{}".format(default_args['brokerhost'],default_args['brokerport'])
             if 'CLOUD_USERNAME' in d: 
               data[r] = "CLOUD_USERNAME={}".format(default_args['cloudusername'])
             if 'CLOUD_PASSWORD' in d: 
               data[r] = "CLOUD_PASSWORD={}".format(default_args['cloudpassword'])
                  
             r += 1
          with open(mainfile, 'w', encoding='utf-8') as file: 
            file.writelines(data)
  
  
    @task(task_id="getparams")
    def getparams(args):
       VIPERHOST=""
       VIPERPORT=""
       HTTPADDR="http://"
       HPDEHOST=""
       HPDEPORT=""
      
       with open(basedir + "/Viper-produce/admin.tok", "r") as f:
          VIPERTOKEN=f.read()
  
       if VIPERHOST=="":
          with open(basedir + '/Viper-produce/viper.txt', 'r') as f:
            output = f.read()
            VIPERHOST = HTTPADDR + output.split(",")[0]
            VIPERPORT = output.split(",")[1]
          with open('/Hpde/hpde.txt', 'r') as f:
            output = f.read()
            HPDEHOST = HTTPADDR2 + output.split(",")[0]
            HPDEPORT = output.split(",")[1]
  
       ti.xcom_push(key='VIPERTOKEN',value=VIPERTOKEN)
       ti.xcom_push(key='VIPERHOST',value=VIPERHOST)
       ti.xcom_push(key='VIPERPORT',value=VIPERPORT)
       ti.xcom_push(key='HTTPADDR',value=HTTPADDR)
       ti.xcom_push(key='HPDEHOST',value=HPDEHOST)
       ti.xcom_push(key='HPDEPORT',value=HPDEPORT)
               
       updateviperenv()
      
       return [VIPERTOKEN,VIPERHOST,VIPERPORT,HTTPADDR]
       
       tmlsystemparams=getparams(default_args)
       if tmlsystemparams[1]=="":
          print("ERROR: No host specified")
      
   dag = tmlparams()

STEP 2: Create Kafka Topics: tml_system_step_2_kafka_createtopic_dag
-----------------

Below is the complete definition of the **tml_system_step_2_kafka_createtopic_dag** that creates all the topics for your solution.  Users only need to configure the code highlighted in the **USER CHOSEN PARAMETERS**.

.. code-block::
   :emphasize-lines: 12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32

   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from airflow.operators.bash import BashOperator

   from datetime import datetime
   from airflow.decorators import dag, task
   import maadstml 
   import sys
   
   sys.dont_write_bytecode = True
   ######################################## USER CHOOSEN PARAMETERS ################################################################################
   default_args = {
    'owner' : 'Sebastian Maurice', # <<< ********** You change as needed
    'companyname': 'Otics',  # <<< ********** You change as needed
     'myname' : 'Sebastian',  # <<< ********** You change as needed
     'myemail' : 'Sebastian.Maurice',  # <<< ********** You change as needed
     'mylocation' : 'Toronto',  # <<< ********** You change as needed
     'replication' : 1,  # <<< ********** You change as needed (For Cloud Kafka this is MUST be >= 3
     'numpartitions': 1,  # <<< ********** You change as needed
     'enabletls': 1,  # <<< ********** You change as needed
     'brokerhost' : '',  # <<< ********** You change as needed
     'brokerport' : -999,  # <<< ********** You change as needed
     'microserviceid' : '',  # <<< ********** You change as needed
     'raw_data_topic' : 'iot-raw-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'preprocess_data_topic' : 'iot-preprocess-data,iot-preprocess2-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'ml_data_topic' : 'ml-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'prediction_data_topic' : 'prediction-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'description' : 'Topics to store iot data',  # <<< **** You modify as needed
     'start_date': datetime (2024, 6, 29), # <<< **** You modify as needed
     'retries': 1,    # <<< **** You modify as needed
   }
   
   ############################################################### DO NOT MODIFY BELOW #######################################################################
   
   # Instantiate your DAG
   @dag(dag_id="tml_system_step_2_kafka_createtopic_dag", default_args=default_args, tags=["tml-system-step-2-kafka-createtopic"], schedule=None,catchup=False)
   def startkafkasetup():
     @task(task_id="setupkafkatopics")
     def setupkafkatopic(args):
        # Set personal data
         companyname=args['companyname']
         myname=args['myname']
         myemail=args['myemail']
         mylocation=args['mylocation']
   
         # Replication factor for Kafka redundancy
         replication=args['replication']
         # Number of partitions for joined topic
         numpartitions=args['numpartitions']
         # Enable SSL/TLS communication with Kafka
         enabletls=args['enabletls']
         # If brokerhost is empty then this function will use the brokerhost address in your
         # VIPER.ENV in the field 'KAFKA_CONNECT_BOOTSTRAP_SERVERS'
         brokerhost=args['brokerhost']
         # If this is -999 then this function uses the port address for Kafka in VIPER.ENV in the
         # field 'KAFKA_CONNECT_BOOTSTRAP_SERVERS'
         brokerport=args['brokerport']
         # If you are using a reverse proxy to reach VIPER then you can put it here - otherwise if
         # empty then no reverse proxy is being used
         microserviceid=args['microserviceid']
           
         VIPERTOKEN = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERTOKEN")
         VIPERHOST = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERHOST")
         VIPERPORT = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERPORT")
   
         #############################################################################################################
         #                         CREATE TOPIC TO STORE TRAINED PARAMS FROM ALGORITHM  
         
         topickeys = ['raw_data_topic','preprocess_data_topic','ml_data_topic','prediction_data_topic'] 
       
         for k in topickeys:
           producetotopic=args[k]
           description=args['description']
       
           topicsarr = producetotopic.split(",")
         
           for topic in topicsarr:  
             result=maadstml.vipercreatetopic(VIPERTOKEN,VIPERHOST,VIPERPORT,topic,companyname,
                                        myname,myemail,mylocation,description,enabletls,
                                        brokerhost,brokerport,numpartitions,replication,
                                        microserviceid='')
             print("Result=",result)
   
         setupkafkatopic(default_args)
         
         
   dag = startkafkasetup()


STEP 3: Produce to Kafka Topics
-----------------

.. important::

   You must CHOOSE how you want to ingest data and produce to a Kafka topic.  

   **TML solution provides 4 (FOUR) ways to ingest data and produce to a topic: MQTT, gRPC, RESTAPI, LOCALFILE.**  The following DAGs in the table are SERVER 
   files.  These server files wait for connections from the client files. For further convenience, client files are provides to access the server DAGs below.

.. list-table::

   * - **Data Ingest DAG Name**
     - **Client File Name**
     - **Description**
   * - tml-read-MQTT-step-3-kafka-producetotopic-dag.py
     - An **on_message(client, userdata, msg)** event is triggered by the MQTT broker.  This DAGs will automatically handle the on_message event
       and produce the data to Kafka.
     - This DAG is an MQTT server and will listen for a connection from a client.  
       You use this if your TML solution ingests data from MQTT system like HiveMQ and 
       stream it to Kafka.
   * - tml-read-LOCALFILE-step-3-kafka-producetotopic-dag.py
     - You can process a localfile and stream the data to kafka.  See the `IoTSolution DAG <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/dags/tml-iotsolution-step-3-kafka-producetotopic-dag.py>`_
     - This DAG will read a local CSV file for data and stream it to Kafka.
   * - tml-read-gRPC-step-3-kafka-producetotopic-dag
     - Here is the gRPC client: `tml-read-gRPC-step-3-kafka-producetotopic-dag <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/dags/tml-client- 
       gRPC-step-3-kafka-producetotopic.py>`_
       NOTE: For this client you will also need: `tml_grpc_pb2_grpc <https://github.com/smaurice101/raspberrypi/blob/main/tml- 
       airflow/dags/tml_grpc_pb2_grpc.py>`_, and `tml_grpc_pb2 <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/dags/tml_grpc_pb2.py>`_
     - This DAG is an gRPC server and will listen for a connection from a gRPC client.  You use this if your TML 
       solution ingests data from devices and you want to 
       leverage a gRPC connection and stream the data to Kafka.
   * - tml-read-RESTAPI-step-3-kafka-producetotopic-dag
     - Here is the RESTAPI client: `tml-client-RESTAPI-step-3-kafka-producetotopic.py <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/dags/tml- 
       client-RESTAPI-step-3-kafka-producetotopic.py>`_
     - This DAG is an RESTAPI server and will listen for a connection from a REST client.  You use this if your TML 
       solution ingests data from devices and you want 
       to leverage a rest connection and stream the data to Kafka.
   

STEP 3a: Produce Data Using MQTT: tml-read-MQTT-step-3-kafka-producetotopic-dag.py
--------------------- 	

.. code-block::
   :emphasize-lines: 16,17,18,19,20,21,22,23,24,25,26,27,28,29,30

   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from airflow.operators.bash import BashOperator
   from datetime import datetime
   from airflow.decorators import dag, task
   import paho.mqtt.client as paho
   from paho import mqtt
   import sys
   
   sys.dont_write_bytecode = True
   ##################################################  MQTT SERVER #####################################
   # This is a MQTT server that will handle connections from a client.  It will handle connections
   # from an MQTT client for on_message, on_connect, and on_subscribe
   
   ######################################## USER CHOOSEN PARAMETERS ########################################
   default_args = {
     'owner' : 'Sebastian Maurice',  # <<< **** You modify as needed
     'enabletls': 1,   # <<< #**** 1=connections are TLS encrypted
     'microserviceid' : '', # **** leave as is
     'producerid' : 'iotsolution',  # <<< **** You modify as needed
     'topics' : 'iot-raw-data', # ******* This is one of the topic you created in SYSTEM STEP 2
     'identifier' : 'TML solution',  # <<< **** You modify as needed
     'mqtt_broker' : '', # <<<****** Enter MQTT broker i.e. test.mosquitto.org
     'mqtt_port' : '', # <<<******** Enter MQTT port i.e. 1883    
     'mqtt_subscribe_topic' : '', # <<<******** enter name of MQTT to subscribe to i.e. encyclopedia/#  
     'delay' : 7000, # << ******* 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic
     'topicid' : -999, # <<< ********* do not modify      
     'start_date': datetime (2024, 6, 29), # <<< **** You modify as needed
     'retries': 1,  # <<< **** You modify as needed  
   }
   
   ######################################## DO NOT MODIFY BELOW #############################################
   
   # Instantiate your DAG
   @dag(dag_id="tml_mqtt_step_3_kafka_producetotopic_dag", default_args=default_args, tags=["tml-mqtt-step-3-kafka-producetotopic"], schedule=None,catchup=False)
   def startproducingtotopic():
     # This sets the lat/longs for the IoT devices so it can be map
     VIPERTOKEN=""
     VIPERHOST=""
     VIPERPORT=""
       
     # setting callbacks for different events to see if it works, print the message etc.
     def on_connect(client, userdata, flags, rc, properties=None):
       print("CONNACK received with code %s." % rc)
   
     # print which topic was subscribed to
     def on_subscribe(client, userdata, mid, granted_qos, properties=None):
       print("Subscribed: " + str(mid) + " " + str(granted_qos))
   
     data = ''
     def on_message(client, userdata, msg):
       global data
       data=json.loads(msg.payload.decode("utf-8"))
       print(msg.payload.decode("utf-8"))
       readdata(data)
       
     @task(task_id="mqttserverconnect")
     def mqttserverconnect():
        client = paho.Client(paho.CallbackAPIVersion.VERSION2)
        mqttBroker = default_args['mqtt_broker'] 
        mqttport = default_args['mqtt_port']
        client.connect(mqttBroker,mqttport)
       
        if client:
          client.on_subscribe = on_subscribe
          client.on_message = on_message
          client.subscribe(args['mqtt_subscribe_topic'], qos=1)            
          client.on_connect = on_connect
       
          client.loop_start()
       
     def producetokafka(value, tmlid, identifier,producerid,maintopic,substream,args):
        inputbuf=value     
        topicid=args['topicid']
     
        # Add a 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic 
        delay=args['delay']
        enabletls = args['enabletls']
        identifier = args['identifier']
   
        try:
           result=maadstml.viperproducetotopic(VIPERTOKEN,VIPERHOST,VIPERPORT,maintopic,producerid,enabletls,delay,'','', '',0,inputbuf,substream,
                                               topicid,identifier)
        except Exception as e:
           print("ERROR:",e)
   
     @task(task_id="gettmlsystemsparams")         
     def gettmlsystemsparams(rc):
       VIPERTOKEN = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERTOKEN")
       VIPERHOST = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERHOST")
       VIPERPORT = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERPORT")
       
       return [VIPERTOKEN,VIPERHOST,VIPERPORT]
           
     def readdata(valuedata):
         # MAin Kafka topic to store the real-time data
         maintopic = default_args['topics']
         producerid = default_args['producerid']
         try:
             producetokafka(valuedata.strip(), "", "",producerid,maintopic,"",default_args)
             # change time to speed up or slow down data   
             #time.sleep(0.15)
         except Exception as e:
             print(e)  
             pass  
         
     gettmlsystemsparams(mqttserverconnect())
       
   
   dag = startproducingtotopic()

STEP 3b: Produce Data Using RESTAPI: tml-read-RESTAPI-step-3-kafka-producetotopic-dag.py
--------------------- 	

.. code-block::
   :emphasize-lines: 19,20,21,22,23,24,25,26,27,28,29,30,31

   import maadstml
   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from airflow.operators.bash import BashOperator
   import json
   from datetime import datetime
   from airflow.decorators import dag, task
   from flask import Flask
   import sys
   
   sys.dont_write_bytecode = True
   ##################################################  REST API SERVER #####################################
   # This is a REST API server that will handle connections from a client
   # There are two endpoints you can use to stream data to this server:
   # 1. jsondataline -  You can POST a single JSONs from your client app. Your json will be streamed to Kafka topic.
   # 2. jsondataarray -  You can POST JSON arrays from your client app. Your json will be streamed to Kafka topic.
   
   ######################################## USER CHOOSEN PARAMETERS ########################################
   default_args = {
     'owner' : 'Sebastian Maurice', # <<< **** You modify as needed   
     'enabletls': 1, # <<< **** 1=Connection is TLS encrypted
     'microserviceid' : '', # <<< **** Leave as is
     'producerid' : 'iotsolution',  # <<< **** You modify as needed   
     'topics' : 'iot-raw-data', # *************** This is one of the topic you created in SYSTEM STEP 2
     'identifier' : 'TML solution',  # <<< **** You modify as needed   
     'rest_port' : 9001,  # <<< ***** replace replace with port number i.e. this is listening on port 9000 
     'delay' : 7000, # << ******* 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic
     'topicid' : -999, # <<< ********* do not modify          
     'start_date': datetime (2024, 6, 29), # <<< **** You modify as needed   
     'retries': 1, # <<< **** You modify as needed   
   }
   
   ######################################## DO NOT MODIFY BELOW #############################################
   
   # Instantiate your DAG
   @dag(dag_id="tml-read-RESTAPI-step-3-kafka-producetotopic-dag", default_args=default_args, tags=["tml-read-RESTAPI-step-3-kafka-producetotopic-dag"], schedule=None,catchup=False)
   def startproducingtotopic():
     # This sets the lat/longs for the IoT devices so it can be map
     VIPERTOKEN=""
     VIPERHOST=""
     VIPERPORT=""
       
   
     def producetokafka(value, tmlid, identifier,producerid,maintopic,substream,args):
        inputbuf=value     
        topicid=args['topicid']
     
        # Add a 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic 
        delay=args['delay']
        enabletls = args['enabletls']
        identifier = args['identifier']
   
        try:
           result=maadstml.viperproducetotopic(VIPERTOKEN,VIPERHOST,VIPERPORT,maintopic,producerid,enabletls,delay,'','', '',0,inputbuf,substream,
                                               topicid,identifier)
        except Exception as e:
           print("ERROR:",e)
   
     @task(task_id="gettmlsystemsparams")         
     def gettmlsystemsparams():
       VIPERTOKEN = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERTOKEN")
       VIPERHOST = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERHOST")
       VIPERPORT = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERPORT")
   
       if VIPERHOST != "":
           app = Flask(__name__)
           app.run(port=default_args['rest_port'])
   
           @app.route('/jsondataline', methods=['POST'])
           def storejsondataline():
             jdata = request.get_json()
             readdata(jdata)
   
           @app.route('/jsondataarray', methods=['POST'])
           def storejsondataarray():    
             jdata = request.get_json()
             json_array = json.load(jdata)
             for item in json_array: 
                readdata(item)
           
   
        #return [VIPERTOKEN,VIPERHOST,VIPERPORT]
           
     def readdata(valuedata):
         args = default_args    
   
         # MAin Kafka topic to store the real-time data
         maintopic = args['topics']
         producerid = args['producerid']
         try:
             producetokafka(valuedata.strip(), "", "",producerid,maintopic,"",args)
             # change time to speed up or slow down data   
             #time.sleep(0.15)
         except Exception as e:
             print(e)  
             pass  
     
       
     gettmlsystemsparams()   
   
   dag = startproducingtotopic()

STEP 3c: Produce Data Using gRPC: tml-read-gRPC-step-3-kafka-producetotopic-dag.py
--------------------- 	

.. code-block::
   :emphasize-lines: 22,23,24,25,26,27,28,29,30,31,32,33,34

   import maadstml
   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from airflow.operators.bash import BashOperator
   from datetime import datetime
   from airflow.decorators import dag, task
   import grpc
   from concurrent import futures
   import time
   import tml_grpc_pb2_grpc as pb2_grpc
   import tml_grpc_pb2 as pb2
   import sys
   
   sys.dont_write_bytecode = True
   ##################################################  gRPC SERVER ###############################################
   # This is a gRPCserver that will handle connections from a client
   # There are two endpoints you can use to stream data to this server:
   # 1. jsondataline -  You can POST a single JSONs from your client app. Your json will be streamed to Kafka topic.
   # 2. jsondataarray -  You can POST JSON arrays from your client app. Your json will be streamed to Kafka topic.
   
   ######################################## USER CHOOSEN PARAMETERS ########################################
   default_args = {
     'owner' : 'Sebastian Maurice',    
     'enabletls': 1,
     'microserviceid' : '',
     'producerid' : 'iotsolution',  
     'topics' : 'iot-raw-data', # *************** This is one of the topic you created in SYSTEM STEP 2
     'identifier' : 'TML solution',  
     'gRPC_Port' : 9001,  # <<< ***** replace with gRPC port i.e. this gRPC server listening on port 9001 
     'delay' : 7000, # << ******* 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic
     'topicid' : -999, # <<< ********* do not modify          
     'start_date': datetime (2024, 6, 29),
     'retries': 1,
   }
       
   ######################################## DO NOT MODIFY BELOW #############################################
   
   # Instantiate your DAG
   @dag(dag_id="tml-read-gRPC-step-3-kafka-producetotopic-dag", default_args=default_args, tags=["tml-read-gRPC-step-3-kafka-producetotopic-dag"], schedule=None,catchup=False)
   def startproducingtotopic():
     # This sets the lat/longs for the IoT devices so it can be map
     VIPERTOKEN=""
     VIPERHOST=""
     VIPERPORT=""
   
     class TmlprotoService(pb2_grpc.TmlprotoServicer):
   
       def __init__(self, *args, **kwargs):
           pass
   
       def GetServerResponse(self, request, context):
   
           # get the string from the incoming request
           message = request.message
           readata(message)
           #result = f'Hello I am up and running received "{message}" message from you'
           #result = {'message': result, 'received': True}
   
           #return pb2.MessageResponse(**result)
       
     @task(task_id="serve")  
     def serve():
       server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
       pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
       server.add_insecure_port("[::]:{}".format(default_args['gRPC_Port']))
       server.start()
       server.wait_for_termination()
       
     def producetokafka(value, tmlid, identifier,producerid,maintopic,substream,args):
        inputbuf=value     
        topicid=args['topicid']
     
        # Add a 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic 
        delay=args['delay']
        enabletls = args['enabletls']
        identifier = args['identifier']
   
        try:
           result=maadstml.viperproducetotopic(VIPERTOKEN,VIPERHOST,VIPERPORT,maintopic,producerid,enabletls,delay,'','', '',0,inputbuf,substream,
                                               topicid,identifier)
        except Exception as e:
           print("ERROR:",e)
   
     @task(task_id="gettmlsystemsparams")         
     def gettmlsystemsparams():
       VIPERTOKEN = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERTOKEN")
       VIPERHOST = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERHOST")
       VIPERPORT = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERPORT")
       
       return [VIPERTOKEN,VIPERHOST,VIPERPORT]
           
             
     def readdata(valuedata):
         args = default_args
         # MAin Kafka topic to store the real-time data
         maintopic = args['topics']
         producerid = args['producerid']
       
         try:
             producetokafka(valuedata.strip(), "", "",producerid,maintopic,"",args)
             # change time to speed up or slow down data   
             time.sleep(0.15)
         except Exception as e:
             print(e)  
             pass  
     
       
     serve()
   
   dag = startproducingtotopic()

STEP 3d: Produce Data Using LOCALFILE: tml-read-LOCALFILE-step-3-kafka-producetotopic-dag.py
--------------------- 	

.. code-block::
   :emphasize-lines: 10,11,12,13,14,15,16,17,18,19,20,21,22,23

   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from airflow.operators.bash import BashOperator
   from datetime import datetime
   from airflow.decorators import dag, task
   import sys
   
   sys.dont_write_bytecode = True
   ######################################## USER CHOOSEN PARAMETERS ########################################
   default_args = {
     'owner' : 'Sebastian Maurice',    
     'enabletls': 1,
     'microserviceid' : '',
     'producerid' : 'iotsolution',  
     'topics' : 'iot-raw-data', # *************** This is one of the topic you created in SYSTEM STEP 2
     'identifier' : 'TML solution',  
     'inputfile' : '/rawdata/?',  # <<< ***** replace ?  to input file name to read. NOTE this data file should be JSON messages per line and stored in the HOST folder mapped to /rawdata folder 
     'delay' : 7000, # << ******* 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic
     'topicid' : -999, # <<< ********* do not modify  
     'start_date': datetime (2024, 6, 29),
     'retries': 1,
   }
      
   ######################################## DO NOT MODIFY BELOW #############################################
   
   # Instantiate your DAG
   @dag(dag_id="tml_localfile_step_3_kafka_producetotopic_dag", default_args=default_args, tags=["tml-localfile-step-3-kafka-producetotopic"], schedule=None,catchup=False)
   def startproducingtotopic():
     # This sets the lat/longs for the IoT devices so it can be map
     VIPERTOKEN=""
     VIPERHOST=""
     VIPERPORT=""
       
     
     def producetokafka(value, tmlid, identifier,producerid,maintopic,substream,args):
        inputbuf=value     
        topicid=args['topicid']
     
        # Add a 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic 
        delay = args['delay']
        enabletls = args['enabletls']
        identifier = args['identifier']
   
        try:
           result=maadstml.viperproducetotopic(VIPERTOKEN,VIPERHOST,VIPERPORT,maintopic,producerid,enabletls,delay,'','', '',0,inputbuf,substream,
                                               topicid,identifier)
        except Exception as e:
           print("ERROR:",e)
   
     @task(task_id="gettmlsystemsparams")         
     def gettmlsystemsparams():
       VIPERTOKEN = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERTOKEN")
       VIPERHOST = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERHOST")
       VIPERPORT = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERPORT")
       
       return [VIPERTOKEN,VIPERHOST,VIPERPORT]
           
     @task(task_id="readdata")        
     def readdata(params):
         args = default_args    
         basedir = '/'  
         inputfile=basedir + args['inputfile']
   
         # MAin Kafka topic to store the real-time data
         maintopic = args['topics']
         producerid = args['producerid']
       
         k=0
   
         file1 = open(inputfile, 'r')
         print("Data Producing to Kafka Started:",datetime.datetime.now())
   
         while True:
           line = file1.readline()
           line = line.replace(";", " ")
           # add lat/long/identifier
           k = k + 1
           try:
             if not line or line == "":
               #break
               file1.seek(0)
               k=0
               print("Reached End of File - Restarting")
               print("Read End:",datetime.datetime.now())
               continue
   
             producetokafka(line.strip(), "", "",producerid,maintopic,"",args)
             # change time to speed up or slow down data   
             #time.sleep(0.15)
           except Exception as e:
             print(e)  
             pass  
     
         file1.close()
       
     readdata(gettmlsystemsparams())
       
   dag = startproducingtotopic()

Preprocessing Types
-----------------

TML preprocesses real-time data for every entity along each sliding time window.  This is quick and powerful way to accelerate insights from real-time data with very little effort.  TML provide over 35 different preprocessing types:

.. list-table::

   * - **Preprocessing Type**
     - **Description**
   * - anomprob
     - This will determine the probability that there is an anomaly for each entity in the sliding time windows
   * - anomprobx-y
     - where X and Y are numbers or "n", if "n" means examine all anomalies for recurring patterns. 
       This will find the anomalies in the data - ignoring set patterns. They allow you to check if the anomaly
       in the streams are truly anomalies and not some pattern. For example, if a IoT device shuts off and turns on again routinely, 
       this may be picked up as an anomaly when in fact it is normal behaviour. So, to ignore these cases, if ANOMPROB2-5, tells Viper, 
       check anomaly with patterns of 2-5 peaks. If the stream has two classes and these two classes are like 0 and 1000, and show a pattern, 
       then they should not be considered an anomaly. Meaning, class=0, is the device shutting down, class=1000 is the device turning back on. 
       If ANOMPROB3-10, Viper will check for patterns of classes 3 to 10 to see if they recur routinely. This is very helpful to reduce false 
       positives and false negatives.
   * - autocorr
     - This will determine the autocorrelation in the data for each entity in the sliding time windows
   * - avg
     - This will determine the average value for each entity in the sliding time windows
   * - avgtimediff
     - This will determine the average time in seconds between the first and last timestamp for each entity in sliding windows; time should be in this 
       layout:2006-01-02T15:04:05.
   * - consistency
     - This will check if the data all have consistent data types. Returns 1 for consistent data types, 0 otherwise for each entity in sliding windows
   * - count
     - This will count the number of numeric data points in the sliding time windows for each entity
   * - countstr
     - This will count the number of string values in the sliding time windows for each entity
   * - cv
     - This will determine the coefficient of variation average of the median and the midhinge for each entity in sliding windows
   * - dataage_[UTC offset]_[timetype]
     - dataage can be used to check the last update time of the data in the data stream from current local time. You can specify the UTC offset to adjust the 
       current time to match the timezone of the data stream. You can specify timetype as millisecond, second, minute, hour, day. For example, if 
       dataage_1_minute, then this processtype will compare the last timestamp in the data stream, to the local UTC time offset +1 and compute the time difference 
       between the data stream timestamp and current local time and return the difference in minutes. This is a very powerful processtype for data quality and 
       data assurance programs for any number of data streams.
   * - diff
     - This will find the difference between the highest and lowest points in the sliding time windows for each entity
   * - diffmargin
     - This will find the percentage difference between the highest and lowest points in the sliding time windows for each entity
   * - entropy
     - This will determine the entropy in the data for each entity in the sliding time windows; will compute the amount of information in the data stream.
   * - geodiff
     - This will determine the distance in kilimetres between two latitude and longitude points for each entity in sliding windows 
   * - gm (geometric mean)
     - This will determine the geometric mean for each entity in sliding windows
   * - hm (harmonic mean)
     - This will determine the harmonic mean for each entity in sliding windows
   * - iqr
     - This will compute the interquartile range between Q1 and Q3 for each entity in sliding windows
   * - kurtosis
     - This will determine the kurtosis for each entity in sliding windows
   * - mad
     - This will determine the mean absolute deviation for each entity in sliding windows
   * - max
     - This will determine the maximum value for each entity in the sliding time windows
   * - median
     - This will find the median of the numeric points in the sliding time windows for each entity
   * - meanci95
     - returns a 95% confidence interval: mean, low, high for each entity in sliding windows.
   * - meanci99
     - returns a 99% confidence interval: mean, low, high for each entity in sliding windows.
   * - midhinge
     - This will determine the average of the first and third quartiles for each entity in sliding windows
   * - min
     - This will determine the minimum value for each entity in the sliding time windows
   * - outliers
     - This will find the outliers of the numeric points in the sliding time windows for each entity
   * - outliersx-y
     - where X and Y are numbers or "n", if "n" means examine all outliers for recurring patterns. 
       This will find the outliers in the data - ignoring set patterns. They allow you to check if the outlier
       in the streams are truly outliers and not some pattern. For example, if a IoT device shuts off and turns on again routinely, 
       this may be picked up as an outlier when in fact it is normal behaviour. So, to ignore these cases, if OUTLIER2-5, tells Viper, 
       check outliers with patterns of 2-5 peaks. If the stream has two classes and these two classes are like 0 and 1000, and show a pattern, 
       then they should not be considered an outlier. Meaning, class=0, is the device shutting down, class=1000 is the device turning back on. 
       If OUTLIER3-10, Viper will check for patterns of classes 3 to 10 to see if they recur routinely. This is very helpful to reduce false 
       positives and false negatives.
   * - raw
     - Will not process data stream for each entity in sliding windows.
   * - skewness
     - This will determine the skewness for each entity in sliding windows
   * - spikedetect
     - This will determine if there are any spikes in the data using the zscore, using lag = 5, threshold = 3.5 (standard deviation), influence = 0.5,  for each 
       entity in sliding 
       windows
   * - sum
     - This will find the sum of the numeric points in the sliding time windows for each entity
   * - timediff
     - This will determine, in seconds, the time difference between the first and last timestamp for each entity in sliding windows; time should be in this 
       layout:2006-01-02T15:04:05.
   * - trend
     - This will determine the trend value for each entity in the sliding time windows.  If the trend value is less than zero then
       data in the sliding time window is decreasing, if trend value is greater than zero then it is increasing.
   * - trimean
     - This will determine the average of the median and the midhinge for each entity in sliding windows
   * - unique
     - This will determine if there are unique numeric values in the data for each entity in sliding windows. Returns 1 if no data duplication (unique), 0 
       otherwise.
   * - uniquestr
     - This will determine if there are unique string values in the data for each entity in sliding windows. Checks string data for duplication. Returns 1 if no 
       data duplication (unique), 0 otherwise. 
   * - variance
     - This will find the variane of the numeric points in the sliding time windows for each entity
   * - varied
     - This will determine if there is variation in the data in the sliding time windows for each entity.  

STEP 4: Preprocesing Data: tml-system-step-4-kafka-preprocess-dag.py
--------------------------------

.. code-block::
   :emphasize-lines: 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40

   from airflow import DAG
   from airflow.operators.python import PythonOperator
   from airflow.operators.bash import BashOperator   
   from datetime import datetime
   from airflow.decorators import dag, task
   import sys
   
   sys.dont_write_bytecode = True
   ######################################## USER CHOOSEN PARAMETERS ########################################
   default_args = {
     'owner' : 'Sebastian Maurice',  # <<< *** Change as needed      
     'enabletls': 1, # <<< *** 1=connection is encrypted, 0=no encryption
     'microserviceid' : '',  # <<< *** leave blank
     'producerid' : 'iotsolution',   # <<< *** Change as needed   
     'raw_data_topic' : 'iot-raw-data', # *************** CONSUME DATA - This is one of the topic you created in SYSTEM STEP 2
     'preprocess_data_topic' : 'iot-preprocess-data', # **** PRODUCE PREPROCESS DATA TO THIS TOPIC - This is one of the topic you created in SYSTEM STEP 2
     'maxrows' : 500, # <<< ********** Number of offsets to rollback the data stream -i.e. rollback stream by 500 offsets
     'offset' : -1, # <<< Rollback from the end of the data streams  
     'brokerhost' : '',   # <<< *** Change as needed   
     'brokerport' : -999,  # <<< *** Change as needed   
     'preprocessconditions' : '', # <<< *** Change as needed   
     'delay' : 70, # Add a 70 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic     
     'array' : 0, # do not modify
     'saveasarray' : 1, # do not modify
     'topicid' : -999, # do not modify
     'rawdataoutput' : 1, # <<< 1 to output raw data used in the preprocessing, 0 do not output
     'asynctimeout' : 120, # <<< 120 seconds for connection timeout - Change as needed
     'timedelay' : 0, # <<< connection delay
     'tmlfilepath' : '', # leave blank
     'usemysql' : 1, # do not modify
     'streamstojoin' : '', # leave blank
     'identifier' : 'IoT device performance and failures', # <<< ** Change as needed
     'preprocesstypes' : 'anomprob,trend,avg', # <<< **** MAIN PREPROCESS TYPES CHANGE AS NEEDED REFER TO PREPROCESS TYPES TABLE
     'pathtotmlattrs' : '', # Leave blank         
     'jsoncriteria' : '', # <<< **** Specify your json criteria  refer to JSON PROCESSING section
     'identifier' : 'TML solution',   # <<< *** Change as needed   
     'start_date': datetime (2024, 6, 29),  # <<< *** Change as needed   
     'retries': 1,  # <<< *** Change as needed         
   }
   
   ######################################## DO NOT MODIFY BELOW #############################################
   
   # Instantiate your DAG
   @dag(dag_id="tml-system-step-4-kafka-preprocess-dag", default_args=default_args, tags=["tml-system-step-4-kafka-preprocess-dag"], schedule=None,catchup=False)
   def startprocessing():
     # This sets the lat/longs for the IoT devices so it can be map
     VIPERTOKEN=""
     VIPERHOST=""
     VIPERPORT=""
       
     @task(task_id="processtransactiondata")
     def processtransactiondata():
   
        preprocesstopic = default_args['preprocess_data_topic']
        maintopic =  default_args['raw_data_topic']  
        mainproducerid = default_args['producerid']     
                   
        VIPERTOKEN = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERTOKEN")
        VIPERHOST = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERHOST")
        VIPERPORT = ti.xcom_pull(dag_id='tml_system_step_1_getparams_dag',task_ids='getparams',key="VIPERPORT")
           
    #############################################################################################################
         #                                    PREPROCESS DATA STREAMS
   
         # Roll back each data stream by 10 percent - change this to a larger number if you want more data
         # For supervised machine learning you need a minimum of 30 data points in each stream
        maxrows=default_args['maxrows']
           
         # Go to the last offset of each stream: If lastoffset=500, then this function will rollback the 
         # streams to offset=500-50=450
        offset=default_args['offset']
         # Max wait time for Kafka to response on milliseconds - you can increase this number if
         #maintopic to produce the preprocess data to
        topic=maintopic
         # producerid of the topic
        producerid=mainproducerid
         # use the host in Viper.env file
        brokerhost=default_args['brokerhost']
         # use the port in Viper.env file
        brokerport=default_args['brokerport']
         #if load balancing enter the microsericeid to route the HTTP to a specific machine
        microserviceid=default_args['microserviceid']
   
     
         # You can preprocess with the following functions: MAX, MIN, SUM, AVG, COUNT, DIFF,OUTLIERS
         # here we will take max values of the arcturus-humidity, we will Diff arcturus-temperature, and average arcturus-Light_Intensity
         # NOTE: The number of process logic functions MUST match the streams - the operations will be applied in the same order
   #
        preprocessconditions=default_args['preprocessconditions']
            
        # Add a 7000 millisecond maximum delay for VIPER to wait for Kafka to return confirmation message is received and written to topic 
        delay=default_args['delay']
        # USE TLS encryption when sending to Kafka Cloud (GCP/AWS/Azure)
        enabletls=default_args['enabletls']
        array=default_args['array']
        saveasarray=default_args['saveasarray']
        topicid=default_args['topicid']
       
        rawdataoutput=default_args['rawdataoutput']
        asynctimeout=default_args['asynctimeout']
        timedelay=default_args['timedelay']
   
        jsoncriteria = default_args['jsoncriteria']
           
        tmlfilepath=default_args['tmlfilepath']
        usemysql=default_args['usemysql']
   
        streamstojoin=default_args['streamstojoin']
        identifier = default_args['identifier']
   
        # if dataage - use:dataage_utcoffset_timetype
        preprocesstypes=default_args['preprocesstypes']
   
        pathtotmlattrs=default_args['pathtotmlattrs']       
        try: 
           result=maadstml.viperpreprocesscustomjson(VIPERTOKEN, VIPERHOST, VIPERPORT, topic, producerid, offset, jsoncriteria, rawdataoutput, maxrows,enabletls, 
                 delay, brokerhost, brokerport, microserviceid, topicid, streamstojoin, preprocesstypes, preprocessconditions, identifier,                                         preprocesstopic, array,saveasarray, timedelay, asynctimeout, usemysql, tmlfilepath, pathtotmlattrs)
           return result
        except Exception as e:
           print(e)
           return e
     
     processtransactiondata()
       
   dag = startprocessing()

Entity Based Machine Learning By TML
-------------------

Another powerful feature of TML is performing machine learning at the entity level.  See :ref:`TML Performs Entity Level Machine Learning and Processing` for refresher.  For example, if TML is processing real-time data from 1 million IoT devices, it can create 1 million individual machine learnig models for each device.  TML uses the following ML algorithms:

.. list-table::

   * - **Algorithm**
     - **Description**   
   * - Logistic Regression
     - Performs classification regression and predicts probabilities
   * - Linear Regression
     - Performs linear regression using OLS algorithm
   * - Gradient Boosting
     - Gradient boosting for non-linear real-time data
   * - Ridge Regression
     - Ridge Regression for non-linear real-time data
   * - Neural networks
     - Neural networks non-linear real-time data

.. code-block::
   :emphasize-lines: 10,11,12,13,14,15,16,17,18,19

Predictions
--------------

GenAI
---------


Example TML Solution Container Reference Architecture
-----------------------------------------------

.. figure:: solutioncontainer.png

The above image shows a typical TML solution container

.. note::

   * Every TML solution runs in a Docker container
   * Linux is installed in the container
   * `TMUX (terminal multiplexer) <https://github.com/tmux/tmux/wiki>`_ is used to structure TML solution components in their own task windows to make it easier to 
     maintain and operationalize TML solutions
   * Apache Kafka is installed (Cloud Kafka can easily be used)
   * maria db is used as a configuration database for TML solutions
   * specific solution python scripts are installed and run the TML solution
   * TML dashboard code (html/javascript) runs in the container
   * java is installed
