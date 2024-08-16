TML and Generative AI
=================

TML solutions can be built to access GPT technology in real-time using the `MAADSTML python library <https://pypi.org/project/maadstml/>`_ functions:

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

   You should see the private GPT website below.

.. figure:: pgpt1.png

.. note::
   
   If you set WEB_CONCURRENCY greater than 1, you will need Qdrant Vector DB running (see below)


PrivateGPT Container With NO GPU
-----------------

.. note::

   If you do not have a Nvidia GPU you can use the docker container with NO GPU: 

   docker run -d -p 8001:8001 --env PORT=8001 --env GPU=0 --env CUDA_VISIBLE_DEVICES=0 maadsdocker/tml-privategpt-no-gpu-amd64


Accessing PrivateGPT With MAADSTML Python API
-----------------

Once you have the PrivateGPT container running you can access it using the maadstml API. Here is some sample Python code to access the privateGPT container:

.. note:

   Since PrivateGPT is compatible with REST API, you can use any programming language, and take advantage of free, and fast AI.

.. code-block::
   :emphasize-lines: 4,11,21,22,23,26

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
        message=sendpromptgpt(prompt,pgptip,pgptport) 

.. list-table::

   * - **Details of LLM Used in privateGPT Container**
   * - llm_load_print_meta: format = GGUF V2
   * - llm_load_print_meta: arch = llama
   * - llm_load_print_meta: vocab type = SPM
   * - llm_load_print_meta: n_vocab = 32000
   * - llm_load_print_meta: n_merges = 0
   * - llm_load_print_meta: n_ctx_train = 32768
   * - llm_load_print_meta: n_embd = 4096
   * - llm_load_print_meta: n_head = 32
   * - llm_load_print_meta: n_head_kv = 8
   * - llm_load_print_meta: n_layer = 32
   * - llm_load_print_meta: n_rot = 128
   * - llm_load_print_meta: n_gqa = 4
   * - llm_load_print_meta: f_norm_eps = 0.0e+00
   * - llm_load_print_meta: f_norm_rms_eps = 1.0e-05
   * - llm_load_print_meta: f_clamp_kqv = 0.0e+00
   * - llm_load_print_meta: f_max_alibi_bias = 0.0e+00
   * - llm_load_print_meta: n_ff = 14336
   * - llm_load_print_meta: rope scaling = linear
   * - llm_load_print_meta: freq_base_train = 10000.0
   * - llm_load_print_meta: freq_scale_train = 1
   * - llm_load_print_meta: n_yarn_orig_ctx = 32768
   * - llm_load_print_meta: rope_finetuned = unknown
   * - llm_load_print_meta: model type = 7B
   * - llm_load_print_meta: model ftype = mostly Q4_K - Medium
   * - llm_load_print_meta: model params = 7.24 B
   * - llm_load_print_meta: model size = 4.07 GiB (4.83 BPW)
   * - **llm_load_print_meta: general.name = mistralai_mistral-7b-instruct-v0.2**
   * - llm_load_print_meta: BOS token = 1 ''
   * - llm_load_print_meta: EOS token = 2 ''
   * - llm_load_print_meta: UNK token = 0 ''
   * - llm_load_print_meta: LF token = 13 '<0x0A>'
   * - llm_load_tensors: ggml ctx size = 0.11 MB
   * - llm_load_tensors: mem required = 4165.47 MB

Qdrant Vector Database
---------------------

The privateGPT is also integrated with `Qdrant Vector DB <https://qdrant.tech/>`_

.. code-block::

   docker run -d -p 6333:6333 -v $(pwd)/qdrant_storage:/qdrant/storage:z qdrant/qdrant
