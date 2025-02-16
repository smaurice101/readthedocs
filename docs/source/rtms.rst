How TML Maintains Past Memory of Events Using Sliding Time Windows
============================================

* The growth of real-time data according to IDC Research will reach 30% of global data in 2025 or roughly 90 ZB or 90 trillion gigabytes mainly from IoT devices connected to the Internet

* This raises concerns and opportunities to process real-time data with Transactional Machine Learning (TML)

* The major concern with real-time streaming data from connected devices is the risk of Cybersecurity attacks

* Cyber crime is expected to cost the global economy $10.7 Trillion in 2025 and this number is growing

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
   NOTE: RTMS can exceed 1 because the pattern score can be greater than 1 i.e. events can exceed user pattern threshold
   These score will obviously fluctuate in real-time time and alerts can be set up to trigger ALARMS of a cyber attack
