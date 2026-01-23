from typing import overload
from enum import IntEnum
import typing

import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Brokerages.Backtesting
import QuantConnect.Brokerages.Paper
import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Securities
import System.Collections.Generic


class PaperBrokerage(QuantConnect.Brokerages.Backtesting.BacktestingBrokerage):
    """Paper Trading Brokerage"""

    @property
    def concurrency_enabled(self) -> bool:
        """Enables or disables concurrent processing of messages to and from the brokerage."""
        ...

    @concurrency_enabled.setter
    def concurrency_enabled(self, value: bool) -> None:
        ...

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Creates a new PaperBrokerage
        
        :param algorithm: The algorithm under analysis
        :param job: The job packet
        """
        ...

    def get_account_holdings(self) -> typing.List[QuantConnect.Holding]:
        """
        Gets all holdings for the account
        
        :returns: The current holdings from the account.
        """
        ...

    def get_cash_balance(self) -> typing.List[QuantConnect.Securities.CashAmount]:
        """
        Gets the current cash balance for each currency held in the brokerage account
        
        :returns: The current cash balance for each currency available for trading.
        """
        ...

    def scan(self) -> None:
        """
        Scans all the outstanding orders and applies the algorithm model fills to generate the order events.
        This override adds dividend detection and application
        """
        ...


class PaperBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """The factory type for the PaperBrokerage"""

    @property
    def brokerage_data(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Gets the brokerage data required to run the IB brokerage from configuration"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the PaperBrokerageFactory class"""
        ...

    def create_brokerage(self, job: QuantConnect.Packets.LiveNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Interfaces.IBrokerage:
        """
        Creates a new IBrokerage instance
        
        :param job: The job packet to create the brokerage for
        :param algorithm: The algorithm instance
        :returns: A new brokerage instance.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def get_brokerage_model(self, order_provider: QuantConnect.Securities.IOrderProvider) -> QuantConnect.Brokerages.IBrokerageModel:
        """
        Gets a new instance of the InteractiveBrokersBrokerageModel
        
        :param order_provider: The order provider
        """
        ...


