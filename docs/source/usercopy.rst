Copying TML Project(s) From Others Git Repo
======================================

With TSS you have the ability to copy TML projects from others Git repo.  This is  convient if you want to share your TML projects with others.

The process of copying from otheres Git repo is simple:

#. Goto the TSS and select from the top menu item: Admin -> Dags Code Editor

#. Navigate to the File: **root/tml-airflow/dags/tml-solutions/CREATETMLPROJECT.txt**
   See figure below.

   .. figure:: usercopy1.png
      :scale: 70%

Once you are in the **CREATETMLPROJECT.txt** file - you can do the following scenarios:

You want to copy ALL TML Projects from another users Git Repo  
------------------------------------------------------
   
To do this:

  - You need the other persons Git repo
  - Enter -1 after the repo
  - For example:
    - Say I want to copy all TML Project from: **https://github.com/smaurice101/raspberrypitss**
    - Then Enter:
      
      .. code-block::

         https://github.com/smaurice101/raspberrypitss,-1
    
    - Then enter 

      .. figure:: usercopy2.png
         :scale: 70%

    **TSS will pull all TML projects from the other user's Git Repo and commit them to your repo.  TSS will take care of file changes.  Within few seconds, on your Git Repo you will see ALL of the other user's TML projects.**
