TML Solution Building
======================

The fastest way to build TML solutions with your real-time data is to use the **TML Solution Studio Container** located here: [Dockerhub]

Apache Airflow DAGs
-------------------

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
