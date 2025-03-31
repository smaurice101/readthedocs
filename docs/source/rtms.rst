How TML Maintains Past Memory of Events Using Sliding Time Windows in Real-Time
============================================

.. tip::
   This capability is implemented in :ref:`STEP 4c: Preprocesing 3 Data: tml-system-step-4c-kafka-preprocess-dag`

.. note::
   While the Real-Time memory of sliding time windows (RTMS) is demonstrated for Cyber security, **it can be applied to any usecase in Retail, Finance, IoT, Energy, 
   Manufacturing etc..** Anytime you want to analyse TEXT files and determine if events have occured in the past and quantify their importance (or lack of 
   importance) then this is a powerful feature for you.  

   Also, if you want to **cross-reference TML machine learning output of every entity to text files** i.e. log files, and "remember" their behaviour then this 
   feature becomes very powerful for you. For example, you may be processing Entities in `Step 4 <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4-preprocesing-data-tml-system-step-4-kafka-preprocess-dag>`_ and then want to determine if an entity is showing up in the logs or whether it is hacking in to your 
   company using a slow and "occasional" attempt over time to EVADE detection algorithms, then RTMS can be very powerful to detect this complex behaviour.

Importance of Real-Time Data and Cyber Crime
---------------------------

* The growth of **real-time data** according to IDC Research **will reach 30% of global data in 2025 or roughly 90 ZB or 90 trillion gigabytes** mainly from IoT devices connected to the Internet

* This raises concerns and opportunities to process real-time data with Transactional Machine Learning (TML)

* The major concern with real-time streaming data from connected devices is the risk of Cybersecurity attacks

* **Cyber crime is expected to cost the global economy $10.7 Trillion in 2025 and this number is growing**

* This makes Cyber crime prevention and mitigation a Top Priority for global organizations regardless of size

* TML presents a powerful method of detecting, mitigating and preventing cyber attacks at the entity level by “remembering” past events in past sliding time windows and quantifies this by computing three scores:

   * **Attack Score (AS):** Quantifies the attack vector.  Higher number, more likely attack is occurring
  
   * **Pattern Score (PS):** Quantifies the pattern vector.  Higher number, more likely a pattern in the attack
  
   * **Real-Time Memory Score (RTMS):** Combines both the Attack and Pattern Scores for an OVERALL score

The Method
-------------------

#. User tells TML to keep a memory of past sliding time windows

#. User wants TML to search for malicious events from each entity (i.e. IP address, devices, etc..)

#. Malicious events are TEXT like: “authentication failures”, “unknown password”, “unknown users”

#. TML does a direct STRING search for these terms in the sliding time windows
  
   .. note::
      THIS METHOD DOES NOT NEED A VECTOR DB or PRIVATEGPT only TML Processing– this makes TML method very light weight and fast

#. The Data TML searches, in real-time, are text files that are most likely log files 

#. The Log files can be files on the file system that TML reads OR logs that are directly streamed to Kafka with LogStash, Splunk, etc..
   
   .. note:: 
      Note: This data does NOT have to be any specific format – it can be ANY text file streamed in raw form.

#. As TML process these data in sliding time windows (for details on sliding time window go here: :ref:`TML Performs Entity Level Machine Learning and Processing`) it is computing in real-time the following Scores:

   #. **AttackScore** is computing the occurrence of malicious events in past windows and how likely this is an attack

   #. **PatternScore** uses a pattern threshold set by the users (we use 10 for demo) it counts the occurrence of  events (that user is searching for) in past windows

   #. **RTMS Score** simply combines the Attack and Pattern scores for an overall score.  

.. note:: 
   NOTE: RTMS can exceed 1 because the pattern score can be greater than 1 i.e. events can exceed user pattern threshold.
   These score will obviously fluctuate in real-time time and alerts can be set up to trigger ALARMS of a cyber attack.

High-Level Reference Architecture
-----------------------

