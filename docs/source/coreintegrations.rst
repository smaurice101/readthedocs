TML Core Technology Integration
================================

.. important::

   - All TML solutions can be run on-premise or in the cloud using Apache Kafka.

   - All TML solutions process data in-memory - no external databases are needed - ONLY Apache Kafka.

   - All TML solutions use TLS encryption to encrypt real-time data.

   - All TML solutions compress real-time data using advanced compression algorithms like: snappy, gzip, lz4

   - All TML solutions use JSON processing - not SQL - for faster, more cost effective, processing of real-time data.  Refer to :ref:`JSON PROCESSING`

   - All TML solutions perform entity based processing and machine learning. Refer to :ref:`TML Performs Entity Level Machine Learning and Processing`

   - All TML solutions are containerized with Docker and scale with Kubernetes.

   - All TML solutions are developed in Python using the MAADSTML Python Library and DAGs. Refer to :ref:`MAADSTML Python Library API` and :ref:`TML Solution 
     Building`

   - All TML solutions use REST API.

   - All TML solutions can have a real-time visualization dashboards using websockets enabled by TML binary: Viperviz. Refer to :ref:`TML Real-Time Dashboards`

Below are all the technologies TML integrates with for fast, scalable, cost-effective, real-time solutions.

1. Apache Kafka
--------------

Apache Kafka is the world's largest open source platform for storage of real-time data streams.   TML integrates with `Apache Kafka on-premise <https://kafka.apache.org/>`_ or in the cloud using `AWS MSK <https://aws.amazon.com/msk/features/>`_ or `Confluent Cloud <https://www.confluent.io/>`_.

2. Apache Airflow
----------------

`Apache Airflow <https://airflow.apache.org/>`_ is an open-source workflow management platform for data engineering pipelines. It started at Airbnb in October 2014[2] as a solution to manage the company's increasingly complex workflows.

TML Solution Studio Container uses Airflow to build highly advanced, scalable, real-time TML solutions. Refer to :ref:`TML Solution Studio Container` for more details.

3. TML Binaries
-----------

TML uses THREE (3) core binaries: Viper, HPDE, Viperviz, for TML solutions.  More details here :ref:`1. TML Components: Three Binaries`

4. TML Python Library
-----------

TML solutions are built with the `MAADSTML Python Libary <https://pypi.org/project/maadstml/>`_.  Refer to :ref:`MAADSTML Python Library API` for more details.

5. TML GenAI With PrivateGPT and Qdrant Vector DB
-----------

TML solutions integrate with GenAI using a special `PrivateGPT docker container <https://hub.docker.com/r/maadsdocker/tml-privategpt-with-gpu-nvidia-amd64>`_.   This allows for very secure, private, and highly cost-effective LLM capabilities.  Refer to :ref:`TML and Generative AI` for more details.

The PrivateGPT container is integrated with `Qdrant <https://qdrant.tech/>`_ vector DB for localized AI processing with LLMs.

6. TMUX (Terminal Multiplexing)
----------------------------

All TML solution use `TMUX <https://github.com/tmux/tmux/wiki>`_ to optimize TML solutions in Linux to enhance support and maintenance of solutions.

7. MariaDB (MySQL)
----------------------------

All TML solution use `MariaDB <https://mariadb.com/>`_ as a configuration database for TML solutions.

8. Docker
-----------

TML solutions are containerized using `Docker <https://hub.docker.com/>`_.

9. Kubernetes
--------------

TML solution containers are scaled with `Kubernetes <https://kubernetes.io/>`_.

10. Github
--------

TML solutions are tightly integrated with `Github <https://github.com/>`_ and can commit code locally and to remote branches directly from the TML Solution Studio container.  Refer to :ref:`TML Solution Studio’s Tight Integration with GitHub`.

11. Python and DAGs (Directed Acylic Graphs)
-----------

All TML solutions are written using Pre-written `Python <https://www.python.org/>`_ DAGs: see the :ref:`DAG Table`.  Refer to :ref:`TML Solutions Can Be Built In 10 Steps Using Pre-Written DAGs (Directed Acyclic Graphs)`.  

