from typing import overload
from enum import IntEnum
import QuantConnect.Brokerages.CrossZero
import QuantConnect.Orders
import System


class CrossZeroFirstOrderRequest(System.Object):
    """Represents a first request to cross zero order."""

    @property
    def lean_order(self) -> QuantConnect.Orders.Order:
        """Gets the original lean order."""
        ...

    @property
    def order_type(self) -> QuantConnect.Orders.OrderType:
        """Gets the type of the order."""
        ...

    @property
    def order_quantity(self) -> float:
        """Gets the quantity of the order."""
        ...

    @property
    def absolute_order_quantity(self) -> float:
        """Gets the absolute quantity of the order."""
        ...

    @property
    def order_quantity_holding(self) -> float:
        """Gets the current holding quantity of the order's symbol."""
        ...

    @property
    def order_position(self) -> QuantConnect.Orders.OrderPosition:
        """Gets the position of the order."""
        ...

    def __init__(self, lean_order: QuantConnect.Orders.Order, order_type: QuantConnect.Orders.OrderType, order_quantity: float, order_quantity_holding: float, order_position: QuantConnect.Orders.OrderPosition) -> None:
        """
        Initializes a new instance of the CrossZeroFirstOrderRequest struct.
        
        :param lean_order: The lean order.
        :param order_type: The type of the order.
        :param order_quantity: The quantity of the order.
        :param order_quantity_holding: The current holding quantity of the order's symbol.
        :param order_position: The position of the order, which depends on the order_quantity_holding.
        """
        ...


class CrossZeroSecondOrderRequest(QuantConnect.Brokerages.CrossZero.CrossZeroFirstOrderRequest):
    """Represents a second request to cross zero order."""

    @property
    def first_part_cross_zero_order(self) -> QuantConnect.Brokerages.CrossZero.CrossZeroFirstOrderRequest:
        """Gets or sets the first part of CrossZeroOrder."""
        ...

    def __init__(self, lean_order: QuantConnect.Orders.Order, order_type: QuantConnect.Orders.OrderType, order_quantity: float, order_quantity_holding: float, order_position: QuantConnect.Orders.OrderPosition, cross_zero_first_order: QuantConnect.Brokerages.CrossZero.CrossZeroFirstOrderRequest) -> None:
        """
        Initializes a new instance of the CrossZeroFirstOrderRequest struct.
        
        :param lean_order: The lean order.
        :param order_type: The type of the order.
        :param order_quantity: The quantity of the order.
        :param order_quantity_holding: The current holding quantity of the order's symbol.
        :param order_position: The position of the order, which depends on the order_quantity_holding.
        :param cross_zero_first_order: The first part of the cross zero order.
        """
        ...


class CrossZeroOrderResponse:
    """Represents a response for a cross zero order request."""

    @property
    def brokerage_order_id(self) -> str:
        """Gets the brokerage order ID."""
        ...

    @property
    def is_order_placed_successfully(self) -> bool:
        """Gets a value indicating whether the order was placed successfully."""
        ...

    @property
    def message(self) -> str:
        """Gets the message of the order."""
        ...

    def __init__(self, brokerage_order_id: str, is_order_placed_successfully: bool, message: str = ...) -> None:
        """
        Initializes a new instance of the CrossZeroOrderResponse struct.
        
        :param brokerage_order_id: The brokerage order ID.
        :param is_order_placed_successfully: if set to true <is order placed successfully>.
        :param message: The message of the order. This parameter is optional and defaults to null.
        """
        ...


