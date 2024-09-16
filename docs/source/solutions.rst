TML Solution Templates
==========================

TML solution templates are designed to dramatically accelerate TML solution solution in a few minutes, when it would normally take companies weeks or months to build end-end real-time solutions at scale, with integrations with advanced machine learning, GenAI, automated docker container deployments and automated documentation, with automated Github code commits.

Solution templated require NO CODE or Configurations.  Just RUN THEM in TSS! An example will be shown to make this easy to understand here :ref:`Running A Solution Container`

.. important::
   **ALL TML SOLUTIONS MUST BE DEVELOPED USING "COPIES" OF THESE SOLUTION TEMPLATES IN YOUR TML PROJECT FOLDER.** Copies of these solution templates are automatically made for you when you create a TML project: Refer to here for details :ref:`Lets Start Building a TML Solution`

   These solution templates execute all of the TML DAGs here :ref:`DAG Solution Process Explanation`  

   All you do is configure the parameters in the TML DAGs and RUN the Solution Templates.  THAT IS IT!

The Solution Template Naming Conventions  
-------------------------------------
The namees of the solution template tell you what the solution is about.  Each solution template performs functions:

1. processing - using ingested data from: local file, MQTT, gRPC, REST

2. ML/predictions - using ingested data from: local file, MQTT, gRPC, REST

3. AI - using ingested data from: local file, MQTT, gRPC, REST

