TML Solution Studio (TSS) Container
======================================

Coming Soon.

.. figure:: tmlarch.png
   :scale: 70%

This is the main container that you need to use to build TML solutions.  Below is the :ref:`TSS Docker Run Command` to run the container.

.. important::
   Use this TSS container and start building amazing, advanced and scalable real-time data streaming solutions - with real-time dashboards - auto deployment to 
   Docker - auto solution documentation - integrated with AI - integrated with Github - integrated with Apache Airflow - integrated with Apache Kafka - in just a 
   few hours.

.. attention::

   **The following prerequisites MUST be met before you run the TML Solution Studio Container:**

   1. You MUST Install Docker - in Ubuntu run: sudo apt install docker.io

   2. You MUST have a `Github Account <https://github.com/>`_

   3. You MUST Clone Github Repo: https://github.com/smaurice101/raspberrypi.git

   4. You MUST Create Github **Personal Access Token** (Refer to :ref:`Generating Personal Access Tokens in Github`)

   5. You MUST have sign up for a `Docker Hub account: <https://hub.docker.com/>`_

   6. Create a `Readthedocs <https://app.readthedocs.org/>`_ account and get an API token: :ref:`Set Up Readthedocs`

   FOLLOW THE :ref:`How To Use the TML Solution Container` SECTION.

TSS Contains a TML Dev Environment
----------------------------

.. important::
   Another powerful feature is the TSS TML Development environment which is contained directly inside the TSS container.  TSS comes with all the TML solution 
   components installed like: 1. Apache Kafka, 2. TML binaries, 3. MariaDB config db 4. your TML DAG scripts, 5. Viperviz for visualization

   Once you are satisfied with your solution - you can use the :ref:`STEP 8: Deploy TML Solution to Docker : tml-system-step-8-deploy-solution-to-docker-dag.py` 
   to deploy your solution to Docker.

.. tip::
   TML developers can test each component or their entire TML solution inside the TSS before deploying the solution in the container.  This is a very convenient 
   way to make sure all the solution components are working before shipping your TML product.

TSS Logging
-----------------

The entire TSS solution build process is logged and committed to Github.  This makes it very convenient to check for any errors in the TSS build process, and because errors are commited to the remote branch, the errors become visible to others to help in quickly rectifying any issues.

.. figure:: tsslogs.png

.. tip::
    The logs are committed to your Github folder: **/tml-airflow/logs/logs.txt**

.. figure:: tsslogs2.png

TSS Docker Run Command
--------------------

.. important::
   If you are producing data using a local file, you need to add an extra -v volume map to the /rawdata folder in the container: Refer to :ref:`Producing Data 
   Using a Local File`.

   For example add **-v /your_localmachine/foldername:/rawdata:z**, where **your_localmachine/foldername** is a path in your local machine, and it is where you 
   save your local file for processing.

   Your file must contains JSON messages on each line.  See `Sample File <https://github.com/smaurice101/raspberrypi/blob/main/tml- 
   airflow/data/IoTDatasample.txt>`_

.. code-block::

   docker run -d --net="host" 
   --env CHIP="AMD64"
   --env MAINHOST=127.0.0.1 
   --env TSS=1
   --env SOLUTIONNAME=TSS
   --env AIRFLOWPORT=9000 
   --env VIPERVIZPORT=9005
   -v /var/run/docker.sock:/var/run/docker.sock:z 
   -v /<your local dagsbackup folder>:/dagslocalbackup:z
   --env READTHEDOCS=<Token>
   --env GITREPOURL=<your git hub repo> 
   --env  GITUSERNAME=<your github username> 
   --env GITPASSWORD=<Personal Access Token> 
   --env DOCKERUSERNAME=<your docker hub account> 
   --env DOCKERPASSWORD=<password> 
   maadsdocker/tml-solution-studio-with-airflow

.. list-table::

   * - **Parameter**
     - **Description**
   * - CHIP
     - Specifies the container OS.  NOTE: If you are using MAC then 
 
       change to CHIP=ARM64 and run:
 
       **maadsdocker/tml-solution-studio-with-airflow-arm64** containter
   * - --env MAINHOST=127.0.0.1
     - This is the IP address for the TML solution 

       container.  It will normally listen 

       on 127.0.0.1
   * - TSS
     - Do not modify.
   * - SOLUTIONNAME
     - Do not modify.
   * - --env AIRFLOWPORT=9000 
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
     - If you like, you can also backsup the dags to your local folder with this volume mapping
   * - -v /var/run/docker.sock:/var/run/docker.sock:z 
     - This maps the docker volume to the container - 

       so TML studio can automatically build 

       your solution container.
   * - --env READTHEDOCS=<Token>
     - Create, copy and paste the Readthedocs token here.  Refer to :ref:`Set Up Readthedocs`
   * - --env GITREPOURL=<your github repo> 
     - This is your Git repo you cloned from: 

       https://github.com/smaurice101/raspberrypi.git. 
   * - --env GITUSERNAME=<your github username> 
     - This is the username to your repo.
   * - --env GITPASSWORD=<Personal Access Token> 
     - This is the **Personal Access Token** for 

       your repo.   

       Look at the image below to find out how 

       to generate this token.
   * - --env DOCKERUSERNAME=<your docker hub account> 
     - This is your Docker Hub username.
   * - --env DOCKERPASSWORD=<password> 
     - This is your password to Dockerhub account.
   * - **maadsdocker/tml-solution-studio-with-airflow**
     - This is the official TML Solution 
 
       Studio container.

