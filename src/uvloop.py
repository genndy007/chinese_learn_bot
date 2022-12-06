import asyncio
import sys

import uvloop


def run_uvloop(coro):
    if sys.version_info >= (3, 11):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(coro)
    else:
        uvloop.install()
        asyncio.run(coro)
