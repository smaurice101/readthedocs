TML Solution Building
======================

The fastest way to build TML solutions with your real-time data is to use the **TML Solution Studio Container** located here: [Dockerhub]

Apache Airflow DAGs
-------------------

DAGs (Directed Acyclic Graphs) are a powerful and easy way to build powerful (real-time) TML solutions quickly.  Users are provided with the following DAGs:

.. list-table::

   * - **DAG**
     - Description
   * - tml_system_step_1_getparams_dag
     - Description
   * - tml_system_step_2_kafka_createtopic_dag
     - Description
   * - tml_mqtt_step_3_kafka_producetotopic_dag
     - Description
   * - tml_localfile_step_3_kafka_producetotopic_dag
     - Description
   * - tml-read-gRPC-step-3-kafka-producetotopic-dag
     - Description
   * - tml-read-RESTAPI-step-3-kafka-producetotopic-dag
     - Description
   * - tml-system-step-4-kafka-preprocess-dag
     - Description
   * - tml-system-step-5-kafka-machine-learning-dag
     - Description
   * - tml-system-step-6-kafka-predictions-dag
     - Description
   * - tml-system-step-7-kafka-visualization-dag
     - Description
   * - tml_system_step_8_deploy_solution_to_docker_dag
     - Description
   * - tml_system_step_9_privategpt_qdrant_dag
     - Description

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