.. important:: 

    **Some important points to note about the architecture below:**

    #. The TML RTMS solution can analyse ANY log file and AS MANY as you like
    #. You can use third-party tools like `LogStash <https://www.elastic.co/logstash>`_, `Splunk <https://www.splunk.com/>`_ etc.  to stream directly to Apache Kafka
    #. No format is needed for the log files - JUST STREAM IT TO KAFKA IN RAW FORM and tell TML in `Step 4c <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4c-preprocesing-3-data-tml-system-step-4c-kafka-preprocess-dag>`_ what the Kafka Topic is in the **rtmsstream** JSON field.
    #.  You do NOT have to use Entities - you can immediately start analysing your log files for anomalies
    #. If you are using entities - start processing in `Step 4 <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4-preprocesing-data-tml-system-step-4-kafka-preprocess-dag>`_ and connect the entities by specifying the topic you stored entities (in Step 4) to **raw_data_topic** in Step 4c.  Thats IT!
    #. Build as many TML RTMS solutions you want with the `TSS <https://tml.readthedocs.io/en/latest/docker.html#tml-solution-studio-tss-container>`_.

.. figure:: rtms3.png
   :scale: 70%

**Enjoy the POWER of TML RTMS solution - that integrates real-time ML/AI entity level predictions with text files (like log files) to protect your global organizations - UNLIKE ANY OTHER TECHNOLOGY IN THE MARKET.**

Past Memory Demonstration
-----------------------

.. important::
   **It is important to note the following about the Attack and Pattern scores:**

   * - **Pattern Score** will look for all occurrences of search terms in each sliding time window.  Meaning there may be MULTIPLE occurrences of search terms in the SAME sliding time window.  This number can be greater than 1.

     * - **Pattern score** will check the number of windows GOING BACK as far as **RTMSMAXWINDOWS** parameter in `STEP 1 <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-1-get-tml-core-params-tml-system-step-1-getparams-dag>`_.  

     * - So, if this number is 1000, TML will check all 1000 sliding time windows for the occurrence of the search terms.

     * - The **patternscorethreshold** can be set in `Step 4c <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4c-preprocesing-3-data-tml-system-step-4c-kafka-preprocess-dag>`_.  This is the maximum occurrence of a pattern before raising an ALERT.  This means the **Pattern Score MAY BE GREATER THAN 1**.

   * - **Attack Score** ONLY checks if window CONTAINS AN OCCURENCE of the search term.  This number is either 1 or 0.  The attack score is GOING BACK as far as the **rememberpastwindows** parameter in `Step 4c <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4c-preprocesing-3-data-tml-system-step-4c-kafka-preprocess-dag>`_.

   * - **User parameters:** `rememberpastwindows <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4c-preprocesing-3-data-tml-system-step-4c-kafka-preprocess-dag>`_ and `RTMSMAXWINDOWS <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-1-get-tml-core-params-tml-system-step-1-getparams-dag>`_ are the core parameters that allows TML to **REMEMBER past events in real-time**.

.. figure:: rtms1.png
   :scale: 70%

.. figure:: rtms2.png
   :scale: 70%

TML Output of RTMS Scores
---------------

.. code-block:: JSON
            
      {
      	"hyperprediction": "0.00",
      	"Entity": "5.14",
      	"Maintopic": "iot-preprocess",
      	"Topicid": "topicid10_rtms-stream-mylogs",
      	"Topic": "rtms-stream-mylogs",
      	"Type": "External",
      	"ProducerId": "RTMS",
      	"TimeStamp": "2025-03-22 15:33:49",
      	"Unixtime": 1742657629034578889,
      	"kafkakey": "OAA-N1rvV8-f7VZLG0ZxwSJlqLDrrFmHs1",
      	"Preprocesstype": "rtms",
      	"SearchTextFound": [
      		"Message Found: m 84.102.20.2 () at Sun Jul 24 02:38:22 2005 Jul 24 02:38:23 combo ftpd16781: ANONYMOUS FTP LOGIN FROM 84.102.20.2  (anonymous) Jul 24 02:38:23 combo ftpd16782: ANONYMOUS FTP - using search term: anonymous ftp login. Date Found: 22 Mar 2025 15:33:37UTC",
      		"Message Found: MOUS FTP LOGIN FROM 84.102.20.2  (anonymous) Jul 24 02:38:23 combo ftpd16782: ANONYMOUS FTP LOGIN FROM 84.102.20.2  (anonymous) Jul 24 04:20:19 combo su(pam_unix)17283: - using search term: anonymous ftp login. Date Found: 22 Mar 2025 15:33:37UTC"
      	],
      	"FinalAttackScore": "0.00",
      	"FinalPatternScore": "0.07",
      	"RTMSSCORE": "0.00",
      	"NumAttackWindowsFound": "1",
      	"NumPatternWindowsFound": "2",
      	"Filename": "/rawdata/rtms2/rtms-stream-mylogs_10_anonymousftplogin.txt.log",
      	"TMLComment": "The RTMS score of 0.00 seems to show low activity or risk.  The AttackScore of 0.00 is less than PatternScore of 0.07, which suggests likely no attack, but could be a pattern developing.  The number of windows searched for an occurence of a pattern is 2. TML will continue monitoring and these numbers may change over time.",
      	"ActivityLevel": "Low",
      	"RememberPastWindows": "500",
      	"RTMSMAXWINDOWS": "1000",
      	"PatternThreshold": "30",
      	"SearchEntity": "ANONYMOUS FTP LOGIN;",
      	"PartitionOffsetFound": "0:9810;",
      	"Hash": "l8-ckFLfU4H5DveB9bSj7lThjws=",
      	"GithubRemoteUrl": "https://github.com/smaurice101/raspberrypitss/blob/main/tml-airflow/dags/tml-solutions/cybersecurityrtms-3f10/rtms2/rtms-stream-mylogs_10_anonymousftplogin.txt.log",
      	"rtmsfolder": "rtms2"
      }

