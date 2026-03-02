==========================
TML Flask API Endpoints
==========================

This service exposes endpoints to create topics, preprocess data, run machine learning pipelines, generate predictions, and consume data from topics through the Viper backend.

Each endpoint expects JSON input via POST requests.

--------------------------
POST /createtopic
--------------------------

**Description:**
Create one or more topics in the Viper message broker.

**Request JSON Parameters:**

- ``topics`` *(string, required)* – Comma-separated list of topic names.
- ``numpartitions`` *(int, optional, default=3)* – Number of partitions for each topic.
- ``replication`` *(int, optional, default=1)* – Replication factor.
- ``description`` *(string, optional, default="user topic")* – Description of the topic.
- ``enabletls`` *(int, optional, default=1)* – Enable TLS (1 = on, 0 = off).

**Example Request:**

.. code-block:: json

    {
        "topics": "raw-data,processed-data",
        "numpartitions": 6,
        "replication": 2,
        "description": "Industrial IoT streams",
        "enabletls": 1
    }

**Example Response:**
- *200* – Topics created successfully (plain text).
- *400* – ``"Missing topics"``

--------------------------
POST /preprocess
--------------------------

**Description:**
Trigger preprocessing steps for data streams.

**Request JSON Parameters:**

- ``step`` *(string, required)* – Processing mode (`"4"` or `"4c"`).
- ``rawdatatopic`` *(string, required)* – Source topic with raw data.

**For step = '4':**
- ``preprocessdatatopic``, ``preprocesstypes``, ``jsoncriteria``, ``windowinstance`` *(optional)*

**For step = '4c':**
- ``maxrows``, ``searchterms``, ``rememberpastwindows``, ``patternwindowthreshold``,
- ``raw_data_topic``, ``rtmsstream``, various thresholds, ``windowinstance``

**Example Request (step=4):**
.. code-block:: json

    {
        "step": "4",
        "rawdatatopic": "raw-sensor-data",
        "preprocessdatatopic": "clean-sensor-data",
        "preprocesstypes": "normalize,filter",
        "jsoncriteria": "{\"min_value\": 0, \"max_value\": 1000}",
        "windowinstance": "sensor-batch-1"
    }

**Example Response:**
- *200* – Preprocessing started (plain text).
- *400* – ``"Missing preprocess or invalid preprocess"``

--------------------------
POST /ml
--------------------------

**Description:**
Train a machine learning model using preprocessed data.

**Request JSON Parameters (step='5'):**
- ``trainingdatafolder``, ``ml_data_topic``, ``preprocess_data_topic``
- ``islogistic``, ``dependentvariable``, ``independentvariables``, ``processlogic``
- ``rollbackoffsets``, ``windowinstance``

**Example Request:**
.. code-block:: json

    {
        "step": "5",
        "trainingdatafolder": "/data/training/2026Q1",
        "ml_data_topic": "ml-features",
        "preprocess_data_topic": "clean-sensor-data",
        "islogistic": 1,
        "dependentvariable": "equipment_failure",
        "independentvariables": "temp,vibration,pressure",
        "processlogic": "balance_classes=true",
        "rollbackoffsets": 100,
        "windowinstance": "ml-training-v1"
    }

**Example Response:**
- *200* – Training initiated.
- *400* – ``"Missing ml or invalid ml"``

--------------------------
POST /predict
--------------------------

**Description:**
Run prediction using trained ML models and streaming data.

**Request JSON Parameters (step='6'):**
- ``pathtoalgos``, ``maxrows``, ``consumefrom``, ``inputdata``, ``streamstojoin``
- ``ml_prediction_topic``, ``preprocess_data_topic``, ``windowinstance``

**Example Request:**
.. code-block:: json

    {
        "step": "6",
        "pathtoalgos": "/models/equipment_failure_v1",
        "maxrows": 1000,
        "consumefrom": "live-sensor-stream",
        "inputdata": "{\"sensor_id\": \"SENSOR_123\"}",
        "streamstojoin": "metadata,alerts",
        "ml_prediction_topic": "failure_predictions",
        "preprocess_data_topic": "clean-sensor-data",
        "windowinstance": "prediction-stream-1"
    }

**Example Response:**
- *200* – Prediction started.
- *400* – ``"Missing ml or invalid prediction"``

--------------------------
POST /consume
--------------------------

**Description:**
Consume messages from a given topic and optionally forward results.

**Request JSON Parameters:**
- ``topic`` *(required)*, ``forwardurl`` *(optional)*, ``osdu`` *(optional)*
- ``rollbackoffset``, ``enabletls``, ``offset``, ``topicid``

**Example Request:**
.. code-block:: json

    {
        "topic": "failure_predictions",
        "forwardurl": "https://webhook1.example.com,https://webhook2.example.com",
        "rollbackoffset": 50,
        "osdu": "false",
        "enabletls": 1
    }

**Example Response (osdu=false):**
.. code-block:: json

    {
        "status": "consumed",
        "topic": "failure_predictions",
        "messages": [{"offset": 123, "data": {...}}, {...}],
        "consumer_id": "tmlconsumerplugin"
    }

**Example Response (osdu=true + forwarding):**
.. code-block:: json

    {
        "kind": "tml",
        "id": "osdu:tml:consume:failure_predictions:1640995200",
        "data": {
            "Topic": "failure_predictions",
            "Messages": [...],
            "meta": {...}
        },
        "forward_statuses": [
            {"url": "https://webhook1.example.com", "status": 200, "success": true},
            {"url": "https://webhook2.example.com", "status": 200, "success": true}
        ]
    }

**Responses:**
- *200* – Consumed messages returned.
- *400* – Missing topic.
- *500* – Consumption failed.

--------------------------
POST /jsondataline
--------------------------

**Description:**
Send a single JSON data object to a topic.

**Example Request:**
.. code-block:: json

    {
        "topic": "raw-sensor-data",
        "timestamp": "2026-03-01T21:54:00Z",
        "sensor_id": "SENSOR_123",
        "temperature": 72.5,
        "vibration": 0.8
    }

**Example Response:**
.. code-block:: json

    "ok"

--------------------------
POST /jsondataarray
--------------------------

**Description:**
Send a JSON array of objects to a topic.

**Example Request:**

.. code-block:: json

    {
        "topic": "raw-sensor-data",
        [...]
    }

**Example body (array directly):**

.. code-block:: json

    [
        {
            "timestamp": "2026-03-01T21:54:00Z",
            "sensor_id": "SENSOR_123",
            "temperature": 72.5
        },
        {
            "timestamp": "2026-03-01T21:55:00Z", 
            "sensor_id": "SENSOR_124",
            "temperature": 73.2
        }
    ]

**Example Response:**

.. code-block:: json

    "ok"

