from typing import overload
from enum import IntEnum
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Api
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Optimizer
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Generic
import System.Collections.Specialized
import System.Text.RegularExpressions


class ApiUtils(System.Object):
    """API utility methods"""

    @staticmethod
    def create_json_post_request(endpoint: str, payload: typing.Any = None, json_serializer_settings: typing.Any = None) -> typing.Any:
        """
        Creates a POST HttpRequestMessage with the specified endpoint and payload as json body
        
        :param endpoint: The request endpoint
        :param payload: The request payload
        :param json_serializer_settings: Settings for the json serializer
        :returns: The POST request.
        """
        ...

    @staticmethod
    def create_post_request(endpoint: str, payload: typing.List[System.Collections.Generic.KeyValuePair[str, str]] = None) -> typing.Any:
        """
        Creates a POST HttpRequestMessage with the specified endpoint and payload as form url encoded content.
        
        :param endpoint: The request endpoint
        :param payload: The request payload
        :returns: The POST request.
        """
        ...


class ApiConnection(System.Object, System.IDisposable):
    """API Connection and Hash Manager"""

    @property
    def client(self) -> typing.Any:
        """
        Authorized client to use for requests.
        
        
        RestSharp is deprecated and will be removed in a future release. Please use the SetClient method or the request methods that take an HttpRequestMessage
        """
        warnings.warn("RestSharp is deprecated and will be removed in a future release. Please use the SetClient method or the request methods that take an HttpRequestMessage", DeprecationWarning)

    @client.setter
    def client(self, value: typing.Any) -> None:
        warnings.warn("RestSharp is deprecated and will be removed in a future release. Please use the SetClient method or the request methods that take an HttpRequestMessage", DeprecationWarning)

    @property
    def connected(self) -> bool:
        """Return true if connected successfully."""
        ...

    @overload
    def __init__(self, user_id: int, token: str) -> None:
        """
        Create a new Api Connection Class.
        
        :param user_id: User Id number from QuantConnect.com account. Found at www.quantconnect.com/account
        :param token: Access token for the QuantConnect account. Found at www.quantconnect.com/account
        """
        ...

    @overload
    def __init__(self, user_id: int, token: str, base_url: str = None, default_headers: System.Collections.Generic.Dictionary[str, str] = None, timeout: int = 0) -> None:
        """
        Create a new Api Connection Class.
        
        :param user_id: User Id number from QuantConnect.com account. Found at www.quantconnect.com/account
        :param token: Access token for the QuantConnect account. Found at www.quantconnect.com/account
        :param base_url: The client's base address
        :param default_headers: Default headers for the client
        :param timeout: The client timeout in seconds
        """
        ...

    def dispose(self) -> None:
        """Disposes of the HTTP client"""
        ...

    def set_client(self, base_url: str, default_headers: System.Collections.Generic.Dictionary[str, str] = None, timeout: int = 0) -> None:
        """
        Overrides the current client
        
        :param base_url: The client's base address
        :param default_headers: Default headers for the client
        :param timeout: The client timeout in seconds
        """
        ...


class StringRepresentation(System.Object):
    """Class to return the string representation of an API response class"""

    def to_string(self) -> str:
        """Returns the string representation of this object"""
        ...


class RestResponse(QuantConnect.Api.StringRepresentation):
    """Base API response class for the QuantConnect API."""

    @property
    def success(self) -> bool:
        """Indicate if the API request was successful."""
        ...

    @success.setter
    def success(self, value: bool) -> None:
        ...

    @property
    def errors(self) -> typing.List[str]:
        """List of errors with the API call."""
        ...

    @errors.setter
    def errors(self, value: typing.List[str]) -> None:
        ...

    def __init__(self) -> None:
        """JSON Constructor"""
        ...


