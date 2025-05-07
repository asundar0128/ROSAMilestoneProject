import asyncio
from nats.aio.client import Client as NATS
from nats.js.api import StreamConfig
import os

# Environment defaults
generatedNATServer = os.getenv("NATS_URL", "nats://127.0.0.1:4222")
generatedDefaultSubject = os.getenv("NATS_SUBJECT", "rosa.agent")

class generatedNATSInterface:
    def __init__(self):
        self.nc = NATS()
        self.subject = generatedDefaultSubject

    async def connect(self):
        await self.nc.connect(servers=[generatedNATServer])
        print(f"[NATS] Connected to {generatedNATServer}")

    async def subscribe(self, generatedSubjectValue=None, generatedCallbackValue=None):
        generatedSubjectValue = generatedSubjectValue or self.subject
        if not generatedCallbackValue:
            generatedCallbackValue = self._default_callback
        await self.nc.subscribe(generatedSubjectValue, cb=generatedCallbackValue)
        print(f"[NATS] Subscribed to {subject}")

    async def publish(self, generatedMessage: str, generatedSubjectValue=None):
        generatedSubjectValue = generatedSubjectValue or self.subject
        await self.nc.publish(generatedSubjectValue, generatedMessage.encode())
        print(f"[NATS] Published to {generatedSubjectValue}: {generatedMessage}")

    async def _default_callback(self, messageValue):
        print(f"[NATS] Received [{messageValue.subject}]: {messageValue.data.decode()}")

    async def setup_jetstream(self, stream="rosa", subjects=["rosa.*"]):
        generatedJS = self.nc.jetstream()
        await generatedJS.add_stream(StreamConfig(name=stream, subjects=subjects))
        print(f"[NATS] JetStream stream '{stream}' added.")

    async def close(self):
        await self.nc.close()

# Standalone test
if __name__ == "__main__":
    async def test():
        generatedClientValue = generatedNATSInterface()
        await generatedClientValue.connect()
        await generatedClientValue.setup_jetstream()
        await generatedClientValue.subscribe("rosa.chat")
        await generatedClientValue.publish("Hello from NATS!", "rosa.chat")
        await asyncio.sleep(2)
        await generatedClientValue.close()

    asyncio.run(test())
