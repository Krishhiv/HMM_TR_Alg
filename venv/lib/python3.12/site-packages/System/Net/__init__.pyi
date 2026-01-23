from typing import overload
from enum import IntEnum
import abc
import datetime
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.IO
import System.Net
import System.Net.Sockets
import System.Runtime.Serialization
import System.Security
import System.Security.Authentication.ExtendedProtection

System_Net_IPNetwork = typing.Any
System_Net_IPAddress = typing.Any
System_Net_IPEndPoint = typing.Any


class WebUtility(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def html_decode(value: str) -> str:
        ...

    @staticmethod
    @overload
    def html_decode(value: str, output: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    @overload
    def html_encode(value: str) -> str:
        ...

    @staticmethod
    @overload
    def html_encode(value: str, output: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    def url_decode(encoded_value: str) -> str:
        ...

    @staticmethod
    def url_decode_to_bytes(encoded_value: typing.List[int], offset: int, count: int) -> typing.List[int]:
        ...

    @staticmethod
    def url_encode(value: str) -> str:
        ...

    @staticmethod
    def url_encode_to_bytes(value: typing.List[int], offset: int, count: int) -> typing.List[int]:
        ...


class ICredentials(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_credential(self, uri: System.Uri, auth_type: str) -> System.Net.NetworkCredential:
        ...


class ICredentialsByHost(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_credential(self, host: str, port: int, authentication_type: str) -> System.Net.NetworkCredential:
        ...


class NetworkCredential(System.Object, System.Net.ICredentials, System.Net.ICredentialsByHost):
    """This class has no documentation."""

    @property
    def user_name(self) -> str:
        ...

    @user_name.setter
    def user_name(self, value: str) -> None:
        ...

    @property
    def password(self) -> str:
        ...

    @password.setter
    def password(self, value: str) -> None:
        ...

    @property
    def secure_password(self) -> System.Security.SecureString:
        ...

    @secure_password.setter
    def secure_password(self, value: System.Security.SecureString) -> None:
        ...

    @property
    def domain(self) -> str:
        ...

    @domain.setter
    def domain(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: str) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: str, domain: str) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: System.Security.SecureString) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: System.Security.SecureString, domain: str) -> None:
        ...

    @overload
    def get_credential(self, uri: System.Uri, authentication_type: str) -> System.Net.NetworkCredential:
        ...

    @overload
    def get_credential(self, host: str, port: int, authentication_type: str) -> System.Net.NetworkCredential:
        ...


class DecompressionMethods(IntEnum):
    """This class has no documentation."""

    NONE = 0

    G_ZIP = ...

    DEFLATE = ...

    BROTLI = ...

    ALL = ...


class IWebProxy(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def credentials(self) -> System.Net.ICredentials:
        ...

    @credentials.setter
    def credentials(self, value: System.Net.ICredentials) -> None:
        ...

    def get_proxy(self, destination: System.Uri) -> System.Uri:
        ...

    def is_bypassed(self, host: System.Uri) -> bool:
        ...


class TransportContext(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_channel_binding(self, kind: System.Security.Authentication.ExtendedProtection.ChannelBindingKind) -> System.Security.Authentication.ExtendedProtection.ChannelBinding:
        ...


class Cookie(System.Object):
    """This class has no documentation."""

    @property
    def comment(self) -> str:
        ...

    @comment.setter
    def comment(self, value: str) -> None:
        ...

    @property
    def comment_uri(self) -> System.Uri:
        ...

    @comment_uri.setter
    def comment_uri(self, value: System.Uri) -> None:
        ...

    @property
    def http_only(self) -> bool:
        ...

    @http_only.setter
    def http_only(self, value: bool) -> None:
        ...

    @property
    def discard(self) -> bool:
        ...

    @discard.setter
    def discard(self, value: bool) -> None:
        ...

    @property
    def domain(self) -> str:
        ...

    @domain.setter
    def domain(self, value: str) -> None:
        ...

    @property
    def expired(self) -> bool:
        ...

    @expired.setter
    def expired(self, value: bool) -> None:
        ...

    @property
    def expires(self) -> datetime.datetime:
        ...

    @expires.setter
    def expires(self, value: datetime.datetime) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def path(self) -> str:
        ...

    @path.setter
    def path(self, value: str) -> None:
        ...

    @property
    def port(self) -> str:
        ...

    @port.setter
    def port(self, value: str) -> None:
        ...

    @property
    def secure(self) -> bool:
        ...

    @secure.setter
    def secure(self, value: bool) -> None:
        ...

    @property
    def time_stamp(self) -> datetime.datetime:
        ...

    @property
    def value(self) -> str:
        ...

    @value.setter
    def value(self, value: str) -> None:
        ...

    @property
    def version(self) -> int:
        ...

    @version.setter
    def version(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str, path: str) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str, path: str, domain: str) -> None:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class CookieCollection(System.Object, System.Collections.Generic.ICollection[System.Net.Cookie], System.Collections.Generic.IReadOnlyCollection[System.Net.Cookie], System.Collections.ICollection, typing.Iterable[System.Net.Cookie]):
    """This class has no documentation."""

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    @overload
    def __getitem__(self, index: int) -> System.Net.Cookie:
        ...

    @overload
    def __getitem__(self, name: str) -> System.Net.Cookie:
        ...

    def __init__(self) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Net.Cookie]:
        ...

    @overload
    def add(self, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def add(self, cookies: System.Net.CookieCollection) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, cookie: System.Net.Cookie) -> bool:
        ...

    @overload
    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System.Net.Cookie], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def remove(self, cookie: System.Net.Cookie) -> bool:
        ...


class CookieContainer(System.Object):
    """This class has no documentation."""

    DEFAULT_COOKIE_LIMIT: int = 300

    DEFAULT_PER_DOMAIN_COOKIE_LIMIT: int = 20

    DEFAULT_COOKIE_LENGTH_LIMIT: int = 4096

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def max_cookie_size(self) -> int:
        ...

    @max_cookie_size.setter
    def max_cookie_size(self, value: int) -> None:
        ...

    @property
    def per_domain_capacity(self) -> int:
        ...

    @per_domain_capacity.setter
    def per_domain_capacity(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, capacity: int, per_domain_capacity: int, max_cookie_size: int) -> None:
        ...

    @overload
    def add(self, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def add(self, cookies: System.Net.CookieCollection) -> None:
        ...

    @overload
    def add(self, uri: System.Uri, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def add(self, uri: System.Uri, cookies: System.Net.CookieCollection) -> None:
        ...

    def get_all_cookies(self) -> System.Net.CookieCollection:
        ...

    def get_cookie_header(self, uri: System.Uri) -> str:
        ...

    def get_cookies(self, uri: System.Uri) -> System.Net.CookieCollection:
        ...

    def set_cookies(self, uri: System.Uri, cookie_header: str) -> None:
        ...


class PathList(System.Object):
    """This class has no documentation."""


class HttpVersion(System.Object):
    """This class has no documentation."""

    UNKNOWN: System.Version = ...

    VERSION_10: System.Version = ...

    VERSION_11: System.Version = ...

    VERSION_20: System.Version = ...

    VERSION_30: System.Version = ...


class HttpStatusCode(IntEnum):
    """This class has no documentation."""

    CONTINUE = 100

    SWITCHING_PROTOCOLS = 101

    PROCESSING = 102

    EARLY_HINTS = 103

    OK = 200

    CREATED = 201

    ACCEPTED = 202

    NON_AUTHORITATIVE_INFORMATION = 203

    NO_CONTENT = 204

    RESET_CONTENT = 205

    PARTIAL_CONTENT = 206

    MULTI_STATUS = 207

    ALREADY_REPORTED = 208

    IM_USED = 226

    MULTIPLE_CHOICES = 300

    AMBIGUOUS = 300

    MOVED_PERMANENTLY = 301

    MOVED = 301

    FOUND = 302

    REDIRECT = 302

    SEE_OTHER = 303

    REDIRECT_METHOD = 303

    NOT_MODIFIED = 304

    USE_PROXY = 305

    UNUSED = 306

    TEMPORARY_REDIRECT = 307

    REDIRECT_KEEP_VERB = 307

    PERMANENT_REDIRECT = 308

    BAD_REQUEST = 400

    UNAUTHORIZED = 401

    PAYMENT_REQUIRED = 402

    FORBIDDEN = 403

    NOT_FOUND = 404

    METHOD_NOT_ALLOWED = 405

    NOT_ACCEPTABLE = 406

    PROXY_AUTHENTICATION_REQUIRED = 407

    REQUEST_TIMEOUT = 408

    CONFLICT = 409

    GONE = 410

    LENGTH_REQUIRED = 411

    PRECONDITION_FAILED = 412

    REQUEST_ENTITY_TOO_LARGE = 413

    REQUEST_URI_TOO_LONG = 414

    UNSUPPORTED_MEDIA_TYPE = 415

    REQUESTED_RANGE_NOT_SATISFIABLE = 416

    EXPECTATION_FAILED = 417

    MISDIRECTED_REQUEST = 421

    UNPROCESSABLE_ENTITY = 422

    UNPROCESSABLE_CONTENT = 422

    LOCKED = 423

    FAILED_DEPENDENCY = 424

    UPGRADE_REQUIRED = 426

    PRECONDITION_REQUIRED = 428

    TOO_MANY_REQUESTS = 429

    REQUEST_HEADER_FIELDS_TOO_LARGE = 431

    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    INTERNAL_SERVER_ERROR = 500

    NOT_IMPLEMENTED = 501

    BAD_GATEWAY = 502

    SERVICE_UNAVAILABLE = 503

    GATEWAY_TIMEOUT = 504

    HTTP_VERSION_NOT_SUPPORTED = 505

    VARIANT_ALSO_NEGOTIATES = 506

    INSUFFICIENT_STORAGE = 507

    LOOP_DETECTED = 508

    NOT_EXTENDED = 510

    NETWORK_AUTHENTICATION_REQUIRED = 511


class EndPoint(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    def create(self, socket_address: System.Net.SocketAddress) -> System.Net.EndPoint:
        ...

    def serialize(self) -> System.Net.SocketAddress:
        ...


class DnsEndPoint(System.Net.EndPoint):
    """This class has no documentation."""

    @property
    def host(self) -> str:
        ...

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    @property
    def port(self) -> int:
        ...

    @overload
    def __init__(self, host: str, port: int) -> None:
        ...

    @overload
    def __init__(self, host: str, port: int, address_family: System.Net.Sockets.AddressFamily) -> None:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class CredentialCache(System.Object, System.Net.ICredentials, System.Net.ICredentialsByHost, System.Collections.IEnumerable):
    """This class has no documentation."""

    DEFAULT_CREDENTIALS: System.Net.ICredentials

    DEFAULT_NETWORK_CREDENTIALS: System.Net.NetworkCredential

    def __init__(self) -> None:
        ...

    @overload
    def add(self, uri_prefix: System.Uri, auth_type: str, cred: System.Net.NetworkCredential) -> None:
        ...

    @overload
    def add(self, host: str, port: int, authentication_type: str, credential: System.Net.NetworkCredential) -> None:
        ...

    @overload
    def get_credential(self, uri_prefix: System.Uri, auth_type: str) -> System.Net.NetworkCredential:
        ...

    @overload
    def get_credential(self, host: str, port: int, authentication_type: str) -> System.Net.NetworkCredential:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def remove(self, uri_prefix: System.Uri, auth_type: str) -> None:
        ...

    @overload
    def remove(self, host: str, port: int, authentication_type: str) -> None:
        ...


class IPAddress(System.Object, System.ISpanFormattable, System.ISpanParsable[System_Net_IPAddress], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Net_IPAddress]):
    """This class has no documentation."""

    ANY: System.Net.IPAddress = ...

    LOOPBACK: System.Net.IPAddress = ...

    BROADCAST: System.Net.IPAddress = ...

    NONE: System.Net.IPAddress = ...

    I_PV_6_ANY: System.Net.IPAddress = ...

    I_PV_6_LOOPBACK: System.Net.IPAddress = ...

    I_PV_6_NONE: System.Net.IPAddress = ...

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    @property
    def scope_id(self) -> int:
        ...

    @scope_id.setter
    def scope_id(self, value: int) -> None:
        ...

    @property
    def is_i_pv_6_multicast(self) -> bool:
        ...

    @property
    def is_i_pv_6_link_local(self) -> bool:
        ...

    @property
    def is_i_pv_6_site_local(self) -> bool:
        ...

    @property
    def is_i_pv_6_teredo(self) -> bool:
        ...

    @property
    def is_i_pv_6_unique_local(self) -> bool:
        ...

    @property
    def is_i_pv_4_mapped_to_i_pv_6(self) -> bool:
        ...

    @property
    def address(self) -> int:
        warnings.warn("IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead.", DeprecationWarning)

    @address.setter
    def address(self, value: int) -> None:
        warnings.warn("IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead.", DeprecationWarning)

    @overload
    def __init__(self, new_address: int) -> None:
        ...

    @overload
    def __init__(self, address: typing.List[int], scopeid: int) -> None:
        ...

    @overload
    def __init__(self, address: System.ReadOnlySpan[int], scopeid: int) -> None:
        ...

    @overload
    def __init__(self, address: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, address: System.ReadOnlySpan[int]) -> None:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        ...

    def get_address_bytes(self) -> typing.List[int]:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def host_to_network_order(host: int) -> int:
        ...

    @staticmethod
    def is_loopback(address: System.Net.IPAddress) -> bool:
        ...

    @staticmethod
    def is_valid(ip_span: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    def is_valid_utf_8(utf_8_text: System.ReadOnlySpan[int]) -> bool:
        ...

    def map_to_i_pv_4(self) -> System.Net.IPAddress:
        ...

    def map_to_i_pv_6(self) -> System.Net.IPAddress:
        ...

    @staticmethod
    def network_to_host_order(network: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(ip_string: str) -> System.Net.IPAddress:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Net.IPAddress:
        ...

    @staticmethod
    @overload
    def parse(ip_span: System.ReadOnlySpan[str]) -> System.Net.IPAddress:
        ...

    def to_string(self) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(ip_string: str, address: typing.Optional[System.Net.IPAddress]) -> typing.Tuple[bool, System.Net.IPAddress]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Net.IPAddress]) -> typing.Tuple[bool, System.Net.IPAddress]:
        ...

    @staticmethod
    @overload
    def try_parse(ip_span: System.ReadOnlySpan[str], address: typing.Optional[System.Net.IPAddress]) -> typing.Tuple[bool, System.Net.IPAddress]:
        ...

    def try_write_bytes(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class IPNetwork(System.IEquatable[System_Net_IPNetwork], System.ISpanFormattable, System.ISpanParsable[System_Net_IPNetwork], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Net_IPNetwork]):
    """This class has no documentation."""

    @property
    def base_address(self) -> System.Net.IPAddress:
        ...

    @property
    def prefix_length(self) -> int:
        ...

    def __eq__(self, right: System.Net.IPNetwork) -> bool:
        ...

    def __init__(self, base_address: System.Net.IPAddress, prefix_length: int) -> None:
        ...

    def __ne__(self, right: System.Net.IPNetwork) -> bool:
        ...

    def contains(self, address: System.Net.IPAddress) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Net.IPNetwork) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Net.IPNetwork:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str]) -> System.Net.IPNetwork:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Net.IPNetwork:
        ...

    def to_string(self) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Net.IPNetwork]) -> typing.Tuple[bool, System.Net.IPNetwork]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Net.IPNetwork]) -> typing.Tuple[bool, System.Net.IPNetwork]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Net.IPNetwork]) -> typing.Tuple[bool, System.Net.IPNetwork]:
        ...


