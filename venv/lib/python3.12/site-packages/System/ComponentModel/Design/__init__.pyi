from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Collections
import System.ComponentModel
import System.ComponentModel.Design
import System.Globalization
import System.IO
import System.Reflection
import System.Resources
import System.Runtime.InteropServices
import System.Runtime.Serialization

IServiceProvider = typing.Any

System_ComponentModel_Design__EventContainer_Callable = typing.TypeVar("System_ComponentModel_Design__EventContainer_Callable")
System_ComponentModel_Design__EventContainer_ReturnType = typing.TypeVar("System_ComponentModel_Design__EventContainer_ReturnType")


class TypeDescriptionProviderService(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def get_provider(self, instance: typing.Any) -> System.ComponentModel.TypeDescriptionProvider:
        ...

    @overload
    def get_provider(self, type: typing.Type) -> System.ComponentModel.TypeDescriptionProvider:
        ...


class IResourceService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_resource_reader(self, info: System.Globalization.CultureInfo) -> System.Resources.IResourceReader:
        ...

    def get_resource_writer(self, info: System.Globalization.CultureInfo) -> typing.Any:
        ...


class ITypeDescriptorFilterService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def filter_attributes(self, component: System.ComponentModel.IComponent, attributes: System.Collections.IDictionary) -> bool:
        ...

    def filter_events(self, component: System.ComponentModel.IComponent, events: System.Collections.IDictionary) -> bool:
        ...

    def filter_properties(self, component: System.ComponentModel.IComponent, properties: System.Collections.IDictionary) -> bool:
        ...


class IEventBindingService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def create_unique_method_name(self, component: System.ComponentModel.IComponent, e: System.ComponentModel.EventDescriptor) -> str:
        ...

    def get_compatible_methods(self, e: System.ComponentModel.EventDescriptor) -> System.Collections.ICollection:
        ...

    def get_event(self, property: System.ComponentModel.PropertyDescriptor) -> System.ComponentModel.EventDescriptor:
        ...

    def get_event_properties(self, events: System.ComponentModel.EventDescriptorCollection) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_event_property(self, e: System.ComponentModel.EventDescriptor) -> System.ComponentModel.PropertyDescriptor:
        ...

    @overload
    def show_code(self) -> bool:
        ...

    @overload
    def show_code(self, line_number: int) -> bool:
        ...

    @overload
    def show_code(self, component: System.ComponentModel.IComponent, e: System.ComponentModel.EventDescriptor) -> bool:
        ...


class HelpKeywordAttribute(System.Attribute):
    """This class has no documentation."""

    DEFAULT: System.ComponentModel.Design.HelpKeywordAttribute = ...

    @property
    def help_keyword(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, keyword: str) -> None:
        ...

    @overload
    def __init__(self, t: typing.Type) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class IDesignerOptionService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_option_value(self, page_name: str, value_name: str) -> System.Object:
        ...

    def set_option_value(self, page_name: str, value_name: str, value: typing.Any) -> None:
        ...


class DesignerOptionService(System.Object, System.ComponentModel.Design.IDesignerOptionService, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class DesignerOptionCollection(System.Object, System.Collections.IList):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        @property
        def name(self) -> str:
            ...

        @property
        def parent(self) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            ...

        @property
        def properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
            ...

        @overload
        def __getitem__(self, index: int) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            ...

        @overload
        def __getitem__(self, name: str) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            ...

        def copy_to(self, array: System.Array, index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.IEnumerator:
            ...

        def index_of(self, value: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection) -> int:
            ...

        def show_dialog(self) -> bool:
            ...

    @property
    def options(self) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
        ...

    def create_option_collection(self, parent: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection, name: str, value: typing.Any) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
        ...

    def populate_option_collection(self, options: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection) -> None:
        ...

    def show_dialog(self, options: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection, option_object: typing.Any) -> bool:
        ...


class IServiceContainer(IServiceProvider, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any) -> None:
        ...

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any, promote: bool) -> None:
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object]) -> None:
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object], promote: bool) -> None:
        ...

    @overload
    def remove_service(self, service_type: typing.Type) -> None:
        ...

    @overload
    def remove_service(self, service_type: typing.Type, promote: bool) -> None:
        ...


