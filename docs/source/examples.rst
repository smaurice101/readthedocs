TML Solution Examples
======================

All examples simply follow the steps here :ref:`Lets Start Building a TML Solution`

.. list-table::

   * - **Example**
   * - :ref:`Real-Time IoT Data Preprocessing Example`
       
       This will process IoT for anomalies, stream the results to a dashboad,

       build and push the container to docker hub, automatically create the

       solution documentation on Readthdocs, and auto-commit your solution

       to GitHub.

       Data Used is here (unzip the file): `Demo Data <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/data/IoTData.zip>`_
   * - :ref:`Real-Time IoT Data Preprocessing and Machine Learning Example`
      
       This will process IoT data, and perform entity level machine learning (TML)

       on the data, stream the results to a dashboad,

       build and push the container to docker hub, automatically create the

       solution documentation on Readthdocs, and auto-commit your solution

       to GitHub.

       Data Used is here (unzip the file): `Demo Data <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/data/IoTData.zip>`_
   * - :ref:`Cybersecurity Solution with PrivateGPT, MQTT, HiveMQ`
     
       This will process cybersecurity data for anomalies, 

       and further process the TML anomalies
      
       data by sending the results to privateGPT container. It will stream 

       the results to a dashboad,

       build and push the container to docker hub, automatically create the

       solution documentation on Readthdocs, and auto-commit your solution

       to GitHub.

       MQTT Client File here is: `MQTT Client <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/python/cyberwithprivategptmqtt.py>`_

       Data Used is here (unzip the file): `Demo Data <https://github.com/smaurice101/raspberrypi/blob/main/tml-airflow/data/cisco_network_data.zip>`_

.. note::
   While we are using a local file for the demos, this is to make it easy for users to build and run these solutions themselves.  Ideally, in industry, we would use APIs like MQTT, REST and gRPC to ingest data from devices and stream it to TML solutions.  TSS allows you to build solutions with these APIs with pre-written DAGs here:

   - :ref:`STEP 3a: Produce Data Using MQTT: tml-read-MQTT-step-3-kafka-producetotopic-dag`

     - With pre-built client library: :ref:`STEP 3a.i: MQTT CLIENT`

   - :ref:`STEP 3b: Produce Data Using RESTAPI: tml-read-RESTAPI-step-3-kafka-producetotopic-dag`

     - With pre-built client library: :ref:`STEP 3b.i: REST API CLIENT`

   - :ref:`STEP 3c: Produce Data Using gRPC: tml-read-gRPC-step-3-kafka-producetotopic-dag`

     - With pre-built client library: :ref:`STEP 3c.i: gRPC API CLIENT`

Real-Time IoT Data Preprocessing Example
----------------------

:ref:`Solution DAG Code: solution_preprocessing_dag-myawesometmlsolution-3f10`

This IoT Data Preprocessing Solution DAG: **solution_preprocessing_dag-myawesometmlsolution-3f10** reads local file data in **/rawdata/IoTdata.txt** and streams it to Kafka.  The streaming data are then processed with TML binary Viper and the output data are streamed to a browser that runs the dashboard: dashboard.html that is located in /Viperviz/viperviz/views.  

The solution will automatically build and push the solution container to docker hub, automatically create documentation on READTHEDOCS.io and **automatically commits your solution code to Github, all in about 2 minutes.**

.. figure:: soldags1.png
   :scale: 70%

Solution DAG Code: solution_preprocessing_dag-myawesometmlsolution-3f10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Python code below is the code representtion for the figure.  **This code builds the entire end-end TML solution in about 2 minutes.**

