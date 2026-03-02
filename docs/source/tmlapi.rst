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

**Example Request (Python):**

.. code-block:: python

    import requests
    import json

    url = "http://localhost:5000/createtopic"
    payload = {
        "topics": "raw-data,processed-data",
        "numpartitions": 6,
        "replication": 2,
        "description": "Industrial IoT streams",
        "enabletls": 1
    }
    
    response = requests.post(url, json=payload)
    print(response.status_code, response.text)

**Example Request (JavaScript):**

.. code-block:: javascript

    const url = 'http://localhost:5000/createtopic';
    const payload = {
        topics: 'raw-data,processed-data',
        numpartitions: 6,
        replication: 2,
        description: 'Industrial IoT streams',
        enabletls: 1
    };

    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })
    .then(response => response.text())
    .then(data => console.log('Success:', data))
    .catch(error => console.error('Error:', error));

**Example Request (React):**

.. code-block:: jsx

    import { useState } from 'react';

    function CreateTopic() {
        const [status, setStatus] = useState('');
        
        const handleSubmit = async (e) => {
            e.preventDefault();
            const payload = {
                topics: 'raw-data,processed-data',
                numpartitions: 6,
                replication: 2,
                description: 'Industrial IoT streams'
            };
            
            try {
                const response = await fetch('http://localhost:5000/createtopic', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                setStatus(response.ok ? 'Topics created!' : 'Failed');
            } catch (error) {
                setStatus('Error: ' + error.message);
            }
        };

        return (
            <form onSubmit={handleSubmit}>
                <button type="submit">Create Topics</button>
                <p>{status}</p>
            </form>
        );
    }

**Responses:**
- *200* – Topics created successfully.
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

**Example Request (Python) - step=4:**

.. code-block:: python

    payload = {
        "step": "4",
        "rawdatatopic": "raw-sensor-data",
        "preprocessdatatopic": "clean-sensor-data",
        "preprocesstypes": "normalize,filter",
        "jsoncriteria": '{"min_value": 0, "max_value": 1000}',
        "windowinstance": "sensor-batch-1"
    }
    response = requests.post("http://localhost:5000/preprocess", json=payload)

**Example Request (JavaScript) - step=4:**

.. code-block:: javascript

    const payload = {
        step: '4',
        rawdatatopic: 'raw-sensor-data',
        preprocessdatatopic: 'clean-sensor-data',
        preprocesstypes: 'normalize,filter',
        jsoncriteria: '{"min_value": 0, "max_value": 1000}',
        windowinstance: 'sensor-batch-1'
    };
    fetch('http://localhost:5000/preprocess', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    });

**Example Request (React) - step=4:**

.. code-block:: jsx

    function PreprocessStep4() {
        const [status, setStatus] = useState('');
        
        const handlePreprocess = async () => {
            const payload = {
                step: '4',
                rawdatatopic: 'raw-sensor-data',
                preprocessdatatopic: 'clean-sensor-data',
                preprocesstypes: 'normalize,filter',
                jsoncriteria: '{"min_value": 0, "max_value": 1000}'
            };
            
            const response = await fetch('http://localhost:5000/preprocess', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            setStatus(response.ok ? 'Preprocessing started' : 'Failed');
        };

        return (
            <button onClick={handlePreprocess}>
                Start Preprocessing
            </button>
        );
    }

**Responses:**
- *200* – Preprocessing started.
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

**Example Request (Python):**

.. code-block:: python

    payload = {
        "step": "5",
        "trainingdatafolder": "/data/training/2026Q1",
        "ml_data_topic": "ml-features",
        "preprocess_data_topic": "clean-sensor-data",
        "islogistic": 1,
        "dependentvariable": "equipment_failure",
        "independentvariables": "temp,vibration,pressure",
        "rollbackoffsets": 100
    }
    response = requests.post("http://localhost:5000/ml", json=payload)

**Example Request (JavaScript):**

.. code-block:: javascript

    const payload = {
        step: '5',
        trainingdatafolder: '/data/training/2026Q1',
        ml_data_topic: 'ml-features',
        preprocess_data_topic: 'clean-sensor-data',
        islogistic: 1,
        dependentvariable: 'equipment_failure',
        independentvariables: 'temp,vibration,pressure',
        rollbackoffsets: 100
    };
    fetch('http://localhost:5000/ml', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    });

**Example Request (React):**

.. code-block:: jsx

    function TrainML() {
        const [status, setStatus] = useState('');
        
        const trainModel = async () => {
            const payload = {
                step: '5',
                trainingdatafolder: '/data/training/2026Q1',
                ml_data_topic: 'ml-features',
                preprocess_data_topic: 'clean-sensor-data',
                islogistic: 1,
                dependentvariable: 'equipment_failure',
                independentvariables: 'temp,vibration,pressure'
            };
            
            const response = await fetch('http://localhost:5000/ml', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            setStatus(response.ok ? 'Training started!' : 'Training failed');
        };

        return <button onClick={trainModel}>Train Model</button>;
    }


**Responses:**
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

**Example Request (Python):**

.. code-block:: python

    payload = {
        "step": "6",
        "pathtoalgos": "/models/equipment_failure_v1",
        "maxrows": 1000,
        "consumefrom": "live-sensor-stream",
        "ml_prediction_topic": "failure_predictions",
        "preprocess_data_topic": "clean-sensor-data"
    }
    response = requests.post("http://localhost:5000/predict", json=payload)

**Example Request (JavaScript):**

.. code-block:: javascript

    const payload = {
        step: '6',
        pathtoalgos: '/models/equipment_failure_v1',
        maxrows: 1000,
        consumefrom: 'live-sensor-stream',
        ml_prediction_topic: 'failure_predictions',
        preprocess_data_topic: 'clean-sensor-data'
    };
    fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    });

