Sidomo
======

Simple Docker Module: If you can get your software to work in a docker container, then this module will make it work in Python.
-------------------------------------------------------------------------------------------------------------------------------

How to install:
^^^^^^^^^^^^^^^

.. code:: bash

    pip install -e git+https://github.com/deepgram/sidomo.git#egg=sidomo

How to use:
^^^^^^^^^^^

.. code:: python

    from sidomo import Container

    with Container('ubuntu') as c:
        for output_line in c.run('echo hello world'):
            print(output_line)

Examples:
^^^^^^^^^

-  hello\_world.py is ‘Hello, World!’ as a module
-  ffmpeg.py fetches audio from a URL and transcodes it to WAV format

Ideas:
^^^^^^

-  Replace leaky glue code
-  Run Erlang from Python
-  Resurrect legacy software for use in a modern environment
-  Make a Python module more portable (the only dependency is Docker
   itself)

Issues:
^^^^^^^

-  Display better error message when Docker isn't installed

Example

.. code:: bash

    (venv) smollah:examples smollah$ python ffmpeg.py
    I'm gonna transcode an audio file and only print the stderr.
    Traceback (most recent call last):
      File "ffmpeg.py", line 26, in <module>
        for line in transcode_file(url):
      File "ffmpeg.py", line 10, in transcode_file
        stdout=False
      File "/Users/smollah/workspace/sidomo/examples/venv/src/sidomo/sidomo/sidomo.py", line 32, in __enter__
        stdin_open=True
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/api/container.py", line 119, in create_container
        return self.create_container_from_config(config, name)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/api/container.py", line 129, in create_container_from_config
        res = self._post_json(u, data=config, params=params)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/client.py", line 170, in _post_json
        return self._post(url, data=json.dumps(data2), **kwargs)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/utils/decorators.py", line 47, in inner
        return f(self, *args, **kwargs)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/client.py", line 108, in _post
        return self.post(url, **self._set_request_timeout(kwargs))
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/requests/sessions.py", line 511, in post
        return self.request('POST', url, data=data, json=json, **kwargs)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/requests/sessions.py", line 468, in request
        resp = self.send(prep, **send_kwargs)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/requests/sessions.py", line 576, in send
        r = adapter.send(request, **kwargs)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/requests/adapters.py", line 426, in send
        raise ConnectionError(err, request=request)
    requests.exceptions.ConnectionError: ('Connection aborted.', error(2, 'No such file or directory'))

-  Don't error out when the image doesn't exist -- auto-pull from Docker Hub maybe?

Example

.. code:: bash

    (venv) smollah:examples smollah$ python ffmpeg.py
    I'm gonna transcode an audio file and only print the stderr.
    Traceback (most recent call last):
      File "ffmpeg.py", line 26, in <module>
        for line in transcode_file(url):
      File "ffmpeg.py", line 10, in transcode_file
        stdout=False
      File "/Users/smollah/workspace/sidomo/examples/venv/src/sidomo/sidomo/sidomo.py", line 32, in __enter__
        stdin_open=True
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/api/container.py", line 119, in create_container
        return self.create_container_from_config(config, name)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/api/container.py", line 130, in create_container_from_config
        return self._result(res, True)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/client.py", line 150, in _result
        self._raise_for_status(response)
      File "/Users/smollah/workspace/sidomo/examples/venv/lib/python2.7/site-packages/docker/client.py", line 145, in _raise_for_status
        raise errors.NotFound(e, response, explanation=explanation)
    docker.errors.NotFound: 404 Client Error: Not Found ("No such image: cellofellow/ffmpeg:latest")