class ServiceContainer(System.Object, System.ComponentModel.Design.IServiceContainer, System.IDisposable):
    """This class has no documentation."""

    @property
    def default_services(self) -> typing.List[typing.Type]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, parent_provider: typing.Optional[IServiceProvider]) -> None:
        ...

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any) -> None:
        ...

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any, promote: bool) -> None:
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object]) -> None:
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object], promote: bool) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        ...

    def get_service(self, service_type: typing.Type) -> System.Object:
        ...

    @overload
    def remove_service(self, service_type: typing.Type) -> None:
        ...

    @overload
    def remove_service(self, service_type: typing.Type, promote: bool) -> None:
        ...


class ViewTechnology(IntEnum):
    """This class has no documentation."""

    PASSTHROUGH = 0

    WINDOWS_FORMS = 1

    DEFAULT = 2


class DesignerTransaction(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def canceled(self) -> bool:
        ...

    @property
    def committed(self) -> bool:
        ...

    @property
    def description(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, description: str) -> None:
        ...

    def cancel(self) -> None:
        ...

    def commit(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        ...

    def on_cancel(self) -> None:
        ...

    def on_commit(self) -> None:
        ...


class StandardToolWindows(System.Object):
    """This class has no documentation."""

    OBJECT_BROWSER: System.Guid = ...

    OUTPUT_WINDOW: System.Guid = ...

    PROJECT_EXPLORER: System.Guid = ...

    PROPERTY_BROWSER: System.Guid = ...

    RELATED_LINKS: System.Guid = ...

    SERVER_EXPLORER: System.Guid = ...

    TASK_LIST: System.Guid = ...

    TOOLBOX: System.Guid = ...


class HelpKeywordType(IntEnum):
    """This class has no documentation."""

    F_1_KEYWORD = 0

    GENERAL_KEYWORD = 1

    FILTER_KEYWORD = 2


class CommandID(System.Object):
    """This class has no documentation."""

    @property
    def id(self) -> int:
        ...

    @property
    def guid(self) -> System.Guid:
        ...

    def __init__(self, menu_group: System.Guid, command_id: int) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class MenuCommand(System.Object):
    """This class has no documentation."""

    @property
    def checked(self) -> bool:
        ...

    @checked.setter
    def checked(self, value: bool) -> None:
        ...

    @property
    def enabled(self) -> bool:
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...

    @property
    def properties(self) -> System.Collections.IDictionary:
        ...

    @property
    def supported(self) -> bool:
        ...

    @supported.setter
    def supported(self, value: bool) -> None:
        ...

    @property
    def visible(self) -> bool:
        ...

    @visible.setter
    def visible(self, value: bool) -> None:
        ...

    @property
    def command_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @command_changed.setter
    def command_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    def command_id(self) -> System.ComponentModel.Design.CommandID:
        ...

    @property
    def ole_status(self) -> int:
        ...

    def __init__(self, handler: typing.Callable[[System.Object, System.EventArgs], typing.Any], command: System.ComponentModel.Design.CommandID) -> None:
        ...

    @overload
    def invoke(self, arg: typing.Any) -> None:
        ...

    @overload
    def invoke(self) -> None:
        ...

    def on_command_changed(self, e: System.EventArgs) -> None:
        ...

    def to_string(self) -> str:
        ...


class DesignerVerb(System.ComponentModel.Design.MenuCommand):
    """This class has no documentation."""

    @property
    def description(self) -> str:
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def text(self) -> str:
        ...

    @overload
    def __init__(self, text: str, handler: typing.Callable[[System.Object, System.EventArgs], typing.Any]) -> None:
        ...

    @overload
    def __init__(self, text: str, handler: typing.Callable[[System.Object, System.EventArgs], typing.Any], start_command_id: System.ComponentModel.Design.CommandID) -> None:
        ...

    def to_string(self) -> str:
        ...


class DesignerVerbCollection(System.Collections.CollectionBase):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System.ComponentModel.Design.DesignerVerb:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[System.ComponentModel.Design.DesignerVerb]) -> None:
        ...

    def __setitem__(self, index: int, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def add(self, value: System.ComponentModel.Design.DesignerVerb) -> int:
        ...

    @overload
    def add_range(self, value: typing.List[System.ComponentModel.Design.DesignerVerb]) -> None:
        ...

    @overload
    def add_range(self, value: System.ComponentModel.Design.DesignerVerbCollection) -> None:
        ...

    def contains(self, value: System.ComponentModel.Design.DesignerVerb) -> bool:
        ...

    def copy_to(self, array: typing.List[System.ComponentModel.Design.DesignerVerb], index: int) -> None:
        ...

    def index_of(self, value: System.ComponentModel.Design.DesignerVerb) -> int:
        ...

    def insert(self, index: int, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def on_validate(self, value: typing.Any) -> None:
        ...

    def remove(self, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...


class IDesignerFilter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def post_filter_attributes(self, attributes: System.Collections.IDictionary) -> None:
        ...

    def post_filter_events(self, events: System.Collections.IDictionary) -> None:
        ...

    def post_filter_properties(self, properties: System.Collections.IDictionary) -> None:
        ...

    def pre_filter_attributes(self, attributes: System.Collections.IDictionary) -> None:
        ...

    def pre_filter_events(self, events: System.Collections.IDictionary) -> None:
        ...

    def pre_filter_properties(self, properties: System.Collections.IDictionary) -> None:
        ...


class ComponentRenameEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def component(self) -> System.Object:
        ...

    @property
    def old_name(self) -> str:
        ...

    @property
    def new_name(self) -> str:
        ...

    def __init__(self, component: typing.Any, old_name: str, new_name: str) -> None:
        ...


class CheckoutException(System.Runtime.InteropServices.ExternalException):
    """This class has no documentation."""

    CANCELED: System.ComponentModel.Design.CheckoutException = ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, error_code: int) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ComponentChangedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def component(self) -> System.Object:
        ...

    @property
    def member(self) -> System.ComponentModel.MemberDescriptor:
        ...

    @property
    def new_value(self) -> System.Object:
        ...

    @property
    def old_value(self) -> System.Object:
        ...

    def __init__(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor, old_value: typing.Any, new_value: typing.Any) -> None:
        ...


class IExtenderListService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_extender_providers(self) -> typing.List[System.ComponentModel.IExtenderProvider]:
        ...


class IDesigner(System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def component(self) -> System.ComponentModel.IComponent:
        ...

    @property
    @abc.abstractmethod
    def verbs(self) -> System.ComponentModel.Design.DesignerVerbCollection:
        ...

    def do_default_action(self) -> None:
        ...

    def initialize(self, component: System.ComponentModel.IComponent) -> None:
        ...


class DesignerTransactionCloseEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def transaction_committed(self) -> bool:
        ...

    @property
    def last_transaction(self) -> bool:
        ...

    @overload
    def __init__(self, commit: bool, last_transaction: bool) -> None:
        ...

    @overload
    def __init__(self, commit: bool) -> None:
        ...


class IDesignerHost(System.ComponentModel.Design.IServiceContainer, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def loading(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def in_transaction(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def container(self) -> System.ComponentModel.IContainer:
        ...

    @property
    @abc.abstractmethod
    def root_component(self) -> System.ComponentModel.IComponent:
        ...

    @property
    @abc.abstractmethod
    def root_component_class_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def transaction_description(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def activated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @activated.setter
    def activated(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def deactivated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @deactivated.setter
    def deactivated(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def load_complete(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @load_complete.setter
    def load_complete(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_closed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], typing.Any], typing.Any]:
        ...

    @transaction_closed.setter
    def transaction_closed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_closing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], typing.Any], typing.Any]:
        ...

    @transaction_closing.setter
    def transaction_closing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_opened(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @transaction_opened.setter
    def transaction_opened(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_opening(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @transaction_opening.setter
    def transaction_opening(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    def activate(self) -> None:
        ...

    @overload
    def create_component(self, component_class: typing.Type) -> System.ComponentModel.IComponent:
        ...

    @overload
    def create_component(self, component_class: typing.Type, name: str) -> System.ComponentModel.IComponent:
        ...

    @overload
    def create_transaction(self) -> System.ComponentModel.Design.DesignerTransaction:
        ...

    @overload
    def create_transaction(self, description: str) -> System.ComponentModel.Design.DesignerTransaction:
        ...

    def destroy_component(self, component: System.ComponentModel.IComponent) -> None:
        ...

    def get_designer(self, component: System.ComponentModel.IComponent) -> System.ComponentModel.Design.IDesigner:
        ...

    def get_type(self, type_name: str) -> typing.Type:
        ...


class ActiveDesignerEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def old_designer(self) -> System.ComponentModel.Design.IDesignerHost:
        ...

    @property
    def new_designer(self) -> System.ComponentModel.Design.IDesignerHost:
        ...

    def __init__(self, old_designer: System.ComponentModel.Design.IDesignerHost, new_designer: System.ComponentModel.Design.IDesignerHost) -> None:
        ...


class ComponentChangingEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def component(self) -> System.Object:
        ...

    @property
    def member(self) -> System.ComponentModel.MemberDescriptor:
        ...

    def __init__(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        ...


class IComponentInitializer(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def initialize_existing_component(self, default_values: System.Collections.IDictionary) -> None:
        ...

    def initialize_new_component(self, default_values: System.Collections.IDictionary) -> None:
        ...


class IMenuCommandService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def verbs(self) -> System.ComponentModel.Design.DesignerVerbCollection:
        ...

    def add_command(self, command: System.ComponentModel.Design.MenuCommand) -> None:
        ...

    def add_verb(self, verb: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def find_command(self, command_id: System.ComponentModel.Design.CommandID) -> System.ComponentModel.Design.MenuCommand:
        ...

    def global_invoke(self, command_id: System.ComponentModel.Design.CommandID) -> bool:
        ...

    def remove_command(self, command: System.ComponentModel.Design.MenuCommand) -> None:
        ...

    def remove_verb(self, verb: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def show_context_menu(self, menu_id: System.ComponentModel.Design.CommandID, x: int, y: int) -> None:
        ...


class ComponentEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def component(self) -> System.ComponentModel.IComponent:
        ...

    def __init__(self, component: System.ComponentModel.IComponent) -> None:
        ...


class IComponentChangeService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def component_added(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]:
        ...

    @component_added.setter
    def component_added(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_adding(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]:
        ...

    @component_adding.setter
    def component_adding(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangedEventArgs], typing.Any], typing.Any]:
        ...

    @component_changed.setter
    def component_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangedEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_changing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangingEventArgs], typing.Any], typing.Any]:
        ...

    @component_changing.setter
    def component_changing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangingEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_removed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]:
        ...

    @component_removed.setter
    def component_removed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_removing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]:
        ...

    @component_removing.setter
    def component_removing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_rename(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentRenameEventArgs], typing.Any], typing.Any]:
        ...

    @component_rename.setter
    def component_rename(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentRenameEventArgs], typing.Any], typing.Any]) -> None:
        ...

    def on_component_changed(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor, old_value: typing.Any, new_value: typing.Any) -> None:
        ...

    def on_component_changing(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        ...


class SelectionTypes(IntEnum):
    """This class has no documentation."""

    AUTO = ...

    NORMAL = ...

    REPLACE = ...

    MOUSE_DOWN = ...

    MOUSE_UP = ...

    CLICK = ...

    PRIMARY = ...

    TOGGLE = ...

    ADD = ...

    REMOVE = ...

    VALID = ...


class ISelectionService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def primary_selection(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def selection_count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def selection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @selection_changed.setter
    def selection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def selection_changing(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @selection_changing.setter
    def selection_changing(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...

    def get_component_selected(self, component: typing.Any) -> bool:
        ...

    def get_selected_components(self) -> System.Collections.ICollection:
        ...

    @overload
    def set_selected_components(self, components: System.Collections.ICollection) -> None:
        ...

    @overload
    def set_selected_components(self, components: System.Collections.ICollection, selection_type: System.ComponentModel.Design.SelectionTypes) -> None:
        ...


class IDesignerHostTransactionState(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def is_closing_transaction(self) -> bool:
        ...


class DesignerCollection(System.Object, System.Collections.ICollection):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    def __getitem__(self, index: int) -> System.ComponentModel.Design.IDesignerHost:
        ...

    @overload
    def __init__(self, designers: typing.List[System.ComponentModel.Design.IDesignerHost]) -> None:
        ...

    @overload
    def __init__(self, designers: System.Collections.IList) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...


class DesignerEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def designer(self) -> System.ComponentModel.Design.IDesignerHost:
        ...

    def __init__(self, host: System.ComponentModel.Design.IDesignerHost) -> None:
        ...


class IDesignerEventService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def active_designer(self) -> System.ComponentModel.Design.IDesignerHost:
        ...

    @property
    @abc.abstractmethod
    def designers(self) -> System.ComponentModel.Design.DesignerCollection:
        ...

    @property
    @abc.abstractmethod
    def active_designer_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ActiveDesignerEventArgs], typing.Any], typing.Any]:
        ...

    @active_designer_changed.setter
    def active_designer_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ActiveDesignerEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def designer_created(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], typing.Any], typing.Any]:
        ...

    @designer_created.setter
    def designer_created(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def designer_disposed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], typing.Any], typing.Any]:
        ...

    @designer_disposed.setter
    def designer_disposed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], typing.Any], typing.Any]) -> None:
        ...

    @property
    @abc.abstractmethod
    def selection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]:
        ...

    @selection_changed.setter
    def selection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], typing.Any], typing.Any]) -> None:
        ...