Integrating RTMS with Real-Time AI Using PrivateGPT Containers and MITRE ATT&CK Classification
-----------------

Below is output from `Step 9 task <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-9-privategpt-and-qdrant-integration-tml-system-step-9-privategpt-qdrant-dag>`_, that takes messages in the "SearchTextFound", and send it to the `PrivateGPT special containers <https://github.com/smaurice101/readthedocs/blob/main/docs/source/genai.rst#privategpt-special-containers>`_

By using AI, users can prompt for any anomalies and resolutions suggested by AI.  This is all done in real-time using local privateGPT containers, that makes this integration 100% FREE, SECURE and SCALABLE. 

Also, RTMS automatically classified the messages in accordance with `MITRE ATT&CK classification matrix <https://attack.mitre.org/>`_:

 - **TACTIC**: Initial_Access
 - **TECHNIQUE**: Phishing

.. code-block::

      {
      	"ActivityLevel": "Low",
      	"Consumerid": "StreamConsumerpred3",
      	"CurrentRTMSMAXWINDOW": 1,
      	"CurrentRememberPastWindow": 1,
      	"Entity": "5.17",
      	"Filename": "/rawdata/rtms2/rtms-stream-mylogs_17_anonymousftplogin.txt.log",
      	"FinalAttackScore": "0.00",
      	"FinalPatternScore": "0.10",
      	"Generated": "2025-03-30T20:44:51.607 00:00",
      	"GithubRemoteUrl": "https://github.com/smaurice101/raspberrypitss/blob/main/tml-airflow/dags/tml-solutions/cybersecurityrtms-3f10-ai/rtms2/rtms-stream-mylogs_17_anonymousftplogin.txt.log",
      	"Hash": "gDhw-DJfSysWEAbErkKFt7Ktm38=",
      	"LastOffsetProcessed": 50029,
      	"LastPartitionProcessed": 0,
      	"Maintopic": "iot-preprocess",
      	"NumAttackWindowsFound": "1",
      	"NumPatternWindowsFound": "3",
      	"Offset": 1708,
      	"Partition": 0,
      	"PartitionOffsetFound": "0:49835:0:49923:",
      	"PatternThreshold": "30",
      	"Preprocesstype": "rtms",
      	"ProducerId": "RTMS",
      	"RTMSMAXWINDOWS": "1000000",
      	"RTMSSCORE": "0.00",
      	"RememberPastWindows": "500",
      	"SearchEntity": "ANONYMOUS FTP LOGIN:",
      	"SearchTextFound": [
      		"Message Found: ApplicableState: 112  CurrentState:112 2016-09-29 02:04:22  Info CBS Session: 30546354_3183ANONYMOUS FTP LOGIN714279 initialized by client WindowsUpdateAgent. 2016-09-29 02:04:22  Info CBS - using search term: anonymous ftp login. Date Found: 30 Mar 2025 20:40:02 UTC",
      		"Message Found: from 84.102.20.2 () at Sun Jul 24 02:38:22 2005 Jul 24 02:38:23 combo ftpd16781: ANONYMOUS FTP LOGIN FROM 84.102.20.2  (anonymous) Jul 24 02:38:23 combo ftpd16782: ANONYMOUS FTP - using search term: anonymous ftp login. Date Found: 30 Mar 2025 20:40:02 UTC",
      		"Message Found: ANONYMOUS FTP LOGIN FROM 84.102.20.2  (anonymous) Jul 24 02:38:23 combo ftpd16782: ANONYMOUS FTP LOGIN FROM 84.102.20.2  (anonymous) Jul 24 04:20:19 combo su(pam_unix)17283: - using search term: anonymous ftp login. Date Found: 30 Mar 2025 20:40:02 UTC"
      	],
      	"TMLComment": "The RTMS score of 0.00 seems to show low activity or risk.  The AttackScore of 0.00 is less than PatternScore of 0.10, which suggests likely no attack, but could be a pattern developing.  The number of windows searched for an occurence of a pattern is 1. TML will continue monitoring and these numbers may change over time.",
      	"TimeStamp": "2025-03-30 20:40:20",
      	"Topic": "rtms-stream-mylogs",
      	"Topicid": "topicid17_rtms-stream-mylogs",
      	"Type": "External",
      	"Unixtime": 1743367220717241000,
      	"hyperprediction": "0.00",
      	"kafkakey": "OAA-nkLUEpO9WXmNMO6sbEYYrNTTju4LKz",
      	"rtmsfolder": "rtms2",
      	"privateGPT_AI_response": "Based on the provided log messages, there are repeated instances of \"ANONYMOUS FTP LOGIN\" attempts from the IP address 84.102.20.2. Anonymous FTP access is generally considered insecure because it allows users to connect without providing a username or password. This can make your system vulnerable to attacks, as anyone can try to access your FTP server using no credentials at all. The repeated attempts from the same IP address suggest that there might be an automated script or bot trying to exploit this vulnerability. The search term \"anonymous ftp login\" in some of the log messages also indicates that the system is actively looking for such entries, which could be a sign of heightened security awareness or an attempt to investigate and mitigate potential threats. The MITRE ATTandCK classification for these messages would likely fall under the following techniques: - Initial Access: Brute Force (T1102.001) - Anonymous login attempts can be considered a form of brute force attack, as the attacker is trying to gain access using generic or weak credentials. - Initial Access: Phishing (T1566.001) - In some cases, an anonymous FTP login attempt could be part of a phishing campaign, where the attacker tries to trick users into revealing sensitive information or granting unauthorized access. To mitigate this risk, it is recommended to: - Disable anonymous FTP access on your server and require authentication for all connections. - Implement strong password policies and enforce regular password changes. - Use a firewall to block or limit access to the FTP port from untrusted sources. - Monitor your logs regularly for suspicious activity and configure alerts for specific events, such as failed login attempts or unusual traffic patterns. - Keep your software up-to-date with the latest security patches and updates.",
      	"prompt": "[INST] Are there any errors or suspicious activity in the log messages found? Give a detailed response, and any resolutions that need to be done. Also, Can you give me the MITRE ATTandCK classification for these messages?[/INST]",
      	"context": "This data are from network log files. This log file data have been filtered using the search terms shown in the messages. The filtered messages may indicate potential suspicious log entries that could indicate a cyber attack.",
      	"pgptcontainer": "maadsdocker/tml-privategpt-with-gpu-nvidia-amd64-v2",
      	"pgpt_consumefrom": "rtms-preprocess",
      	"pgpt_data_topic": "rtms-pgpt-ai",
      	"contextwindowsize": 8192,
      	"temperature": "0.1",
      	"pgptrollbackoffset": 5,
      	"tactic": "Initial_Access",
      	"technique": "Phishing"
      }