.. important::
   It is highly recommended you map your local folder to the **dagslocalbackup** folder: 

    **-v /<your local dagsbackup folder>:/dagslocalbackup:z**

    This ensures that if anything happens to Github you always have a local copy of all

    of your solution dags.

Generating Personal Access Tokens in Github
-------------------------

.. figure:: tmlgit2.png

Generating Personal Access Tokens in Github: Explanation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tip:: 
   Follow these steps:

      1. Log in to your Github account
      
      2. In the Top-Right corner of your Github account click **Settings**
      
      3. In the next screen, scroll all the way down and click **<> Developer settings**
      
      4. Click **Personal access tokens**
      
      5. Choose **Tokens (classic)**
      
      6. Click **Generate new token** -  Your token should start with **ghp_**
      
      7. Copy and paste token in **GITPASSWORD** docker run command: :ref:`TSS Docker Run Command`

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

.. attention::

   Next go into the DAG Code Editor: Select Drop-down menu **Admin --> DAGs Code Editor**.  Most of your TML Solution building will be done here.  Note the DAGs 
   solution process flows defined here: :ref:`Apache Airflow DAGs`

.. figure:: ts4.png

Lets Start Building a TML Solution
--------------------------------

After you are in the **DAG code editor** you must go into the following folder:

STEP 0. Go into **tml-airflow** folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: sol11.png

STEP 1. **tml-airflow -> dags -> tml-solutions** - you will see the following as shown in figure below:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: sol1.png

STEP 2. **Click the file: CREATETMLPROJECT.txt** - you will see the following as shown in figure below:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: sol2.png

STEP 3. **Type the name of your project** 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::
   You should use lowecase letters.  DO NOT ENTER ANY SPACES - Enter any name like **myawesometmlproject** then **PRESS SAVE**

   .. figure:: sol3.png

.. note:: 
   All projects will be "appended" with parts of your READTHEDOCS token.  This is to ensure project uniqness on READTHEDOCS.

STEP 4. You just created a TML Project and committed to Github. Congratulations!  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To confirm everything went ok go to the Github account:

   i.e. **/raspberrypi/tml-airflow/dags/tml-solutions/** you should see a folder for **myawesometmlproject**

   .. figure:: sol4.png

Deleting a Project
""""""""""""""""""""
.. tip::
   If you want to DELETE this project simply type a - (minus) in front of it (as shown below):

   **-myawesometmlproject**

   The TSS will delete the entire project and commit the changes to Github.

.. warning::
   All information/code related to this project will be deleted and may not 

   be recoverable.

.. figure:: deleteproject.png 
   :scale: 70%

STEP 5. Click the folder: **myawesometmlproject-3f10** - you will see the figure below - VOILA!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: sol5.png

STEP 6. Confirm Your New Project Was Created in TSS and Committed to Github
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To confirm the new DAGs for **myawesometmlproject** were created properly, in TSS click DAGs (top menu item)

Then enter a filter: myawesometmlproject Click Enter.  

You should see all your DAGs (note if they don't show up just wait 30 seconds or so) - you should see figure below:

   .. figure:: sol6.png

.. important::
   What did you just do?

   You copied **TML TEMPLATE** DAGs to your own solution folder - for your own TML solution build.  

   If you want to create another TML solution - just repeat STEPS 1-3 with a new project name.

.. tip::
   New project could take 30 seconds or more to show up on the main Airflow screen.  

   Please be patient.  If there are no errors - it will show up.

Copying A Previous Project
""""""""""""""""""""""""

.. tip::
   If you want to copy from a previous TML project and **rename** to a new project then:

   a. In STEP 3 type **myawesometmlproject>myawesometmlproject2**, the character ">" means copy myawesometmlproject to myawesometmlproject2 (as shown in figure below)
   b. Hit Save
   c. Voila! You just copied an older projec to a new one and saved the time in entering paramters in the DAGs.

.. figure:: sol7.png

To confirm the new project was properly copied repeat STEPS 4 - 6.  You should see your **myawesometmlproject2** committed to Github:

.. figure:: sol8.png

Here are your new DAGs:

.. figure:: sol9.png

.. tip::
   Check the logs for status updates: Go to **/raspberrypi/tml-airflow/logs/logs.txt**

.. figure:: sol10.png

.. tip::
   For details on the editor go to `Codemirror <https://codemirror.net/5/doc/manual.html#commands>`_
