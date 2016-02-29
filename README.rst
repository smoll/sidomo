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
-  ~~Don't error out when the image doesn't exist~~ auto-pulls from Docker Hub by default
-  Unable to `docker rmi` because stopped container locks it up. Consider doing `docker rm -f` via some kind of hard-cleanup `rm_f=True` flag?

Notes:
^^^^^^

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

.. code:: bash

    (venv) smollah:examples smollah$ docker rmi ade4121f1cb0
    Failed to remove image (ade4121f1cb0): Error response from daemon: conflict: unable to delete ade4121f1cb0 (must be forced) - image is being used by stopped container 13e4f8d65aee
    (venv) smollah:examples smollah$ docker rm -f 13e4f8d65aee
    13e4f8d65aee
    (venv) smollah:examples smollah$ docker rmi ade4121f1cb0
    Untagged: cellofellow/ffmpeg:latest
    Deleted: sha256:ade4121f1cb02c9f2066fa7de9f5dfdf92655daa54c79a38ec357f22458c4017
    Deleted: sha256:37c2673d91ba35e8407eea1a0052a8f3ec353ad4ff5f399225330b9bd0e19a92
    Deleted: sha256:4d2b1fe3e086b56b04c6735ed1528a46dbbcadc1e86660923f8c8e7aea81634a
    Deleted: sha256:89e71b1430d2d0cc25fce383739145ff2d1cb386e8cbd897a9ccb0f0a745e85b
    Deleted: sha256:32e86fbe8f1d7be575b30fd5e837643ad4d4a24bbcbc03f464983df0e2bdfc6c
    Deleted: sha256:9187644f6c65a4c7e142c2f2da7821b9dbfca5caba088ed1048146799e4b6d6b
    Deleted: sha256:dbae8a1b4cd7f25cb77e06df0591cd0fe9cb174062b48b52f7c77c83d73c036b
    Deleted: sha256:b0ff47601b4f0f34b9ba1adb3039c4dbd7829e2e5e839194d7144e326e13723d
    Deleted: sha256:12aaf55eee7e3800c31213ab9afc58ec1e256296acb3ff6943452440a4841bb1
    Deleted: sha256:8865f1cd2a437710c2df6cb5cd72948eab45ec8ba6ac9359a2fecd783057e28e
    Deleted: sha256:f5e633d8ba5995cf8ae5b75f2ecfbbfb69c84217486e6fd49e9fed2f059db4be
    Deleted: sha256:e484ff6705381eb89356f5fa5eb69bb51aaa6491106a6719ff62aa2a149f687c
    Deleted: sha256:78867582c2fd59ae096b53203c491f9b7231e4c1b522159222b1d9a7ca35d792
    Deleted: sha256:4a88531d8793568ecf7a781c1ba5246274f39080ce3914600eb6a638a153ed2c
