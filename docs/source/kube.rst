Scaling TML Solutions with Kubernetes
=================================

All TML solutions can be scaled with Kubernetes to perform unlimited processing of real-time data wit machine learning and AI - as shown in the figure below.

.. figure:: kube.png
   :scale: 70%

Everytime you create a TML solution in the TSS - TSS will generate YAML files automatically.  These YAML files can be used immediately to scale your solution.

.. important::
   You can scale your TML solution to process unlimited data with integration with PrivateGPT and Qdrant vector DB for fast AI. 

   Note: If scaling your TML solution you should use KAFKA CLOUD for efficient processing of large amounts of real-time data.  Because TML uses sliding time windows, instances of TML pods, 
   replicated by Kubernetes, will not duplicate the processing of sliding time windows.  **For example, if you have 100 TML pods running, each TML pod will check if a sliding time has 
   already 
   been processed by another TML pod, if so, it will not re-process that window.  This dramatically saves on processing time and leverages the fully capabilites of kubernetes to manage the 
   sending of data to pods that are not busy.** 

Five YAML files are auto-generated for every TML solution and are found in your READTHEDOCS solution documentation:

.. list-table::

   * - **YAML File**
     - **Description**
   * - TML Solution Yaml File
     - This is your main TML solution YAML 

       that Kubernetes will need to replicate 

       your TML solution.  This solution Yaml

       will be auto-generated and found in your 

       readthedocs solution documentation.
   * - MySQL DB Deployment Yaml File
     - MySQL DB is used for TML configurations.  

       This DB Yaml service will allow all 

       TML solutions to process
   * - MySQL DB Storage Yaml File
     - This Yaml file claims storage for the MySQL db.
   * - PrivateGPT Yaml (Optional)
     - A privateGPT yaml file is provided if your

       TML solution is perform AI using Step 9 Dag.

       This is a powerful way to incorporate fast AI 

       in your TML solution.
   * - Qdrant Vector DB Yaml (Optional)
     - If you are concurrently performing AI 

       in the provateGPT container by setting 

       WEB_CONCURRENCY > 1, then you MUST 

       have Qdrant vector DB running.
  
.. tip::
   These YAMLs can be applied to your Kubernetes cluster as follows:

   **kubectl apply -f mysql-storage.yml -f mysql-db-deployment.yml -f <TML solution name>.yml**, where you replace <TML solution name> with your actual TML solution name.

   If using AI:

   **kubectl apply -f mysql-storage.yml -f mysql-db-deployment.yml -f privategpt.yml -f qdrant.yml -f <TML solution name>.yml**, where you replace <TML solution name> with your actual TML 
   solution name.

Installing minikube
-------------------

Follow these steps to install minikube - which is a 1 node kubernetes cluster for testing and development.

.. note::
      1.	Create a folder in your VM called kubernetes
       a. Note minikube is a ONE node Kubernetes cluster – it is the SAME functionality as a production grade Kubernetes cluster
      2.	cd to kubernetes folder
      3. Now install Kubernetes (minikube):
       a. RUN: wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
       b. RUN: sudo install minikube-linux-amd64 minikube
      
      4.	Now install kubectl
       a. curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
       b. RUN: sudo chmod +x kubectl
       c. RUN: sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
      
      
      5.	RUN Kubernetes: minikube start --driver=docker
       a. make sure docker engine is installed. If not run: sudo apt-get install docker.io
       b. RUN: sudo chmod 666 /var/run/docker.sock
       c. Note: If you have a Nvidia GPU then use: minikube start --driver docker \-\-container-runtime docker \-\-gpus all

      6.	Create POD inside Kubernetes running your Docker Container
       a. RUN: kubectl apply -f <YAML files>
       b. RUN: kubectl get pods
            
      7.	PORT Forward 9005:
       a. RUN: kubectl port-forward <pod name> 9005:9005

Scaling EXAMPLE: Scaling Cybersecurity with privateGPT solution
--------------------------------------------

To show how simple it is to scale TML solutions in kubernetes, we will scale :ref:`Cybersecurity Solution with PrivateGPT, MQTT, HiveMQ`

.. tip::
   If you do not have Kubernetes cluster access then install minikube locally: See this section :ref:`Installing minikube`

.. note::
   Here are the steps to scaling the cybersecurity solution with privateGPT:

   1. Run the :ref:`Solution DAG Code: solution_preprocessing_ai_mqtt_dag-cybersecuritywithprivategpt-3f10` in the TSS.  
   2. Go to the `solution documentation on readthedocs <https://cybersecuritywithprivategpt-3f10.readthedocs.io/en/latest/index.html>`_
   3. Go to section: `Scaling [cybersecuritywithprivategpt-3f10] With Kubernetes <https://cybersecuritywithprivategpt-3f10.readthedocs.io/en/latest/kube.html#scaling-cybersecuritywithprivategpt-3f10-with-kubernetes>`_
   4. Copy the following YML files and save to your local computer in Linux:
     a. `mysql-storage.yml <https://cybersecuritywithprivategpt-3f10.readthedocs.io/en/latest/kube.html#mysql-storage-yml>`_
     b. `mysql-db-deployment.yml <https://cybersecuritywithprivategpt-3f10.readthedocs.io/en/latest/kube.html#mysql-db-deployment-yml>`_
     c. `privategpt.yml <https://cybersecuritywithprivategpt-3f10.readthedocs.io/en/latest/kube.html#privategpt-yml>`_
     d. `qdrant.yml <https://cybersecuritywithprivategpt-3f10.readthedocs.io/en/latest/kube.html#qdrant.yml>`_
     d. `cybersecuritywithprivategpt-3f10.yml <https://cybersecuritywithprivategpt-3f10.readthedocs.io/en/latest/kube.html#cybersecuritywithprivategpt-3f10-yml>`_
   5. Now apply the YML files to your Kubernetes cluster:
     a. kubectl apply -f mysql-storage.yml -f mysql-db-deployment.yml -f privategpt.yml -f cybersecuritywithprivategpt-3f10.yml
   6. Run: kubectl get pods
     a. You should see a list of pods - as shown in figure below.
   7. Run the Cybersecurity dashboard.
     a. Run: kubectl get deployment
     b. Run: kubectl port-forward <deployment name> 9005:9005
     c. Run the Dashboard - it should look like :ref:`The Dashboard with PrivateGPT`:
         `http://localhost:9005/tml-cisco-network-privategpt-monitor.html?topic=cisco-network-preprocess,cisco-network- 
         privategpt&offset=-1&groupid=&rollbackoffset=400&topictype=prediction&append=0&secure=1 <http://localhost:9005/tml-cisco-network-privategpt-monitor.html?topic=cisco-network-preprocess,cisco-network- 
         privategpt&offset=-1&groupid=&rollbackoffset=400&topictype=prediction&append=0&secure=1>`_

This image shows 3 replicas of the TML solution: cybersecuritywithprivategpt-3f10, along with a mysql pod and a privategpt pod.  

.. figure:: kubectl.png
   :scale: 50%

.. tip::
   The number of replicas can be changed in the **cybersecuritywithprivategpt-3f10.yml** file: look for **replicas**.  You can increase or decrease the number of replicas based on the amout of real-time data you are processing.

   To inside the pods, you can type command: 

    COMMAND: **kubectl exec -it <pod name> \-\- bash** (replace <pod name> with actual pod name)

   To delete the pods type:

    COMMAND: **kubectl delete all \-\-all \-\-all-namespaces**

   To get information on a pod type:

    COMMAND: **kubectl describe pod <pod name>** (replace <pod name> with actual pod name)