.. code-block:: PYTHON

      from __future__ import annotations
      
      import pendulum
      from airflow.decorators import task
      from airflow.models.dag import DAG
      from airflow.operators.bash import BashOperator
      from airflow.sensors.external_task import ExternalTaskSensor 
      import tsslogging
      import os
      from datetime import datetime
      import importlib
      from airflow.operators.python import (
          ExternalPythonOperator,
          PythonOperator
      )
      step1 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_1_getparams_dag-myawesometmlsolution-3f10")
      step2 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_2_kafka_createtopic_dag-myawesometmlsolution-3f10")
      step3 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_read_LOCALFILE_step_3_kafka_producetotopic_dag-myawesometmlsolution-3f10")
      step4 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_4_kafka_preprocess_dag-myawesometmlsolution-3f10")
      step5 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_5_kafka_machine_learning_dag-myawesometmlsolution-3f10")
      step6 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_6_kafka_predictions_dag-myawesometmlsolution-3f10")
      step7 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_7_kafka_visualization_dag-myawesometmlsolution-3f10")
      step8 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_8_deploy_solution_to_docker_dag-myawesometmlsolution-3f10")
      step9 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_9_privategpt_qdrant_dag-myawesometmlsolution-3f10")
      step10 = importlib.import_module("tml-solutions.myawesometmlsolution-3f10.tml_system_step_10_documentation_dag-myawesometmlsolution-3f10")
      
      
      with DAG(
          dag_id="solution_preprocessing_dag-myawesometmlsolution-3f10",
          start_date=datetime(2023, 1, 1),
          schedule=None,
      ) as dag:
        start_task = BashOperator(
          task_id="start_tasks_tml_preprocessing",
          bash_command="echo 'Start task'",
        )
      # STEP 1: Get the Parameters
        sensor_A = PythonOperator(
                  task_id="step_1_solution_task_getparams",
                  python_callable=step1.getparams,
                  provide_context=True,
        )
      
      # STEP 2: Create the Kafka topics
        sensor_B = PythonOperator(
            task_id="step_2_solution_task_createtopic",
            python_callable=step2.setupkafkatopics,
            provide_context=True,
        )
      # STEP 3: Produce data to topic        
        sensor_C = PythonOperator(
            task_id="step_3_solution_task_producetotopic",
            python_callable=step3.startproducing,
            provide_context=True,
        )
      # STEP 4: Preprocess the data        
        sensor_D = PythonOperator(
            task_id="step_4_solution_task_preprocess",
            python_callable=step4.dopreprocessing,
            provide_context=True,
        )
      # STEP 7: Containerize the solution     
        sensor_E = PythonOperator(
            task_id="step_7_solution_task_visualization",
            python_callable=step7.startstreamingengine,
            provide_context=True,
        )
      # STEP 8: Containerize the solution        
        sensor_F = PythonOperator(
            task_id="step_8_solution_task_containerize",
            python_callable=step8.dockerit,
            provide_context=True,      
        )
        start_task2 = BashOperator(
          task_id="Starting_Docker",
          bash_command="echo 'Start task Completed'",
        )    
        start_task3 = BashOperator(
          task_id="Starting_Documentation",
          bash_command="echo 'Start task Completed'",
        )
        start_task4 = BashOperator(
          task_id="Completed_TML_Setup_Now_Spawn_Main_Processes",
          bash_command="echo 'Start task Completed'",
        )
      # STEP 10: Document the solution
        sensor_G = PythonOperator(
            task_id="step_10_solution_task_document",
            python_callable=step10.generatedoc,
            provide_context=True,      
        )
      
        start_task >> sensor_A >> sensor_B >> start_task4 >> [sensor_C, sensor_D, sensor_E] >> start_task2 >> sensor_F >> start_task3  >> sensor_G