Output Explanation
==========================

.. list-table::

   * - **Field**
     - **Explanation**
   * - hyperprediction
     - This is the RTMS Score
   * - Entity
     - This is the entity being analysed.  This can be 

       anything you want.
   * - GithubRemoteUrl
     - This is the GitHub Url for te RTMS solution output 
      
       specific to your TML solution.  All RTMS outputs are 

       logged to Github automatically AND to Kafka topic.

       The log files are important for testing and validation.

   * - Maintopic
     - This is the topic that holds the entity

       preprocessing from `Step 4 <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4-preprocesing-data-tml-system-step-4-kafka-preprocess-dag>`_
   * - Topicid
     - TML gives entity an internal integer ID.
 
       This entity (192.168.5.24) has an internal

       ID of 17. The format is the:
   
       **topicid<internal entity number>_<name of RTMS topic searched>**
   * - Topic
     - The RTMS topic searched - containing TEXT
   * - Type
     - Internal label
   * - ProducerId
     - Internal label
   * - TimeStamp
     - The time results were generated.
   * - Unixtime
     - The Unixtime of TimeStamp
   * - kafkakey
     - Unique key for this JSON in Kafka.

       If you want to audit these results 

       these keys identify each message uniquely.
   * - Preprocesstype
     - Type is **rtms**
   * - UserSearchValues
     - These are the user search values. See tip below.
   * - SearchTextFound
     - This is list of text that was found in the 
 
       the Text files (log files) that contain your 

       search terms.  The list is truncated to 3000.
  
       But, this will give you a good indication of
 
       whats happening.
   * - FinalAttackScore
     - The Final attack score
   * - FinalPatternScore
     - The final pattern score
   * - hash
     - Unique internal message hash
   * - RTMSSCORE
     - The RTMS score.
   * - NumAttackWindowsSearched
     - The number of attack windows that contain the search
     
       terms.  This is upto **RememberPastWindows**
   * - NumPatternWindowsSearched
     - This the number of windows that contain the search terms.

       Note: This in not restricted to RememberPastWindows, but

       upto **RTMSMAXWINDOWS** in `Step 1 <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-1-get-tml-core-params-tml-system-step-1-getparams-dag>`_ 
    
       JSON field.
   * - Filename
     - This is a file of these results saved to:
     
       **/rawdata/rtms** folder in the container.
   * - TMLComment
     - This is the suggested auto-generated TML comment.
   * - ActivityLevel
     - Based on the RTMS score this is what TML suggests.
   
       You can ofcourse use your own judgement.
   * - RememberPastWindows
     - TML will remember the sliding windows upto
 
       this number.
   * - PatternThreshold
     - This is a user threshold to alert when a pattern

       is equal to or greater than this number.
   * - privateGPT_AI_response
     - This is the real-time response from the privateGPT container 

       running LLM models from Deepseek or Mistral AI.

       See `here <https://tml.readthedocs.io/en/latest/genai.html#privategpt-special-containers>`_ for details.
   * - prompt
     - The prompt provided by the user.
   * - context
     - The context provided by the user.
   * - pgptcontainer
     - The privateGPT container used from `here <https://tml.readthedocs.io/en/latest/genai.html#privategpt-special-containers>`_.
   * - pgpt_consumefrom
     - The kafka topic that Step 9 task will consume from.
   * - pgpt_data_topic
     - The kafka topic Step 9 task will output results to.
   * - contextwindowsize
     - The context window for the LLM.  This is basically

       the maximum number of words LLM will process.
   * - temperature
     - This is the LLM temperature parameter.  

       Close to 0, the LLM will be more conservative 
    
       in responses; close to 1, it will hallucinate.
   * - pgptrollbackoffset
     - The amount of offsets to rollback the **pgpt_consumefrom** topic.

