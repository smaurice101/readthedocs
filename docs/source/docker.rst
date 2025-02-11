TML Solution Studio (TSS) Container
======================================

TSS Containers:

.. list-table::
   * - Linux Users: `<https://hub.docker.com/r/maadsdocker/tml-solution-studio-with-airflow-amd64>`_
   * - Mac/Linux Users: `<https://hub.docker.com/r/maadsdocker/tml-solution-studio-with-airflow-arm64>`_

.. tip::
   Watch the TSS `YouTube Video <https://www.youtube.com/watch?v=z3h2nJXVgUs>`_

.. important::
   You MUST have the pre-requisites met before running this container: :ref:`TSS Pre-Requisites`

.. figure:: tmlarch.png
   :scale: 70%

This is the main container that you need to use to build TML solutions.  Below is the :ref:`TSS Docker Run Command` to run the container.

.. important::
   Use this TSS container and start building amazing, advanced and scalable real-time data streaming solutions - with real-time dashboards - auto deployment to 
   Docker - auto solution documentation - integrated with AI - integrated with Github - integrated with Apache Airflow - integrated with Apache Kafka - in just a 
   few hours.

TSS Pre-Requisites
-------------------

.. attention::

   **The following prerequisites MUST be met before you run the TML Solution Studio Container** using the :ref:`TSS Docker Run Command` :

   1. You MUST Install Docker - in Linux Ubuntu run (if using Windows use `WSL <https://learn.microsoft.com/en- us/windows/wsl/install>`_): 

      .. code-block::
      
         sudo apt update
         sudo apt upgrade
         sudo apt install docker.io
         sudo docker --version
         sudo docker run hello-world
         sudo docker ps

   2. You MUST have a `Github Account <https://github.com/>`_

   3. You MUST Clone Github Repo: https://github.com/smaurice101/raspberrypi.git

   4. You MUST Create Github **Personal Access Token**. Refer to :ref:`Set Up Personal Access Tokens in Github`

   5. You MUST have sign up for a `Docker Hub account: <https://hub.docker.com/>`_

   6. Create a `Readthedocs <https://app.readthedocs.org/>`_ account and get an API token: :ref:`Set Up Readthedocs`

   7. Create a `HiveMQ account <https://www.hivemq.com/>`_ - while this is OPTIONAL - if using MQTT and HiveMQ you will need this.

   8. Kafka Cloud API keys from `Confluent <https://www.confluent.io>`_ or `AWS MSK <https://aws.amazon.com/msk/>`_ - while this is OPTONAL - it will be for production, or large scale, deployments.

   FOLLOW THE :ref:`How To Use the TML Solution Container` SECTION.

TSS Contains a TML Dev Environment
----------------------------

.. important::
   Another powerful feature is the TSS TML Development environment which is contained directly inside the TSS container.  TSS comes with all the TML solution 
   components installed like: 1. Apache Kafka, 2. TML binaries, 3. MariaDB config db 4. your TML DAG scripts, 5. Viperviz for visualization

   Once you are satisfied with your solution - you can use the :ref:`STEP 8: Deploy TML Solution to Docker : tml-system-step-8-deploy-solution-to-docker-dag` to deploy your solution to Docker.

.. tip::
   TML developers can test each component or their entire TML solution inside the TSS before deploying the solution 
   in the container.  This is a very convenient way to make sure all the solution components are working before 
   shipping your TML product.

TSS Docker Run Command
--------------------

.. note::
   **If you are producing data using a local file, you need to add an extra -v volume map to the /rawdata folder in the container:** Refer to :ref:`Producing Data 
   Using a Local File`.

   For example add **-v /your_localmachine/foldername:/rawdata:z**, where **your_localmachine/foldername** is a path in your local machine, and it is where you 
   save your local file for processing.

   Your file must contains JSON messages on each line.  See `Sample File <https://github.com/smaurice101/raspberrypi/blob/main/tml- 
   airflow/data/IoTDatasample-small.txt>`_