class ITreeDesigner(System.ComponentModel.Design.IDesigner, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def children(self) -> System.Collections.ICollection:
        ...

    @property
    @abc.abstractmethod
    def parent(self) -> System.ComponentModel.Design.IDesigner:
        ...


class IExtenderProviderService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def add_extender_provider(self, provider: System.ComponentModel.IExtenderProvider) -> None:
        ...

    def remove_extender_provider(self, provider: System.ComponentModel.IExtenderProvider) -> None:
        ...


class StandardCommands(System.Object):
    """This class has no documentation."""

    ALIGN_BOTTOM: System.ComponentModel.Design.CommandID = ...

    ALIGN_HORIZONTAL_CENTERS: System.ComponentModel.Design.CommandID = ...

    ALIGN_LEFT: System.ComponentModel.Design.CommandID = ...

    ALIGN_RIGHT: System.ComponentModel.Design.CommandID = ...

    ALIGN_TO_GRID: System.ComponentModel.Design.CommandID = ...

    ALIGN_TOP: System.ComponentModel.Design.CommandID = ...

    ALIGN_VERTICAL_CENTERS: System.ComponentModel.Design.CommandID = ...

    ARRANGE_BOTTOM: System.ComponentModel.Design.CommandID = ...

    ARRANGE_RIGHT: System.ComponentModel.Design.CommandID = ...

    BRING_FORWARD: System.ComponentModel.Design.CommandID = ...

    BRING_TO_FRONT: System.ComponentModel.Design.CommandID = ...

    CENTER_HORIZONTALLY: System.ComponentModel.Design.CommandID = ...

    CENTER_VERTICALLY: System.ComponentModel.Design.CommandID = ...

    VIEW_CODE: System.ComponentModel.Design.CommandID = ...

    DOCUMENT_OUTLINE: System.ComponentModel.Design.CommandID = ...

    COPY: System.ComponentModel.Design.CommandID = ...

    CUT: System.ComponentModel.Design.CommandID = ...

    DELETE: System.ComponentModel.Design.CommandID = ...

    GROUP: System.ComponentModel.Design.CommandID = ...

    HORIZ_SPACE_CONCATENATE: System.ComponentModel.Design.CommandID = ...

    HORIZ_SPACE_DECREASE: System.ComponentModel.Design.CommandID = ...

    HORIZ_SPACE_INCREASE: System.ComponentModel.Design.CommandID = ...

    HORIZ_SPACE_MAKE_EQUAL: System.ComponentModel.Design.CommandID = ...

    PASTE: System.ComponentModel.Design.CommandID = ...

    PROPERTIES: System.ComponentModel.Design.CommandID = ...

    REDO: System.ComponentModel.Design.CommandID = ...

    MULTI_LEVEL_REDO: System.ComponentModel.Design.CommandID = ...

    SELECT_ALL: System.ComponentModel.Design.CommandID = ...

    SEND_BACKWARD: System.ComponentModel.Design.CommandID = ...

    SEND_TO_BACK: System.ComponentModel.Design.CommandID = ...

    SIZE_TO_CONTROL: System.ComponentModel.Design.CommandID = ...

    SIZE_TO_CONTROL_HEIGHT: System.ComponentModel.Design.CommandID = ...

    SIZE_TO_CONTROL_WIDTH: System.ComponentModel.Design.CommandID = ...

    SIZE_TO_FIT: System.ComponentModel.Design.CommandID = ...

    SIZE_TO_GRID: System.ComponentModel.Design.CommandID = ...

    SNAP_TO_GRID: System.ComponentModel.Design.CommandID = ...

    TAB_ORDER: System.ComponentModel.Design.CommandID = ...

    UNDO: System.ComponentModel.Design.CommandID = ...

    MULTI_LEVEL_UNDO: System.ComponentModel.Design.CommandID = ...

    UNGROUP: System.ComponentModel.Design.CommandID = ...

    VERT_SPACE_CONCATENATE: System.ComponentModel.Design.CommandID = ...

    VERT_SPACE_DECREASE: System.ComponentModel.Design.CommandID = ...

    VERT_SPACE_INCREASE: System.ComponentModel.Design.CommandID = ...

    VERT_SPACE_MAKE_EQUAL: System.ComponentModel.Design.CommandID = ...

    SHOW_GRID: System.ComponentModel.Design.CommandID = ...

    VIEW_GRID: System.ComponentModel.Design.CommandID = ...

    REPLACE: System.ComponentModel.Design.CommandID = ...

    PROPERTIES_WINDOW: System.ComponentModel.Design.CommandID = ...

    LOCK_CONTROLS: System.ComponentModel.Design.CommandID = ...

    F_1_HELP: System.ComponentModel.Design.CommandID = ...

    ARRANGE_ICONS: System.ComponentModel.Design.CommandID = ...

    LINEUP_ICONS: System.ComponentModel.Design.CommandID = ...

    SHOW_LARGE_ICONS: System.ComponentModel.Design.CommandID = ...

    VERB_FIRST: System.ComponentModel.Design.CommandID = ...

    VERB_LAST: System.ComponentModel.Design.CommandID = ...


class IDictionaryService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_key(self, value: typing.Any) -> System.Object:
        ...

    def get_value(self, key: typing.Any) -> System.Object:
        ...

    def set_value(self, key: typing.Any, value: typing.Any) -> None:
        ...


class IInheritanceService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def add_inherited_components(self, component: System.ComponentModel.IComponent, container: System.ComponentModel.IContainer) -> None:
        ...

    def get_inheritance_attribute(self, component: System.ComponentModel.IComponent) -> System.ComponentModel.InheritanceAttribute:
        ...


class HelpContextType(IntEnum):
    """This class has no documentation."""

    AMBIENT = 0

    WINDOW = 1

    SELECTION = 2

    TOOL_WINDOW_SELECTION = 3


class ITypeDiscoveryService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_types(self, base_type: typing.Type, exclude_global_types: bool) -> System.Collections.ICollection:
        ...


class DesigntimeLicenseContext(System.ComponentModel.LicenseContext):
    """This class has no documentation."""

    @property
    def usage_mode(self) -> System.ComponentModel.LicenseUsageMode:
        ...

    def get_saved_license_key(self, type: typing.Type, resource_assembly: System.Reflection.Assembly) -> str:
        ...

    def set_saved_license_key(self, type: typing.Type, key: str) -> None:
        ...


class DesigntimeLicenseContextSerializer(System.Object):
    """This class has no documentation."""

    @staticmethod
    def serialize(o: System.IO.Stream, crypto_key: str, context: System.ComponentModel.Design.DesigntimeLicenseContext) -> None:
        ...


class IHelpService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def add_context_attribute(self, name: str, value: str, keyword_type: System.ComponentModel.Design.HelpKeywordType) -> None:
        ...

    def clear_context_attributes(self) -> None:
        ...

    def create_local_context(self, context_type: System.ComponentModel.Design.HelpContextType) -> System.ComponentModel.Design.IHelpService:
        ...

    def remove_context_attribute(self, name: str, value: str) -> None:
        ...

    def remove_local_context(self, local_context: System.ComponentModel.Design.IHelpService) -> None:
        ...

    def show_help_from_keyword(self, help_keyword: str) -> None:
        ...

    def show_help_from_url(self, help_url: str) -> None:
        ...


class IReferenceService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_component(self, reference: typing.Any) -> System.ComponentModel.IComponent:
        ...

    def get_name(self, reference: typing.Any) -> str:
        ...

    def get_reference(self, name: str) -> System.Object:
        ...

    @overload
    def get_references(self) -> typing.List[System.Object]:
        ...

    @overload
    def get_references(self, base_type: typing.Type) -> typing.List[System.Object]:
        ...


class IRootDesigner(System.ComponentModel.Design.IDesigner, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def supported_technologies(self) -> typing.List[System.ComponentModel.Design.ViewTechnology]:
        ...

    def get_view(self, technology: System.ComponentModel.Design.ViewTechnology) -> System.Object:
        ...


class ITypeResolutionService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def get_assembly(self, name: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        ...

    @overload
    def get_assembly(self, name: System.Reflection.AssemblyName, throw_on_error: bool) -> System.Reflection.Assembly:
        ...

    def get_path_of_assembly(self, name: System.Reflection.AssemblyName) -> str:
        ...

    @overload
    def get_type(self, name: str) -> typing.Type:
        ...

    @overload
    def get_type(self, name: str, throw_on_error: bool) -> typing.Type:
        ...

    @overload
    def get_type(self, name: str, throw_on_error: bool, ignore_case: bool) -> typing.Type:
        ...

    def reference_assembly(self, name: System.Reflection.AssemblyName) -> None:
        ...


class IComponentDiscoveryService(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_component_types(self, designer_host: System.ComponentModel.Design.IDesignerHost, base_type: typing.Type) -> System.Collections.ICollection:
        ...


class _EventContainer(typing.Generic[System_ComponentModel_Design__EventContainer_Callable, System_ComponentModel_Design__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_ComponentModel_Design__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_ComponentModel_Design__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_ComponentModel_Design__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