class Version(System.Object):
    """API response for version"""

    @property
    def id(self) -> int:
        """ID of the LEAN version"""
        ...

    @id.setter
    def id(self, value: int) -> None:
        ...

    @property
    def created(self) -> typing.Optional[datetime.datetime]:
        """Date when this version was created"""
        ...

    @created.setter
    def created(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def description(self) -> str:
        """Description of the LEAN version"""
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def lean_hash(self) -> str:
        """Commit Hash in the LEAN repository"""
        ...

    @lean_hash.setter
    def lean_hash(self, value: str) -> None:
        ...

    @property
    def lean_cloud_hash(self) -> str:
        """Commit Hash in the LEAN Cloud repository"""
        ...

    @lean_cloud_hash.setter
    def lean_cloud_hash(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the branch where the commit is"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def ref(self) -> str:
        """Reference to the branch where the commit is"""
        ...

    @ref.setter
    def ref(self, value: str) -> None:
        ...

    @property
    def public(self) -> bool:
        """Indicates if the version is available for the public (1) or not (0)"""
        ...

    @public.setter
    def public(self, value: bool) -> None:
        ...


class VersionsResponse(QuantConnect.Api.RestResponse):
    """Read versions response"""

    @property
    def versions(self) -> typing.List[QuantConnect.Api.Version]:
        """List of LEAN versions"""
        ...

    @versions.setter
    def versions(self, value: typing.List[QuantConnect.Api.Version]) -> None:
        ...


class GridChart(System.Object):
    """The chart display properties"""

    @property
    def chart_name(self) -> str:
        """The chart name"""
        ...

    @chart_name.setter
    def chart_name(self, value: str) -> None:
        ...

    @property
    def width(self) -> int:
        """Width of the chart"""
        ...

    @width.setter
    def width(self, value: int) -> None:
        ...

    @property
    def height(self) -> int:
        """Height of the chart"""
        ...

    @height.setter
    def height(self, value: int) -> None:
        ...

    @property
    def row(self) -> int:
        """Number of rows of the chart"""
        ...

    @row.setter
    def row(self, value: int) -> None:
        ...

    @property
    def column(self) -> int:
        """Number of columns of the chart"""
        ...

    @column.setter
    def column(self, value: int) -> None:
        ...

    @property
    def sort(self) -> int:
        """Sort of the chart"""
        ...

    @sort.setter
    def sort(self, value: int) -> None:
        ...

    @property
    def definition(self) -> typing.List[str]:
        """Optionally related definition"""
        ...

    @definition.setter
    def definition(self, value: typing.List[str]) -> None:
        ...


class Grid(System.Object):
    """The grid arrangement of charts"""

    @property
    def xs(self) -> typing.List[QuantConnect.Api.GridChart]:
        """List of chart in the xs (Extra small) position"""
        ...

    @xs.setter
    def xs(self, value: typing.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def sm(self) -> typing.List[QuantConnect.Api.GridChart]:
        """List of chart in the sm (Small) position"""
        ...

    @sm.setter
    def sm(self, value: typing.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def md(self) -> typing.List[QuantConnect.Api.GridChart]:
        """List of chart in the md (Medium) position"""
        ...

    @md.setter
    def md(self, value: typing.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def lg(self) -> typing.List[QuantConnect.Api.GridChart]:
        """List of chart in the lg (Large) position"""
        ...

    @lg.setter
    def lg(self, value: typing.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def xl(self) -> typing.List[QuantConnect.Api.GridChart]:
        """List of chart in the xl (Extra large) position"""
        ...

    @xl.setter
    def xl(self, value: typing.List[QuantConnect.Api.GridChart]) -> None:
        ...


class EncryptionKey(System.Object):
    """Encryption key details"""

    @property
    def id(self) -> str:
        """Encryption key id"""
        ...

    @id.setter
    def id(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the encryption key"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...


class Collaborator(System.Object):
    """Collaborator responses"""

    @property
    def uid(self) -> typing.Optional[int]:
        """User ID"""
        ...

    @uid.setter
    def uid(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def live_control(self) -> bool:
        """Indicate if the user have live control"""
        ...

    @live_control.setter
    def live_control(self, value: bool) -> None:
        ...

    @property
    def permission(self) -> str:
        """
        The permission this user is given. Can be "read"
        or "write"
        """
        ...

    @permission.setter
    def permission(self, value: str) -> None:
        ...

    @property
    def public_id(self) -> str:
        """The user public ID"""
        ...

    @public_id.setter
    def public_id(self, value: str) -> None:
        ...

    @property
    def profile_image(self) -> str:
        """The url of the user profile image"""
        ...

    @profile_image.setter
    def profile_image(self, value: str) -> None:
        ...

    @property
    def email(self) -> str:
        """The registered email of the user"""
        ...

    @email.setter
    def email(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """The display name of the user"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def bio(self) -> str:
        """The biography of the user"""
        ...

    @bio.setter
    def bio(self, value: str) -> None:
        ...

    @property
    def owner(self) -> bool:
        """Indicate if the user is the owner of the project"""
        ...

    @owner.setter
    def owner(self, value: bool) -> None:
        ...


class Parameter(System.Object):
    """Parameter set"""

    @property
    def name(self) -> str:
        """Name of parameter"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def value(self) -> str:
        """Value of parameter"""
        ...

    @value.setter
    def value(self, value: str) -> None:
        ...


class Library(System.Object):
    """Library response"""

    @property
    def projectid(self) -> int:
        """Project Id of the library project"""
        ...

    @projectid.setter
    def projectid(self, value: int) -> None:
        ...

    @property
    def library_name(self) -> str:
        """Name of the library project"""
        ...

    @library_name.setter
    def library_name(self, value: str) -> None:
        ...

    @property
    def owner_name(self) -> str:
        """Name of the library project owner"""
        ...

    @owner_name.setter
    def owner_name(self, value: str) -> None:
        ...

    @property
    def access(self) -> bool:
        """Indicate if the library project can be accessed"""
        ...

    @access.setter
    def access(self, value: bool) -> None:
        ...


class Project(QuantConnect.Api.RestResponse):
    """Response from reading a project by id."""

    @property
    def project_id(self) -> int:
        """Project id"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the project"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def created(self) -> datetime.datetime:
        """Date the project was created"""
        ...

    @created.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def modified(self) -> datetime.datetime:
        """Modified date for the project"""
        ...

    @modified.setter
    def modified(self, value: datetime.datetime) -> None:
        ...

    @property
    def language(self) -> QuantConnect.Language:
        """Programming language of the project"""
        ...

    @language.setter
    def language(self, value: QuantConnect.Language) -> None:
        ...

    @property
    def owner_id(self) -> int:
        """The projects owner id"""
        ...

    @owner_id.setter
    def owner_id(self, value: int) -> None:
        ...

    @property
    def organization_id(self) -> str:
        """The organization ID"""
        ...

    @organization_id.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def collaborators(self) -> typing.List[QuantConnect.Api.Collaborator]:
        """List of collaborators"""
        ...

    @collaborators.setter
    def collaborators(self, value: typing.List[QuantConnect.Api.Collaborator]) -> None:
        ...

    @property
    def lean_version_id(self) -> int:
        """The version of LEAN this project is running on"""
        ...

    @lean_version_id.setter
    def lean_version_id(self, value: int) -> None:
        ...

    @property
    def lean_pinned_to_master(self) -> bool:
        """Indicate if the project is pinned to the master branch of LEAN"""
        ...

    @lean_pinned_to_master.setter
    def lean_pinned_to_master(self, value: bool) -> None:
        ...

    @property
    def owner(self) -> bool:
        """Indicate if you are the owner of the project"""
        ...

    @owner.setter
    def owner(self, value: bool) -> None:
        ...

    @property
    def description(self) -> str:
        """The project description"""
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def channel_id(self) -> str:
        """Channel id"""
        ...

    @channel_id.setter
    def channel_id(self, value: str) -> None:
        ...

    @property
    def parameters(self) -> typing.List[QuantConnect.Api.Parameter]:
        """Optimization parameters"""
        ...

    @parameters.setter
    def parameters(self, value: typing.List[QuantConnect.Api.Parameter]) -> None:
        ...

    @property
    def libraries(self) -> typing.List[QuantConnect.Api.Library]:
        """The library projects"""
        ...

    @libraries.setter
    def libraries(self, value: typing.List[QuantConnect.Api.Library]) -> None:
        ...

    @property
    def grid(self) -> QuantConnect.Api.Grid:
        """Configuration of the backtest view grid"""
        ...

    @grid.setter
    def grid(self, value: QuantConnect.Api.Grid) -> None:
        ...

    @property
    def live_grid(self) -> QuantConnect.Api.Grid:
        """Configuration of the live view grid"""
        ...

    @live_grid.setter
    def live_grid(self, value: QuantConnect.Api.Grid) -> None:
        ...

    @property
    def paper_equity(self) -> typing.Optional[float]:
        """The equity value of the last paper trading instance"""
        ...

    @paper_equity.setter
    def paper_equity(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def last_live_deployment(self) -> typing.Optional[datetime.datetime]:
        """The last live deployment active time"""
        ...

    @last_live_deployment.setter
    def last_live_deployment(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def live_form(self) -> System.Object:
        """The last live wizard content used"""
        ...

    @live_form.setter
    def live_form(self, value: System.Object) -> None:
        ...

    @property
    def encrypted(self) -> typing.Optional[bool]:
        """Indicates if the project is encrypted"""
        ...

    @encrypted.setter
    def encrypted(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    def code_running(self) -> bool:
        """Indicates if the project is running or not"""
        ...

    @code_running.setter
    def code_running(self, value: bool) -> None:
        ...

    @property
    def lean_environment(self) -> int:
        """LEAN environment of the project running on"""
        ...

    @lean_environment.setter
    def lean_environment(self, value: int) -> None:
        ...

    @property
    def encryption_key(self) -> QuantConnect.Api.EncryptionKey:
        """Text file with at least 32 characters to be used to encrypt the project"""
        ...

    @encryption_key.setter
    def encryption_key(self, value: QuantConnect.Api.EncryptionKey) -> None:
        ...


class ProjectResponse(QuantConnect.Api.VersionsResponse):
    """Project list response"""

    @property
    def projects(self) -> typing.List[QuantConnect.Api.Project]:
        """List of projects for the authenticated user"""
        ...

    @projects.setter
    def projects(self, value: typing.List[QuantConnect.Api.Project]) -> None:
        ...


class ProjectFile(System.Object):
    """File for a project"""

    @property
    def name(self) -> str:
        """Name of a project file"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def code(self) -> str:
        """Contents of the project file"""
        ...

    @code.setter
    def code(self, value: str) -> None:
        ...

    @property
    def date_modified(self) -> datetime.datetime:
        """DateTime project file was modified"""
        ...

    @date_modified.setter
    def date_modified(self, value: datetime.datetime) -> None:
        ...

    @property
    def is_library(self) -> bool:
        """Indicates if the project file is a library or not"""
        ...

    @is_library.setter
    def is_library(self, value: bool) -> None:
        ...

    @property
    def open(self) -> bool:
        """Indicates if the project file is open or not"""
        ...

    @open.setter
    def open(self, value: bool) -> None:
        ...

    @property
    def project_id(self) -> int:
        """ID of the project"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def id(self) -> typing.Optional[int]:
        """ID of the project file, can be null"""
        ...

    @id.setter
    def id(self, value: typing.Optional[int]) -> None:
        ...


class ProjectFilesResponse(QuantConnect.Api.RestResponse):
    """Response received when creating a file or reading one file or more in a project"""

    @property
    def files(self) -> typing.List[QuantConnect.Api.ProjectFile]:
        """List of project file information"""
        ...

    @files.setter
    def files(self, value: typing.List[QuantConnect.Api.ProjectFile]) -> None:
        ...


class NodePrices(System.Object):
    """Class for deserializing node prices from node object"""

    @property
    def monthly(self) -> int:
        """The monthly price of the node in US dollars"""
        ...

    @monthly.setter
    def monthly(self, value: int) -> None:
        ...

    @property
    def yearly(self) -> int:
        """The yearly prices of the node in US dollars"""
        ...

    @yearly.setter
    def yearly(self, value: int) -> None:
        ...


class Node(System.Object):
    """
    Node class built for API endpoints nodes/read and nodes/create.
    Converts JSON properties from API response into data members for the class.
    Contains all relevant information on a Node to interact through API endpoints.
    """

    @property
    def speed(self) -> float:
        """The nodes cpu clock speed in GHz."""
        ...

    @speed.setter
    def speed(self, value: float) -> None:
        ...

    @property
    def prices(self) -> QuantConnect.Api.NodePrices:
        """
        The monthly and yearly prices of the node in US dollars,
        see NodePrices for type.
        """
        ...

    @prices.setter
    def prices(self, value: QuantConnect.Api.NodePrices) -> None:
        ...

    @property
    def cpu_count(self) -> int:
        """CPU core count of node."""
        ...

    @cpu_count.setter
    def cpu_count(self, value: int) -> None:
        ...

    @property
    def has_gpu(self) -> int:
        """Indicate if the node has GPU (1) or not (0)"""
        ...

    @has_gpu.setter
    def has_gpu(self, value: int) -> None:
        ...

    @property
    def ram(self) -> float:
        """Size of RAM in Gigabytes."""
        ...

    @ram.setter
    def ram(self, value: float) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the node."""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def sku(self) -> str:
        """Node type identifier for configuration."""
        ...

    @sku.setter
    def sku(self, value: str) -> None:
        ...

    @property
    def description(self) -> str:
        """Description of the node."""
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def used_by(self) -> str:
        """User currently using the node."""
        ...

    @used_by.setter
    def used_by(self, value: str) -> None:
        ...

    @property
    def user_profile(self) -> str:
        """URL of the user using the node"""
        ...

    @user_profile.setter
    def user_profile(self, value: str) -> None:
        ...

    @property
    def project_name(self) -> str:
        """Project the node is being used for."""
        ...

    @project_name.setter
    def project_name(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> typing.Optional[int]:
        """Id of the project the node is being used for."""
        ...

    @project_id.setter
    def project_id(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def busy(self) -> bool:
        """Indicates if the node is currently busy."""
        ...

    @busy.setter
    def busy(self, value: bool) -> None:
        ...

    @property
    def id(self) -> str:
        """Full ID of node."""
        ...

    @id.setter
    def id(self, value: str) -> None:
        ...

    @property
    def assets(self) -> int:
        """Maximum number of assets recommended for this node."""
        ...

    @assets.setter
    def assets(self, value: int) -> None:
        ...

    @property
    def host(self) -> str:
        """Node host."""
        ...

    @host.setter
    def host(self, value: str) -> None:
        ...

    @property
    def active(self) -> bool:
        """Indicate if this is the active node. The project will use this node if it's not busy."""
        ...

    @active.setter
    def active(self, value: bool) -> None:
        ...


class NodeList(QuantConnect.Api.RestResponse):
    """Collection of Node objects for each target environment."""

    @property
    def backtest_nodes(self) -> typing.List[QuantConnect.Api.Node]:
        """Collection of backtest nodes"""
        ...

    @backtest_nodes.setter
    def backtest_nodes(self, value: typing.List[QuantConnect.Api.Node]) -> None:
        ...

    @property
    def research_nodes(self) -> typing.List[QuantConnect.Api.Node]:
        """Collection of research nodes"""
        ...

    @research_nodes.setter
    def research_nodes(self, value: typing.List[QuantConnect.Api.Node]) -> None:
        ...

    @property
    def live_nodes(self) -> typing.List[QuantConnect.Api.Node]:
        """Collection of live nodes"""
        ...

    @live_nodes.setter
    def live_nodes(self, value: typing.List[QuantConnect.Api.Node]) -> None:
        ...


class ProjectNodesResponse(QuantConnect.Api.RestResponse):
    """Response received when reading or updating some nodes of a project"""

    @property
    def nodes(self) -> QuantConnect.Api.NodeList:
        """List of project nodes."""
        ...

    @nodes.setter
    def nodes(self, value: QuantConnect.Api.NodeList) -> None:
        ...

    @property
    def auto_select_node(self) -> bool:
        """Indicate if the node is automatically selected"""
        ...

    @auto_select_node.setter
    def auto_select_node(self, value: bool) -> None:
        ...


class CompileState(IntEnum):
    """State of the compilation request"""

    IN_QUEUE = 0
    """Compile waiting in the queue to be processed."""

    BUILD_SUCCESS = 1
    """Compile was built successfully"""

    BUILD_ERROR = 2
    """Build error, check logs for more information"""


class Compile(QuantConnect.Api.RestResponse):
    """Response from the compiler on a build event"""

    @property
    def compile_id(self) -> str:
        """Compile Id for a sucessful build"""
        ...

    @compile_id.setter
    def compile_id(self, value: str) -> None:
        ...

    @property
    def state(self) -> QuantConnect.Api.CompileState:
        """True on successful compile"""
        ...

    @state.setter
    def state(self, value: QuantConnect.Api.CompileState) -> None:
        ...

    @property
    def logs(self) -> typing.List[str]:
        """Logs of the compilation request"""
        ...

    @logs.setter
    def logs(self, value: typing.List[str]) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project Id we sent for compile"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def signature(self) -> str:
        """Signature key of compilation"""
        ...

    @signature.setter
    def signature(self, value: str) -> None:
        ...

    @property
    def signature_order(self) -> typing.List[str]:
        """Signature order of files to be compiled"""
        ...

    @signature_order.setter
    def signature_order(self, value: typing.List[str]) -> None:
        ...


class BasicBacktest(QuantConnect.Api.RestResponse):
    """Base class for backtest result object response"""

    @property
    def error(self) -> str:
        """Backtest error message"""
        ...

    @error.setter
    def error(self, value: str) -> None:
        ...

    @property
    def stacktrace(self) -> str:
        """Backtest error stacktrace"""
        ...

    @stacktrace.setter
    def stacktrace(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """Assigned backtest Id"""
        ...

    @backtest_id.setter
    def backtest_id(self, value: str) -> None:
        ...

    @property
    def status(self) -> str:
        """Status of the backtest"""
        ...

    @status.setter
    def status(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the backtest"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def created(self) -> datetime.datetime:
        """Backtest creation date and time"""
        ...

    @created.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def progress(self) -> float:
        """Progress of the backtest in percent 0-1."""
        ...

    @progress.setter
    def progress(self, value: float) -> None:
        ...

    @property
    def optimization_id(self) -> str:
        """Optimization task ID, if the backtest is part of an optimization"""
        ...

    @optimization_id.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def tradeable_dates(self) -> int:
        """Number of tradeable days"""
        ...

    @tradeable_dates.setter
    def tradeable_dates(self, value: int) -> None:
        ...

    @property
    def parameter_set(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """Optimization parameters"""
        ...

    @parameter_set.setter
    def parameter_set(self, value: QuantConnect.Optimizer.Parameters.ParameterSet) -> None:
        ...

    @property
    def snap_shot_id(self) -> int:
        """Snapshot id of this backtest result"""
        ...

    @snap_shot_id.setter
    def snap_shot_id(self, value: int) -> None:
        ...


class ResearchGuide(System.Object):
    """A power gauge for backtests, time and parameters to estimate the overfitting risk"""

    @property
    def minutes(self) -> int:
        """Number of minutes used in developing the current backtest"""
        ...

    @minutes.setter
    def minutes(self, value: int) -> None:
        ...

    @property
    def backtest_count(self) -> int:
        """The quantity of backtests run in the project"""
        ...

    @backtest_count.setter
    def backtest_count(self, value: int) -> None:
        ...

    @property
    def parameters(self) -> int:
        """Number of parameters detected"""
        ...

    @parameters.setter
    def parameters(self, value: int) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project ID"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...


class Backtest(QuantConnect.Api.BasicBacktest):
    """Results object class. Results are exhaust from backtest or live algorithms running in LEAN"""

    @property
    def note(self) -> str:
        """Note on the backtest attached by the user"""
        ...

    @note.setter
    def note(self, value: str) -> None:
        ...

    @property
    def completed(self) -> bool:
        """Boolean true when the backtest is completed."""
        ...

    @completed.setter
    def completed(self, value: bool) -> None:
        ...

    @property
    def organization_id(self) -> str:
        """Organization ID"""
        ...

    @organization_id.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def rolling_window(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @rolling_window.setter
    def rolling_window(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]) -> None:
        ...

    @property
    def total_performance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Total algorithm performance statistics."""
        ...

    @total_performance.setter
    def total_performance(self, value: QuantConnect.Statistics.AlgorithmPerformance) -> None:
        ...

    @property
    def charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @charts.setter
    def charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]) -> None:
        ...

    @property
    def statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Statistics information sent during the algorithm operations."""
        ...

    @statistics.setter
    def statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @runtime_statistics.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def research_guide(self) -> QuantConnect.Api.ResearchGuide:
        """A power gauge for backtests, time and parameters to estimate the overfitting risk"""
        ...

    @research_guide.setter
    def research_guide(self, value: QuantConnect.Api.ResearchGuide) -> None:
        ...

    @property
    def backtest_start(self) -> typing.Optional[datetime.datetime]:
        """The starting time of the backtest"""
        ...

    @backtest_start.setter
    def backtest_start(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def backtest_end(self) -> typing.Optional[datetime.datetime]:
        """The ending time of the backtest"""
        ...

    @backtest_end.setter
    def backtest_end(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def has_initialize_error(self) -> bool:
        """Indicates if the backtest has error during initialization"""
        ...

    @has_initialize_error.setter
    def has_initialize_error(self, value: bool) -> None:
        ...

    @property
    def node_name(self) -> str:
        """The backtest node name"""
        ...

    @node_name.setter
    def node_name(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """The associated project id"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """End date of out of sample data"""
        ...

    @out_of_sample_max_end_date.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_days(self) -> typing.Optional[int]:
        """Number of days of out of sample days"""
        ...

    @out_of_sample_days.setter
    def out_of_sample_days(self, value: typing.Optional[int]) -> None:
        ...


class ReadChartResponse(QuantConnect.Api.RestResponse):
    """Class for wrapping Read Chart response"""

    @property
    def chart(self) -> QuantConnect.Chart:
        """Chart object from the ReadChart response"""
        ...

    @chart.setter
    def chart(self, value: QuantConnect.Chart) -> None:
        ...


class BacktestSummary(QuantConnect.Api.BasicBacktest):
    """Result object class for the List Backtest response from the API"""

    @property
    def sharpe_ratio(self) -> typing.Optional[float]:
        """Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk"""
        ...

    @sharpe_ratio.setter
    def sharpe_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def alpha(self) -> typing.Optional[float]:
        """Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns"""
        ...

    @alpha.setter
    def alpha(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def beta(self) -> typing.Optional[float]:
        """Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance"""
        ...

    @beta.setter
    def beta(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def compounding_annual_return(self) -> typing.Optional[float]:
        """Annual compounded returns statistic based on the final-starting capital and years"""
        ...

    @compounding_annual_return.setter
    def compounding_annual_return(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def drawdown(self) -> typing.Optional[float]:
        """Drawdown maximum percentage"""
        ...

    @drawdown.setter
    def drawdown(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def loss_rate(self) -> typing.Optional[float]:
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @loss_rate.setter
    def loss_rate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def net_profit(self) -> typing.Optional[float]:
        """Net profit percentage"""
        ...

    @net_profit.setter
    def net_profit(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def parameters(self) -> typing.Optional[int]:
        """Number of parameters in the backtest"""
        ...

    @parameters.setter
    def parameters(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def psr(self) -> typing.Optional[float]:
        """Price-to-sales ratio"""
        ...

    @psr.setter
    def psr(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def security_types(self) -> str:
        """SecurityTypes present in the backtest"""
        ...

    @security_types.setter
    def security_types(self, value: str) -> None:
        ...

    @property
    def sortino_ratio(self) -> typing.Optional[float]:
        """Sortino ratio with respect to risk free rate: measures excess of return per unit of downside risk"""
        ...

    @sortino_ratio.setter
    def sortino_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trades(self) -> typing.Optional[int]:
        """Number of trades in the backtest"""
        ...

    @trades.setter
    def trades(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def treynor_ratio(self) -> typing.Optional[float]:
        """Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk"""
        ...

    @treynor_ratio.setter
    def treynor_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def win_rate(self) -> typing.Optional[float]:
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @win_rate.setter
    def win_rate(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def tags(self) -> typing.List[str]:
        """Collection of tags for the backtest"""
        ...

    @tags.setter
    def tags(self, value: typing.List[str]) -> None:
        ...


class BacktestSummaryList(QuantConnect.Api.RestResponse):
    """Collection container for a list of backtest summaries for a project"""

    @property
    def backtests(self) -> typing.List[QuantConnect.Api.BacktestSummary]:
        """Collection of summarized backtest summary objects"""
        ...

    @backtests.setter
    def backtests(self, value: typing.List[QuantConnect.Api.BacktestSummary]) -> None:
        ...

    @property
    def count(self) -> int:
        """Number of backtest summaries retrieved in the response"""
        ...

    @count.setter
    def count(self, value: int) -> None:
        ...


class InsightResponse(QuantConnect.Api.RestResponse):
    """Class containing insights and the number of insights of the live algorithm in the request criteria"""

    @property
    def insights(self) -> typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Collection of insights"""
        ...

    @insights.setter
    def insights(self, value: typing.List[QuantConnect.Algorithm.Framework.Alphas.Insight]) -> None:
        ...

    @property
    def length(self) -> int:
        """Total number of returned insights"""
        ...

    @length.setter
    def length(self, value: int) -> None:
        ...


class BaseLiveAlgorithm(QuantConnect.Api.RestResponse):
    """Class representing the REST response from QC API when creating or reading a live algorithm"""

    @property
    def project_id(self) -> int:
        """Project id for the live instance"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def deploy_id(self) -> str:
        """Unique live algorithm deployment identifier (similar to a backtest id)."""
        ...

    @deploy_id.setter
    def deploy_id(self, value: str) -> None:
        ...


class CreateLiveAlgorithmResponse(QuantConnect.Api.BaseLiveAlgorithm):
    """Class representing the REST response from QC API when creating a live algorithm"""

    @property
    def version_id(self) -> int:
        """The version of the Lean used to run the algorithm"""
        ...

    @version_id.setter
    def version_id(self, value: int) -> None:
        ...

    @property
    def source(self) -> str:
        """Id of the node that will run the algorithm"""
        ...

    @source.setter
    def source(self, value: str) -> None:
        ...

    @property
    def response_code(self) -> str:
        """HTTP status response code"""
        ...

    @response_code.setter
    def response_code(self, value: str) -> None:
        ...


class LiveAlgorithmSummary(QuantConnect.Api.BaseLiveAlgorithm):
    """Response from List Live Algorithms request to QuantConnect Rest API."""

    @property
    def status(self) -> QuantConnect.AlgorithmStatus:
        """Algorithm status: running, stopped or runtime error."""
        ...

    @status.setter
    def status(self, value: QuantConnect.AlgorithmStatus) -> None:
        ...

    @property
    def launched(self) -> datetime.datetime:
        """Datetime the algorithm was launched in UTC."""
        ...

    @launched.setter
    def launched(self, value: datetime.datetime) -> None:
        ...

    @property
    def stopped(self) -> typing.Optional[datetime.datetime]:
        """Datetime the algorithm was stopped in UTC, null if its still running."""
        ...

    @stopped.setter
    def stopped(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def brokerage(self) -> str:
        """Brokerage"""
        ...

    @brokerage.setter
    def brokerage(self, value: str) -> None:
        ...

    @property
    def subscription(self) -> str:
        """Chart we're subscribed to"""
        ...

    @subscription.setter
    def subscription(self, value: str) -> None:
        ...

    @property
    def error(self) -> str:
        """Live algorithm error message from a crash or algorithm runtime error."""
        ...

    @error.setter
    def error(self, value: str) -> None:
        ...


class LiveList(QuantConnect.Api.RestResponse):
    """List of the live algorithms running which match the requested status"""

    @property
    def algorithms(self) -> typing.List[QuantConnect.Api.LiveAlgorithmSummary]:
        """Algorithm list matching the requested status."""
        ...

    @algorithms.setter
    def algorithms(self, value: typing.List[QuantConnect.Api.LiveAlgorithmSummary]) -> None:
        ...


class LiveAlgorithmResults(QuantConnect.Api.RestResponse):
    """Details a live algorithm from the "live/read" Api endpoint"""

    @property
    def message(self) -> str:
        """Error message"""
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def status(self) -> str:
        """Indicates the status of the algorihtm, i.e. 'Running', 'Stopped'"""
        ...

    @status.setter
    def status(self, value: str) -> None:
        ...

    @property
    def deploy_id(self) -> str:
        """Algorithm deployment ID"""
        ...

    @deploy_id.setter
    def deploy_id(self, value: str) -> None:
        ...

    @property
    def clone_id(self) -> int:
        """The snapshot project ID for cloning the live development's source code."""
        ...

    @clone_id.setter
    def clone_id(self, value: int) -> None:
        ...

    @property
    def launched(self) -> datetime.datetime:
        """Date the live algorithm was launched"""
        ...

    @launched.setter
    def launched(self, value: datetime.datetime) -> None:
        ...

    @property
    def stopped(self) -> typing.Optional[datetime.datetime]:
        """Date the live algorithm was stopped"""
        ...

    @stopped.setter
    def stopped(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def brokerage(self) -> str:
        """Brokerage used in the live algorithm"""
        ...

    @brokerage.setter
    def brokerage(self, value: str) -> None:
        ...

    @property
    def security_types(self) -> str:
        """Security types present in the live algorithm"""
        ...

    @security_types.setter
    def security_types(self, value: str) -> None:
        ...

    @property
    def project_name(self) -> str:
        """Name of the project the live algorithm is in"""
        ...

    @project_name.setter
    def project_name(self, value: str) -> None:
        ...

    @property
    def datacenter(self) -> str:
        """Name of the data center where the algorithm is physically located."""
        ...

    @datacenter.setter
    def datacenter(self, value: str) -> None:
        ...

    @property
    def public(self) -> bool:
        """Indicates if the algorithm is being live shared"""
        ...

    @public.setter
    def public(self, value: bool) -> None:
        ...

    @property
    def files(self) -> typing.List[QuantConnect.Api.ProjectFile]:
        """Files present in the project in which the algorithm is"""
        ...

    @files.setter
    def files(self, value: typing.List[QuantConnect.Api.ProjectFile]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @runtime_statistics.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @charts.setter
    def charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]) -> None:
        ...


class Portfolio(System.Object):
    """Class containing the basic portfolio information of a live algorithm"""

    @property
    def holdings(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Holding]:
        """Dictionary of algorithm holdings information"""
        ...

    @holdings.setter
    def holdings(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Holding]) -> None:
        ...

    @property
    def cash(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Dictionary of algorithm cash currencies information"""
        ...

    @cash.setter
    def cash(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]) -> None:
        ...


class PortfolioResponse(QuantConnect.Api.RestResponse):
    """Response class for reading the portfolio of a live algorithm"""

    @property
    def portfolio(self) -> QuantConnect.Api.Portfolio:
        """Object containing the basic portfolio information of a live algorithm"""
        ...

    @portfolio.setter
    def portfolio(self, value: QuantConnect.Api.Portfolio) -> None:
        ...


class LiveLog(QuantConnect.Api.RestResponse):
    """Logs from a live algorithm"""

    @property
    def logs(self) -> typing.List[str]:
        """List of logs from the live algorithm"""
        ...

    @logs.setter
    def logs(self, value: typing.List[str]) -> None:
        ...

    @property
    def length(self) -> int:
        """Total amount of rows in the logs"""
        ...

    @length.setter
    def length(self, value: int) -> None:
        ...

    @property
    def deployment_offset(self) -> int:
        """Amount of log rows before the current deployment"""
        ...

    @deployment_offset.setter
    def deployment_offset(self, value: int) -> None:
        ...


class DataLink(QuantConnect.Api.RestResponse):
    """Data/Read response wrapper, contains link to requested data"""

    @property
    def link(self) -> str:
        """Url to the data requested"""
        ...

    @link.setter
    def link(self, value: str) -> None:
        ...

    @property
    def balance(self) -> float:
        """Remaining QCC balance on account after this transaction"""
        ...

    @balance.setter
    def balance(self, value: float) -> None:
        ...

    @property
    def cost(self) -> float:
        """QCC Cost for this data link"""
        ...

    @cost.setter
    def cost(self, value: float) -> None:
        ...


class DataList(QuantConnect.Api.RestResponse):
    """Data/List response wrapper for available data"""

    @property
    def available_data(self) -> typing.List[str]:
        """List of all available data from this request"""
        ...

    @available_data.setter
    def available_data(self, value: typing.List[str]) -> None:
        ...


class PriceEntry(System.Object):
    """Prices entry for Data/Prices response"""

    @property
    def vendor(self) -> str:
        """Vendor for this price"""
        ...

    @vendor.setter
    def vendor(self, value: str) -> None:
        ...

    @property
    def reg_ex(self) -> System.Text.RegularExpressions.Regex:
        """
        Regex for this data price entry
        Trims regex open, close, and multiline flag
        because it won't match otherwise
        """
        ...

    @property
    def raw_reg_ex(self) -> str:
        """RegEx directly from response"""
        ...

    @raw_reg_ex.setter
    def raw_reg_ex(self, value: str) -> None:
        ...

    @property
    def price(self) -> typing.Optional[int]:
        """The price for this entry in QCC"""
        ...

    @price.setter
    def price(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def type(self) -> str:
        """The type associated to this price entry if any"""
        ...

    @type.setter
    def type(self, value: str) -> None:
        ...

    @property
    def subscribed(self) -> typing.Optional[bool]:
        """True if the user is subscribed"""
        ...

    @subscribed.setter
    def subscribed(self, value: typing.Optional[bool]) -> None:
        ...

    @property
    def product_id(self) -> int:
        """The associated product id"""
        ...

    @product_id.setter
    def product_id(self, value: int) -> None:
        ...

    @property
    def paths(self) -> System.Collections.Generic.HashSet[str]:
        """The associated data paths"""
        ...

    @paths.setter
    def paths(self, value: System.Collections.Generic.HashSet[str]) -> None:
        ...


class DataPricesList(QuantConnect.Api.RestResponse):
    """Data/Prices response wrapper for prices by vendor"""

    @property
    def prices(self) -> typing.List[QuantConnect.Api.PriceEntry]:
        """Collection of prices objects"""
        ...

    @prices.setter
    def prices(self, value: typing.List[QuantConnect.Api.PriceEntry]) -> None:
        ...

    @property
    def agreement_url(self) -> str:
        """The Agreement URL for this Organization"""
        ...

    @agreement_url.setter
    def agreement_url(self, value: str) -> None:
        ...

    def get_price(self, path: str) -> int:
        """
        Get the price in QCC for a given data file
        
        :param path: Lean data path of the file
        :returns: QCC price for data, -1 if no entry found.
        """
        ...


class BacktestReport(QuantConnect.Api.RestResponse):
    """Backtest Report Response wrapper"""

    @property
    def report(self) -> str:
        """HTML data of the report with embedded base64 images"""
        ...

    @report.setter
    def report(self, value: str) -> None:
        ...


class Card(System.Object):
    """Credit card"""

    @property
    def brand(self) -> str:
        """Credit card brand"""
        ...

    @brand.setter
    def brand(self, value: str) -> None:
        ...

    @property
    def expiration(self) -> datetime.datetime:
        """The credit card expiration"""
        ...

    @expiration.setter
    def expiration(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_four_digits(self) -> float:
        """The last 4 digits of the card"""
        ...

    @last_four_digits.setter
    def last_four_digits(self, value: float) -> None:
        ...


class Account(QuantConnect.Api.RestResponse):
    """Account information for an organization"""

    @property
    def organization_id(self) -> str:
        """The organization Id"""
        ...

    @organization_id.setter
    def organization_id(self, value: str) -> None:
        ...

    @property
    def credit_balance(self) -> float:
        """The current account balance"""
        ...

    @credit_balance.setter
    def credit_balance(self, value: float) -> None:
        ...

    @property
    def card(self) -> QuantConnect.Api.Card:
        """The current organizations credit card"""
        ...

    @card.setter
    def card(self, value: QuantConnect.Api.Card) -> None:
        ...


class DataAgreement(System.Object):
    """Organization Data Agreement"""

    @property
    def epoch_signed_time(self) -> typing.Optional[int]:
        """Epoch time the Data Agreement was Signed"""
        ...

    @epoch_signed_time.setter
    def epoch_signed_time(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def signed_time(self) -> typing.Optional[datetime.datetime]:
        """
        DateTime the agreement was signed.
        Uses EpochSignedTime converted to a standard datetime.
        """
        ...

    @property
    def signed(self) -> bool:
        """True/False if it is currently signed"""
        ...

    @signed.setter
    def signed(self, value: bool) -> None:
        ...


class Credit(System.Object):
    """Organization Credit Object"""

    @property
    def balance(self) -> float:
        """QCC Current Balance"""
        ...

    @balance.setter
    def balance(self, value: float) -> None:
        ...


class ProductType(IntEnum):
    """
    Product types offered by QuantConnect
    Used by Product class
    """

    PROFESSIONAL_SEATS = 0
    """Professional Seats Subscriptions"""

    BACKTEST_NODE = 1
    """Backtest Nodes Subscriptions"""

    RESEARCH_NODE = 2
    """Research Nodes Subscriptions"""

    LIVE_NODE = 3
    """Live Trading Nodes Subscriptions"""

    SUPPORT = 4
    """Support Subscriptions"""

    DATA = 5
    """Data Subscriptions"""

    MODULES = 6
    """Modules Subscriptions"""


class ProductItem(System.Object):
    """QuantConnect ProductItem"""

    @property
    def id(self) -> int:
        """ID for this product"""
        ...

    @id.setter
    def id(self, value: int) -> None:
        ...

    @property
    def quantity(self) -> int:
        """Quantity for this product"""
        ...

    @quantity.setter
    def quantity(self, value: int) -> None:
        ...


class Product(System.Object):
    """QuantConnect Products"""

    @property
    def type(self) -> QuantConnect.Api.ProductType:
        """Product Type"""
        ...

    @type.setter
    def type(self, value: QuantConnect.Api.ProductType) -> None:
        ...

    @property
    def items(self) -> typing.List[QuantConnect.Api.ProductItem]:
        """
        Collection of item subscriptions
        Nodes/Data/Seats/etc
        """
        ...

    @items.setter
    def items(self, value: typing.List[QuantConnect.Api.ProductItem]) -> None:
        ...


class Organization(QuantConnect.Api.StringRepresentation):
    """Object representation of Organization from QuantConnect Api"""

    @property
    def data_agreement(self) -> QuantConnect.Api.DataAgreement:
        """Data Agreement information"""
        ...

    @data_agreement.setter
    def data_agreement(self, value: QuantConnect.Api.DataAgreement) -> None:
        ...

    @property
    def products(self) -> typing.List[QuantConnect.Api.Product]:
        """Organization Product Subscriptions"""
        ...

    @products.setter
    def products(self, value: typing.List[QuantConnect.Api.Product]) -> None:
        ...

    @property
    def credit(self) -> QuantConnect.Api.Credit:
        """Organization Credit Balance and Transactions"""
        ...

    @credit.setter
    def credit(self, value: QuantConnect.Api.Credit) -> None:
        ...


class Estimate(QuantConnect.Api.StringRepresentation):
    """Estimate response packet from the QuantConnect.com API."""

    @property
    def estimate_id(self) -> str:
        """Estimate id"""
        ...

    @estimate_id.setter
    def estimate_id(self, value: str) -> None:
        ...

    @property
    def time(self) -> int:
        """Estimate time in seconds"""
        ...

    @time.setter
    def time(self, value: int) -> None:
        ...

    @property
    def balance(self) -> int:
        """Estimate balance in QCC"""
        ...

    @balance.setter
    def balance(self, value: int) -> None:
        ...


class BaseOptimization(QuantConnect.Api.RestResponse):
    """BaseOptimization item from the QuantConnect.com API."""

    @property
    def optimization_id(self) -> str:
        """Optimization ID"""
        ...

    @optimization_id.setter
    def optimization_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project ID of the project the optimization belongs to"""
        ...

    @project_id.setter
    def project_id(self, value: int) -> None:
        ...

    @property
    def name(self) -> str:
        """Name of the optimization"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def status(self) -> QuantConnect.Optimizer.OptimizationStatus:
        """Status of the optimization"""
        ...

    @status.setter
    def status(self, value: QuantConnect.Optimizer.OptimizationStatus) -> None:
        ...

    @property
    def node_type(self) -> str:
        """Optimization node type"""
        ...

    @node_type.setter
    def node_type(self, value: str) -> None:
        ...

    @property
    def out_of_sample_days(self) -> int:
        """Number of days of out of sample days"""
        ...

    @out_of_sample_days.setter
    def out_of_sample_days(self, value: int) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """End date of out of sample data"""
        ...

    @out_of_sample_max_end_date.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def parameters(self) -> typing.List[QuantConnect.Optimizer.Parameters.OptimizationParameter]:
        """Parameters used in this optimization"""
        ...

    @parameters.setter
    def parameters(self, value: typing.List[QuantConnect.Optimizer.Parameters.OptimizationParameter]) -> None:
        ...

    @property
    def criterion(self) -> QuantConnect.Optimizer.Objectives.Target:
        """Optimization statistical target"""
        ...

    @criterion.setter
    def criterion(self, value: QuantConnect.Optimizer.Objectives.Target) -> None:
        ...


class OptimizationSummary(QuantConnect.Api.BaseOptimization):
    """Optimization summary response for creating an optimization"""

    @property
    def created(self) -> datetime.datetime:
        """Date when this optimization was created"""
        ...

    @created.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def psr(self) -> typing.Optional[float]:
        """Price-sales ratio stastic"""
        ...

    @psr.setter
    def psr(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def sharpe_ratio(self) -> typing.Optional[float]:
        """Sharpe ratio statistic"""
        ...

    @sharpe_ratio.setter
    def sharpe_ratio(self, value: typing.Optional[float]) -> None:
        ...

    @property
    def trades(self) -> typing.Optional[int]:
        """Number of trades"""
        ...

    @trades.setter
    def trades(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def clone_id(self) -> typing.Optional[int]:
        """ID of project, were this current project was originally cloned"""
        ...

    @clone_id.setter
    def clone_id(self, value: typing.Optional[int]) -> None:
        ...


class OptimizationBacktest(System.Object):
    """OptimizationBacktest object from the QuantConnect.com API."""

    @property
    def progress(self) -> float:
        """Progress of the backtest as a percentage from 0-1 based on the days lapsed from start-finish."""
        ...

    @progress.setter
    def progress(self, value: float) -> None:
        ...

    @property
    def name(self) -> str:
        """The backtest name"""
        ...

    @property
    def host_name(self) -> str:
        """The backtest host name"""
        ...

    @host_name.setter
    def host_name(self, value: str) -> None:
        ...

    @property
    def backtest_id(self) -> str:
        """The backtest id"""
        ...

    @property
    def parameter_set(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """Represent a combination as key value of parameters, i.e. order doesn't matter"""
        ...

    @property
    def statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """The backtest statistics results"""
        ...

    @statistics.setter
    def statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def equity(self) -> QuantConnect.CandlestickSeries:
        """The backtest equity chart series"""
        ...

    @equity.setter
    def equity(self, value: QuantConnect.CandlestickSeries) -> None:
        ...

    @property
    def exit_code(self) -> int:
        """The exit code of this backtest"""
        ...

    @exit_code.setter
    def exit_code(self, value: int) -> None:
        ...

    @property
    def out_of_sample_max_end_date(self) -> typing.Optional[datetime.datetime]:
        """Backtest maximum end date"""
        ...

    @out_of_sample_max_end_date.setter
    def out_of_sample_max_end_date(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def out_of_sample_days(self) -> int:
        """The backtest out of sample day count"""
        ...

    @out_of_sample_days.setter
    def out_of_sample_days(self, value: int) -> None:
        ...

    @property
    def start_date(self) -> datetime.datetime:
        """The backtest start date"""
        ...

    @start_date.setter
    def start_date(self, value: datetime.datetime) -> None:
        ...

    @property
    def end_date(self) -> datetime.datetime:
        """The backtest end date"""
        ...

    @end_date.setter
    def end_date(self, value: datetime.datetime) -> None:
        ...

    def __init__(self, parameter_set: QuantConnect.Optimizer.Parameters.ParameterSet, backtest_id: str, name: str) -> None:
        """
        Creates a new instance
        
        :param parameter_set: The parameter set
        :param backtest_id: The backtest id if any
        :param name: The backtest name
        """
        ...


class Optimization(QuantConnect.Api.BaseOptimization):
    """Optimization response packet from the QuantConnect.com API."""

    @property
    def snapshot_id(self) -> typing.Optional[int]:
        """Snapshot ID of this optimization"""
        ...

    @snapshot_id.setter
    def snapshot_id(self, value: typing.Optional[int]) -> None:
        ...

    @property
    def optimization_target(self) -> str:
        """Statistic to be optimized"""
        ...

    @optimization_target.setter
    def optimization_target(self, value: str) -> None:
        ...

    @property
    def grid_layout(self) -> typing.List[QuantConnect.Api.GridChart]:
        """List with grid charts representing the grid layout"""
        ...

    @grid_layout.setter
    def grid_layout(self, value: typing.List[QuantConnect.Api.GridChart]) -> None:
        ...

    @property
    def runtime_statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics for the optimization"""
        ...

    @runtime_statistics.setter
    def runtime_statistics(self, value: System.Collections.Generic.IDictionary[str, str]) -> None:
        ...

    @property
    def constraints(self) -> typing.Sequence[QuantConnect.Optimizer.Objectives.Constraint]:
        """Optimization constraints"""
        ...

    @constraints.setter
    def constraints(self, value: typing.Sequence[QuantConnect.Optimizer.Objectives.Constraint]) -> None:
        ...

    @property
    def parallel_nodes(self) -> int:
        """Number of parallel nodes for optimization"""
        ...

    @parallel_nodes.setter
    def parallel_nodes(self, value: int) -> None:
        ...

    @property
    def backtests(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Api.OptimizationBacktest]:
        """Optimization constraints"""
        ...

    @backtests.setter
    def backtests(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Api.OptimizationBacktest]) -> None:
        ...

    @property
    def strategy(self) -> str:
        """Optimization strategy"""
        ...

    @strategy.setter
    def strategy(self, value: str) -> None:
        ...

    @property
    def requested(self) -> datetime.datetime:
        """Optimization requested date and time"""
        ...

    @requested.setter
    def requested(self, value: datetime.datetime) -> None:
        ...


class BasicObjectStore(System.Object):
    """Class contining basic store properties present in the REST response from QC API"""

    @property
    def key(self) -> str:
        """Object store key"""
        ...

    @key.setter
    def key(self, value: str) -> None:
        ...

    @property
    def modified(self) -> typing.Optional[datetime.datetime]:
        """Last time it was modified"""
        ...

    @modified.setter
    def modified(self, value: typing.Optional[datetime.datetime]) -> None:
        ...

    @property
    def mime(self) -> str:
        """MIME type"""
        ...

    @mime.setter
    def mime(self, value: str) -> None:
        ...

    @property
    def size(self) -> typing.Optional[float]:
        """File size"""
        ...

    @size.setter
    def size(self, value: typing.Optional[float]) -> None:
        ...


class PropertiesObjectStore(QuantConnect.Api.BasicObjectStore):
    """Object Store file properties"""

    @property
    def created(self) -> datetime.datetime:
        """Date this object was created"""
        ...

    @created.setter
    def created(self, value: datetime.datetime) -> None:
        ...

    @property
    def md_5(self) -> str:
        """MD5 (hashing algorithm) hash authentication code"""
        ...

    @md_5.setter
    def md_5(self, value: str) -> None:
        ...

    @property
    def preview(self) -> str:
        """Preview of the Object Store file content"""
        ...

    @preview.setter
    def preview(self, value: str) -> None:
        ...


class PropertiesObjectStoreResponse(QuantConnect.Api.RestResponse):
    """Response received containing the properties of the requested Object Store"""

    @property
    def properties(self) -> QuantConnect.Api.PropertiesObjectStore:
        """Object Store properties"""
        ...

    @properties.setter
    def properties(self, value: QuantConnect.Api.PropertiesObjectStore) -> None:
        ...


class SummaryObjectStore(QuantConnect.Api.BasicObjectStore):
    """Summary information of the Object Store"""

    @property
    def name(self) -> str:
        """File or folder name"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def is_folder(self) -> bool:
        """True if it is a folder, false otherwise"""
        ...

    @is_folder.setter
    def is_folder(self, value: bool) -> None:
        ...


class ListObjectStoreResponse(QuantConnect.Api.RestResponse):
    """Response received containing a list of stored objects metadata, as well as the total size of all of them."""

    @property
    def path(self) -> str:
        """Path to the files in the Object Store"""
        ...

    @path.setter
    def path(self, value: str) -> None:
        ...

    @property
    def objects(self) -> typing.List[QuantConnect.Api.SummaryObjectStore]:
        """List of objects stored"""
        ...

    @objects.setter
    def objects(self, value: typing.List[QuantConnect.Api.SummaryObjectStore]) -> None:
        ...

    @property
    def object_storage_used(self) -> int:
        """Size of all objects stored in bytes"""
        ...

    @object_storage_used.setter
    def object_storage_used(self, value: int) -> None:
        ...

    @property
    def object_storage_used_human(self) -> str:
        """Size of all the objects stored in human-readable format"""
        ...

    @object_storage_used_human.setter
    def object_storage_used_human(self, value: str) -> None:
        ...


class Api(System.Object, QuantConnect.Interfaces.IApi, QuantConnect.Interfaces.IDownloadProvider):
    """QuantConnect.com Interaction Via API."""

    @property
    def serializer_settings(self) -> typing.Any:
        """
        Serializer settings to use
        
        
        This codeEntityType is protected.
        """
        ...

    @serializer_settings.setter
    def serializer_settings(self, value: typing.Any) -> None:
        ...

    @property
    def api_connection(self) -> QuantConnect.Api.ApiConnection:
        """
        Returns the underlying API connection
        
        
        This codeEntityType is protected.
        """
        ...

    @property
    def connected(self) -> bool:
        """Check if Api is successfully connected with correct credentials"""
        ...

    def __init__(self) -> None:
        """Creates a new instance of Api"""
        ...

    def abort_optimization(self, optimization_id: str) -> QuantConnect.Api.RestResponse:
        """
        Abort an optimization
        
        :param optimization_id: Optimization id for the optimization we want to abort
        :returns: RestResponse.
        """
        ...

    def add_project_file(self, project_id: int, name: str, content: str) -> QuantConnect.Api.RestResponse:
        """
        Add a file to a project
        
        :param project_id: The project to which the file should be added
        :param name: The name of the new file
        :param content: The content of the new file
        :returns: ProjectFilesResponse that includes information about the newly created file.
        """
        ...

    def broadcast_live_command(self, organization_id: str, exclude_project_id: typing.Optional[int], command: typing.Any) -> QuantConnect.Api.RestResponse:
        """
        Broadcast a live command
        
        :param organization_id: Organization ID of the projects we would like to broadcast the command to
        :param exclude_project_id: Project for the live instance we want to exclude from the broadcast list
        :param command: The command to run
        :returns: RestResponse.
        """
        ...

    def create_api_connection(self, user_id: int, token: str) -> QuantConnect.Api.ApiConnection:
        """
        Create the api connection instance to use
        
        
        This codeEntityType is protected.
        """
        ...

    def create_backtest(self, project_id: int, compile_id: str, backtest_name: str) -> QuantConnect.Api.Backtest:
        """
        Create a new backtest request and get the id.
        
        :param project_id: Id for the project to backtest
        :param compile_id: Compile id for the project
        :param backtest_name: Name for the new backtest
        :returns: Backtestt.
        """
        ...

    def create_compile(self, project_id: int) -> QuantConnect.Api.Compile:
        """
        Create a new compile job request for this project id.
        
        :param project_id: Project id we wish to compile.
        :returns: Compile object result.
        """
        ...

    @overload
    def create_live_algorithm(self, project_id: int, compile_id: str, node_id: str, brokerage_settings: typing.Any, version_id: str = "-1", data_providers: typing.Any = None) -> QuantConnect.Api.CreateLiveAlgorithmResponse:
        """
        Create a live algorithm.
        
        :param project_id: Id of the project on QuantConnect
        :param compile_id: Id of the compilation on QuantConnect
        :param node_id: Id of the node that will run the algorithm
        :param brokerage_settings: Python Dictionary with brokerage specific settings. Each brokerage requires certain specific credentials
                                in order to process the given orders. Each key in this dictionary represents a required field/credential
                                to provide to the brokerage API and its value represents the value of that field. For example: "brokerage_settings: {
                                "id": "Binance", "binance-api-secret": "123ABC", "binance-api-key": "ABC123"}. It is worth saying,
                                that this dictionary must always contain an entry whose key is "id" and its value is the name of the brokerage
                                (see Brokerages.BrokerageName)
        :param version_id: The version of the Lean used to run the algorithm.
                                -1 is master, however, sometimes this can create problems with live deployments.
                                If you experience problems using, try specifying the version of Lean you would like to use.
        :param data_providers: Python Dictionary with data providers credentials. Each data provider requires certain credentials
                                in order to retrieve data from their API. Each key in this dictionary describes a data provider name
                                and its corresponding value is another dictionary with the required key-value pairs of credential
                                names and values. For example: "data_providers: { "InteractiveBrokersBrokerage" : { "id": 12345, "environment" : "paper",
                                "username": "testUsername", "password": "testPassword"}}"
        :returns: Information regarding the new algorithm CreateLiveAlgorithmResponse.
        """
        ...

    @overload
    def create_live_algorithm(self, project_id: int, compile_id: str, node_id: str, brokerage_settings: System.Collections.Generic.Dictionary[str, System.Object], version_id: str = "-1", data_providers: System.Collections.Generic.Dictionary[str, System.Object] = None) -> QuantConnect.Api.CreateLiveAlgorithmResponse:
        """
        Create a live algorithm.
        
        :param project_id: Id of the project on QuantConnect
        :param compile_id: Id of the compilation on QuantConnect
        :param node_id: Id of the node that will run the algorithm
        :param brokerage_settings: Dictionary with brokerage specific settings. Each brokerage requires certain specific credentials
                                in order to process the given orders. Each key in this dictionary represents a required field/credential
                                to provide to the brokerage API and its value represents the value of that field. For example: "brokerage_settings: {
                                "id": "Binance", "binance-api-secret": "123ABC", "binance-api-key": "ABC123"}. It is worth saying,
                                that this dictionary must always contain an entry whose key is "id" and its value is the name of the brokerage
                                (see Brokerages.BrokerageName)
        :param version_id: The version of the Lean used to run the algorithm.
                                -1 is master, however, sometimes this can create problems with live deployments.
                                If you experience problems using, try specifying the version of Lean you would like to use.
        :param data_providers: Dictionary with data providers credentials. Each data provider requires certain credentials
                                in order to retrieve data from their API. Each key in this dictionary describes a data provider name
                                and its corresponding value is another dictionary with the required key-value pairs of credential
                                names and values. For example: "data_providers: { "InteractiveBrokersBrokerage" : { "id": 12345, "environment" : "paper",
                                "username": "testUsername", "password": "testPassword"}}"
        :returns: Information regarding the new algorithm CreateLiveAlgorithmResponse.
        """
        ...

    def create_live_command(self, project_id: int, command: typing.Any) -> QuantConnect.Api.RestResponse:
        """
        Create a live command
        
        :param project_id: Project for the live instance we want to run the command against
        :param command: The command to run
        :returns: RestResponse.
        """
        ...

    def create_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: typing.Sequence[QuantConnect.Optimizer.Objectives.Constraint], estimated_cost: float, node_type: str, parallel_nodes: int) -> QuantConnect.Api.OptimizationSummary:
        """
        Create an optimization with the specified parameters via QuantConnect.com API
        
        :param project_id: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param target_to: Target extremum of the optimization, for example "max" or "min"
        :param target_value: Optimization target value
        :param strategy: Optimization strategy, QuantConnect.Optimizer.Strategies.GridSearchOptimizationStrategy
        :param compile_id: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :param estimated_cost: Estimated cost for optimization
        :param node_type: Optimization node type OptimizationNodes
        :param parallel_nodes: Number of parallel nodes for optimization
        :returns: BaseOptimization object from the API.
        """
        ...

    def create_project(self, name: str, language: QuantConnect.Language, organization_id: str = None) -> QuantConnect.Api.ProjectResponse:
        """
        Create a project with the specified name and language via QuantConnect.com API
        
        :param name: Project name
        :param language: Programming language to use
        :param organization_id: Optional param for specifying organization to create project under.
        If none provided web defaults to preferred.
        :returns: Project object from the API.
        """
        ...

    @staticmethod
    def create_secure_hash(timestamp: int, token: str) -> str:
        """
        Generate a secure hash for the authorization headers.
        
        :returns: Time based hash of user token and timestamp.
        """
        ...

    def delete_backtest(self, project_id: int, backtest_id: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a backtest from the specified project and backtest_id.
        
        :param project_id: Project for the backtest we want to delete
        :param backtest_id: Backtest id we want to delete
        :returns: RestResponse.
        """
        ...

    def delete_object_store(self, organization_id: str, key: str) -> QuantConnect.Api.RestResponse:
        """
        Request to delete Object Store metadata of a specific organization and key
        
        :param organization_id: Organization ID we would like to delete the Object Store file from
        :param key: Key to the Object Store file
        :returns: RestResponse.
        """
        ...

    def delete_optimization(self, optimization_id: str) -> QuantConnect.Api.RestResponse:
        """
        Delete an optimization
        
        :param optimization_id: Optimization id for the optimization we want to delete
        :returns: RestResponse.
        """
        ...

    def delete_project(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Delete a project
        
        :param project_id: Project id we own and wish to delete
        :returns: RestResponse indicating success.
        """
        ...

    def delete_project_file(self, project_id: int, name: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a file in a project
        
        :param project_id: Project id to which the file belongs
        :param name: The name of the file that should be deleted
        :returns: RestResponse that includes the information about all files in the project.
        """
        ...

    def dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def download(self, address: str, headers: typing.List[System.Collections.Generic.KeyValuePair[str, str]], user_name: str, password: str) -> str:
        """
        Local implementation for downloading data to algorithms
        
        :param address: URL to download
        :param headers: KVP headers
        :param user_name: Username for basic authentication
        :param password: Password for basic authentication
        """
        ...

    def download_bytes(self, address: str, headers: typing.List[System.Collections.Generic.KeyValuePair[str, str]], user_name: str, password: str) -> typing.List[int]:
        """
        Local implementation for downloading data to algorithms
        
        :param address: URL to download
        :param headers: KVP headers
        :param user_name: Username for basic authentication
        :param password: Password for basic authentication
        :returns: A stream from which the data can be read.
        """
        ...

    def download_data(self, file_path: str, organization_id: str) -> bool:
        """
        Method to purchase and download data from QuantConnect
        
        :param file_path: File path representing the data requested
        :param organization_id: Organization to buy the data with
        :returns: A bool indicating whether the data was successfully downloaded or not.
        """
        ...

    def estimate_optimization(self, project_id: int, name: str, target: str, target_to: str, target_value: typing.Optional[float], strategy: str, compile_id: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: typing.Sequence[QuantConnect.Optimizer.Objectives.Constraint]) -> QuantConnect.Api.Estimate:
        """
        Estimate optimization with the specified parameters via QuantConnect.com API
        
        :param project_id: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param target_to: Target extremum of the optimization, for example "max" or "min"
        :param target_value: Optimization target value
        :param strategy: Optimization strategy, QuantConnect.Optimizer.Strategies.GridSearchOptimizationStrategy
        :param compile_id: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :returns: Estimate object from the API.
        """
        ...

    @staticmethod
    def format_path_for_data_request(file_path: str, data_folder: str = None) -> str:
        """
        Helper method to normalize path for api data requests
        
        :param file_path: Filepath to format
        :param data_folder: The data folder to use
        :returns: Normalized path.
        """
        ...

    def get_algorithm_status(self, algorithm_id: str) -> QuantConnect.AlgorithmControl:
        """
        Get the algorithm status from the user with this algorithm id.
        
        :param algorithm_id: String algorithm id we're searching for.
        :returns: Algorithm status enum.
        """
        ...

    def get_object_store(self, organization_id: str, keys: typing.List[str], destination_folder: str = None) -> bool:
        """
        Download the object store files associated with the given organization ID and key
        
        :param organization_id: Organization ID we would like to get the Object Store files from
        :param keys: Keys for the Object Store files
        :param destination_folder: Folder in which the object store files will be stored
        :returns: True if the object store files were retrieved correctly, false otherwise.
        """
        ...

    def get_object_store_properties(self, organization_id: str, key: str) -> QuantConnect.Api.PropertiesObjectStoreResponse:
        """
        Get Object Store properties given the organization ID and the Object Store key
        
        :param organization_id: Organization ID we would like to get the Object Store from
        :param key: Key for the Object Store file
        :returns: PropertiesObjectStoreResponse.
        """
        ...

    def initialize(self, user_id: int, token: str, data_folder: str) -> None:
        """Initialize the API with the given variables"""
        ...

    def liquidate_live_algorithm(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Liquidate a live algorithm from the specified project and deployId.
        
        :param project_id: Project for the live instance we want to stop
        :returns: RestResponse.
        """
        ...

    def list_backtests(self, project_id: int, include_statistics: bool = True) -> QuantConnect.Api.BacktestSummaryList:
        """
        List all the backtest summaries for a project
        
        :param project_id: Project id we'd like to get a list of backtest for
        :param include_statistics: True for include statistics in the response, false otherwise
        :returns: BacktestList.
        """
        ...

    def list_live_algorithms(self, status: typing.Optional[QuantConnect.AlgorithmStatus] = None) -> QuantConnect.Api.LiveList:
        """
        Get a list of live running algorithms for user
        
        :param status: Filter the statuses of the algorithms returned from the api
        :returns: LiveList.
        """
        ...

    def list_object_store(self, organization_id: str, path: str) -> QuantConnect.Api.ListObjectStoreResponse:
        """
        Request to list Object Store files of a specific organization and path
        
        :param organization_id: Organization ID we would like to list the Object Store files from
        :param path: Path to the Object Store files
        :returns: ListObjectStoreResponse.
        """
        ...

    def list_optimizations(self, project_id: int) -> typing.List[QuantConnect.Api.OptimizationSummary]:
        """
        List all the optimizations for a project
        
        :param project_id: Project id we'd like to get a list of optimizations for
        :returns: A list of BaseOptimization objects, BaseOptimization.
        """
        ...

    def list_projects(self) -> QuantConnect.Api.ProjectResponse:
        """
        List details of all projects
        
        :returns: ProjectResponse that contains information regarding the project.
        """
        ...

    def read_account(self, organization_id: str = None) -> QuantConnect.Api.Account:
        """
        Will read the organization account status
        
        :param organization_id: The target organization id, if null will return default organization
        """
        ...

    def read_backtest(self, project_id: int, backtest_id: str, get_charts: bool = True) -> QuantConnect.Api.Backtest:
        """
        Read out a backtest in the project id specified.
        
        :param project_id: Project id to read
        :param backtest_id: Specific backtest id to read
        :param get_charts: True will return backtest charts
        :returns: Backtest.
        """
        ...

    def read_backtest_chart(self, project_id: int, name: str, start: int, end: int, count: int, backtest_id: str) -> QuantConnect.Api.ReadChartResponse:
        """
        Returns a requested chart object from a backtest
        
        :param project_id: Project ID of the request
        :param name: The requested chart name
        :param start: The Utc start seconds timestamp of the request
        :param end: The Utc end seconds timestamp of the request
        :param count: The number of data points to request
        :param backtest_id: Associated Backtest ID for this chart request
        :returns: The chart.
        """
        ...

    def read_backtest_insights(self, project_id: int, backtest_id: str, start: int = 0, end: int = 0) -> QuantConnect.Api.InsightResponse:
        """
        Read out the insights of a backtest
        
        :param project_id: Id of the project from which to read the backtest
        :param backtest_id: Backtest id from which we want to get the insights
        :param start: Starting index of the insights to be fetched
        :param end: Last index of the insights to be fetched. Note that end - start must be less than 100
        :returns: InsightResponse.
        """
        ...

    def read_backtest_orders(self, project_id: int, backtest_id: str, start: int = 0, end: int = 100) -> typing.List[QuantConnect.Orders.ApiOrderResponse]:
        """
        Returns the orders of the specified backtest and project id.
        
        :param project_id: Id of the project from which to read the orders
        :param backtest_id: Id of the backtest from which to read the orders
        :param start: Starting index of the orders to be fetched. Required if end > 100
        :param end: Last index of the orders to be fetched. Note that end - start must be less than 100
        :returns: The list of Order.
        """
        ...

    def read_backtest_report(self, project_id: int, backtest_id: str) -> QuantConnect.Api.BacktestReport:
        """
        Read out the report of a backtest in the project id specified.
        
        :param project_id: Project id to read
        :param backtest_id: Specific backtest id to read
        :returns: BacktestReport.
        """
        ...

    def read_compile(self, project_id: int, compile_id: str) -> QuantConnect.Api.Compile:
        """
        Read a compile packet job result.
        
        :param project_id: Project id we sent for compile
        :param compile_id: Compile id return from the creation request
        :returns: Compile.
        """
        ...

    def read_data_directory(self, file_path: str) -> QuantConnect.Api.DataList:
        """Get valid data entries for a given filepath from data/list"""
        ...

    def read_data_link(self, file_path: str, organization_id: str) -> QuantConnect.Api.DataLink:
        """
        Gets the link to the downloadable data.
        
        :param file_path: File path representing the data requested
        :param organization_id: Organization to download from
        :returns: DataLink to the downloadable data.
        """
        ...

    def read_data_prices(self, organization_id: str) -> QuantConnect.Api.DataPricesList:
        """Gets data prices from data/prices"""
        ...

    def read_lean_versions(self) -> QuantConnect.Api.VersionsResponse:
        """Gets a list of LEAN versions with their corresponding basic descriptions"""
        ...

    def read_live_algorithm(self, project_id: int, deploy_id: str) -> QuantConnect.Api.LiveAlgorithmResults:
        """
        Read out a live algorithm in the project id specified.
        
        :param project_id: Project id to read
        :param deploy_id: Specific instance id to read
        :returns: LiveAlgorithmResults.
        """
        ...

    def read_live_chart(self, project_id: int, name: str, start: int, end: int, count: int) -> QuantConnect.Api.ReadChartResponse:
        """
        Returns a chart object from a live algorithm
        
        :param project_id: Project ID of the request
        :param name: The requested chart name
        :param start: The Utc start seconds timestamp of the request
        :param end: The Utc end seconds timestamp of the request
        :param count: The number of data points to request
        :returns: The chart.
        """
        ...

    def read_live_insights(self, project_id: int, start: int = 0, end: int = 0) -> QuantConnect.Api.InsightResponse:
        """
        Read out the insights of a live algorithm
        
        :param project_id: Id of the project from which to read the live algorithm
        :param start: Starting index of the insights to be fetched
        :param end: Last index of the insights to be fetched. Note that end - start must be less than 100
        :returns: InsightResponse.
        """
        ...

    def read_live_logs(self, project_id: int, algorithm_id: str, start_line: int, end_line: int) -> QuantConnect.Api.LiveLog:
        """
        Gets the logs of a specific live algorithm
        
        :param project_id: Project Id of the live running algorithm
        :param algorithm_id: Algorithm Id of the live running algorithm
        :param start_line: Start line of logs to read
        :param end_line: End line of logs to read
        :returns: LiveLog List of strings that represent the logs of the algorithm.
        """
        ...

    def read_live_orders(self, project_id: int, start: int = 0, end: int = 100) -> typing.List[QuantConnect.Orders.ApiOrderResponse]:
        """
        Returns the orders of the specified project id live algorithm.
        
        :param project_id: Id of the project from which to read the live orders
        :param start: Starting index of the orders to be fetched. Required if end > 100
        :param end: Last index of the orders to be fetched. Note that end - start must be less than 100
        :returns: The list of Order.
        """
        ...

    def read_live_portfolio(self, project_id: int) -> QuantConnect.Api.PortfolioResponse:
        """
        Read out the portfolio state of a live algorithm
        
        :param project_id: Id of the project from which to read the live algorithm
        :returns: PortfolioResponse.
        """
        ...

    def read_optimization(self, optimization_id: str) -> QuantConnect.Api.Optimization:
        """
        Read an optimization
        
        :param optimization_id: Optimization id for the optimization we want to read
        :returns: Optimization.
        """
        ...

    def read_organization(self, organization_id: str = None) -> QuantConnect.Api.Organization:
        """
        Fetch organization data from web API
        
        :param organization_id: 
        """
        ...

    def read_project(self, project_id: int) -> QuantConnect.Api.ProjectResponse:
        """
        Get details about a single project
        
        :param project_id: Id of the project
        :returns: ProjectResponse that contains information regarding the project.
        """
        ...

    def read_project_file(self, project_id: int, file_name: str) -> QuantConnect.Api.ProjectFilesResponse:
        """
        Read a file in a project
        
        :param project_id: Project id to which the file belongs
        :param file_name: The name of the file
        :returns: ProjectFilesResponse that includes the file information.
        """
        ...

    def read_project_files(self, project_id: int) -> QuantConnect.Api.ProjectFilesResponse:
        """
        Read all files in a project
        
        :param project_id: Project id to which the file belongs
        :returns: ProjectFilesResponse that includes the information about all files in the project.
        """
        ...

    def read_project_nodes(self, project_id: int) -> QuantConnect.Api.ProjectNodesResponse:
        """
        Read all nodes in a project.
        
        :param project_id: Project id to which the nodes refer
        :returns: ProjectNodesResponse that includes the information about all nodes in the project.
        """
        ...

    def send_notification(self, notification: QuantConnect.Notifications.Notification, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Sends a notification
        
        :param notification: The notification to send
        :param project_id: The project id
        :returns: RestResponse containing success response and errors.
        """
        ...

    def send_statistics(self, algorithm_id: str, unrealized: float, fees: float, net_profit: float, holdings: float, equity: float, net_return: float, volume: float, trades: int, sharpe: float) -> None:
        """
        Send the statistics to storage for performance tracking.
        
        :param algorithm_id: Identifier for algorithm
        :param unrealized: Unrealized gainloss
        :param fees: Total fees
        :param net_profit: Net profi
        :param holdings: Algorithm holdings
        :param equity: Total equity
        :param net_return: Net return for the deployment
        :param volume: Volume traded
        :param trades: Total trades since inception
        :param sharpe: Sharpe ratio since inception
        """
        ...

    def set_algorithm_status(self, algorithm_id: str, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """
        Algorithm passes back its current status to the UX.
        
        :param status: Status of the current algorithm
        :param algorithm_id: String algorithm id we're setting.
        :param message: Message for the algorithm status event
        :returns: Algorithm status enum.
        """
        ...

    def set_object_store(self, organization_id: str, key: str, object_data: typing.List[int]) -> QuantConnect.Api.RestResponse:
        """
        Upload files to the Object Store
        
        :param organization_id: Organization ID we would like to upload the file to
        :param key: Key to the Object Store file
        :param object_data: File (as an array of bytes) to be uploaded
        :returns: RestResponse.
        """
        ...

    def stop_live_algorithm(self, project_id: int) -> QuantConnect.Api.RestResponse:
        """
        Stop a live algorithm from the specified project and deployId.
        
        :param project_id: Project for the live instance we want to stop
        :returns: RestResponse.
        """
        ...

    def update_backtest(self, project_id: int, backtest_id: str, name: str = None, note: str = ...) -> QuantConnect.Api.RestResponse:
        """
        Update a backtest name
        
        :param project_id: Project for the backtest we want to update
        :param backtest_id: Backtest id we want to update
        :param name: Name we'd like to assign to the backtest
        :param note: Note attached to the backtest
        :returns: RestResponse.
        """
        ...

    def update_backtest_tags(self, project_id: int, backtest_id: str, tags: typing.Sequence[str]) -> QuantConnect.Api.RestResponse:
        """
        Updates the tags collection for a backtest
        
        :param project_id: Project for the backtest we want to update
        :param backtest_id: Backtest id we want to update
        :param tags: The new backtest tags
        :returns: RestResponse.
        """
        ...

    def update_optimization(self, optimization_id: str, name: str = None) -> QuantConnect.Api.RestResponse:
        """
        Update an optimization
        
        :param optimization_id: Optimization id we want to update
        :param name: Name we'd like to assign to the optimization
        :returns: RestResponse.
        """
        ...

    def update_project_file_content(self, project_id: int, file_name: str, new_file_contents: str) -> QuantConnect.Api.RestResponse:
        """
        Update the contents of a file
        
        :param project_id: Project id to which the file belongs
        :param file_name: The name of the file that should be updated
        :param new_file_contents: The new contents of the file
        :returns: RestResponse indicating success.
        """
        ...

    def update_project_file_name(self, project_id: int, old_file_name: str, new_file_name: str) -> QuantConnect.Api.RestResponse:
        """
        Update the name of a file
        
        :param project_id: Project id to which the file belongs
        :param old_file_name: The current name of the file
        :param new_file_name: The new name for the file
        :returns: RestResponse indicating success.
        """
        ...

    def update_project_nodes(self, project_id: int, nodes: typing.List[str]) -> QuantConnect.Api.ProjectNodesResponse:
        """
        Update the active state of some nodes to true.
        If you don't provide any nodes, all the nodes become inactive and AutoSelectNode is true.
        
        :param project_id: Project id to which the nodes refer
        :param nodes: List of node ids to update
        :returns: ProjectNodesResponse that includes the information about all nodes in the project.
        """
        ...


class OrganizationResponse(QuantConnect.Api.RestResponse):
    """Response wrapper for Organizations/Read"""

    @property
    def organization(self) -> QuantConnect.Api.Organization:
        """Organization read from the response"""
        ...

    @organization.setter
    def organization(self, value: QuantConnect.Api.Organization) -> None:
        ...


class Authentication(System.Object):
    """Helper methods for api authentication and interaction"""

    @staticmethod
    @overload
    def hash(timestamp: int) -> str:
        """
        Generate a secure hash for the authorization headers.
        
        :returns: Time based hash of user token and timestamp.
        """
        ...

    @staticmethod
    @overload
    def hash(timestamp: int, token: str) -> str:
        """
        Generate a secure hash for the authorization headers.
        
        :returns: Time based hash of user token and timestamp.
        """
        ...

    @staticmethod
    def link(endpoint: str, payload: typing.List[System.Collections.Generic.KeyValuePair[str, System.Object]] = None) -> str:
        """
        Create an authenticated link for the target endpoint using the optional given payload
        
        :param endpoint: The endpoint
        :param payload: The payload
        :returns: The authenticated link to trigger the request.
        """
        ...

    @staticmethod
    def populate_query_string(query_string: System.Collections.Specialized.NameValueCollection, payload: typing.List[System.Collections.Generic.KeyValuePair[str, System.Object]] = None) -> None:
        """Helper method to populate a query string with the given payload"""
        ...


class LiveAlgorithmResultsJsonConverter:
    """Custom JsonConverter for LiveResults data for live algorithms"""

    @property
    def can_write(self) -> bool:
        """Gets a value indicating whether this Newtonsoft.Json.JsonConverter can write JSON."""
        ...

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class AuthenticationResponse(QuantConnect.Api.RestResponse):
    """Verify if the credentials are OK."""


class ParameterSetJsonConverter:
    """Json converter for ParameterSet which creates a light weight easy to consume serialized version"""

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """Writes a JSON object from a Parameter set"""
        ...


class OptimizationBacktestJsonConverter:
    """Json converter for OptimizationBacktest which creates a light weight easy to consume serialized version"""

    def can_convert(self, object_type: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param object_type: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def read_json(self, reader: typing.Any, object_type: typing.Type, existing_value: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param object_type: Type of the object.
        :param existing_value: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def write_json(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class OptimizationResponseWrapper(QuantConnect.Api.RestResponse):
    """Wrapper class for Optimizations/Read endpoint JSON response"""

    @property
    def optimization(self) -> QuantConnect.Api.Optimization:
        """Optimization object"""
        ...

    @optimization.setter
    def optimization(self, value: QuantConnect.Api.Optimization) -> None:
        ...


class OptimizationList(QuantConnect.Api.RestResponse):
    """Collection container for a list of summarized optimizations for a project"""

    @property
    def optimizations(self) -> typing.List[QuantConnect.Api.OptimizationSummary]:
        """Collection of summarized optimization objects"""
        ...

    @optimizations.setter
    def optimizations(self, value: typing.List[QuantConnect.Api.OptimizationSummary]) -> None:
        ...

    @property
    def count(self) -> int:
        """The optimization count"""
        ...


class CreatedNode(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/create, reads in the nodes information into a
    node object
    """

    @property
    def node(self) -> QuantConnect.Api.Node:
        """The created node from node/create"""
        ...

    @node.setter
    def node(self, value: QuantConnect.Api.Node) -> None:
        ...


class NodeType(IntEnum):
    """
    NodeTypes enum for all possible options of target environments
    Used in conjuction with SKU class as a NodeType is a required parameter for SKU
    """

    BACKTEST = 0
    """A node for running backtests (0)"""

    RESEARCH = 1
    """A node for running research (1)"""

    LIVE = 2
    """A node for live trading (2)"""


class SKU(System.Object):
    """
    Class for generating a SKU for a node with a given configuration
    Every SKU is made up of 3 variables:
    - Target environment (L for live, B for Backtest, R for Research)
    - CPU core count
    - Dedicated RAM (GB)
    """

    @property
    def cores(self) -> int:
        """The number of CPU cores in the node"""
        ...

    @cores.setter
    def cores(self, value: int) -> None:
        ...

    @property
    def memory(self) -> int:
        """Size of RAM in GB of the Node"""
        ...

    @memory.setter
    def memory(self, value: int) -> None:
        ...

    @property
    def target(self) -> QuantConnect.Api.NodeType:
        """Target environment for the node"""
        ...

    @target.setter
    def target(self, value: QuantConnect.Api.NodeType) -> None:
        ...

    def __init__(self, cores: int, memory: int, target: QuantConnect.Api.NodeType) -> None:
        """
        Constructs a SKU object out of the provided node configuration
        
        :param cores: Number of cores
        :param memory: Size of RAM in GBs
        :param target: Target Environment Live/Backtest/Research
        """
        ...

    def to_string(self) -> str:
        """
        Generates the SKU string for API calls based on the specifications of the node
        
        :returns: String representation of the SKU.
        """
        ...


class OptimizationNodes(System.Object):
    """Supported optimization nodes"""

    O_2_8: str
    """2 CPUs 8 GB ram"""

    O_4_12: str
    """4 CPUs 12 GB ram"""

    O_8_16: str
    """8 CPUs 16 GB ram"""


class LiveResultsData(System.Object):
    """Holds information about the state and operation of the live running algorithm"""

    @property
    def version(self) -> int:
        """Results version"""
        ...

    @version.setter
    def version(self, value: int) -> None:
        ...

    @property
    def resolution(self) -> QuantConnect.Resolution:
        """Temporal resolution of the results returned from the Api"""
        ...

    @resolution.setter
    def resolution(self, value: QuantConnect.Resolution) -> None:
        ...

    @property
    def results(self) -> QuantConnect.Packets.LiveResult:
        """Class to represent the data groups results return from the Api"""
        ...

    @results.setter
    def results(self, value: QuantConnect.Packets.LiveResult) -> None:
        ...


class LiveAlgorithmApiSettingsWrapper(System.Object):
    """Helper class to put BaseLiveAlgorithmSettings in proper format."""

    @property
    def version_id(self) -> str:
        """-1 is master"""
        ...

    @version_id.setter
    def version_id(self, value: str) -> None:
        ...

    @property
    def project_id(self) -> int:
        """Project id for the live instance"""
        ...

    @property
    def compile_id(self) -> str:
        """Compile Id for the live algorithm"""
        ...

    @property
    def node_id(self) -> str:
        """Id of the node being used to run live algorithm"""
        ...

    @property
    def signature(self) -> str:
        """Signature of the live algorithm"""
        ...

    @property
    def automatic_redeploy(self) -> bool:
        """
        True to enable Automatic Re-Deploy of the live algorithm,
        false otherwise
        """
        ...

    @property
    def brokerage(self) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """The API expects the settings as part of a brokerage object"""
        ...

    @property
    def data_providers(self) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Dictionary with the data providers and their corresponding credentials"""
        ...

    @property
    def parameters(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Dictionary with the parameters to be used in the live algorithm"""
        ...

    @property
    def notification(self) -> System.Collections.Generic.Dictionary[str, typing.List[str]]:
        """Dictionary with the lists of events and targets"""
        ...

    def __init__(self, project_id: int, compile_id: str, node_id: str, settings: System.Collections.Generic.Dictionary[str, System.Object], version: str = "-1", data_providers: System.Collections.Generic.Dictionary[str, System.Object] = None, parameters: System.Collections.Generic.Dictionary[str, str] = None, notification: System.Collections.Generic.Dictionary[str, typing.List[str]] = None) -> None:
        """
        Constructor for LiveAlgorithmApiSettingsWrapper
        
        :param project_id: Id of project from QuantConnect
        :param compile_id: Id of compilation of project from QuantConnect
        :param node_id: Server type to run live Algorithm
        :param settings: Dictionary with brokerage specific settings. Each brokerage requires certain specific credentials
                                in order to process the given orders. Each key in this dictionary represents a required field/credential
                                to provide to the brokerage API and its value represents the value of that field. For example: "brokerageSettings: {
                                "id": "Binance", "binance-api-secret": "123ABC", "binance-api-key": "ABC123"}. It is worth saying,
                                that this dictionary must always contain an entry whose key is "id" and its value is the name of the brokerage
                                (see Brokerages.BrokerageName)
        :param version: The version identifier
        :param data_providers: Dictionary with data providers credentials. Each data provider requires certain credentials
                                in order to retrieve data from their API. Each key in this dictionary describes a data provider name
                                and its corresponding value is another dictionary with the required key-value pairs of credential
                                names and values. For example: "data_providers: {InteractiveBrokersBrokerage : { "id": 12345, "environement" : "paper",
                                "username": "testUsername", "password": "testPassword"}}"
        :param parameters: Dictionary to specify the parameters for the live algorithm
        :param notification: Dictionary with the lists of events and targets
        """
        ...


class GetObjectStoreResponse(QuantConnect.Api.RestResponse):
    """Response received when fetching Object Store"""

    @property
    def job_id(self) -> str:
        """Job ID which can be used for querying state or packaging"""
        ...

    @job_id.setter
    def job_id(self, value: str) -> None:
        ...

    @property
    def url(self) -> str:
        """The URL to download the object. This can also be null"""
        ...

    @url.setter
    def url(self, value: str) -> None:
        ...


class BacktestResponseWrapper(QuantConnect.Api.RestResponse):
    """
    Wrapper class for Backtest/* endpoints JSON response
    Currently used by Backtest/Read and Backtest/Create
    """

    @property
    def backtest(self) -> QuantConnect.Api.Backtest:
        """Backtest Object"""
        ...

    @backtest.setter
    def backtest(self, value: QuantConnect.Api.Backtest) -> None:
        ...

    @property
    def debugging(self) -> bool:
        """Indicates if the backtest is run under debugging mode"""
        ...

    @debugging.setter
    def debugging(self, value: bool) -> None:
        ...


class BacktestList(QuantConnect.Api.RestResponse):
    """Collection container for a list of backtests for a project"""

    @property
    def backtests(self) -> typing.List[QuantConnect.Api.Backtest]:
        """Collection of summarized backtest objects"""
        ...

    @backtests.setter
    def backtests(self, value: typing.List[QuantConnect.Api.Backtest]) -> None:
        ...


class BacktestTags(QuantConnect.Api.RestResponse):
    """Collection container for a list of backtest tags"""

    @property
    def tags(self) -> typing.List[str]:
        """Collection of tags for a backtest"""
        ...

    @tags.setter
    def tags(self, value: typing.List[str]) -> None:
        ...


class EstimateResponseWrapper(QuantConnect.Api.RestResponse):
    """
    Wrapper class for Optimizations/* endpoints JSON response
    Currently used by Optimizations/Estimate
    """

    @property
    def estimate(self) -> QuantConnect.Api.Estimate:
        """Estimate object"""
        ...

    @estimate.setter
    def estimate(self, value: QuantConnect.Api.Estimate) -> None:
        ...


