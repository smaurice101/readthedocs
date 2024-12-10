Welcome to Transactional Machine Learning (TML) and TML Solution Studio (TSS) Documentation!
===================================

TML Solution Studio (TSS): NO-CODE TML Solution Development Using Real-Time Data Streams
----------------------

TSS is a revolutionary platform for building, enterprise-ready, process-driven, advanced, scalable, intelligent real-time TML solutions **really fast** with :ref:`Pre-Written 10 Apache Airflow DAGs To Speed Up TML Solution Builds` - within minutes - what can take orgaizations up to 6 months to build. 

These real-time TML solutions can process any real-time data from devices and systems. The real-time data are ingested using RESTful, gRPC, MQTT APIs or localfile on the file system. **All TML solutions are containerized with Docker (scale with Kubernetes), come with automated documentation about the solution, automated commits to Github for real-time logging, and automated real-time dashboard for visualization using websockets.**

TML solutions run on Linux operating systems (or windows/mac/and other OS), and on any current and legacy chipsets. TML solutions can be deployed on the cloud (**with Internet**) or on-premise (**without Internet**) to process unlimited real-time data globally.  TML solutions can run on any cloud infrastructure.

Watch The TSS Youtube Videos
"""""""""""""""""""""""""""""""

.. list-table::

   * - **Video Name**
     - **YouTube URL**
   * - **TSS Video:** 
     - `Youtube Video <https://www.youtube.com/watch?v=z3h2nJXVgUs>`_
   * - **Managing TML Projects (Creating,** 

       **deleting, copying and stopping):** 
     - `Youtube Video <https://youtu.be/46k18ExfLLE>`_ See details here 

       :ref:`Lets Start Building a TML Solution`
   * - **Scaling TML Solutions with Kubernetes** 

     - `Youtube Video <https://www.youtube.com/watch?v=MEbmTXIQpVo>`_ See details here 

       :ref:`Scaling TML Solutions with Kubernetes`
   * - **Storing Secure Passwords in Kubernetes**
     - `Youtube Video <https://youtu.be/Xyw_XE9L22U>`_

       Describes how to store secure passwords in Kubernetes

       to make your TML solutions more secure and in
       compliance with IT security standards.
   * - **Running TML Projects in TSS:** 
     - `Youtube Video <https://youtu.be/MH-l0LBkxXc>`_ 

       Describes how to run a TML project. See details 

       here :ref:`Lets Start Building a TML Solution`
   * - **Ingesting Real-Time Data into TML Solutions:** 
     - `Youtube Video <https://youtu.be/o0Xk8pHV4nw>`_ 

       Describes how to ingest real-time data using:

       MQTT, RESTful API, gRPC API or Local file.

       See here :ref:`STEP 3: Produce to Kafka Topics`
   * - **How To Create Amazing TML Real-Time Dashboards:** 
     - `Youtube Video <https://youtu.be/ZnaU1RJfXT8>`_ 

       Describes how to create TML real-time dashboards

       using websockets, and no third-party tools.

       See here :ref:`TML Real-Time Dashboards` and,

       :ref:`STEP 7: Real-Time Visualization: tml-system-step-7-kafka-visualization-dag`
   * - **TML Examples Video**: 
     - `YouTube Video <https://www.youtube.com/watch?v=ZzLL3tfBsh0>`_ 

       Describes examples shown here: :ref:`TML Solution Examples`
   * - **TML JSON Criteria Creator**: 
     - `YouTube Video <https://www.youtube.com/watch?v=3s5-7tiE1-s>`_ 

       Describes Json Criteria creation for Json 

       Processing shown here: :ref:`JSON PROCESSING`
   * - **Zoom student meeting at Seneca Polytechnic:** 
     - `YouTube Video <https://youtu.be/lZI50X6dp48>`_ Zoom meeting 
 
       to students to show how to run Examples 1 nand 3 with data 
 
       streaming to a MQTT broker in HiveMQ.  

       See here :ref:`TML Solution Examples`
   * - **TML Step 1 Dag Configurations**: 
     - `YouTube Video <https://youtu.be/N2ghgJuZAiU>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 1: Get TML Core Params: tml_system_step_1_getparams_dag`
   * - **TML Step 2 Dag Configurations**: 
     - `YouTube Video <https://youtu.be/h9HL_xarNgw>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 2: Create Kafka Topics: tml_system_step_2_kafka_createtopic_dag`
   * - **TML Step 3 Dag Configurations**: 
     - Refer to **Ingesting Real-Time Data into TML Solutions:**
       
       :ref:`STEP 3: Produce to Kafka Topics`
   * - **TML Step 4 Dag Configurations**: 
     - `YouTube Video <https://youtu.be/mLvi__oNyCA>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 4: Preprocesing Data: tml-system-step-4-kafka-preprocess-dag`
   * - **TML Step 4b Dag Configurations**: 
     - `YouTube Video <https://youtu.be/UA_gm2eqaAU>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 4b: Preprocesing 2 Data: tml-system-step-4b-kafka-preprocess-dag`
   * - **TML Step 5 Dag Configurations**: 
     - `YouTube Video <https://youtu.be/oVIne8JCowI>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 5: Entity Based Machine Learning : tml-system-step-5-kafka-machine-learning-dag`
   * - **TML Step 6 Dag Configurations**: 
     - `YouTube Video <https://youtu.be/S0qQD8n56JU>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 6: Entity Based Predictions: tml-system-step-6-kafka-predictions-dag`
   * - **TML Step 7 Dag Configurations**: 
     - Refer to **How To Create Amazing TML Real-Time Dashboards:**

       :ref:`STEP 7: Real-Time Visualization: tml-system-step-7-kafka-visualization-dag`
   * - **TML Step 8 Dag**: 
     - Step 8 Dag for docker container - Does not require any configurations. 

       See :ref:`STEP 8: Deploy TML Solution to Docker : tml-system-step-8-deploy-solution-to-docker-dag`
   * - **TML Step 9 Dag Configurations**: 
     - `YouTube Video <https://youtu.be/dGzsqx8MtIY>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 9: PrivateGPT and Qdrant Integration: tml-system-step-9-privategpt_qdrant-dag`
   * - **TML Step 10 Dag Configurations**: 
     - `YouTube Video <https://youtu.be/iue3ljO_bBU>`_ 

       Describes key parameter configurations in: 
      
       :ref:`STEP 10: Create TML Solution Documentation: tml-system-step-10-documentation-dag`

