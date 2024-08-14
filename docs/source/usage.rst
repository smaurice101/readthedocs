TML Solution Components
=====

Below describes the entire TML technologgy solution stack.

TML Components: Three Binaries
------------

**TML is comprised of 3 binaries written in Go:** https://github.com/smaurice101/transactionalmachinelearning

1. *Viper* - source - sink binary for Apache Kafka
2. *HPDE* - AutoML binary for real-time data
3. *Viperviz* - Visualization binary for real-time dashboards

.. list-table::

   * - Binary
     - Description
   * - Viper

TML Component: One Core Python Library
--------------------------

**TML Python Library:** https://pypi.org/project/maadstml/

4. *MAADSTML* Python library : API to build TML solutions that connect to the Viper binary

TML Component: Apache Kafka
--------------------------

TML integrates with Apache Kafka - on-premise or in the cloud.

.. important::

   TML binaries are integrated with Apache Kafka.

TML Component: Docker Containers
--------------------------

All TML solutions are containerized with docker for production deployments.

TML Component: Kubernetes
--------------------------

All TML solution containers scale with Kubernetes.  This allows companies to build fast, scalable, real-time solutions.

How The TML Components Are Integrated 
--------------------------

TML solutions are developed using the MAADSTML Python library that connects to the TML Binaries for streaming real-time data to Apache Kafka, processing data in Kafka, and performing machine learning.  Once the TML solutions are built, they are containerized with Docker and scaled with Kubernetes.

.. important::

   TML performs **in-memory processing** of real-time data and **does NOT require an external database** - ONLY KAFKA is needed.  This results in dramatic cost- 
   savings for storage, compute and network data transfers.

   TML **does NOT perform SQL queries**, it performs :ref:`JSON PROCESSING`.  This results in much faster, and much cheaper processing of real-time data.