Successful Run Screen
"""""""""""""""""""""""

Below the TSS/Airflow screen that shows a successful TML solution build.  All colors should be green for all of the steps.  If you see a red color, it means your DAG has an error.

.. figure:: p53.png
   :scale: 50%

Solution Documentation Example
---------------------------
This is the solution documentation that is auto-generated by TSS.  Every TML solution you create will have its own auto-generated documentation that will provide details on the entire solution.

.. figure:: sp1.png
   :scale: 60%

.. important::
   You will need to run the solution in your own TSS environment for the links to work in this documentation.  It is provided as an example of the powerful capabilities of TSS: `https://myawesometmlsolution-3f10.readthedocs.io/ <https://myawesometmlsolution-3f10.readthedocs.io/>`_

Here is the Solution Real-Time Dashboard:

.. figure:: sp4.png
   :scale: 50%

Here is the Solution Docker Run container:

.. figure:: sp6.png
   :scale: 50%

The entire end-end real-time solution took less than 2 minutes to build:

.. figure:: sp7.png
   :scale: 50%

Github Commits
----------------

.. figure:: sp9.png
   :scale: 50%

Real-Time IoT Data Preprocessing and Machine Learning Example 
-----------------------------

:ref:`Solution DAG Code: solution_preprocessing_ml_dag-myawesometmlsolutionml-3f10`

This IoT Data Preprocessing and Machine Learning Solution DAG: **solution_preprocessing_ml_dag-myawesometmlsolutionml-3f10** reads local file data in /rawdata/IoTdata.txt and streams it to Kafka. **The streaming data are then processed and entity level machine learning is performed with TML binaries Viper and HPDE**, the output data are streamed to a browser that runs the dashboard: iot-failure-machinelearning.html, that is located in /Viperviz/viperviz/views.

The solution will automatically build and push the solution container to docker hub, automatically create documentation on READTHEDOCS.io and automatically commit your solution code to Github, all in about 2 minutes.

Solution DAG Code: solution_preprocessing_ml_dag-myawesometmlsolutionml-3f10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: PYTHON

    from __future__ import annotations
    
    import pendulum
    from airflow.decorators import task
    from airflow.models.dag import DAG
    from airflow.operators.bash import BashOperator
    from airflow.sensors.external_task import ExternalTaskSensor 
    import tsslogging
    import os
    from datetime import datetime
    import importlib
    from airflow.operators.python import (
        ExternalPythonOperator,
        PythonOperator
    )
    step1 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_1_getparams_dag-myawesometmlsolutionml-3f10")
    step2 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_2_kafka_createtopic_dag-myawesometmlsolutionml-3f10")
    step3 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_read_LOCALFILE_step_3_kafka_producetotopic_dag-myawesometmlsolutionml-3f10")
    step4 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_4_kafka_preprocess_dag-myawesometmlsolutionml-3f10")
    step5 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_5_kafka_machine_learning_dag-myawesometmlsolutionml-3f10")
    step6 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_6_kafka_predictions_dag-myawesometmlsolutionml-3f10")
    step7 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_7_kafka_visualization_dag-myawesometmlsolutionml-3f10")
    step8 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_8_deploy_solution_to_docker_dag-myawesometmlsolutionml-3f10")
    step9 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_9_privategpt_qdrant_dag-myawesometmlsolutionml-3f10")
    step10 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_10_documentation_dag-myawesometmlsolutionml-3f10")
    
    with DAG(
        dag_id="solution_preprocessing_ml_dag-myawesometmlsolutionml-3f10",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ml",
        bash_command="echo 'Start task'",
      )
    # STEP 1: Get the Parameters
      sensor_A = PythonOperator(
                task_id="step_1_solution_task_getparams",
                python_callable=step1.getparams,
                provide_context=True,
      )
    
    # STEP 2: Create the Kafka topics
      sensor_B = PythonOperator(
          task_id="step_2_solution_task_createtopic",
          python_callable=step2.setupkafkatopics,
          provide_context=True,
      )
    # STEP 3: Produce data to topic        
      sensor_C = PythonOperator(
          task_id="step_3_solution_task_producetotopic",
          python_callable=step3.startproducing,
          provide_context=True,
      )
    # STEP 4: Preprocess the data        
      sensor_D = PythonOperator(
          task_id="step_4_solution_task_preprocess",
          python_callable=step4.dopreprocessing,
          provide_context=True,
      )
    # STEP 5: ML        
      sensor_E = PythonOperator(
          task_id="step_5_solution_task_ml",
          python_callable=step5.startml,
          provide_context=True,
      )
    # STEP 6: Predictions        
      sensor_F = PythonOperator(
          task_id="step_6_solution_task_prediction",
          python_callable=step6.startpredictions,
          provide_context=True,
      )    
        
    # STEP 7: Visualization the solution     
      sensor_G = PythonOperator(
          task_id="step_7_solution_task_visualization",
          python_callable=step7.startstreamingengine,
          provide_context=True,
      )
    # STEP 8: Containerize the solution        
      sensor_H = PythonOperator(
          task_id="step_8_solution_task_containerize",
          python_callable=step8.dockerit,
          provide_context=True,      
      )
      start_task2 = BashOperator(
        task_id="Starting_Docker",
        bash_command="echo 'Start task Completed'",
      )    
      start_task3 = BashOperator(
        task_id="Starting_Documentation",
        bash_command="echo 'Start task Completed'",
      )
      start_task4 = BashOperator(
        task_id="Completed_TML_Setup_Now_Spawn_Main_Processes",
        bash_command="echo 'Start task Completed'",
      )
    # STEP 10: Document the solution
      sensor_J = PythonOperator(
          task_id="step_10_solution_task_document",
          python_callable=step10.generatedoc,
          provide_context=True,      
      )
    
      start_task >> sensor_A >> sensor_B >> start_task4 >> [sensor_C, sensor_D, sensor_E, sensor_F, sensor_G] >> start_task2 >> sensor_H >> start_task3 >> sensor_J

Here is the TSS successful run:

.. figure:: ml3.png
   :scale: 50%     

Here is the automated readthedocs documentation

.. figure:: ml2.png
   :scale: 50%     


This is the real-time dashboard generated:

.. figure:: mldash.png
   :scale: 50%     

Here is the docker container that was automatically built and pushed to Docker hub:

.. figure:: ml4.png
   :scale: 50%     


Cybersecurity Solution with PrivateGPT, MQTT, HiveMQ
-------------------------------------

:ref:`Solution DAG Code: solution_preprocessing_ai_mqtt_dag-cybersecuritywithprivategpt-3f10`

This Cybersecurity Data Preprocessing with GenAI Solution DAG: **solution_preprocessing_ai_dag-cybersecuritysolutionwithprivategpt-3f10** reads local file data in /rawdata/cisco_network_data.txt and streams it to Kafka. **The streaming data are then processed, the processed output data sent to the privateGPT container and Qdrant vector DB for further analysis.** Processing is done by Viper and AI is performed by privateGPT, the output data are streamed to a browser that runs the dashboard: tml-cisco-network-privategpt-monitor.html, that is located in /Viperviz/viperviz/views.

The solution will automatically build and push the solution container to docker hub, automatically create documentation on READTHEDOCS.io and automatically commit your solution code to Github, all in about 2 minutes.

Note also the solution will start the privateGPT and Qdrant containers automatically for you.

Solution DAG Code: solution_preprocessing_ai_mqtt_dag-cybersecuritywithprivategpt-3f10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: PYTHON

    from __future__ import annotations
    
    import pendulum
    from airflow.decorators import task
    from airflow.models.dag import DAG
    from airflow.operators.bash import BashOperator
    from airflow.sensors.external_task import ExternalTaskSensor 
    import tsslogging
    import os
    from datetime import datetime
    import importlib
    from airflow.operators.python import (
        ExternalPythonOperator,
        PythonOperator
    )
    step1 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_1_getparams_dag-cybersecuritywithprivategpt-3f10")
    step2 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_2_kafka_createtopic_dag-cybersecuritywithprivategpt-3f10")
    step3 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_read_MQTT_step_3_kafka_producetotopic_dag-cybersecuritywithprivategpt-3f10")
    step4 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_4_kafka_preprocess_dag-cybersecuritywithprivategpt-3f10")
    step5 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_5_kafka_machine_learning_dag-cybersecuritywithprivategpt-3f10")
    step6 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_6_kafka_predictions_dag-cybersecuritywithprivategpt-3f10")
    step7 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_7_kafka_visualization_dag-cybersecuritywithprivategpt-3f10")
    step8 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_8_deploy_solution_to_docker_dag-cybersecuritywithprivategpt-3f10")
    step9 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_9_privategpt_qdrant_dag-cybersecuritywithprivategpt-3f10")
    step10 = importlib.import_module("tml-solutions.cybersecuritywithprivategpt-3f10.tml_system_step_10_documentation_dag-cybersecuritywithprivategpt-3f10")
    
    
    with DAG(
        dag_id="solution_preprocessing_ai_mqtt_dag-cybersecuritywithprivategpt-3f10",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ai_mqtt",
        bash_command="echo 'Start task'",
      )
    # STEP 1: Get the Parameters
      sensor_A = PythonOperator(
                task_id="step_1_solution_task_getparams",
                python_callable=step1.getparams,
                provide_context=True,
      )
    
    # STEP 2: Create the Kafka topics
      sensor_B = PythonOperator(
          task_id="step_2_solution_task_createtopic",
          python_callable=step2.setupkafkatopics,
          provide_context=True,
      )
    # STEP 3: Produce data to topic        
      sensor_C = PythonOperator(
          task_id="step_3_solution_task_producetotopic",
          python_callable=step3.startproducing,
          provide_context=True,
      )
    # STEP 4: Preprocess the data        
      sensor_D = PythonOperator(
          task_id="step_4_solution_task_preprocess",
          python_callable=step4.dopreprocessing,
          provide_context=True,
      )
    # STEP 7: Containerize the solution     
      sensor_E = PythonOperator(
          task_id="step_7_solution_task_visualization",
          python_callable=step7.startstreamingengine,
          provide_context=True,
      )
    # STEP 8: Containerize the solution        
      sensor_F = PythonOperator(
          task_id="step_8_solution_task_containerize",
          python_callable=step8.dockerit,
          provide_context=True,      
      )
    # STEP 9: PrivateGPT      
      sensor_I = PythonOperator(
          task_id="step_9_solution_task_ai",
          python_callable=step9.startprivategpt,
          provide_context=True,      
      )       
      start_task2 = BashOperator(
        task_id="Starting_Docker",
        bash_command="echo 'Start task Completed'",
      )    
      start_task3 = BashOperator(
        task_id="Starting_Documentation",
        bash_command="echo 'Start task Completed'",
      )
      start_task4 = BashOperator(
        task_id="Completed_TML_Setup_Now_Spawn_Main_Processes",
        bash_command="echo 'Start task Completed'",
      )
    # STEP 10: Document the solution
      sensor_G = PythonOperator(
          task_id="step_10_solution_task_document",
          python_callable=step10.generatedoc,
          provide_context=True,      
      )
    
      start_task >> sensor_A >> sensor_B  >> start_task4 >> [sensor_I, sensor_C, sensor_D, sensor_E] >> start_task2 >> sensor_F >> start_task3  >> sensor_G

DAG Successful Run
^^^^^^^^^^^^^^^^^

.. figure:: gptdash2.png
   :scale: 50%

The Dashboard with PrivateGPT
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: gptdash.png
   :scale: 50%

The HiveMQ Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: mqttcluster.png
   :scale: 50%


Solution Documentation
^^^^^^^^^^^^^^^^^

.. figure:: cyberdoc.png
   :scale: 50%

Solution Docker Container
^^^^^^^^^^^^^^^^^

.. figure:: dockercyber.png
   :scale: 50%