.. code-block::

   docker run -d --net="host" \
   --env CHIP="AMD64" \
   --env MAINHOST=127.0.0.1 \ 
   --env TSS=1 \
   --env SOLUTIONNAME=TSS \
   --env AIRFLOWPORT=9000 \ 
   --env VIPERVIZPORT=9005 \
   --env EXTERNALPORT=-1 \
   -v /var/run/docker.sock:/var/run/docker.sock:z \ 
   -v /<your local dagsbackup folder>:/dagslocalbackup:z \
   -v /your_localmachine/foldername:/rawdata:z \
   --env READTHEDOCS='<Token>' \
   --env GITREPOURL='<your git hub repo>' \ 
   --env  GITUSERNAME='<your github username>' \ 
   --env GITPASSWORD='<Personal Access Token>' \ 
   --env DOCKERUSERNAME='<your docker hub account>' \ 
   --env DOCKERPASSWORD='<password>' \
   --env MQTTUSERNAME='<enter MQTT username>' \
   --env MQTTPASSWORD='<enter MQTT password>' \
   --env KAFKACLOUDUSERNAME='' \
   --env KAFKACLOUDPASSWORD='<Enter your API secret>' \
   --env UPDATE=1 \
   maadsdocker/tml-solution-studio-with-airflow-amd64

.. list-table::

   * - **Parameter**
     - **Description**
   * - CHIP
     - Specifies the container OS.  NOTE: If you are using MAC then 
 
       change to CHIP=ARM64
   * - MAINHOST=127.0.0.1
     - This is the IP address for the TML solution 

       container.  It will normally listen 

       on 127.0.0.1
   * - TSS
     - Do not modify.
   * - SOLUTIONNAME
     - Do not modify.
   * - AIRFLOWPORT=9000 
     - This is the AIRFLOWPORT.  This port 

       will be needed to access the TML 

       solution studio from your browser.  

       For sample, enter: http://localhost:9000/
 
       You will be asked for a 

       username and password: enter **tml** for both.
   * - VIPERVIZPORT
     - Choose a Viperviz port for visualization.  

       For example, 9005
   * - -v /<your local dagsbackup folder>:/dagslocalbackup:z
     - If you like, you can also backsup the dags to your 

       local folder with this volume mapping
   * - -v /your_localmachine/foldername:/rawdata:z
     - If you like, you can also map our local folder
  
       to the rawdata folder.  This is neede if you 

       will be processing local files with TML. 
   * - -v /var/run/docker.sock:/var/run/docker.sock:z 
     - This maps the docker volume to the container - 

       so TML studio can automatically build 

       your solution container.
   * - READTHEDOCS=<Token>
     - Create, copy and paste the Readthedocs token here.  

       Refer to :ref:`Set Up Readthedocs`
   * - GITREPOURL=<your github repo> 
     - This is your Git repo you cloned from: 

       https://github.com/smaurice101/raspberrypi.git. 
   * - GITUSERNAME=<your github username> 
     - This is the username to your repo.
   * - GITPASSWORD=<Personal Access Token> 
     - This is the **Personal Access Token** for 

       your repo.   

       Look at the image below to find out how 

       to generate this token.
   * - DOCKERUSERNAME=<your docker hub account> 
     - This is your Docker Hub username.
   * - DOCKERPASSWORD=<password> 
     - This is your password to Dockerhub account.
   * - MQTTUSERNAME=<your MQTT username> 
     - This is your MQTT username.
   * - MQTTPASSWORD=<MQTT password> 
     - This is your password to MQTT cluster.
   * - UPDATE=1 
     - This enables system updates if set to 1: meaning

       any updates to the system DAGS made by the TSS

       system maintainer will update all the user DAGS

       in all of the projects.  This is a remote GitHub

       pull that keeps users ALWAYS with the updated Dags.

       You can Turn OFF system updates by setting to 0. 
   * - **maadsdocker/tml-solution-studio-with-airflow-amd64**
     - This is the official TML Solution Studio container

       for Window/Linux users with AMD64 chip architecture.

       If using MAC/Linux change: **amd64** to **arm64**       

       **For example:**

        maadsdocker/tml-solution-studio-with-airflow-**arm64**

        .. code-block::

            docker run -d --net="host" \
            --env CHIP="ARM64" \
            --env MAINHOST=127.0.0.1 \
            --env TSS=1 \
            --env SOLUTIONNAME=TSS \
            --env AIRFLOWPORT=9000 \
            --env VIPERVIZPORT=9005 \
            --env EXTERNALPORT=-1 \
            -v /var/run/docker.sock:/var/run/docker.sock:z \
            -v /<your local dagsbackup folder>:/dagslocalbackup:z \
            -v /your_localmachine/foldername:/rawdata:z \
            --env READTHEDOCS='<Token>' \
            --env GITREPOURL='<your git hub repo>' \
            --env  GITUSERNAME='<your github username>' \
            --env GITPASSWORD='<Personal Access Token>' \
            --env DOCKERUSERNAME='<your docker hub account>' \
            --env DOCKERPASSWORD='<password>' \
            --env MQTTUSERNAME='<enter MQTT username>' \
            --env MQTTPASSWORD='<enter MQTT password>' \
            --env KAFKACLOUDUSERNAME='' \
            --env KAFKACLOUDPASSWORD='<Enter your API secret>' \
            --env UPDATE=1 \
            maadsdocker/tml-solution-studio-with-airflow-arm64

