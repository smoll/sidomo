"""Manages the lifecycle of a docker container.

Use via the with statement:

with Container(some_image) as c:
    for line in c.run("some_command"):
        print line
"""
import docker


# sets the docker host from your environment variables
client = docker.Client(
    **docker.utils.kwargs_from_env(assert_hostname=False))


class Container:
    """Represents a single docker container on the host."""

    def __init__(self, image, memory_limit_gb=4, stderr=True, stdout=True):
        self.image = image
        self.memory_limit_bytes = int(memory_limit_gb * 1e9)
        self.stderr = stderr
        self.stdout = stdout

    def __enter__(self):
        """Power on."""
        self.container_id = client.create_container(
            image=self.image,
            host_config=client.create_host_config(
                mem_limit=self.memory_limit_bytes),
            stdin_open=True
        )['Id']

        client.start(self.container_id)

        return self

    def __exit__(self, type, value, traceback):
        """Power off."""
        client.stop(self.container_id)

    def run(self, command):
        """Just like 'docker run CMD'.

        This is a generator that yields lines of container output.
        """
        exec_id = client.exec_create(
            container=self.container_id,
            cmd=command,
            stdout=self.stdout,
            stderr=self.stderr
        )['Id']

        for line in client.exec_start(exec_id, stream=True):
            yield line
