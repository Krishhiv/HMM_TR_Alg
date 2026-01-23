from typing import overload
from enum import IntEnum
import datetime
import typing

import Common.Data.Consolidators
import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Securities


class DollarVolumeRenkoConsolidator(QuantConnect.Data.Consolidators.VolumeRenkoConsolidator):
    """This class has no documentation."""

    def __init__(self, bar_size: float) -> None:
        ...

    def adjust_volume(self, volume: float, price: float) -> float:
        ...


class SessionConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect.Data.BaseData, QuantConnect.Data.Market.SessionBar]):
    """This class has no documentation."""

    def __init__(self, exchange_hours: QuantConnect.Securities.SecurityExchangeHours, source_tick_type: QuantConnect.TickType, symbol: typing.Union[QuantConnect.Symbol, str, QuantConnect.Data.Market.BaseContract, QuantConnect.Securities.Security]) -> None:
        ...

    def aggregate_bar(self, working_bar: QuantConnect.Data.Market.SessionBar, data: QuantConnect.Data.BaseData) -> None:
        ...

    def on_data_consolidated(self, e: QuantConnect.Data.Market.SessionBar) -> None:
        ...

    def reset(self) -> None:
        ...

    def reset_working_bar(self) -> None:
        ...

    def validate_and_scan(self, current_local_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...


