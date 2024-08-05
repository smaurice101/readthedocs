TML and Generative AI
=================

TML solutions can be built to access GPT technology in real-time using the MAADSTML python library functions:

.. list-table::

   * - **MAADSTML Python Function**
     - **Description**
   * - pgptingestdocs
     - Set Context for PrivateGPT by ingesting PDFs or text documents. All responses will then use these documents for context.
   * - pgptgetingestedembeddings
     - After documents are ingested, you can retrieve the embeddings for the ingested documents. These embeddings allow you to filter the documents for specific 
       context.
   * - pgptchat
     - Send any prompt to privateGPT (with or without context) and get back a response.
   * - pgptdeleteembeddings
     - Delete embeddings.
   * - pgpthealth
     - Check the health of the privateGPT http server.

Private GPT Container
--------------------

The privateGPT container can be found on Docker hub.  The container will require a NVIDIA GPU.

.. code-block::

   docker pull maadsdocker/tml-privategpt-with-gpu-nvidia-amd64

.. code-block::

   docker run -d -p 8001:8001 --gpus all --net=host --env PORT=8001 --env GPU=1 --env WEB_CONCURRENCY=1 --env COLLECTION=tml-cisco --env CUDA_VISIBLE_DEVICES=0 
   maadsdocker/tml-privategpt-with-gpu-nvidia-amd64

.. important::

   To check if privateGPT is running enter this in your browser: http://localhost:8001

   If you set WEB_CONCURRENCY greater than 1, you will need Qdrant Vector DB running (see below)

Here is some sample code to access the privateGPT container using the maadstml API:

.. code-block::
   :emphasize-lines: 3,10,20,21,22,25

   import maadstml
   import json

   def sendpromptgpt(prompt,pgptip,pgptport):
     pgptendpoint="/v1/completions"
     includesources=False
     docfilter=""
     context=False

     try:
       response=maadstml.pgptchat(prompt,context,docfilter,pgptport,includesources,pgptip,pgptendpoint)
       jb=json.loads(response)
       response=jb['choices'][0]['message']['content']
      
     except Exception as e:
      print("ERROR: connecting to PrivateGPT=",e)
      return ""

     return response

   def setupprompt():
        pgptip="http://127.0.0.1"
        pgptport="8001"

        prompt="Who is the prime minister of Canada?"
        message=sendpromptgpt(prompt,pgptip,pgptport) #"content=[TextBlock(text=yeah monitortype='text')" #


Qdrant Vector Database
---------------------

The privateGPT is also integrated with `Qdrant Vector DB <https://qdrant.tech/>`_

.. code-block::

   docker run -d -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage:z qdrant/qdrant
