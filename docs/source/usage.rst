TML Solution Components
=====

Below describes the entire TML technologgy solution stack.

1. TML Components: Three Binaries
------------

**TML is comprised of 3 binaries written in **Go**:** https://github.com/smaurice101/transactionalmachinelearning

1. *Viper* - source - sink binary for Apache Kafka
2. *HPDE* - AutoML binary for real-time data
3. *Viperviz* - Visualization binary for real-time dashboards

.. list-table::

   * - **Binary**
     - **Description**
   * - Viper
     - This is the CORE binary that performs all the major TML functions of processing and machine learning.  This binary acts like a microservice that can be 
       instantiated any number of times to process large amounts of real-time data.

       This binary is compatible with REST API.  TML solutions (using Python) connect to this binary and instruct it to stream data to Kafka, preprocess data, and 
       develop training data sets for machine learning.
   * - HPDE
     - Hyper-prediction technology performs all machine learning functions.  Viper connects to HPDE, using REST, and instructs it to perform machine learning.  By 
       off-loading this function to HPDE, TML can perform very fast machine learning (in few seconds) for each entity and sliding time window.  Refer to :ref:`TML 
       Performs Entity Level Machine Learning and Processing` and :ref:`Entity Based Machine Learning By TML`
   * - Viperviz
     - This binary performs real-time streaming visualization using websockets.  This is a very powerful binary because it uses the underlying network to streaming 
       data to a client browser for fast, and very cost-effective, visualization of real-time TML solution outputs.  This means users do NOT need a third-party 
       visualization tool like Tableau or PowerBI. Users can create amazing real-time dashboards quickly and cheaply.  Refer to example dashboards here :ref:`TML 
       Real-Time Dashboards`

2. TML Component: One Core Python Library
--------------------------

**TML Python Library:** https://pypi.org/project/maadstml/

*MAADSTML* Python library : API to build TML solutions that connect to the Viper binary

3. TML Component: Apache Kafka
--------------------------

TML integrates with Apache Kafka - on-premise or in the cloud.

.. important::

   TML binaries are integrated with Apache Kafka.

4. TML Component: Docker Containers
--------------------------

All TML solutions are containerized with docker for production deployments.

5. TML Component: Kubernetes
--------------------------

All TML solution containers scale with Kubernetes.  This allows companies to build fast, scalable, real-time solutions.

How The TML Components Are Integrated 
--------------------------

TML solutions are developed using the MAADSTML Python library that connects to the TML Binaries, using REST API, for streaming real-time data to Apache Kafka, processing data in Kafka, and performing machine learning.  Once the TML solutions are built, they are containerized with Docker and scaled with Kubernetes.

.. important::

   TML performs **in-memory processing** of real-time data and **does NOT require an external database** - ONLY KAFKA is needed.  This results in dramatic cost- 
   savings for storage, compute and network data transfers.

   TML **does NOT perform SQL queries**, it performs :ref:`JSON PROCESSING`.  This results in much faster, and much cheaper processing of real-time data.




