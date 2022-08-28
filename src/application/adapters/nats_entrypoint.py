import asyncio
import nats
import json

from nats import NATS
from nats.aio.subscription import Subscription
from typing import AsyncContextManager, AsyncIterator
from contextlib import asynccontextmanager
from src.application.ports.entrypoint import Entrypoint
from src.application.adapters.dto.features import MessageRequestDTO
from src.core.ports.prediction_request_handler_port import PredictionRequestHandlerPort


class NatsEntrypoint(Entrypoint):
    def __init__(
        self,
        prediction_request_handler: PredictionRequestHandlerPort,
        nats_server_url: str,
        prediction_request_channel: str,
        prediction_response_channel: str,
    ):
        self.__nats_server_url = nats_server_url
        self.__prediction_request_channel = prediction_request_channel
        self.__prediction_response_channel = prediction_response_channel
        self.__prediction_request_handler = prediction_request_handler

    @asynccontextmanager
    async def __nats_client(self) -> AsyncContextManager[NATS]:
        try:
            nats_connection = await nats.connect(self.__nats_server_url)
            yield nats_connection
        finally:
            await nats_connection.drain()

    async def __prediction_message_subscriber(self):
        async with self.__nats_client() as nats_connection:
            subscription: Subscription = await nats_connection.subscribe(
                self.__prediction_request_channel
            )

            try:
                async for message in subscription.messages:
                    prediction = self.__predict(message.data.decode())
                    encoded_prediction = json.dumps(prediction).encode("utf-8")

                    await nats_connection.publish(
                        self.__prediction_response_channel, encoded_prediction
                    )
            except Exception as error:
                pass

    def __predict(self, feature_request: MessageRequestDTO):
        return self.__prediction_request_handler.handle(feature_request.features)

    def run(self):
        asyncio.run(self.__prediction_message_subscriber())

        return self
