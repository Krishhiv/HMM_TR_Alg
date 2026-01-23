from typing import overload
from enum import IntEnum
import typing

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Queues
import System


class JobQueue(System.Object, QuantConnect.Interfaces.IJobQueueHandler):
    """Implementation of local/desktop job request:"""

    @property
    def language(self) -> QuantConnect.Language:
        """
        This property is protected for testing purposes
        
        
        This codeEntityType is protected.
        """
        ...

    def acknowledge_job(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Desktop/Local acknowledge the task processed. Nothing to do.
        
        :param job: 
        """
        ...

    @staticmethod
    def get_factory_from_data_queue_handler(data_queue_handler: str) -> QuantConnect.Interfaces.IBrokerageFactory:
        """
        Gets Brokerage Factory for provided IDQH
        
        :param data_queue_handler: 
        :returns: An Instance of Brokerage Factory if possible, otherwise null.
        """
        ...

    def initialize(self, api: QuantConnect.Interfaces.IApi, messaging_handler: QuantConnect.Interfaces.IMessagingHandler) -> None:
        """Initialize the job queue:"""
        ...

    def next_job(self, algorithm_path: typing.Optional[str]) -> typing.Tuple[QuantConnect.Packets.AlgorithmNodePacket, str]:
        """Desktop/Local Get Next Task - Get task from the Algorithm folder of VS Solution."""
        ...


