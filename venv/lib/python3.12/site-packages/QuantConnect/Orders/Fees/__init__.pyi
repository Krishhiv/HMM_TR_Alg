from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Securities
import System


class OrderFee(System.Object):
    """Defines the result for IFeeModel.get_order_fee"""

    @property
    def value(self) -> QuantConnect.Securities.CashAmount:
        """Gets the order fee"""
        ...

    @value.setter
    def value(self, value: QuantConnect.Securities.CashAmount) -> None:
        ...

    ZERO: QuantConnect.Orders.Fees.OrderFee = ...
    """Gets an instance of OrderFee that represents zero."""

    def __init__(self, order_fee: QuantConnect.Securities.CashAmount) -> None:
        """
        Initializes a new instance of the OrderFee class
        
        :param order_fee: The order fee
        """
        ...

    def apply_to_portfolio(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Applies the order fee to the given portfolio
        
        :param portfolio: The portfolio instance
        :param fill: The order fill event
        """
        ...

    def to_string(self) -> str:
        """This is for backward compatibility with old 'decimal' order fee"""
        ...


class ModifiedFillQuantityOrderFee(QuantConnect.Orders.Fees.OrderFee):
    """
    An order fee where the fee quantity has already been subtracted from the filled quantity so instead we subtracted
    from the quote currency when applied to the portfolio
    """

    def __init__(self, order_fee: QuantConnect.Securities.CashAmount, quote_currency: str, contract_multiplier: float) -> None:
        """
        Initializes a new instance of the ModifiedFillQuantityOrderFee class
        
        :param order_fee: The order fee
        :param quote_currency: The associated security quote currency
        :param contract_multiplier: The associated security contract multiplier
        """
        ...

    def apply_to_portfolio(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Applies the order fee to the given portfolio
        
        :param portfolio: The portfolio instance
        :param fill: The order fill event
        """
        ...


class OrderFeeParameters(System.Object):
    """Defines the parameters for IFeeModel.get_order_fee"""

    @property
    def security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the OrderFeeParameters class
        
        :param security: The security
        :param order: The order
        """
        ...


class IFeeModel(metaclass=abc.ABCMeta):
    """Represents a model the simulates order fees"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class IndiaFeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def brokerage_multiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @brokerage_multiplier.setter
    def brokerage_multiplier(self, value: float) -> None:
        ...

    @property
    def max_brokerage(self) -> float:
        """
        Maximum brokerage per order
        
        
        This codeEntityType is protected.
        """
        ...

    @max_brokerage.setter
    def max_brokerage(self, value: float) -> None:
        ...

    @property
    def securities_transaction_tax_total_multiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @securities_transaction_tax_total_multiplier.setter
    def securities_transaction_tax_total_multiplier(self, value: float) -> None:
        ...

    @property
    def exchange_transaction_charge_multiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @exchange_transaction_charge_multiplier.setter
    def exchange_transaction_charge_multiplier(self, value: float) -> None:
        ...

    @property
    def state_tax_multiplier(self) -> float:
        """
        State Tax calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @state_tax_multiplier.setter
    def state_tax_multiplier(self, value: float) -> None:
        ...

    @property
    def sebi_charges_multiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @sebi_charges_multiplier.setter
    def sebi_charges_multiplier(self, value: float) -> None:
        ...

    @property
    def stamp_charges_multiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @stamp_charges_multiplier.setter
    def stamp_charges_multiplier(self, value: float) -> None:
        ...

    @property
    def is_stamp_charges_from_order_value(self) -> bool:
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        
        This codeEntityType is protected.
        """
        ...

    @is_stamp_charges_from_order_value.setter
    def is_stamp_charges_from_order_value(self, value: bool) -> None:
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        """
        ...


class ZerodhaFeeModel(QuantConnect.Orders.Fees.IndiaFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def brokerage_multiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def max_brokerage(self) -> float:
        """
        Maximum brokerage per order
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def securities_transaction_tax_total_multiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def exchange_transaction_charge_multiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def state_tax_multiplier(self) -> float:
        """
        State Tax calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def sebi_charges_multiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def stamp_charges_multiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def is_stamp_charges_from_order_value(self) -> bool:
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        
        This codeEntityType is protected.
        """
        ...


class FeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Base class for any order fee model"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class KrakenFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Kraken order fees"""

    MAKER_TIER_1_CRYPTO_FEE: float = 0.0016
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#kraken-pro
    """

    TAKER_TIER_1_CRYPTO_FEE: float = 0.0026
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#kraken-pro
    """

    TIER_1_FX_FEE: float = 0.002
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#stablecoin-fx-pairs
    """

    @property
    def fx_stablecoin_list(self) -> typing.List[str]:
        """Fiats and stablecoins list that have own fee."""
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order.
        If sell - fees in base currency
        If buy - fees in quote currency
        It can be defined manually in KrakenOrderProperties
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The fee of the order.
        """
        ...


class AlphaStreamsFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models order fees that alpha stream clients pay/receive"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class SamcoFeeModel(QuantConnect.Orders.Fees.IndiaFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def brokerage_multiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def max_brokerage(self) -> float:
        """
        Maximum brokerage per order
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def securities_transaction_tax_total_multiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def exchange_transaction_charge_multiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def state_tax_multiplier(self) -> float:
        """
        State Tax calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def sebi_charges_multiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def stamp_charges_multiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        
        This codeEntityType is protected.
        """
        ...


class RBIFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models RBI order fees"""

    def __init__(self, fees_per_share: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param fees_per_share: The fees per share to apply
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class BinanceFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Binance order fees"""

    MAKER_TIER_1_FEE: float = 0.001
    """
    Tier 1 maker fees
    https://www.binance.com/en/fee/schedule
    """

    TAKER_TIER_1_FEE: float = 0.001
    """
    Tier 1 taker fees
    https://www.binance.com/en/fee/schedule
    """

    def __init__(self, m_fee: float = ..., t_fee: float = ...) -> None:
        """
        Creates Binance fee model setting fees values
        
        :param m_fee: Maker fee value
        :param t_fee: Taker fee value
        """
        ...

    @overload
    def get_fee(self, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the fee factor for the given order
        
        
        This codeEntityType is protected.
        
        :param order: The order to get the fee factor for
        :returns: The fee factor for the given order.
        """
        ...

    @staticmethod
    @overload
    def get_fee(order: QuantConnect.Orders.Order, maker_fee: float, taker_fee: float) -> float:
        """
        Gets the fee factor for the given order taking into account the maker and the taker fee
        
        
        This codeEntityType is protected.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class BinanceCoinFuturesFeeModel(QuantConnect.Orders.Fees.BinanceFeeModel):
    """Provides an implementation of FeeModel that models Binance Coin Futures order fees"""

    MAKER_TIER_1_FEE: float = 0.0001
    """
    Tier 1 maker fees
    https://www.binance.com/en/fee/deliveryFee
    """

    TAKER_TIER_1_FEE: float = 0.0005
    """
    Tier 1 taker fees
    https://www.binance.com/en/fee/deliveryFee
    """

    def __init__(self, m_fee: float = ..., t_fee: float = ...) -> None:
        """
        Creates Binance Coin Futures fee model setting fees values
        
        :param m_fee: Maker fee value
        :param t_fee: Taker fee value
        """
        ...


class InteractiveBrokersFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides the default implementation of IFeeModel"""

    def __init__(self, monthly_forex_trade_amount_in_us_dollars: float = 0, monthly_options_trade_amount_in_contracts: float = 0) -> None:
        """
        Initializes a new instance of the ImmediateFillModel
        
        :param monthly_forex_trade_amount_in_us_dollars: Monthly FX dollar volume traded
        :param monthly_options_trade_amount_in_contracts: Monthly options contracts traded
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...

    @staticmethod
    def get_potential_order_price(order: QuantConnect.Orders.Order, security: QuantConnect.Securities.Security) -> float:
        """
        Approximates the order's price based on the order type
        
        
        This codeEntityType is protected.
        """
        ...


class CoinbaseFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Represents a fee model specific to Coinbase.
    This class extends the base fee model.
    """

    MAKER_ADVANCED_1: float = 0.006
    """
    Level Advanced 1 maker fee
    Tab "Fee tiers" on https://www.coinbase.com/advanced-fees
    """

    TAKER_ADVANCED_1: float = 0.008
    """
    Level Advanced 1 taker fee
    Tab "Fee tiers" on https://www.coinbase.com/advanced-fees
    """

    MAKER_STABLE_PAIRS: float = 0
    """
    Stable Pairs maker fee
    Tab "Stable pairs" on https://www.coinbase.com/advanced-fees
    """

    TAKER_STABLE_PARIS: float = 0.00001
    """
    Stable Pairs taker fee
    Tab "Stable pairs" on https://www.coinbase.com/advanced-fees
    """

    def __init__(self, maker_fee: float = ..., taker_fee: float = ...) -> None:
        """
        Create Coinbase Fee model setting fee values
        
        :param maker_fee: Maker fee value
        :param taker_fee: Taker fee value
        """
        ...

    @staticmethod
    def get_fee_percentage(utc_time: typing.Union[datetime.datetime, datetime.date], is_maker: bool, is_stable_coin: bool, maker_fee: float, taker_fee: float) -> float:
        """
        Returns the maker/taker fee percentage effective at the requested date.
        
        
        This codeEntityType is protected.
        
        :param utc_time: The date/time requested (UTC)
        :param is_maker: true if the maker percentage fee is requested, false otherwise
        :param is_stable_coin: true if the order security symbol is a StableCoin, false otherwise
        :param maker_fee: maker fee amount
        :param taker_fee: taker fee amount
        :returns: The fee percentage.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class GDAXFeeModel(QuantConnect.Orders.Fees.CoinbaseFeeModel):
    """
    Provides an implementation of FeeModel that models GDAX order fees
    
    
    GDAXFeeModel is deprecated. Use CoinbaseFeeModel instead.
    """


class dYdXFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """dYdX fee model implementation"""

    def __init__(self, m_fee: float = ..., t_fee: float = ...) -> None:
        """
        Creates Binance fee model setting fees values
        
        :param m_fee: Maker fee value
        :param t_fee: Taker fee value
        """
        ...

    def get_fee(self, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the fee factor for the given order
        
        
        This codeEntityType is protected.
        
        :param order: The order to get the fee factor for
        :returns: The fee factor for the given order.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class TDAmeritradeFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models TDAmeritrade order fees"""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class CharlesSchwabFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Represents a fee model specific to Charles Schwab."""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Calculates the order fee based on the security type and order parameters.
        
        :param parameters: The parameters for the order fee calculation, which include security and order details.
        :returns: An OrderFee instance representing the calculated order fee.
        """
        ...


class ExanteFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Provides an implementation of FeeModel that models Exante order fees.
    According to:
    https://support.exante.eu/hc/en-us/articles/115005873143-Fees-overview-exchange-imposed-fees?source=searchhttps://exante.eu/markets/
    """

    MARKET_USA_RATE: float = 0.02
    """Market USA rate"""

    DEFAULT_RATE: float = 0.02
    """Default rate"""

    def __init__(self, forex_commission_rate: float = 0.25) -> None:
        """
        Creates a new instance
        
        :param forex_commission_rate: Commission rate for FX operations
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class FTXFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Provides an implementation of FeeModel that models FTX order fees
    https://help.ftx.com/hc/en-us/articles/360024479432-Fees
    """

    @property
    def maker_fee(self) -> float:
        """Tier 1 maker fees"""
        ...

    @property
    def taker_fee(self) -> float:
        """Tier 1 taker fees"""
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class FTXUSFeeModel(QuantConnect.Orders.Fees.FTXFeeModel):
    """
    Provides an implementation of FeeModel that models FTX order fees
    https://help.ftx.us/hc/en-us/articles/360043579273-Fees
    """

    @property
    def maker_fee(self) -> float:
        """Tier 1 maker fees"""
        ...

    @property
    def taker_fee(self) -> float:
        """Tier 1 taker fees"""
        ...


class AxosFeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Provides an implementation of FeeModel that models Axos order fees"""

    def __init__(self, fees_per_share: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param fees_per_share: The fees per share to apply
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class BybitFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Bybit fee model implementation"""

    MAKER_NON_VIP_FEE: float = 0.001
    """
    Tier 1 maker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    TAKER_NON_VIP_FEE: float = 0.001
    """
    Tier 1 taker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    def __init__(self, m_fee: float = ..., t_fee: float = ...) -> None:
        """
        Creates Binance fee model setting fees values
        
        :param m_fee: Maker fee value
        :param t_fee: Taker fee value
        """
        ...

    def get_fee(self, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the fee factor for the given order
        
        
        This codeEntityType is protected.
        
        :param order: The order to get the fee factor for
        :returns: The fee factor for the given order.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class BybitFuturesFeeModel(QuantConnect.Orders.Fees.BybitFeeModel):
    """Bybit futures fee model implementation"""

    MAKER_NON_VIP_FEE: float = 0.0002
    """
    Tier 1 maker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    TAKER_NON_VIP_FEE: float = 0.00055
    """
    Tier 1 taker fees
    https://learn.bybit.com/bybit-guide/bybit-trading-fees/
    """

    def __init__(self, maker_fee: float = ..., taker_fee: float = ...) -> None:
        """
        Initializes a new instance of the BybitFuturesFeeModel class
        
        :param maker_fee: The accounts maker fee
        :param taker_fee: The accounts taker fee
        """
        ...


class BinanceFuturesFeeModel(QuantConnect.Orders.Fees.BinanceFeeModel):
    """Provides an implementation of FeeModel that models Binance Futures order fees"""

    MAKER_TIER_1_USDT_FEE: float = 0.0002
    """
    Tier 1 USDT maker fees
    https://www.binance.com/en/fee/futureFee
    """

    TAKER_TIER_1_USDT_FEE: float = 0.0004
    """
    Tier 1 USDT taker fees
    https://www.binance.com/en/fee/futureFee
    """

    MAKER_TIER_1_BUSD_FEE: float = 0.00012
    """
    Tier 1 BUSD maker fees
    https://www.binance.com/en/fee/futureFee
    """

    TAKER_TIER_1_BUSD_FEE: float = 0.00036
    """
    Tier 1 BUSD taker fees
    https://www.binance.com/en/fee/futureFee
    """

    def __init__(self, m_usdt_fee: float = ..., t_usdt_fee: float = ..., m_busd_fee: float = ..., t_busd_fee: float = ...) -> None:
        """
        Creates Binance Futures fee model setting fees values
        
        :param m_usdt_fee: Maker fee value for USDT pair contracts
        :param t_usdt_fee: Taker fee value for USDT pair contracts
        :param m_busd_fee: Maker fee value for BUSD pair contracts
        :param t_busd_fee: Taker fee value for BUSD pair contracts
        """
        ...

    def get_fee(self, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the fee for the given order
        
        
        This codeEntityType is protected.
        """
        ...


class TastytradeFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Represents a fee model specific to Tastytrade."""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee for a given security and order.
        
        :param parameters: The parameters including the security and order details.
        :returns: A OrderFee instance representing the total fee for the order,
        or OrderFee.ZERO if no fee is applicable.
        """
        ...


class EzeFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Eze fee model implementation"""


class FxcmFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models FXCM order fees"""

    def __init__(self, currency: str = "USD") -> None:
        """
        Creates a new instance
        
        :param currency: The currency of the order fee, for FXCM this is the account currency
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in units of the account currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class ConstantFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an order fee model that always returns the same order fee."""

    def __init__(self, fee: float, currency: str = "USD") -> None:
        """
        Initializes a new instance of the ConstantFeeModel class with the specified fee
        
        :param fee: The constant order fee used by the model
        :param currency: The currency of the order fee
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Returns the constant fee for the model in units of the account currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class TradeStationFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Represents a fee model specific to TradeStation."""

    @property
    def us_resident(self) -> bool:
        """Gets or sets a value indicating whether the entity or person is a resident of the United States."""
        ...

    @us_resident.setter
    def us_resident(self, value: bool) -> None:
        ...

    def __init__(self, us_resident: bool = True) -> None:
        """
        Initializes a new instance of the TradeStationFeeModel class.
        
        :param us_resident: A boolean value indicating whether the entity or person is a US resident.
        Default is true.
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Calculates the order fee based on the security type and order parameters.
        
        :param parameters: The parameters for the order fee calculation, which include security and order details.
        :returns: An OrderFee instance representing the calculated order fee.
        """
        ...


class AlpacaFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Represents the fee model specific to Alpaca trading platform."""

    MAKER_CRYPTO_FEE: float = 0.0015
    """The fee percentage for a maker transaction in cryptocurrency."""

    TAKER_CRYPTO_FEE: float = 0.0025
    """The fee percentage for a taker transaction in cryptocurrency."""

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class WolverineFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Wolverine order fees"""

    def __init__(self, fees_per_share: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param fees_per_share: The fees per share to apply
        """
        ...

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class BitfinexFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Bitfinex order fees"""

    MAKER_FEE: float = 0.001
    """
    Tier 1 maker fees
    Maker fees are paid when you add liquidity to our order book by placing a limit order under the ticker price for buy and above the ticker price for sell.
    https://www.bitfinex.com/fees
    """

    TAKER_FEE: float = 0.002
    """
    Tier 1 taker fees
    Taker fees are paid when you remove liquidity from our order book by placing any order that is executed against an order of the order book.
    Note: If you place a hidden order, you will always pay the taker fee. If you place a limit order that hits a hidden order, you will always pay the maker fee.
    https://www.bitfinex.com/fees
    """

    def get_order_fee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object
        containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class FeeModelExtensions(System.Object):
    """
    Provide extension method for IFeeModel to enable
    backwards compatibility of invocations.
    """

    @staticmethod
    def get_order_fee(model: QuantConnect.Orders.Fees.IFeeModel, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param model: The fee model
        :param security: The security matching the order
        :param order: The order to compute fees for
        :returns: The cost of the order in units of the account currency.
        """
        ...


