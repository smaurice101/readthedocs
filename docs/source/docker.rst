TML Solution Studio (TSS) Container
======================================

Comming Soon.

This is the main container that you need to use to build TML solutions.  Below is the **docker run** command to run the container.

.. note::
   Use this TSS container and start building amazing, advanced and scalable real-time data streaming solutions - with real-time dashboards - auto deployment to 
   Docker - auto solution documentation - integrated with AI - integrated with Github - integrated with Apache Airflow - integrated with Apache Kafka - in just a few hours.

.. important::

   **The following prerequisites MUST be met before you run the TML Solution Studio Container:**

   1. You MUST Install Docker - in Ubuntu run: sudo apt install docker.io

   2. You MUST have a Github Account

   3. You MUST Clone Github Repo: https://github.com/smaurice101/raspberrypi.git

   4. You MUST Create Github **Personal Access Token** (Refer to Docker section)

   5. You MUST have a Docker Hub account

   FOLLOW THE :ref:`How To Use the TML Solution Container` SECTION.

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
     - This is the IP address for the TML solution container.  It will normally listen on 127.0.0.1
   * - --env AIRFLOWPORT=9000 
     - This is the AIRFLOWPORT.  This port will be needed to access the TML solution studion from your browser.  For sample, enter: http://localhost:9000/
       You will be asked for a username and password: enter **tml** for both.
   * - -v /var/run/docker.sock:/var/run/docker.sock:z 
     - This maps the docker volume to the container - so TML studio can automatically build your solution container.
   * - --env GITREPOURL=https://github.com/smaurice101/raspberrypi.git 
     - This is your Git repo. The above is an example.
   * - --env GITUSERNAME=smaurice101 
     - This is the username to your repo.
   * - --env GITPASSWORD=<Personal Access Token> 
     - This is the **Personal Access Token** for your repo.   Look at the image below to find out how to generate this token.
   * - --env DOCKERUSERNAME=maadsdocker 
     - This is your Docker Hub username.
   * - --env DOCKERPASSWORD=<password> 
     - This is your password to Dockerhub account.
   * - **maadsdocker/tml-solution-studio-with-airflow**
     - This is the official TML Solution Studio container.

Generating Personal Access Tokens in Github
-------------------------

.. figure:: tmlgit2.png