.. important::
   It is highly recommended you map your local folder 

   to the **dagslocalbackup** folder: 

   **-v /<your local dagsbackup folder>:/dagslocalbackup:z**

   This ensures that if anything happens to Github you 
 
   always have a local copy of all of your solution dags.

How To Use the TML Solution Container
-------------------------

.. tip::
   Once you have the TML Solution container running you can go to your favourite browser and type the URL: http://localhost:9000

.. note::
   
   The PORT number in the URL is what you specified in the Docker Run AIRFLOWPORT parameter i.e. **--env AIRFLOWPORT=9000**

After you enter the URL you will the following website:

.. figure:: ts1.png

.. tip::

   The username and password are both **tml**

After you have signed in successfully you will see the following screen with example DAGs:

.. figure:: ts2.png

If you scroll down you will see the **TML DAGs** - as defined here: :ref:`DAG Table`.  These are the DAGs you will use to build your TML Solutions:

.. figure:: ts3.png

TSS Code Editor
-----------------

.. important::
   Next go into the DAG Code Editor: Select Drop-down menu **Admin --> DAGs Code Editor**.  Most of your TML Solution building will be done here.  Note the DAGs 
   solution process flows defined here: :ref:`Apache Airflow DAGs`

.. figure:: ts4.png

Common Docker and TMUX Commands
--------------------

This is a list of common commands for Docker and Tmux.

.. list-table::

   * - **Description**
     - **Command**
   * - List Docker containers
     - Type: **docker image ls**
   * - Delete Docker containers
     - From: **docker image ls** and copy the **REPOSITORY** to delete

       Type: **docker rmi <REPOSITORY name> \-\-force**
   * - List Running Docker containers
     - Type: **docker ps**
   * - Stop Running Docker containers
     - From **docker ps** copy the Container ID
   
       Type: **docker stop <paste container ID>**
   * - Go inside the Docker containers
     - From **docker ps** copy the Container ID
   
       Type: **docker exec -it <paste container ID> bash**
   * - List the TMUX windows once inside the container
     - Type: **tmux ls**
   * - Go inside TMUX windows
     - From **tmux ls** copy the window name you want to enter

       Type: **tmux a -t <window name>**
   * - To scroll inside a TMUX window
     - Press: **CTRL+b, [**
   * - To UN-scroll inside a TMUX window
     - Press: **CTRL + [**
   * - To EXIT a TMUX window
     - Press: **CTRL + b, d**
   * - To EXIT docker container
     - Type: **exit**

TSS Logging
-----------------

The entire TSS solution build process is logged and committed to Github.  This makes it very convenient to check for any errors in the TSS build process, and because errors are commited to the remote branch, the errors become visible to others to help in quickly rectifying any issues.

.. figure:: tsslogs.png

.. tip::
    The logs are committed to your Github folder: **/tml-airflow/logs/logs.txt**

.. figure:: tsslogs2.png
