.. _Creating a Task on the Open edX Analytics Developer Stack:

#########################################################
Creating a Task on the Open edX Analytics Developer Stack
#########################################################

This section describes how to create a new task on the Open edX Analytics developer
stack (analytics devstack).

.. contents::
   :local:
   :depth: 1

*******************
Example: Word Count
*******************

#. Create a new Python module for your task.

   .. code-block:: bash

     $ vagrant ssh
     $ cd /edx/app/analytics_pipeline/analytics_pipeline/
     $ touch edx/analytics/tasks/word_count.py

#. Copy the following code into ``edx/analytics/tasks/word_count.py``.

   .. code-block:: python

     import luigi
     from edx.analytics.tasks.url import get_target_from_url, ExternalURL
     from edx.analytics.tasks.mapreduce import MapReduceJobTask
     

     class WordCountTask(MapReduceJobTask):
     
        input_url = luigi.Parameter()
        output_url = luigi.Parameter()
     
        def requires(self):
            return ExternalURL(self.input_url)

        def mapper(self, line):
            for word in line.split(' '):
                yield (word, 1)

        def reducer(self, key, values):
            yield key, sum(values)
     
        def output(self):
            return get_target_from_url(self.output_url)

#. Add the following line to the ``edx.analytics.tasks`` section of ``setup.cfg``:

   .. code-block:: text

     word-count = edx.analytics.tasks.word_count:WordCountTask

   .. note::

        Modifying setup.cfg is only necessary when you are adding a new Python
        module to the project. If you add a task to an existing module, it is
        not necessary to explicitly list it in the entry points.

#. Update the cached entry points in the virtual environment.

   .. code-block:: bash

     $ source ../venvs/analytics_pipeline/bin/activate
     $ make develop-local

#. Switch to the hadoop user.

   .. code-block:: bash

     $ sudo su hadoop
     $ source ../venvs/analytics_pipeline/bin/activate

#. Create a test input file.

   .. code-block:: bash

     $ echo "this test is a test" | hdfs dfs -put - /tmp/word_count/input.txt

#. Run the word count task.

   .. code-block:: bash

     $ export LUIGI_CONFIG_PATH="$PWD/config/devstack.cfg"
     $ launch-task WordCountTask --local-scheduler --input-url hdfs://localhost:9000/tmp/word_count/input.txt --output-url hdfs://localhost:9000/tmp/word_count/output/

#. View the output.

   .. code-block:: text

     $ hdfs dfs -cat hdfs://localhost:9000/tmp/word_count/output/*
     is	1
     this	1
     a	1
     test	2

.. include:: ../../../../links/links.rst

