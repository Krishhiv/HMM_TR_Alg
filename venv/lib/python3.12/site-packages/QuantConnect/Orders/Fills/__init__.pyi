from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fills
import QuantConnect.Python
import QuantConnect.Securities
import System
import System.Collections.Generic


class Fill(System.Object, typing.Iterable[QuantConnect.Orders.OrderEvent]):
    """Defines a possible result for IfillModel.fill for a single order"""

    @overload
    def __init__(self, order_events: typing.List[QuantConnect.Orders.OrderEvent]) -> None:
        """
        Creates a new Fill instance
        
        :param order_events: The fill order events
        """
        ...

    @overload
    def __init__(self, order_event: QuantConnect.Orders.OrderEvent) -> None:
        """
        Creates a new Fill instance
        
        :param order_event: The fill order event
        """
        ...

    def __iter__(self) -> typing.Iterator[QuantConnect.Orders.OrderEvent]:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Orders.OrderEvent]:
        """Returns the order events enumerator"""
        ...


class FillModelParameters(System.Object):
    """Defines the parameters for the IFillModel method"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    @property
    def config_provider(self) -> QuantConnect.Interfaces.ISubscriptionDataConfigProvider:
        """Gets the SubscriptionDataConfig provider"""
        ...

    @property
    def stale_price_time_span(self) -> datetime.timedelta:
        """Gets the minimum time span elapsed to consider a market fill price as stale (defaults to one hour)"""
        ...

    @property
    def securities_for_orders(self) -> System.Collections.Generic.Dictionary[QuantConnect.Orders.Order, QuantConnect.Securities.Security]:
        """Gets the collection of securities by order"""
        ...

    @property
    def on_order_updated(self) -> typing.Callable[[QuantConnect.Orders.Order], typing.Any]:
        """Callback to notify when an order is updated by the fill model"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, config_provider: QuantConnect.Interfaces.ISubscriptionDataConfigProvider, stale_price_time_span: datetime.timedelta, securities_for_orders: System.Collections.Generic.Dictionary[QuantConnect.Orders.Order, QuantConnect.Securities.Security], on_order_updated: typing.Callable[[QuantConnect.Orders.Order], typing.Any] = None) -> None:
        """
        Creates a new instance
        
        :param security: Security asset we're filling
        :param order: Order packet to model
        :param config_provider: The ISubscriptionDataConfigProvider to use
        :param stale_price_time_span: The minimum time span elapsed to consider a fill price as stale
        :param securities_for_orders: Collection of securities for each order
        """
        ...


