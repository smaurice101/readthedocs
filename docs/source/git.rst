TML Solution Studio's Tight Integration with GitHub
================================

TML Solution build process is tightly integrated with GitHub to maintain a seamless process of tracking TML solution changes.  The figure below shows this integration.  As TML solution code is updated in Airflow, it can be committed directly from the Airflow UI.  This provides a high-level of convevience to ensure all code is properly checked in and committed to the main branch. 

.. tip::
   You integrate Github with TSS you need to generate a **Personal Access Token** from your Githib repo.  Follow the instructions here: :ref:`Generating Personal 
   Access Tokens in Github`.  You then add this token in the :ref:`TSS Docker Run Command` in the field **GITPASSWORD**.


You can push and pull changes directly from the TML Solution Studio - integrated with Airflow.

.. important::

   You can commit your code in the local and remote branches to ensure tightly controlled code changes.  This is an important aspect of the TML Studio Studio (TSS) 
   as well, all **git pushes** can be done directly from the TSS.

   NOTE: IT IS HIGHLY RECOMMENDED YOU WORK MAINLY IN THE TSS CODE EDITOR.  IF YOU NEED TO MAKE CHANGES IN YOUR GITHUB REPO DIRECTLY - THEN MAKE THOSE CHANGES FIRST, THEN START WORK IN TSS...OTHERWISE THERE MAY BE A CONFLICT BETWEEN YOUR REMOTE AND LOCAL BRANCHES AND YOU MAY LOSE EDITS IN TSS EDITOR.


Push To and Pull From Local and Remote Github Branches
---------------------

All changes are committed to local and remote branches by simple press of a button in the TML Studio Git Workspace.

.. figure:: tmlgit3.png

Viewing Local and Remote Github Branches
---------------------

You can view the local and remote branches conveniently inside the TML Solution Studio.

.. figure:: tmlgit.png

Github Logs
----------
This is your main TSS Github logs.  All TSS processes are committed to Github and logged. 

.. important::
   https:\/\/github.com\/<your github username>\/<repo you cloned>\/blob\/main\/tml-airflow\/logs\/logs.txt