.. tip:: 
   TML gives you are powerful capability to substiitute the **--entity--** placeholder with the **Entity** above. This makes it possible to search for each invidual entity in any log files.

.. note:: 
   If you DO NOT want to use entities simply set the **'raw_data_topic'** to an empty string ('') in `Step 4c <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4c-preprocesing-3-data-tml-system-step-4c-kafka-preprocess-dag>`_.  This will force TML to search ONLY the TEXT file topics for your search terms.

How TML Accomodates Evolving Threats
-------------------------

To detect evolving or changing cyber threats, TML can apply new user search terms in real-time by reading a local file containing search terms.  For example, you can tell TML to read a file containing search terms that are updated every every 30 seconds, or every day, by user's internal process. TML can read this file, and update the search terms immediately to this list.  This allows users to auto-update the threats that TML search for in real-time.

To update the search terms in real-time - you need to update two fields in `Step 4c: <https://tml.readthedocs.io/en/latest/tmlbuilds.html#step-4c-preprocesing-3-data-tml-system-step-4c-kafka-preprocess-dag>`_

#.   **localsearchtermfolder**: 
     - Specify a folder of files containing search terms - each term must be on a new line
     - use comma to apply each folder to the rtmstream topic
     - Use @ =AND, | =OR to specify whether the terms in the file should be AND, OR

       For example, @mysearchfolder1,|mysearchfolder2, means all terms in mysearchfolder1 should be AND |mysearchfolder2, means all search terms should be OR'ed

       .. important::
          **The search folders must exist in the local folder mapped to the /rawdata folder**.  For example, if you specify mysearchfolder1, TML assumes the search files are in /rawdata/mysearchfolder1 (see `here for details <https://tml.readthedocs.io/en/latest/tmlbuilds.html#producing-data-using-a-local-file>`_).

