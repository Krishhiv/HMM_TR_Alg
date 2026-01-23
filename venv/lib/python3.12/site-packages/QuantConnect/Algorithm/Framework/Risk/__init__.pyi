from typing import overload
from enum import IntEnum
import abc
import typing

import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Algorithm.Framework.Risk
import QuantConnect.Data.UniverseSelection
import System


class IRiskManagementModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges, metaclass=abc.ABCMeta):
    """Algorithm framework model that manages an algorithm's risk/downside"""

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class RiskManagementModel(System.Object, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel):
    """Provides a base class for risk management models"""

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class MaximumDrawdownPercentPortfolio(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the drawdown of the portfolio
    to the specified percentage. Once this is triggered the algorithm will need to be manually restarted.
    """

    def __init__(self, maximum_drawdown_percent: float = 0.05, is_trailing: bool = False) -> None:
        """
        Initializes a new instance of the MaximumDrawdownPercentPortfolio class
        
        :param maximum_drawdown_percent: The maximum percentage drawdown allowed for algorithm portfolio
        compared with starting value, defaults to 5% drawdown
        :param is_trailing: If "false", the drawdown will be relative to the starting value of the portfolio.
        If "true", the drawdown will be relative the last maximum portfolio value
        """
        ...

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class MaximumUnrealizedProfitPercentPerSecurity(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the unrealized profit
    per holding to the specified percentage
    """

    def __init__(self, maximum_unrealized_profit_percent: float = 0.05) -> None:
        """
        Initializes a new instance of the MaximumUnrealizedProfitPercentPerSecurity class
        
        :param maximum_unrealized_profit_percent: The maximum percentage unrealized profit allowed for any single security holding,
        defaults to 5% drawdown per security
        """
        ...

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class TrailingStopRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the maximum possible loss
    measured from the highest unrealized profit
    """

    def __init__(self, maximum_drawdown_percent: float = 0.05) -> None:
        """
        Initializes a new instance of the TrailingStopRiskManagementModel class
        
        :param maximum_drawdown_percent: The maximum percentage relative drawdown allowed for algorithm portfolio compared with the highest unrealized profit, defaults to 5% drawdown per security
        """
        ...

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class MaximumDrawdownPercentPerSecurity(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the drawdown
    per holding to the specified percentage
    """

    def __init__(self, maximum_drawdown_percent: float = 0.05) -> None:
        """
        Initializes a new instance of the MaximumDrawdownPercentPerSecurity class
        
        :param maximum_drawdown_percent: The maximum percentage drawdown allowed for any single security holding,
        defaults to 5% drawdown per security
        """
        ...

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class MaximumSectorExposureRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits
    the sector exposure to the specified percentage
    """

    def __init__(self, maximum_sector_exposure: float = 0.20) -> None:
        """
        Initializes a new instance of the MaximumSectorExposureRiskManagementModel class
        
        :param maximum_sector_exposure: The maximum exposure for any sector, defaults to 20% sector exposure.
        """
        ...

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class NullRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """Provides an implementation of IRiskManagementModel that does nothing"""

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class RiskManagementModelPythonWrapper(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """Provides an implementation of IRiskManagementModel that wraps a PyObject object"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the IRiskManagementModel class with wrapped PyObject object
        
        :param model: Model defining how risk is managed
        """
        ...

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class CompositeRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that combines multiple risk
    models into a single risk management model and properly sets each insights 'SourceModel' property.
    """

    @overload
    def __init__(self, *risk_management_models: typing.Union[QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel, typing.Iterable[QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel]]) -> None:
        """
        Initializes a new instance of the CompositeRiskManagementModel class
        
        :param risk_management_models: The individual risk management models defining this composite model
        """
        ...

    @overload
    def __init__(self, risk_management_models: typing.List[QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel]) -> None:
        """
        Initializes a new instance of the CompositeRiskManagementModel class
        
        :param risk_management_models: The individual risk management models defining this composite model
        """
        ...

    @overload
    def __init__(self, *risk_management_models: typing.Union[typing.Any, typing.Iterable[typing.Any]]) -> None:
        """
        Initializes a new instance of the CompositeRiskManagementModel class
        
        :param risk_management_models: The individual risk management models defining this composite model
        """
        ...

    @overload
    def add_risk_management(self, py_risk_management_model: typing.Any) -> None:
        """
        Adds a new IRiskManagementModel instance
        
        :param py_risk_management_model: The risk management model to add
        """
        ...

    @overload
    def add_risk_management(self, risk_management_model: QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel) -> None:
        """
        Adds a new IRiskManagementModel instance
        
        :param risk_management_model: The risk management model to add
        """
        ...

    def manage_risk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> typing.Iterable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step.
        This method patches this call through the each of the wrapped models.
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        :returns: The new portfolio targets.
        """
        ...

    def on_securities_changed(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed.
        This method patches this call through the each of the wrapped models.
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


