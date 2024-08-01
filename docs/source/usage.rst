TML Usage
=====

.. _installation:

Installation
------------
TML is comprised of 3 binaries:

1. Viper - source - sink binary for Apache Kafka
2. HPDE - AutoML binary for real-time data
3. Viperviz - Visualization binary for real-time dashboards

TML Python Library:

4. MAADSTML Python library : API to build TML solutions that connect to the Viper binary

The fastest way to use TML for your real-time data is to use the TML Studio container located here: [Docker Hub]

Details on how to quickly use the TML studio can be seen in the Youtube video here: [Youtube]


For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