#. **localsearchtermfolderinterval**:
   - This is the number of seconds between reading the localsearchtermfolder.  
   
      For example, if 30, the files will be read every 30 seconds - and searchterms will be updated

.. tip::
   You can use RegEX statements in the search terms.  This allows you to do build powerful RegEx expressions to filter log files.

   If using Regex expressions, you must prefix the expression by **rgx:**.  For example, **rgx:p([a-z]+)ch**

   Regex expressions should be the only statement between ~, this is important if your Regex has a comma.  

   With Regular expressions applied in real-time by TML RTMS, you have a MUCH WIDER search space to detect anomalous behaviours.

Regular Expressions Example
-------------------

**To check whether usernames DO NOT follow the proper format in the log files - you can use:**

.. code-block::

   ^[0-9A-Za-z]{6,16}$

* ^ indicates the start of a string, while $ indicates the end. Basically, this is ensuring that the entire string follows our rules, rather than only a subset of the string.
* [...] indicates a particular set of valid characters, otherwise called a character class; 0-9 allows numbers, A-Z allows uppercase letters, a-z allows lowercase. There are other indicators, and you can find a complete list in regex documentation.
* {6,16} indicates the allowed number of characters. If you just used {6}, you're testing for a length of exactly 6, while {6,} tests for minimum length.
* ^ denotes NOT or a negation of the results.  For example, any characters NOT satisfying **[0-9A-Za-z]{6,16}**

**To check whether passwords DO NOT follow the proper format (or any string) - you can use:**

.. code-block::

   ^(?=.*?[0-9])(?=.*?[A-Za-z]).{8,32}$

* (...) is a capture group. You can use them for capturing particular characters in specific orders.
* ?= is a positive lookahead. The search moves rightward through the string from the location in your regex you make this assertion in.
* . signifies any character is possible, while * means 'zero or more' of them.
* The extra question mark in ?=.*? makes the search lazy, which essentially means 'stop looking after the first time this requirement is met'.
* Translated into plain English, the first part of our statement ^(?=.*?[0-9]) means 'from the start of the string, find a number that is preceded by zero or more of any character'.
* Adding (?=.*?[A-Za-z]) means do the same for any letter, or 'from the start of the string, find a letter that is preceded by zero or more of any character'. This allows us to confirm the presence of a specified kind of character within the total set of what is allowed without regard to where it occurs in the string.
* The last part of our statement .{8,32}$ builds on our understanding of . usage. We don't want to limit what kinds of characters the actual password is allowed to be. In contrast, if limiting to letters and numbers only, you'd use [0-9A-Za-z]{8,32}$.

.. code-block::
   
   192\.168\.(224|225)\.\d{1,3}

* Values in yellow—192 and 168—are literal strings to be matched.
* Because the "." character is reserved in the regular expression language, to match a literal ".", you must escape it with a backslash . in your pattern definition.
* The 3rd octet needs to match either "224" or "225" and regex allows that with the "|" character. The OR pattern is bound in parentheses (). If there are more than two selections, | can be used to separate additional values: (224|225|230).
* The "\d" represents a single digit (0-9). In the rex command example, above, I used a "+" to represent one or more of the preceding pattern. In this case, I am going to be more specific. Placing "1,3" in curly braces {1,3}, represents between 1 and 3 digits, since it was preceded by a "\d". 

.. code-block::

   (?<pass>[^&]+)

