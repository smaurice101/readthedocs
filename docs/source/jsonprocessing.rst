TML JSON PROCESSING 
=====================

TML processes json data only.  JSON (Java Script Object Notation) is a standard format used by all applications.  Processing JSON data is highly efficient compared to SQL queries, due mainly to minimal data movements, faster compute, no database needed, and very low cost to process very large amounts of data.

To process your JSON data - you need to tell TML applicate the **JSON paths to the keys and values** to process.

TML requires the following - as shown in the table below. We will go though an example on how to apply this to your JSON data.

.. list-table::

   * - **TML Field**
     - **Description**
   * - uid 
     - This needs to be a unique id for the json message.  For example, if processing IOT device data, this would be the device's serial number. 
   * - subtopics
     - This is the json path to the variable name that identifies the type of data.  For example, if processing IOT, this could be json path to **voltage**
   * - values
     - This needs to be the json path to the value of the subtopics.  For example, for IOT voltage, it needs to be the path to the voltage value.
   * - identifiers
     - This is the path to some metadata about the values.
   * - msgid
     - This is the path to any MSG ID of the json message or blank.
   * - latlong
     - This needs to be path to latitude or longitude or blank.  You can join the fields by semicolon.

Lets take an example.  Lets say we want to process the following JSON message:

     jsoncriteria='uid=metadata.dsn,filter:allrecords~\
subtopics=metadata.property_name~\
values=datapoint.value~\
identifiers=metadata.display_name~\
datetime=datapoint.updated_at~\
msgid=datapoint.id~\
latlong=lat:long'     