**Example Request (React):**

.. code-block:: jsx

    function Predict() {
        const [status, setStatus] = useState('');
        
        const runPrediction = async () => {
            const payload = {
                step: '6',
                pathtoalgos: '/models/equipment_failure_v1',
                maxrows: 1000,
                consumefrom: 'live-sensor-stream',
                ml_prediction_topic: 'failure_predictions'
            };
            
            const response = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            setStatus('Predictions started');
        };

        return <button onClick={runPrediction}>Run Predictions</button>;
    }

**Responses:**
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

**Example Request (Python):**

.. code-block:: python

    payload = {
        "topic": "failure_predictions",
        "forwardurl": "https://webhook1.example.com,https://webhook2.example.com",
        "rollbackoffset": 50,
        "osdu": "false"
    }
    response = requests.post("http://localhost:5000/consume", json=payload)
    print(response.json())

**Example Request (JavaScript):**

.. code-block:: javascript

    const payload = {
        topic: 'failure_predictions',
        forwardurl: 'https://webhook1.example.com,https://webhook2.example.com',
        rollbackoffset: 50,
        osdu: 'false'
    };
    fetch('http://localhost:5000/consume', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    })
    .then(r => r.json())
    .then(data => console.log(data));

**Example Response:**

.. code-block:: json

    {
        "status": "consumed",
        "topic": "failure_predictions",
        "messages": [...],
        "consumer_id": "tmlconsumerplugin"
    }

**Example Request (React):**

.. code-block:: jsx

    import { useState, useEffect } from 'react';

    function ConsumeData() {
        const [messages, setMessages] = useState([]);
        const [loading, setLoading] = useState(false);
        
        const consumeTopic = async () => {
            setLoading(true);
            const payload = {
                topic: 'failure_predictions',
                rollbackoffset: 50,
                osdu: 'false'
            };
            
            try {
                const response = await fetch('http://localhost:5000/consume', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(payload)
                });
                const data = await response.json();
                setMessages(data.messages || []);
            } catch (error) {
                console.error('Consume failed:', error);
            } finally {
                setLoading(false);
            }
        };

        return (
            <div>
                <button onClick={consumeTopic} disabled={loading}>
                    {loading ? 'Consuming...' : 'Consume Latest'}
                </button>
                {messages.length > 0 && (
                    <pre>{JSON.stringify(messages, null, 2)}</pre>
                )}
            </div>
        );
    }

**Example Response:**

.. code-block:: json

    {
        "status": "consumed",
        "topic": "failure_predictions",
        "messages": [...],
        "consumer_id": "tmlconsumerplugin"
    }

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

**Example Request (Python):**

.. code-block:: python

    payload = {
        "topic": "raw-sensor-data",
        "timestamp": "2026-03-01T21:54:00Z",
        "sensor_id": "SENSOR_123",
        "temperature": 72.5
    }
    response = requests.post("http://localhost:5000/jsondataline", json=payload)

**Example Request (JavaScript):**

.. code-block:: javascript

    const payload = {
        topic: 'raw-sensor-data',
        timestamp: '2026-03-01T21:54:00Z',
        sensor_id: 'SENSOR_123',
        temperature: 72.5
    };
    fetch('http://localhost:5000/jsondataline', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(payload)
    });

**Response:** ``"ok"``

**Example Request (React):**

.. code-block:: jsx

    function SendDataLine() {
        const sendData = async () => {
            const payload = {
                topic: 'raw-sensor-data',
                timestamp: '2026-03-01T22:17:00Z',
                sensor_id: 'SENSOR_123',
                temperature: 72.5
            };
            
            await fetch('http://localhost:5000/jsondataline', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
        };

        return <button onClick={sendData}>Send Sensor Data</button>;
    }

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

**Example Request (Python):**

.. code-block:: python

    payload = {
        "topic": "raw-sensor-data",
        "data": [  # Note: actual body should be array directly
            {"timestamp": "2026-03-01T21:54:00Z", "sensor_id": "SENSOR_123", "temperature": 72.5},
            {"timestamp": "2026-03-01T21:55:00Z", "sensor_id": "SENSOR_124", "temperature": 73.2}
        ]
    }
    response = requests.post("http://localhost:5000/jsondataarray", json=payload)

**Example Request (JavaScript):**

.. code-block:: javascript

    const dataArray = [
        {topic: 'raw-sensor-data', timestamp: '2026-03-01T21:54:00Z', sensor_id: 'SENSOR_123', temperature: 72.5},
        {topic: 'raw-sensor-data', timestamp: '2026-03-01T21:55:00Z', sensor_id: 'SENSOR_124', temperature: 73.2}
    ];
    fetch('http://localhost:5000/jsondataarray', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dataArray)
    });

**Response:** ``"ok"``

**Example Request (React):**

.. code-block:: jsx

    function SendDataArray() {
        const dataArray = [
            {
                topic: 'raw-sensor-data',
                timestamp: '2026-03-01T22:17:00Z',
                sensor_id: 'SENSOR_123',
                temperature: 72.5
            },
            {
                topic: 'raw-sensor-data',
                timestamp: '2026-03-01T22:18:00Z',
                sensor_id: 'SENSOR_124',
                temperature: 73.2
            }
        ];
        
        const sendBatch = async () => {
            await fetch('http://localhost:5000/jsondataarray', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(dataArray)
            });
        };

        return <button onClick={sendBatch}>Send Batch Data</button>;
    }