class CookieVariant(IntEnum):
    """This class has no documentation."""

    UNKNOWN = 0

    PLAIN = 1

    RFC_2109 = 2

    RFC_2965 = 3

    DEFAULT = ...


class IPEndPoint(System.Net.EndPoint, System.ISpanFormattable, System.ISpanParsable[System_Net_IPEndPoint], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Net_IPEndPoint]):
    """This class has no documentation."""

    MIN_PORT: int = ...

    MAX_PORT: int = ...

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    @property
    def address(self) -> System.Net.IPAddress:
        ...

    @address.setter
    def address(self, value: System.Net.IPAddress) -> None:
        ...

    @property
    def port(self) -> int:
        ...

    @port.setter
    def port(self, value: int) -> None:
        ...

    @overload
    def __init__(self, address: int, port: int) -> None:
        ...

    @overload
    def __init__(self, address: System.Net.IPAddress, port: int) -> None:
        ...

    def create(self, socket_address: System.Net.SocketAddress) -> System.Net.EndPoint:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Net.IPEndPoint:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str]) -> System.Net.IPEndPoint:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Net.IPEndPoint:
        ...

    def serialize(self) -> System.Net.SocketAddress:
        ...

    def to_string(self) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Net.IPEndPoint]) -> typing.Tuple[bool, System.Net.IPEndPoint]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Net.IPEndPoint]) -> typing.Tuple[bool, System.Net.IPEndPoint]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Net.IPEndPoint]) -> typing.Tuple[bool, System.Net.IPEndPoint]:
        ...


class CookieException(System.FormatException, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, serialization_info: System.Runtime.Serialization.SerializationInfo, streaming_context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, serialization_info: System.Runtime.Serialization.SerializationInfo, streaming_context: System.Runtime.Serialization.StreamingContext) -> None:
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class AuthenticationSchemes(IntEnum):
    """This class has no documentation."""

    NONE = ...

    DIGEST = ...

    NEGOTIATE = ...

    NTLM = ...

    BASIC = ...

    ANONYMOUS = ...

    INTEGRATED_WINDOWS_AUTHENTICATION = ...