.. important::
   **TML Solution Studio (TSS)**

   You will learn how to use the :ref:`TML Solution Studio (TSS) Container` to build advanced, scalable, end-end real-time TML solutions easily with little to no- 
   code.  **The TSS redefines how complex real-time solutions can be built by anyone**, using pre-written Apache Airflow TML DAGs, that are integrated Github, AI 
   (PrivateGPT), Docker, and Kubernetes, with automated online documentation of your entire solution.

   **TSS enables TML solutions to be developed WITHOUT WRITING ANY CODE - ONLY CONFIGURATIONS TO DAGS - dramatically accelerating real-time solution builds.**

Transactional Machine Learning (TML) Overview
----------------------

.. important::
   **Transactional Machine Learning (TML): The Machine Learning and AI Platform for Real-Time Data Streams**

   TML Is Based On the Belief that **"Fast data requires fast machine learning and AI for fast decision-making"** that provides **a faster way to build advanced, scalable, cost- 
   effective and secure real-time solutions that can be built by anyone.**

   TML gives rise in the industy to a **Data Stream Scientist** versus a **Data Scientist** in conventional machine learning (CML). 

**Transactional Machine Learning (TML)** using Data Streams and AutoML is a platform for building and streaming cloud native (or on-prem) solutions using Apache Kafka or Redpanda as the data backbone, with Kubernetes and Docker as core infrastucture components, running on Confluent, AWS, GCP, AZURE, for advanced machine learning solutions using transactional data to learn from, and provide insights, quickly and continuously to any number of devices and humans in any format!

**TML Book Details Found Here:** `Springer (Publisher) site <https://link.springer.com/book/10.1007/978-1-4842-7023-3>`_

**TML Video:** `Watch the Youtube Video <https://youtu.be/ZrhRg2J8YbU>`_

Apply data preprocessing and auto machine learning to data streams and create transactional machine learning (TML) solutions that are:
 
 **1. frictionless**: require minimal to no human intervention 
 
 **2. elastic**: machine learning solutions that can scale up or down using Kubernetes to control or enhance the number of data streams, algorithms (or machine learning models) and predictions instantly and continuously.

.. note::
  
  TML is ideal when data are highly erratic (nonlinear) and you want the machine to learn from the latest dataset by creating sliding windows of training datasets and auto creating micro-machine learning models quickly, that can be easily scaled, managed and the insights used immediately from any device! There are many TML use cases such as:
  
  1. IoT: Capture real-time, fast, data, and build custom micro-machine learning models for every IoT device specific to the environment that the device operates in and predict failures, optimize device settings, and more.
  
  2. IoT Edge: TML is ideal for edge devices with No Internet connections. Simply use the On-Prem version of TML software, with On-Prem Kafka and create large and powerful, real-time, edge solutions.
  
  3. HealthCare: TML is ideal for health data processing for patients, payers, and providers. Open access to health data has been mandated by CMS, which opens up enormous opportunities for TML.
  
  4. Banking/Finance Fraud Detect: Detect fraud using unsupervised learning on data streams and process millions of transactions for fraud - see the LinkedIn blog
  
  5. Financial Trading: Use TML to analyse stock prices and predict sub-second stock prices!
  
  6. Pricing: Use TML to build optimal pricing of products at scale.
  
  7. Oil/Gas: Use TML to optimize oil drilling operations sub-second and drill oil wells faster and cheaper with minimal downtime
  
  8. SO MUCH MORE...
  
  The above usecases are not possible with conventional machine learning methods that require frequent human interventions that create lots of friction, and not very elastic.
  
  By using Apache Kafka On-Premise many advanced, and large, TML usecases are 80-90% cheaper than cloud-native usecases, mainly because storage, compute, Egress/Ingress and Kafka partitions are localized. Given Compute and Storage are extremely low-cost On-Premise solutions with TML are on the rise. TML On-Prem is ideal for small companies or startups that do not want to incur large cloud costs but still want to provide TML solutions to their customers.
  
  Strengthen your knowledge of the inner workings of TML solutions using data streams with auto machine learning integrated with Apache Kafka. You will be at the forefront of an exciting area of machine learning that is focused on speed of data and algorithm creation, scale, and automation.

Contents
=======

Introduction:

.. toctree::
   :numbered:

   quickstart
   tmlbook
   docker
   solutions

Scaling:

.. toctree::
   :numbered:

   kube
   tmlbuilds
   examples
   git
   usage 
   readthedocs
   hive
   gitsetup
   tmllogs
   coreintegrations
   dashboards
   api
   entity
   jsonprocessing
   viper
   genai
   alone
   
   
