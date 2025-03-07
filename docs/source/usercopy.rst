Copying TML Project(s) From Others Git Repo
======================================

With TSS you have the ability to copy TML projects from others Git repo.  This is  convient if you want to share your TML projects with others.

.. tip:: 
   Also see here :ref:`Project Action Commands Summary` on projects in your own repo.

The process of copying from others Git repo is simple:

#. Goto the TSS and select from the top menu item: **Admin -> Dags Code Editor**

#. Navigate to the File: **root/tml-airflow/dags/tml-solutions/CREATETMLPROJECT.txt**

Once you are in the **CREATETMLPROJECT.txt** file - you can do the following scenarios:

You Want to Copy ALL TML Projects From Another Users Git Repo  
------------------------------------------------------
   
To do this:

  - You need the other persons Git repo
  - Enter **-1** after the repo, using comma as the separator.
  - For example:
    - Say you want to copy all TML Project from: **https://github.com/smaurice101/raspberrypitss**
    - Then Enter:
      
      .. code-block::

         https://github.com/smaurice101/raspberrypitss,-1

      .. figure:: usercopy1.png
         :scale: 60%

    - Then press Save:

      .. figure:: usercopy2.png
         :scale: 60%

    **TSS will pull all TML projects from the other user's Git Repo and commit them to your repo.  TSS will take care of file changes.  Within few seconds, on your Git Repo you will see ALL of the other user's TML projects.**

You Want to Copy SPECIFIC TML Projects From Another Users Git Repo  
------------------------------------------------------

To do this:

  - You need the other persons Git repo
  - Enter **the specific projects**, using comma as the separator.
  - For example:
    - Say you want to copy ONLY **myawesometmlsolution-3f10** and **iotsolution-3f10** TML Projects from: **https://github.com/smaurice101/raspberrypitss**
    - Then Enter:
      
      .. code-block::

         https://github.com/smaurice101/raspberrypitss,myawesometmlsolution-3f10,iotsolution-3f10

      .. figure:: usercopy3.png
         :scale: 70%

    Here you are copying TWO projects: myawesometmlsolution-3f10,iotsolution-3f10

    - Then press Save:

      .. figure:: usercopy2.png
         :scale: 70%

    **TSS will pull ONLY those TML projects from the other user's Git Repo and commit them to your repo.  TSS will take care of file changes.  Within few seconds, on your Git Repo you will see those specific projects of the other user's TML projects.**

Thats it!