For example:
"""""""""""""""

**1. solution_preprocessing_dag:** Is doing ONLY preprocessing using LOCAL FILE because it does not use MQTT, REST, gRPC and defaults to local file

**2. solution_preprocessing_dag_mqtt:** Is doing preprocessing using MQTT

**3. solution_preprocessing_ai_grpc_dag:** Is doing preprocessing AND AI using gRPC

**4. solution_preprocessing_ml_ai_mqtt:** Is dong preprocessing, ML AND AI using MQTT

**5. solution_preprocessing_ml_mqtt_dag:** Is doing preprocessing, ML using MQTT

**6. solution_preprocessing_ml_dag:** Is doing preprocessing and ML using LOCAL File

So on...

Here are the solution templates provided
--------------------------------

.. list-table::

   * - **Solution Templates**
   * - :ref:`1. Solution Template: solution_template_processing_ai_dag_grpc.py`
       
       This template will analyse ANY real-time data using the gRPC protocol.
      
       See :ref:`gRPC Reference Architecture` with integration with GenAI 
      
       for real-time AI analysis of TML output data. 
   * - :ref:`2. Solution Template: solution_template_processing_ai_dag_mqtt.py`

       This template will analyse ANY real-time data using the MQTT protocol.

       See :ref:`MQTT Reference Architecture` with integration with GenAI 

       for real-time AI analysis of TML output data.
   * - :ref:`3. Solution Template: solution_template_processing_ai_dag_restapi.py`

       This template will analyse ANY real-time data using the REST protocol.

       See :ref:`REST API Reference Architecture` with integration with GenAI 

       for real-time AI analysis of TML output data.
   * - :ref:`4. Solution Template: solution_template_processing_ai_dag.py`

       This solution template will read a local file from the file system

       and stream it to the TML solution for processing, with integration

       with GenAI for further processing.
   * - :ref:`5. Solution Template: solution_template_processing_dag_grpc.py`

       This solution template will process data ingested using gRPC. 
   * - :ref:`6. Solution Template: solution_template_processing_dag_mqtt.py`

       This solution template will process data using MQTT protocol.
   * - :ref:`7. Solution Template: solution_template_processing_dag_restapi.py`

       This solution template will process data using the REST API.
   * - :ref:`8. Solution Template: solution_template_processing_dag.py`

       This solution template will process data using local file.
   * - :ref:`9. Solution Template: solution_template_processing_ml_ai_dag_grpc.py`

       This solution template will process data, perform machine learning

       and perform AI on the output data, while ingesting data from gRPC protocol.
   * - :ref:`10. Solution Template: solution_template_processing_ml_ai_dag_mqtt.py`

       This solution template will process data, perform machine learning

       and perform AI on the output data, while ingesting data from MQTT protocol.
   * - :ref:`11. Solution Template: solution_template_processing_ml_ai_dag_restapi.py`

       This solution template will process data, perform machine learning

       and perform AI on the output data, while ingesting data from REST API protocol.
   * - :ref:`12. Solution Template: solution_template_processing_ml_ai_dag.py`

       This solution template will process data, perform machine learning

       and perform AI on the output data, while ingesting data from local file.
   * - :ref:`13. Solution Template: solution_template_processing_ml_dag_grpc.py`

       This solution template will process data, perform machine learning

       and predictions while ingesting data from gRPC protocol.
   * - :ref:`14. Solution Template: solution_template_processing_ml_dag_mqtt.py`

       This solution template will process data, perform machine learning

       and predictions while ingesting data from MQTT protocol.
   * - :ref:`15. Solution Template: solution_template_processing_ml_dag_restapi.py`

       This solution template will process data, perform machine learning

       and predictions while ingesting data from REST API protocol.
   * - :ref:`16. Solution Template: solution_template_processing_ml_dag.py`

       This solution template will process data, perform machine learning

       and predictions while ingesting data from local file.

1. Solution Template: solution_template_processing_ai_dag_grpc.py
-----------------------------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_gRPC_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ai_grpc_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ai_grpc",
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
          op_args=['ai'],
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


2. Solution Template: solution_template_processing_ai_dag_mqtt.py
-------------------------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_MQTT_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ai_mqtt_dag",
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

3. Solution Template: solution_template_processing_ai_dag_restapi.py
---------------------------------

.. code-block::

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_RESTAPI_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ai_restapi_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ai_restapi",
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

4. Solution Template: solution_template_processing_ai_dag.py
---------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_LOCALFILE_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ai_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ai",
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
    
      start_task >> sensor_A >> sensor_B >> start_task4 >> [sensor_I, sensor_C, sensor_D, sensor_E] >> start_task2 >> sensor_F >> start_task3  >> sensor_G

5. Solution Template: solution_template_processing_dag_grpc.py
-----------------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_gRPC_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    with DAG(
        dag_id="solution_preprocessing_dag_grpc",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_grpc",
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

6. Solution Template: solution_template_processing_dag_mqtt.py
-------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_MQTT_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    with DAG(
        dag_id="solution_preprocessing_dag_mqtt",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_mqtt",
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

7. Solution Template: solution_template_processing_dag_restapi.py
------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_RESTAPI_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    with DAG(
        dag_id="solution_preprocessing_dag_restapi",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_restapi",
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

8. Solution Template: solution_template_processing_dag.py
----------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_LOCALFILE_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_dag",
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

9. Solution Template: solution_template_processing_ml_ai_dag_grpc.py
---------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_gRPC_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ml_ai_grpc_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ml_ai",
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
      sensor_J = PythonOperator(
          task_id="step_10_solution_task_document",
          python_callable=step10.generatedoc,
          provide_context=True,      
      )
    
      start_task >> sensor_A >> sensor_B >> start_task4 >> [sensor_I, sensor_C, sensor_D, sensor_E, sensor_F, sensor_G] >> start_task2 >> sensor_H >> start_task3 >> sensor_J

10. Solution Template: solution_template_processing_ml_ai_dag_mqtt.py
---------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_MQTT_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ml_ai_mqtt_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ml_ai",
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
      sensor_J = PythonOperator(
          task_id="step_10_solution_task_document",
          python_callable=step10.generatedoc,
          provide_context=True,      
      )
    
      start_task >> sensor_A >> sensor_B >> start_task4 >> [sensor_I, sensor_C, sensor_D, sensor_E, sensor_F, sensor_G] >> start_task2 >> sensor_H >> start_task3 >> sensor_J

11. Solution Template: solution_template_processing_ml_ai_dag_restapi.py
----------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_RESTAPI_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ml_ai_restapi_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ml_ai",
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
      sensor_J = PythonOperator(
          task_id="step_10_solution_task_document",
          python_callable=step10.generatedoc,
          provide_context=True,      
      )
    
      start_task >> sensor_A >> sensor_B >> start_task4 >> [sensor_I, sensor_C, sensor_D, sensor_E, sensor_F, sensor_G] >> start_task2 >> sensor_H >> start_task3 >> sensor_J

12. Solution Template: solution_template_processing_ml_ai_dag.py
-----------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_LOCALFILE_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    with DAG(
        dag_id="solution_preprocessing_ml_ai_dag",
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
      sensor_J = PythonOperator(
          task_id="step_10_solution_task_document",
          python_callable=step10.generatedoc,
          provide_context=True,      
      )
    
      start_task >> sensor_A >> sensor_B >> start_task4 >> [sensor_I, sensor_C, sensor_D, sensor_E, sensor_F, sensor_G] >> start_task2 >> sensor_H >> start_task3 >> sensor_J

13. Solution Template: solution_template_processing_ml_dag_grpc.py
------------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_gRPC_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ml_grpc_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ml_grpc",
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

14. Solution Template: solution_template_processing_ml_dag_mqtt.py
------------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_MQTT_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ml_mqtt_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ml_mqtt",
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

15. Solution Template: solution_template_processing_ml_dag_restapi.py
------------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_RESTAPI_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    
    with DAG(
        dag_id="solution_preprocessing_ml_restapi_dag",
        start_date=datetime(2023, 1, 1),
        schedule=None,
    ) as dag:
      start_task = BashOperator(
        task_id="start_tasks_tml_preprocessing_ml_restapi",
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

16. Solution Template: solution_template_processing_ml_dag.py
----------------------------------

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
    step1 = importlib.import_module("tml_system_step_1_getparams_dag")
    step2 = importlib.import_module("tml_system_step_2_kafka_createtopic_dag")
    step3 = importlib.import_module("tml_read_LOCALFILE_step_3_kafka_producetotopic_dag")
    step4 = importlib.import_module("tml_system_step_4_kafka_preprocess_dag")
    step5 = importlib.import_module("tml_system_step_5_kafka_machine_learning_dag")
    step6 = importlib.import_module("tml_system_step_6_kafka_predictions_dag")
    step7 = importlib.import_module("tml_system_step_7_kafka_visualization_dag")
    step8 = importlib.import_module("tml_system_step_8_deploy_solution_to_docker_dag")
    step9 = importlib.import_module("tml_system_step_9_privategpt_qdrant_dag")
    step10 = importlib.import_module("tml_system_step_10_documentation_dag")
    
    with DAG(
        dag_id="solution_preprocessing_ml_dag",
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

How To Read a Solution Template
------------------------

The key components of a solution template are:

1. import files

   - Consider the following import files:

     - step1 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_1_getparams_dag-myawesometmlsolutionml-3f10")

     - step2 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_2_kafka_createtopic_dag-myawesometmlsolutionml-3f10")

     - step3 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_read_LOCALFILE_step_3_kafka_producetotopic_dag-myawesometmlsolutionml-3f10")

     - step4 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_4_kafka_preprocess_dag-myawesometmlsolutionml-3f10")

     - step5 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_5_kafka_machine_learning_dag-myawesometmlsolutionml-3f10")
    
     - step6 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_6_kafka_predictions_dag-myawesometmlsolutionml-3f10")

     - step7 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_7_kafka_visualization_dag-myawesometmlsolutionml-3f10")

     - step8 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_8_deploy_solution_to_docker_dag-myawesometmlsolutionml-3f10")

     - step9 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_9_privategpt_qdrant_dag-myawesometmlsolutionml-3f10")

     - step10 = importlib.import_module("tml-solutions.myawesometmlsolutionml-3f10.tml_system_step_10_documentation_dag-myawesometmlsolutionml-3f10")


2. tasks

3 tasks groupings


Running A Solution Container
----------------------------------

Follow the instructions here :ref:`Lets Start Building a TML Solution`
