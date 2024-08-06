TML Solution Building
======================

The fastest way to build TML solutions with your real-time data is to use the **TML Solution Studio Container** located here: [Dockerhub]

Apache Airflow DAGs
-------------------

The TML solution process with DAGS (explained in detail below).  **The entire TML solution build process is highly efficient; advanced, scalable, real-time TML solutions can be built in few hours with GenAI integrations!**

.. figure:: tsol1.png

DAGs (Directed Acyclic Graphs) are a powerful and easy way to build powerful (real-time) TML solutions quickly.  Users are provided with the following DAGs:

.. note::
   
   The numbers in the DAGs indicate solution process step.  For example, step 2 is dependent on step 1.

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
