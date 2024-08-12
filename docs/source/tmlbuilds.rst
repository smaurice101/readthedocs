TML Solution Building
======================

The fastest way to build TML solutions with your real-time data is to use the **TML Solution Studio Container** located here: [Dockerhub: To Be Posted Shortly]

Apache Airflow DAGs
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
   * - tml_mqtt_step_3_kafka_producetotopic_dag
     - This DAG is an MQTT server and will listen for a connection from a client.  You use this if your TML solution ingests data from MQTT system like HiveMQ and 
       stream it to Kafka.
   * - tml_localfile_step_3_kafka_producetotopic_dag
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

TML Core Params: tml_system_step_1_getparams_dag
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
     HTTPADDR=""
     with open(basedir + "/Viper-produce/admin.tok", "r") as f:
        VIPERTOKEN=f.read()
   
     if VIPERHOST=="":
        with open(basedir + '/Viper-produce/viper.txt', 'r') as f:
          output = f.read()
          VIPERHOST = HTTPADDR + output.split(",")[0]
          VIPERPORT = output.split(",")[1]
   
     ti.xcom_push(key='VIPERTOKEN',value=VIPERTOKEN)
     ti.xcom_push(key='VIPERHOST',value=VIPERHOST)
     ti.xcom_push(key='VIPERPORT',value=VIPERPORT)
     ti.xcom_push(key='HTTPADDR',value=HTTPADDR)
             
     updateviperenv()
    
     return [VIPERTOKEN,VIPERHOST,VIPERPORT,HTTPADDR]
     
     tmlsystemparams=getparams(default_args)
     if tmlsystemparams[1]=="":
        print("ERROR: No host specified")
    
   dag = tmlparams()

Create Kafka Topics: tml_system_step_2_kafka_createtopic_dag
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
     'replication' : 1,  # <<< ********** You change as needed
     'numpartitions': 1,  # <<< ********** You change as needed
     'enabletls': 1,  # <<< ********** You change as needed
     'brokerhost' : '',  # <<< ********** You change as needed
     'brokerport' : -999,  # <<< ********** You change as needed
     'microserviceid' : '',  # <<< ********** You change as needed
     'raw_data_topic' : 'iot-raw-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'preprocess_data_topic' : 'iot-preprocess-data,iot-preprocess2-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'ml_data_topic' : 'ml-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'prediction_data_topic' : 'prediction-data', # Separate multiple topics with comma <<< ********** You change topic names as needed
     'description' : 'Topics to store iot data',  
     'start_date': datetime (2024, 6, 29),
     'retries': 1,    
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





Preprocessing Data
-----------------

Machine Learning
-------------------

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
