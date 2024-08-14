JSON PROCESSING 
=================

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
   * - datetime
     - This is the path to any datetime field.
   * - msgid
     - This is the path to any MSG ID of the json message or blank.
   * - latlong
     - This needs to be path to latitude or longitude or blank.  You can join the fields by semicolon.

.. note::
   Lets take an example.  Lets say we want to process the following JSON message:

   {"metadata":{"oem_id":"32795e59","oem_model":"SQR141U1XXW","dsn":**"AC000W016399396"**, "property_name":**"Power"**,"display_name":**"Power
   (mW)**","base_type":"integer","event_type":"datapoint"}, lat: **"43.11"**, long: **"127.011"**, "datapoint": {"id":**"de3e8f0e-7faa-11ec-31cb- 
   6b3a1eb15a96"**,"updated_at":**"2022-01- 
   27T19:53:59Z"**,"created_at":"2022-01-27T19:53:59Z","echo":false,"closed":false,"value":**"0"**,"metadata":{},"created_at_from_device":"2022-01- 
   27T19:51:40Z","user_uuid":"f4d3b326-da9a-11eb-87af-0a580ae966af","discarded":false,"scope":"user","direction":"output"}}  

   **The JSONCRITERIA specifies the JSON PATH to each TML Field separated by ~:**

   jsoncriteria='uid=metadata.dsn,filter:allrecords~subtopics=metadata.property_name~ values=datapoint.value~ 
   identifiers=metadata.display_name~datetime=datapoint.updated_at~msgid=datapoint.id~ latlong=lat:long'

   **uid=metadata.dsn** will retrieve the value **AC000W016399396**

   **subtopics=metadata.property_name** will retrieve the value **Power**

   **values=datapoint.value** will retrieve the value **0**

   **identifiers=metadata.display_name** will retrieve the value **Power**

   **datetime=datapoint.updated_at** will retrieve the value **2022-01-27T19:53:59Z**

   **msgid=datapoint.id** will retrieve the value **de3e8f0e-7faa-11ec-31cb-6b3a1eb15a96**

   **latlong=lat:long** will retrieve the value **43.11:127.011**

.. important::
   Json path are an important aspect of instructing TML where to find the data (**value**) in the Json **key** for processing and machine learning.

   The number of JSON paths in the **subtopics** MUST equal the number of JSON paths in the **values**.  Multiple JSON paths can be separated by a comma.

   TML requires the Json path of data to be processed.  Use the "." (dot) to 

Json Path Example
---------------------

Lets consider the following example.

.. list-table::

   * - **Sample Json message**
     - **Json Paths**
   * - {"metadata":{"oem_id":"32795e59","oem_model":"SQR141U1XXW", "dsn":"AC000W016399396", "property_name":"Power", "display_name":"Power 
       (mW)","base_type":"integer","event_type":"datapoint"}, "datapoint":{"id":"de3e8f0e-7faa-11ec-31cb-6b3a1eb15a96", "updated_at":"2022-01- 
       27T19:53:59Z", "created_at":"2022-01-27T19:53:59Z", "echo":false,"closed":false, "value":"0", "metadata":{}, "created_at_from_device":"2022-01- 
       27T19:51:40Z", "user_uuid":"f4d3b326-da9a-11eb-87af-0a580ae966af", "discarded":false, "scope":"user", "direction":"output"} , “lat”: 29.22, “long”: -141.22}
     - The Json Path to the variable: **dsn** is **metadata.dsn**

       The Json Path to the key: **value** is datapoint.value

       The Json criteria will be:
         jsoncriteria=
            uid= metadata.dsn,filter:allrecords~\  # uid: This is the json field to group by for example DSN or Device SerialNumber

            subtopics= metadata.property_name~\  # subtopics:  This is the json field to the name of the field you want to process

            values= datapoint.value~\   # values:  This is the json field containing the value of the subtopic

            identifiers= metadata.display_name~\  # identifier:  This is the json field containing any label or identifier for the values

            datetime= datapoint.updated_at~\  # datetime:  This is the json field in UTC format – i.e. 2006-01-02T15:04:05

            msgid= datapoint.id ~\  #msgid: this is the json field containing further details about the values 

            latlong=lat:long  # This is json field contain latitude and longitude.  You can use a “:” to combine lat:long

   * - Say you have a value you want to extract from a Json array: 
       	"code": {
      		"coding": [
			      {
				      "system": "http://snomed.info/sct",
				      "code": "84489001",
				      "display": "Mold (organism)"
			     }
		     ]},
     - The Json Path to the variable array: **code** is **code.coding.0.code**, 0 is the first element of the array.
