from typing import overload
from enum import IntEnum
import abc
import datetime
import typing

import QuantConnect.Api
import QuantConnect.Brokerages.Authentication
import System
import System.Threading
import System.Threading.Tasks

AuthenticationHeaderValue = typing.Any
HttpResponseMessage = typing.Any

QuantConnect_Brokerages_Authentication_OAuthTokenHandler_TRequest = typing.TypeVar("QuantConnect_Brokerages_Authentication_OAuthTokenHandler_TRequest")
QuantConnect_Brokerages_Authentication_OAuthTokenHandler_TResponse = typing.TypeVar("QuantConnect_Brokerages_Authentication_OAuthTokenHandler_TResponse")


class AccessTokenMetaDataRequest(System.Object, metaclass=abc.ABCMeta):
    """Represents the base request for obtaining an access token, including brokerage and account information."""

    @property
    def brokerage(self) -> str:
        """
        Gets the name of the brokerage associated with the access token request.
        The value is normalized to lowercase.
        """
        ...

    @property
    def account_id(self) -> str:
        """Gets the account identifier (e.g., account number) associated with the brokerage."""
        ...

    def __init__(self, brokerage: str, account_id: str) -> None:
        """
        Initializes a new instance of the AccessTokenMetaDataRequest class.
        
        
        This codeEntityType is protected.
        
        :param brokerage: The name of the brokerage making the request. Will be normalized to lowercase.
        :param account_id: The account number or identifier associated with the brokerage.
        """
        ...

    def to_json(self) -> str:
        """
        Serializes the request into a compact JSON string with camelCase property naming.
        
        :returns: A JSON string representing the current request.
        """
        ...


class TokenType(IntEnum):
    """Defines the supported types of access tokens used for authentication."""

    BEARER = 0
    """A Bearer token, typically used for standard HTTP Authorization headers."""

    SESSION_TOKEN = 1
    """A Session token, typically used for username/password authorization headers."""


class TokenCredentials(System.Object):
    """
    Represents credentials required for token-based authentication,
    including the access token and its type (e.g., Bearer).
    """

    @property
    def token_type(self) -> QuantConnect.Brokerages.Authentication.TokenType:
        """Gets the type of the token (e.g., Bearer)."""
        ...

    @property
    def access_token(self) -> str:
        """Gets the token string used for authentication."""
        ...

    def __init__(self, token_type: QuantConnect.Brokerages.Authentication.TokenType, access_token: str) -> None:
        """
        Initializes a new instance of the TokenCredentials class.
        
        :param token_type: The type of the token.
        :param access_token: The token string.
        """
        ...


class TokenHandler(metaclass=abc.ABCMeta):
    """
    Provides base functionality for token-based HTTP request handling,
    including automatic retries and token refresh on unauthorized responses.
    """

    def __init__(self, create_auth_header: typing.Callable[[QuantConnect.Brokerages.Authentication.TokenType, str], AuthenticationHeaderValue] = None, retry_interval: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initializes a new instance of the TokenHandler class.
        
        
        This codeEntityType is protected.
        
        :param create_auth_header: An optional delegate for creating an AuthenticationHeaderValue
        from the token type and access token. If not provided, a default implementation is used.
        :param retry_interval: An optional time interval to wait between retry attempts when fetching the token or retrying a failed request.
        If null, the default interval of 5 seconds is used.
        """
        ...

    def get_access_token(self, cancellation_token: System.Threading.CancellationToken) -> QuantConnect.Brokerages.Authentication.TokenCredentials:
        """
        Retrieves a valid access token for authenticating HTTP requests.
        Must be implemented by derived classes to provide token type and value,
        with optional support for caching and refresh logic.
        
        :param cancellation_token: A cancellation token that can be used to cancel the token retrieval operation.
        :returns: A TokenCredentials instance containing the token type and access token string.
        """
        ...

    def send(self, request: typing.Any, cancellation_token: System.Threading.CancellationToken) -> typing.Any:
        """
        Sends an HTTP request synchronously with retry support.
        This override includes token-based authentication and refresh logic on 401 Unauthorized responses.
        
        
        This codeEntityType is protected.
        
        :param request: The HTTP request message to send.
        :param cancellation_token: A cancellation token to cancel operation.
        :returns: The HTTP response message.
        """
        ...

    def send_async(self, request: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[HttpResponseMessage]:
        """
        Sends an HTTP request asynchronously by internally invoking the synchronous send(HttpRequestMessage, CancellationToken) method.
        This is useful for compatibility with components that require an asynchronous pipeline, even though the core logic is synchronous.
        
        
        This codeEntityType is protected.
        
        :param request: The HTTP request message to send.
        :param cancellation_token: A cancellation token to cancel the operation.
        :returns: A task representing the asynchronous operation, containing the HTTP response message.
        """
        ...


class OAuthTokenHandler(typing.Generic[QuantConnect_Brokerages_Authentication_OAuthTokenHandler_TRequest, QuantConnect_Brokerages_Authentication_OAuthTokenHandler_TResponse], QuantConnect.Brokerages.Authentication.TokenHandler):
    """
    Handles OAuth token retrieval and caching by interacting with the Lean platform.
    Implements retry and expiration logic for secure HTTP communication.
    """

    def __init__(self, api_client: QuantConnect.Api.ApiConnection, model_request: QuantConnect_Brokerages_Authentication_OAuthTokenHandler_TRequest) -> None:
        """
        Initializes a new instance of the OAuthTokenHandler{TRequest, TResponse} class.
        
        :param api_client: The API client used to communicate with the Lean platform.
        :param model_request: The request model used to generate the access token.
        """
        ...

    def get_access_token(self, cancellation_token: System.Threading.CancellationToken) -> QuantConnect.Brokerages.Authentication.TokenCredentials:
        """
        Retrieves a valid access token from the Lean platform.
        Caches and reuses tokens until expiration to minimize unnecessary requests.
        
        :param cancellation_token: A token used to observe cancellation requests.
        :returns: A tuple containing the token type and access token string.
        """
        ...


class AccessTokenMetaDataResponse(QuantConnect.Api.RestResponse, metaclass=abc.ABCMeta):
    """Represents a response containing metadata about an access token issued by Lean."""

    @property
    def access_token(self) -> str:
        """Gets the access token provided by Lean."""
        ...

    @property
    def token_type(self) -> QuantConnect.Brokerages.Authentication.TokenType:
        """Gets the type of the token (e.g., "Bearer")."""
        ...

    @property
    def expiration(self) -> datetime.datetime:
        """Gets the UTC expiration timestamp of the access token, with a 1-minute safety buffer applied."""
        ...

    @expiration.setter
    def expiration(self, value: datetime.datetime) -> None:
        ...

    def __init__(self, access_token: str, token_type: QuantConnect.Brokerages.Authentication.TokenType, expires: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the AccessTokenMetaDataResponse class.
        
        
        This codeEntityType is protected.
        
        :param access_token: The access token string provided by the authentication service.
        :param token_type: The type of the token (e.g., Bearer).
        :param expires: The expiration time of the access token (in UTC), with safety buffer applied.
        """
        ...


