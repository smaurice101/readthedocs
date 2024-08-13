TML Solution Studio Docker Container
======================================

This is the main container that you need to use to build TML solutions.  Below is the **docker run** command to run the container.

.. code-block::

   docker run -d --net="host" 
   --env MAINHOST=127.0.0.1 
   --env AIRFLOWPORT=9000 
   -v /var/run/docker.sock:/var/run/docker.sock:z 
   --env GITREPOURL=https://github.com/smaurice101/raspberrypi.git 
   --env  GITUSERNAME=smaurice101 
   --env GITPASSWORD=<Personal Access Token> 
   --env DOCKERUSERNAME=maadsdocker 
   --env DOCKERPASSWORD=<password> 
   maadsdocker/tml-solution-studio-with-airflow

.. list-table::

   * - **Parameter**
     - **Description**
   * - --env MAINHOST=127.0.0.1
     - v
   
