TML and Generative AI
=================

TML solutions can be built to access GPT technology in real-time using the MAADSTML python library functions:

.. list-table::

   * - MAADSTML Python Function
     - Description
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

Qdrant Vector Database
---------------------