class IFillModel(metaclass=abc.ABCMeta):
    """Represents a model that simulates order fill events"""

    def fill(self, parameters: QuantConnect.Orders.Fills.FillModelParameters) -> QuantConnect.Orders.Fills.Fill:
        """
        Return an order event with the fill details
        
        :param parameters: A FillModelParameters object containing the security and order
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...


class Prices(System.Object):
    """Prices class used by IFillModels"""

    @property
    def end_time(self) -> datetime.datetime:
        """End time for these prices"""
        ...

    @property
    def current(self) -> float:
        """Current price"""
        ...

    @property
    def open(self) -> float:
        """Open price"""
        ...

    @property
    def high(self) -> float:
        """High price"""
        ...

    @property
    def low(self) -> float:
        """Low price"""
        ...

    @property
    def close(self) -> float:
        """Closing price"""
        ...

    @overload
    def __init__(self, bar: QuantConnect.Data.Market.IBaseDataBar) -> None:
        """
        Create an instance of Prices class with a data bar
        
        :param bar: Data bar to use for prices
        """
        ...

    @overload
    def __init__(self, end_time: typing.Union[datetime.datetime, datetime.date], bar: QuantConnect.Data.Market.IBar) -> None:
        """
        Create an instance of Prices class with a data bar and end time
        
        :param end_time: The end time for these prices
        :param bar: Data bar to use for prices
        """
        ...

    @overload
    def __init__(self, end_time: typing.Union[datetime.datetime, datetime.date], current: float, open: float, high: float, low: float, close: float) -> None:
        """
        Create a instance of the Prices class with specific values for all prices
        
        :param end_time: The end time for these prices
        :param current: Current price
        :param open: Open price
        :param high: High price
        :param low: Low price
        :param close: Close price
        """
        ...


class FillModel(System.Object, QuantConnect.Orders.Fills.IFillModel):
    """Provides a base class for all fill models"""

    @property
    def parameters(self) -> QuantConnect.Orders.Fills.FillModelParameters:
        """
        The parameters instance to be used by the different XxxxFill() implementations
        
        
        This codeEntityType is protected.
        """
        ...

    @parameters.setter
    def parameters(self, value: QuantConnect.Orders.Fills.FillModelParameters) -> None:
        ...

    @property
    def python_wrapper(self) -> QuantConnect.Python.FillModelPythonWrapper:
        """
        This is required due to a limitation in PythonNet to resolved overriden methods.
        When Python calls a C# method that calls a method that's overriden in python it won't
        run the python implementation unless the call is performed through python too.
        
        
        This codeEntityType is protected.
        """
        ...

    @python_wrapper.setter
    def python_wrapper(self, value: QuantConnect.Python.FillModelPythonWrapper) -> None:
        ...

    def combo_leg_limit_fill(self, order: QuantConnect.Orders.Order, parameters: QuantConnect.Orders.Fills.FillModelParameters) -> typing.List[QuantConnect.Orders.OrderEvent]:
        """
        Default combo limit fill model for the base security class. Fills at the limit price for each leg
        
        :param order: Order to fill
        :param parameters: Fill parameters for the order
        :returns: Order fill information detailing the average price and quantity filled for each leg. If any of the fills fails, none of the orders will be filled and the returned list will be empty.
        """
        ...

    def combo_limit_fill(self, order: QuantConnect.Orders.Order, parameters: QuantConnect.Orders.Fills.FillModelParameters) -> typing.List[QuantConnect.Orders.OrderEvent]:
        """
        Default combo limit fill model for the base security class. Fills at the sum of prices for the assets of every leg.
        
        :param order: Order to fill
        :param parameters: Fill parameters for the order
        :returns: Order fill information detailing the average price and quantity filled for each leg. If any of the fills fails, none of the orders will be filled and the returned list will be empty.
        """
        ...

    def combo_market_fill(self, order: QuantConnect.Orders.Order, parameters: QuantConnect.Orders.Fills.FillModelParameters) -> typing.List[QuantConnect.Orders.OrderEvent]:
        """
        Default combo market fill model for the base security class. Fills at the last traded price for each leg.
        
        :param order: Order to fill
        :param parameters: Fill parameters for the order
        :returns: Order fill information detailing the average price and quantity filled for each leg. If any of the fills fails, none of the orders will be filled and the returned list will be empty.
        """
        ...

    def fill(self, parameters: QuantConnect.Orders.Fills.FillModelParameters) -> QuantConnect.Orders.Fills.Fill:
        """
        Return an order event with the fill details
        
        :param parameters: A FillModelParameters object containing the security and order
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def get_prices(self, asset: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Orders.Fills.Prices:
        """
        Get the minimum and maximum price for this security in the last bar:
        
        
        This codeEntityType is protected.
        
        :param asset: Security asset we're checking
        :param direction: The order direction, decides whether to pick bid or ask
        """
        ...

    def get_prices_checking_python_wrapper(self, asset: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Orders.Fills.Prices:
        """
        This is required due to a limitation in PythonNet to resolved
        overriden methods. get_prices
        
        This codeEntityType is protected.
        """
        ...

    def get_subscribed_types(self, asset: QuantConnect.Securities.Security) -> System.Collections.Generic.HashSet[typing.Type]:
        """
        Get data types the Security is subscribed to
        
        
        This codeEntityType is protected.
        
        :param asset: Security which has subscribed data types
        """
        ...

    def is_exchange_open(self, asset: QuantConnect.Securities.Security, is_extended_market_hours: bool) -> bool:
        """
        Determines if the exchange is open using the current time of the asset
        
        
        This codeEntityType is protected.
        """
        ...

    def limit_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.LimitOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default limit order fill model in the base security class.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def limit_if_touched_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.LimitIfTouchedOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default limit if touched fill model implementation in base class security. (Limit If Touched Order Type)
        
        :param asset: 
        :param order: 
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def market_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default market fill model for the base security class. Fills at the last traded price.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def market_on_close_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnCloseOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Market on Close Fill Model. Return an order event with the fill details
        
        :param asset: Asset we're trading with this order
        :param order: Order to be filled
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def market_on_open_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnOpenOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Market on Open Fill Model. Return an order event with the fill details
        
        :param asset: Asset we're trading with this order
        :param order: Order to be filled
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def set_python_wrapper(self, python_wrapper: QuantConnect.Python.FillModelPythonWrapper) -> None:
        """Used to set the FillModelPythonWrapper instance if any"""
        ...

    def stop_limit_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopLimitOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default stop limit fill model implementation in base class security. (Stop Limit Order Type)
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def stop_market_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopMarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default stop fill model implementation in base class security. (Stop Market Order Type)
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def trailing_stop_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.TrailingStopOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default trailing stop fill model implementation in base class security. (Trailing Stop Order Type)
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...


class EquityFillModel(QuantConnect.Orders.Fills.FillModel):
    """Represents the fill model used to simulate order fills for equities"""

    def get_prices(self, asset: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Orders.Fills.Prices:
        """
        Get the minimum and maximum price for this security in the last bar:
        
        
        This codeEntityType is protected.
        
        :param asset: Security asset we're checking
        :param direction: The order direction, decides whether to pick bid or ask
        """
        ...

    def get_prices_checking_python_wrapper(self, asset: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Orders.Fills.Prices:
        """
        This is required due to a limitation in PythonNet to resolved
        overriden methods. get_prices
        
        This codeEntityType is protected.
        """
        ...

    def get_subscribed_types(self, asset: QuantConnect.Securities.Security) -> System.Collections.Generic.HashSet[typing.Type]:
        """
        Get data types the Security is subscribed to
        
        
        This codeEntityType is protected.
        
        :param asset: Security which has subscribed data types
        """
        ...

    def limit_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.LimitOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Limit fill model implementation for Equity.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def limit_if_touched_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.LimitIfTouchedOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default limit if touched fill model implementation in base class security.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def market_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default market fill model for the base security class. Fills at the last traded price.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def market_on_close_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnCloseOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Market on Close Fill Model. Return an order event with the fill details
        
        :param asset: Asset we're trading with this order
        :param order: Order to be filled
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def market_on_open_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnOpenOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Market on Open Fill Model. Return an order event with the fill details
        
        :param asset: Asset we're trading with this order
        :param order: Order to be filled
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def stop_limit_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopLimitOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default stop limit fill model implementation in base class security. (Stop Limit Order Type)
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def stop_market_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopMarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Stop fill model implementation for Equity.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...


class ImmediateFillModel(QuantConnect.Orders.Fills.FillModel):
    """Represents the default fill model used to simulate order fills"""


class FutureFillModel(QuantConnect.Orders.Fills.ImmediateFillModel):
    """Represents the fill model used to simulate order fills for futures"""

    def market_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Default market fill model for the base security class. Fills at the last traded price.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def stop_market_fill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopMarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Stop fill model implementation for Future.
        
        :param asset: Security asset we're filling
        :param order: Order packet to model
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...


class FutureOptionFillModel(QuantConnect.Orders.Fills.FutureFillModel):
    """Represents the default fill model used to simulate order fills for future options"""


class LatestPriceFillModel(QuantConnect.Orders.Fills.ImmediateFillModel):
    """
    This fill model is provided for cases where the trade/quote distinction should be
    ignored and the fill price should be determined from the latest pricing information.
    """

    def get_prices(self, asset: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Orders.Fills.Prices:
        """
        Get the minimum and maximum price for this security in the last bar
        Ignore the Trade/Quote distinction - fill with the latest pricing information
        
        
        This codeEntityType is protected.
        
        :param asset: Security asset we're checking
        :param direction: The order direction, decides whether to pick bid or ask
        """
        ...