* ?<pass> specifies the name of the field that the captured value will be assigned to. In this case, the field name is "pass". This snippet in the regular expression matches anything that is not an ampersand.
* The square brackets [^&]+ signify a class, meaning anything within them will be matched; the carat symbol (in the context of a class) means negation. So, we're matching any single character that is not an ampersand.
* The plus sign extends that single character to one or more matches; this ensures that the expression stops when it gets to an ampersand, which would denote another value in the form_data.
* The parenthesis () signifies a capture group, while the value captured inside is assigned to the field name.

.. code-block::

   4[0-9]{15}

* This describes a string pattern starting with the digit 4 and having 15 digits in total that can have values from 0 to 9.

.. code-block::

   4[0-9]{12}(?:[0-9]{3})?

* This is relevant for strings that begin with the digit 4 and have 12 more digits with possible values from 0 to 9. 
* After this sequence, a string can have or not have three more digits with values from 0 to 9. Thus, we can find not only credit card numbers with 16 digits but those with 13 digits as well.

.. code-block::

   \S+@\S+\.\S+

* A sequence of symbols without spaces before the @ symbol
* The @ symbol
* A sequence of symbols without spaces after the @ symbol
* A . symbol
* A sequence of symbols without spaces

.. code-block::

   (?:[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e- 
   \x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]| 
   [01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])

**This regular expression is also relevant for strings that have an email address format but includes additional bypasses, cycles, and filters. Here’s a description of several constructions used in this RegEx:**

* (?:) — Makes a grouping that cannot be referenced
* [a-z] — Sets possible options for characters
* ? — Makes the expression optional
* \| — Sets alternation of two expressions on the left and right side of |
* \* — Means that an expression matches zero or more of the preceding character

.. code-block::

   (([0-9]{1,4})\)([ .-]?)([0-9]{1,4})([ .-]?)([0-9]{1,4})

