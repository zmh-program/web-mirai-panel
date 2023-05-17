from subprocess import Popen, PIPE, STDOUT
from typing import Generator

class CommandExecutor:
    def __init__(self, command: str):
        self.command = command
        self.process = None

    def start(self) -> Generator[str, None, None]:
        self.process = Popen(self.command, stdout=PIPE, stderr=STDOUT, shell=True, text=True, bufsize=1)
        for output in self._execute():
            yield output

    def _execute(self) -> Generator[str, None, None]:
        for line in self.process.stdout:
            yield line.strip()

        self.process.stdout.close()
        self.process.wait()

    def reset(self):
        if self.process is not None:
            self.process.terminate()
            self.process.wait()
            self.process = None

executor = CommandExecutor('')