* It describes a line in the (####)%####%#### format, where #### could be a sequence from one to four digits, and the % symbol stands for one of three possible separation symbols: space, dot/period, or hyphen.

.. code-block::

   [a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z]+-?[a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z]*

* A RegEx to search for matches with one of the symbols listed in square brackets and divided by the | symbol that represents an alternative for matching the part to the left and the part to the right of the | symbol. An alternative will include options from a to z.

A RegEx that points directly to a capture group:

.. code-block::

   \w+-?\w*

* RegEx examples that work with capture groups — mechanisms that allow you to highlight and save matching text for further use. When a RegEx matches the text, any content within a capture group is saved in temporary variables. You can use those variables later in code.

Link to a capture group (marked as \w):

.. code-block::

   \w+-?1*
 
* A RegEx that includes a link to capture group №1:

RegEx Cheat Sheets
--------------------

Here are RegEx cheat sheets that may help to write more advanced regular for powerful searching of text files.

.. tip::
   To test your RegEx you can use this onine tool: `regexr <https://regexr.com/>`_

.. figure:: regex.png
   :scale: 70%

.. figure:: regex2.png
   :scale: 70%

.. figure:: regex3.png
   :scale: 70%

TML RTMS vs AI RAG
------------

TML using real-time data is similar to `RAG <https://tml.readthedocs.io/en/latest/genai.html#tml-and-rag-a-powerful-combination>`_ but different in other ways.

.. list-table::

   * - **Attribute**
     - **TML RTMS**
     - **AI RAG**
   * - **Speed**
     - TML RTMS is much faster than RAG 

       because TML RTMS does NOT use vector DB.

       All TML RTMS processing is real-time.
     - AI RAG require vector DB for search. 

       Real-time is still difficult with RAG.
   * - **Prompting**
     - TML users direct text based search
     - With RAG you can use prompt
   * - **Combining ML and AI in Real-Time**
     - With TML you can combine TML output

       for each entity and cross-reference 

       with TEXT files
     - This is not currently possible with
       RAG       
   * - **Scalability**
     - TML RTMS scales with Kubernetes

       to process unlimited documents

       at a very low cost
     - Scaling RAG models is difficult

       and can be costly

How RTMS Integrates with MITRE ATT&CK Framework
----------------------------------------------

The `MITRE ATT&CK framework for the Entreprise and Cloud <https://attack.mitre.org/>`_ is used by `80% of global enterprises <https://cltc.berkeley.edu/publication/mitre-attck/#:~:text=While%20some%20enterprises%20adopt%20other,respondents%20indicating%20they%20leverage%20both.>`_.  **TML/RTMS is fully integrated with MITRE ATT&CK framework for Entreprise** level threat detection and classification for improved threat insights to help in further fortifying organizations' threat and security technologies and processes.

.. important::
   A key challenge by majority of organizations is the difficulty and inability to map events to specifc MITRE ATT&CK tactics and techniques.  Specifically, in a research report (`source <https://cltc.berkeley.edu/publication/mitre-attck/#:~:text=While%20some%20enterprises%20adopt%20other,respondents%20indicating%20they%20leverage%20both.>`_)

    **"about 45 percent of survey respondents said their greatest challenge is the framework’s inoperability with their security products and 43 percent said they 
    find it difficult to map event-specific data to tactics and techniques."**

   RTMS eliminates this challenge of mapping events to MITRE ATT&CK tactics and techniques by automating the classifications in real-time using our AI containers.

When RTMS searches logs for suspicious activity the messages it finds are sent to our `privateGPT AI container <https://tml.readthedocs.io/en/latest/genai.html#privategpt-special-containers>`_, the AI determines a mitigation plan, and MITRE ATT&CK classification of the messages.  The Attack, Pattern and RTMS scores are provided for the "grouped" MITRE ATT&CK tactics and techniques.  See figure below of Mitre tactics and techniques.

.. figure:: mitre.png
   :scale: 70%
   

**The RTMS scoring and classification of messages, in accordance with MITRE ATT&CK framework, can offer organizations around the world invaluable insights into their organizations that can help them to:**

 - **determine gaps in deployed security solutions in their enterprise,** 
 -	**for security policy implementation**
 -	**for threat modeling**

TML/RTMS with MITRE ATT&CK integration is a truly unique and powerful technological approach, in real-time, to give organizations **faster identifications of developing threats, but also offering invaluable guidance to fortify their security processes and technologies** that aligns with a global standard like MITRE ATT&CK.

.. note::
   An example of this classification is `here <https://tml.readthedocs.io/en/latest/rtms.html#integrating-rtms-with-real-time-ai-using-privategpt-containers-and-mitre-att-ck-classification>`_.  Look at the last JSON fields:
  
   * **"tactic":** "Initial_Access",
   * **"technique":** "Phishing"

   **The above are MITRE ATT&CK tactic and technique, that are automatically classified by RTMS AI agent for all messages.**  RTMS further groups on these tactic and techniques to compute the **grouped ATTACK, PATTERN and RTMS scores**.  This is a powerful approach to further help organization's fortify their security processes and technologies to dramatically reduce the threat of cyber attacks.

Summary
----------

* This has shown how TML implements real-time memory using sliding time windows for every entity

* For every entity: It quantified this memory in Three (3) scores:
  
  * **AttackScore (AS)**
  * **PatternScore (PS)**
  * **Real-Time Memory Score (RTMS)**

.. important::
   The power of TML maintaining memory and computing the 3 scores is to capture **attacker behaviours that try to EVADE detection algorithms**.  While the AttackScore may not indicate an attack, it may be picked up as a pattern in the PatternScore.  

  Also, TML/RTMS solution will automatically classify (using AI) messages in accourdance with the `Mitre Att&ck framework matrix for the Enterprise <https://attack.mitre.org/>`_. 

  The Mitre Att&ck classifications could provide tremendous help for Enterprises to:
   - determine gaps in deployed security solutions in their enterprise,  
   - for security policy implementation
   -for threat modeling.
 

* Within Cyber security context: The power of this method using sliding time windows is the ability to detect hacking attempts that are deliberate in evading “detection algorithms” from common industry tools

* TML approach and method is a fast, low cost, method of maintaining memory of events as they occur or have occurred in the past that may be “occasional” events and VERY HARD TO DETECT from other commercial tools

* The simplicity of maintaining and incorporating memory by TML for EVERY ENTITY- without the need to vector DB – makes it lightweight, fast, and able to run WITHOUT the need for GPU (only CPU is needed)

* As attackers get more sophisticated in evading commercial algorithms’ detection methods – TML memory offers a continuous awareness of events that are current and have occurred in the past and correlates and quantifies these in a Score for triggering alerts and alarms immediately
