from typing import overload
from enum import IntEnum
import abc
import typing

import System
import System.Runtime.InteropServices.ComTypes


class IPersistFile(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_class_id(self, p_class_id: typing.Optional[System.Guid]) -> typing.Tuple[None, System.Guid]:
        ...

    def get_cur_file(self, ppsz_file_name: typing.Optional[str]) -> typing.Tuple[None, str]:
        ...

    def is_dirty(self) -> int:
        ...

    def load(self, psz_file_name: str, dw_mode: int) -> None:
        ...

    def save(self, psz_file_name: str, f_remember: bool) -> None:
        ...

    def save_completed(self, psz_file_name: str) -> None:
        ...


class FILETIME:
    """This class has no documentation."""

    @property
    def dw_low_date_time(self) -> int:
        ...

    @dw_low_date_time.setter
    def dw_low_date_time(self, value: int) -> None:
        ...

    @property
    def dw_high_date_time(self) -> int:
        ...

    @dw_high_date_time.setter
    def dw_high_date_time(self, value: int) -> None:
        ...


class STATSTG:
    """This class has no documentation."""

    @property
    def pwcs_name(self) -> str:
        ...

    @pwcs_name.setter
    def pwcs_name(self, value: str) -> None:
        ...

    @property
    def type(self) -> int:
        ...

    @type.setter
    def type(self, value: int) -> None:
        ...

    @property
    def cb_size(self) -> int:
        ...

    @cb_size.setter
    def cb_size(self, value: int) -> None:
        ...

    @property
    def mtime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @mtime.setter
    def mtime(self, value: System.Runtime.InteropServices.ComTypes.FILETIME) -> None:
        ...

    @property
    def ctime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @ctime.setter
    def ctime(self, value: System.Runtime.InteropServices.ComTypes.FILETIME) -> None:
        ...

    @property
    def atime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @atime.setter
    def atime(self, value: System.Runtime.InteropServices.ComTypes.FILETIME) -> None:
        ...

    @property
    def grf_mode(self) -> int:
        ...

    @grf_mode.setter
    def grf_mode(self, value: int) -> None:
        ...

    @property
    def grf_locks_supported(self) -> int:
        ...

    @grf_locks_supported.setter
    def grf_locks_supported(self, value: int) -> None:
        ...

    @property
    def clsid(self) -> System.Guid:
        ...

    @clsid.setter
    def clsid(self, value: System.Guid) -> None:
        ...

    @property
    def grf_state_bits(self) -> int:
        ...

    @grf_state_bits.setter
    def grf_state_bits(self, value: int) -> None:
        ...

    @property
    def reserved(self) -> int:
        ...

    @reserved.setter
    def reserved(self, value: int) -> None:
        ...


class IStream(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self, ppstm: typing.Optional[System.Runtime.InteropServices.ComTypes.IStream]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IStream]:
        ...

    def commit(self, grf_commit_flags: int) -> None:
        ...

    def copy_to(self, pstm: System.Runtime.InteropServices.ComTypes.IStream, cb: int, pcb_read: System.IntPtr, pcb_written: System.IntPtr) -> None:
        ...

    def lock_region(self, lib_offset: int, cb: int, dw_lock_type: int) -> None:
        ...

    def read(self, pv: typing.List[int], cb: int, pcb_read: System.IntPtr) -> None:
        ...

    def revert(self) -> None:
        ...

    def seek(self, dlib_move: int, dw_origin: int, plib_new_position: System.IntPtr) -> None:
        ...

    def set_size(self, lib_new_size: int) -> None:
        ...

    def stat(self, pstatstg: typing.Optional[System.Runtime.InteropServices.ComTypes.STATSTG], grf_stat_flag: int) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.STATSTG]:
        ...

    def unlock_region(self, lib_offset: int, cb: int, dw_lock_type: int) -> None:
        ...

    def write(self, pv: typing.List[int], cb: int, pcb_written: System.IntPtr) -> None:
        ...


class BIND_OPTS:
    """This class has no documentation."""

    @property
    def cb_struct(self) -> int:
        ...

    @cb_struct.setter
    def cb_struct(self, value: int) -> None:
        ...

    @property
    def grf_flags(self) -> int:
        ...

    @grf_flags.setter
    def grf_flags(self, value: int) -> None:
        ...

    @property
    def grf_mode(self) -> int:
        ...

    @grf_mode.setter
    def grf_mode(self, value: int) -> None:
        ...

    @property
    def dw_tick_count_deadline(self) -> int:
        ...

    @dw_tick_count_deadline.setter
    def dw_tick_count_deadline(self, value: int) -> None:
        ...


class IEnumString(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumString]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumString]:
        ...

    def next(self, celt: int, rgelt: typing.List[str], pcelt_fetched: System.IntPtr) -> int:
        ...

    def reset(self) -> None:
        ...

    def skip(self, celt: int) -> int:
        ...


class IBindCtx(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def enum_object_param(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumString]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumString]:
        ...

    def get_bind_options(self, pbindopts: System.Runtime.InteropServices.ComTypes.BIND_OPTS) -> None:
        ...

    def get_object_param(self, psz_key: str, ppunk: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_running_object_table(self, pprot: typing.Optional[System.Runtime.InteropServices.ComTypes.IRunningObjectTable]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IRunningObjectTable]:
        ...

    def register_object_bound(self, punk: typing.Any) -> None:
        ...

    def register_object_param(self, psz_key: str, punk: typing.Any) -> None:
        ...

    def release_bound_objects(self) -> None:
        ...

    def revoke_object_bound(self, punk: typing.Any) -> None:
        ...

    def revoke_object_param(self, psz_key: str) -> int:
        ...

    def set_bind_options(self, pbindopts: System.Runtime.InteropServices.ComTypes.BIND_OPTS) -> None:
        ...


class IEnumMoniker(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumMoniker]:
        ...

    def next(self, celt: int, rgelt: typing.List[System.Runtime.InteropServices.ComTypes.IMoniker], pcelt_fetched: System.IntPtr) -> int:
        ...

    def reset(self) -> None:
        ...

    def skip(self, celt: int) -> int:
        ...


class IMoniker(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def bind_to_object(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmk_to_left: System.Runtime.InteropServices.ComTypes.IMoniker, riid_result: System.Guid, ppv_result: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def bind_to_storage(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmk_to_left: System.Runtime.InteropServices.ComTypes.IMoniker, riid: System.Guid, ppv_obj: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def common_prefix_with(self, pmk_other: System.Runtime.InteropServices.ComTypes.IMoniker, ppmk_prefix: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def compose_with(self, pmk_right: System.Runtime.InteropServices.ComTypes.IMoniker, f_only_if_not_generic: bool, ppmk_composite: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def enum(self, f_forward: bool, ppenum_moniker: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumMoniker]:
        ...

    def get_class_id(self, p_class_id: typing.Optional[System.Guid]) -> typing.Tuple[None, System.Guid]:
        ...

    def get_display_name(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmk_to_left: System.Runtime.InteropServices.ComTypes.IMoniker, ppsz_display_name: typing.Optional[str]) -> typing.Tuple[None, str]:
        ...

    def get_size_max(self, pcb_size: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def get_time_of_last_change(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmk_to_left: System.Runtime.InteropServices.ComTypes.IMoniker, p_file_time: typing.Optional[System.Runtime.InteropServices.ComTypes.FILETIME]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.FILETIME]:
        ...

    def hash(self, pdw_hash: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def inverse(self, ppmk: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def is_dirty(self) -> int:
        ...

    def is_equal(self, pmk_other_moniker: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def is_running(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmk_to_left: System.Runtime.InteropServices.ComTypes.IMoniker, pmk_newly_running: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def is_system_moniker(self, pdw_mksys: typing.Optional[int]) -> typing.Tuple[int, int]:
        ...

    def load(self, p_stm: System.Runtime.InteropServices.ComTypes.IStream) -> None:
        ...

    def parse_display_name(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmk_to_left: System.Runtime.InteropServices.ComTypes.IMoniker, psz_display_name: str, pch_eaten: typing.Optional[int], ppmk_out: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Tuple[None, int, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def reduce(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, dw_reduce_how_far: int, ppmk_to_left: System.Runtime.InteropServices.ComTypes.IMoniker, ppmk_reduced: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def relative_path_to(self, pmk_other: System.Runtime.InteropServices.ComTypes.IMoniker, ppmk_rel_path: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def save(self, p_stm: System.Runtime.InteropServices.ComTypes.IStream, f_clear_dirty: bool) -> None:
        ...


class IRunningObjectTable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def enum_running(self, ppenum_moniker: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumMoniker]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumMoniker]:
        ...

    def get_object(self, pmk_object_name: System.Runtime.InteropServices.ComTypes.IMoniker, ppunk_object: typing.Optional[typing.Any]) -> typing.Tuple[int, typing.Any]:
        ...

    def get_time_of_last_change(self, pmk_object_name: System.Runtime.InteropServices.ComTypes.IMoniker, pfiletime: typing.Optional[System.Runtime.InteropServices.ComTypes.FILETIME]) -> typing.Tuple[int, System.Runtime.InteropServices.ComTypes.FILETIME]:
        ...

    def is_running(self, pmk_object_name: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def note_change_time(self, dw_register: int, pfiletime: System.Runtime.InteropServices.ComTypes.FILETIME) -> None:
        ...

    def register(self, grf_flags: int, punk_object: typing.Any, pmk_object_name: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def revoke(self, dw_register: int) -> None:
        ...


class TYPEKIND(IntEnum):
    """This class has no documentation."""

    TKIND_ENUM = 0

    TKIND_RECORD = ...

    TKIND_MODULE = ...

    TKIND_INTERFACE = ...

    TKIND_DISPATCH = ...

    TKIND_COCLASS = ...

    TKIND_ALIAS = ...

    TKIND_UNION = ...

    TKIND_MAX = ...


class TYPEFLAGS(IntEnum):
    """This class has no documentation."""

    TYPEFLAG_FAPPOBJECT = ...

    TYPEFLAG_FCANCREATE = ...

    TYPEFLAG_FLICENSED = ...

    TYPEFLAG_FPREDECLID = ...

    TYPEFLAG_FHIDDEN = ...

    TYPEFLAG_FCONTROL = ...

    TYPEFLAG_FDUAL = ...

    TYPEFLAG_FNONEXTENSIBLE = ...

    TYPEFLAG_FOLEAUTOMATION = ...

    TYPEFLAG_FRESTRICTED = ...

    TYPEFLAG_FAGGREGATABLE = ...

    TYPEFLAG_FREPLACEABLE = ...

    TYPEFLAG_FDISPATCHABLE = ...

    TYPEFLAG_FREVERSEBIND = ...

    TYPEFLAG_FPROXY = ...


class IMPLTYPEFLAGS(IntEnum):
    """This class has no documentation."""

    IMPLTYPEFLAG_FDEFAULT = ...

    IMPLTYPEFLAG_FSOURCE = ...

    IMPLTYPEFLAG_FRESTRICTED = ...

    IMPLTYPEFLAG_FDEFAULTVTABLE = ...


class TYPEDESC:
    """This class has no documentation."""

    @property
    def lp_value(self) -> System.IntPtr:
        ...

    @lp_value.setter
    def lp_value(self, value: System.IntPtr) -> None:
        ...

    @property
    def vt(self) -> int:
        ...

    @vt.setter
    def vt(self, value: int) -> None:
        ...


class IDLFLAG(IntEnum):
    """This class has no documentation."""

    IDLFLAG_NONE = ...

    IDLFLAG_FIN = ...

    IDLFLAG_FOUT = ...

    IDLFLAG_FLCID = ...

    IDLFLAG_FRETVAL = ...


class IDLDESC:
    """This class has no documentation."""

    @property
    def dw_reserved(self) -> System.IntPtr:
        ...

    @dw_reserved.setter
    def dw_reserved(self, value: System.IntPtr) -> None:
        ...

    @property
    def w_idl_flags(self) -> System.Runtime.InteropServices.ComTypes.IDLFLAG:
        ...

    @w_idl_flags.setter
    def w_idl_flags(self, value: System.Runtime.InteropServices.ComTypes.IDLFLAG) -> None:
        ...


class TYPEATTR:
    """This class has no documentation."""

    MEMBER_ID_NIL: int = ...

    @property
    def guid(self) -> System.Guid:
        ...

    @guid.setter
    def guid(self, value: System.Guid) -> None:
        ...

    @property
    def lcid(self) -> int:
        ...

    @lcid.setter
    def lcid(self, value: int) -> None:
        ...

    @property
    def dw_reserved(self) -> int:
        ...

    @dw_reserved.setter
    def dw_reserved(self, value: int) -> None:
        ...

    @property
    def memid_constructor(self) -> int:
        ...

    @memid_constructor.setter
    def memid_constructor(self, value: int) -> None:
        ...

    @property
    def memid_destructor(self) -> int:
        ...

    @memid_destructor.setter
    def memid_destructor(self, value: int) -> None:
        ...

    @property
    def lpstr_schema(self) -> System.IntPtr:
        ...

    @lpstr_schema.setter
    def lpstr_schema(self, value: System.IntPtr) -> None:
        ...

    @property
    def cb_size_instance(self) -> int:
        ...

    @cb_size_instance.setter
    def cb_size_instance(self, value: int) -> None:
        ...

    @property
    def typekind(self) -> System.Runtime.InteropServices.ComTypes.TYPEKIND:
        ...

    @typekind.setter
    def typekind(self, value: System.Runtime.InteropServices.ComTypes.TYPEKIND) -> None:
        ...

    @property
    def c_funcs(self) -> int:
        ...

    @c_funcs.setter
    def c_funcs(self, value: int) -> None:
        ...

    @property
    def c_vars(self) -> int:
        ...

    @c_vars.setter
    def c_vars(self, value: int) -> None:
        ...

    @property
    def c_impl_types(self) -> int:
        ...

    @c_impl_types.setter
    def c_impl_types(self, value: int) -> None:
        ...

    @property
    def cb_size_vft(self) -> int:
        ...

    @cb_size_vft.setter
    def cb_size_vft(self, value: int) -> None:
        ...

    @property
    def cb_alignment(self) -> int:
        ...

    @cb_alignment.setter
    def cb_alignment(self, value: int) -> None:
        ...

    @property
    def w_type_flags(self) -> System.Runtime.InteropServices.ComTypes.TYPEFLAGS:
        ...

    @w_type_flags.setter
    def w_type_flags(self, value: System.Runtime.InteropServices.ComTypes.TYPEFLAGS) -> None:
        ...

    @property
    def w_major_ver_num(self) -> int:
        ...

    @w_major_ver_num.setter
    def w_major_ver_num(self, value: int) -> None:
        ...

    @property
    def w_minor_ver_num(self) -> int:
        ...

    @w_minor_ver_num.setter
    def w_minor_ver_num(self, value: int) -> None:
        ...

    @property
    def tdesc_alias(self) -> System.Runtime.InteropServices.ComTypes.TYPEDESC:
        ...

    @tdesc_alias.setter
    def tdesc_alias(self, value: System.Runtime.InteropServices.ComTypes.TYPEDESC) -> None:
        ...

    @property
    def idldesc_type(self) -> System.Runtime.InteropServices.ComTypes.IDLDESC:
        ...

    @idldesc_type.setter
    def idldesc_type(self, value: System.Runtime.InteropServices.ComTypes.IDLDESC) -> None:
        ...


class FUNCKIND(IntEnum):
    """This class has no documentation."""

    FUNC_VIRTUAL = 0

    FUNC_PUREVIRTUAL = 1

    FUNC_NONVIRTUAL = 2

    FUNC_STATIC = 3

    FUNC_DISPATCH = 4


class INVOKEKIND(IntEnum):
    """This class has no documentation."""

    INVOKE_FUNC = ...

    INVOKE_PROPERTYGET = ...

    INVOKE_PROPERTYPUT = ...

    INVOKE_PROPERTYPUTREF = ...


class CALLCONV(IntEnum):
    """This class has no documentation."""

    CC_CDECL = 1

    CC_MSCPASCAL = 2

    CC_PASCAL = ...

    CC_MACPASCAL = 3

    CC_STDCALL = 4

    CC_RESERVED = 5

    CC_SYSCALL = 6

    CC_MPWCDECL = 7

    CC_MPWPASCAL = 8

    CC_MAX = 9


class PARAMFLAG(IntEnum):
    """This class has no documentation."""

    PARAMFLAG_NONE = 0

    PARAMFLAG_FIN = ...

    PARAMFLAG_FOUT = ...

    PARAMFLAG_FLCID = ...

    PARAMFLAG_FRETVAL = ...

    PARAMFLAG_FOPT = ...

    PARAMFLAG_FHASDEFAULT = ...

    PARAMFLAG_FHASCUSTDATA = ...


class PARAMDESC:
    """This class has no documentation."""

    @property
    def lp_var_value(self) -> System.IntPtr:
        ...

    @lp_var_value.setter
    def lp_var_value(self, value: System.IntPtr) -> None:
        ...

    @property
    def w_param_flags(self) -> System.Runtime.InteropServices.ComTypes.PARAMFLAG:
        ...

    @w_param_flags.setter
    def w_param_flags(self, value: System.Runtime.InteropServices.ComTypes.PARAMFLAG) -> None:
        ...


class ELEMDESC:
    """This class has no documentation."""

    class DESCUNION:
        """This class has no documentation."""

        @property
        def idldesc(self) -> System.Runtime.InteropServices.ComTypes.IDLDESC:
            ...

        @idldesc.setter
        def idldesc(self, value: System.Runtime.InteropServices.ComTypes.IDLDESC) -> None:
            ...

        @property
        def paramdesc(self) -> System.Runtime.InteropServices.ComTypes.PARAMDESC:
            ...

        @paramdesc.setter
        def paramdesc(self, value: System.Runtime.InteropServices.ComTypes.PARAMDESC) -> None:
            ...

    @property
    def tdesc(self) -> System.Runtime.InteropServices.ComTypes.TYPEDESC:
        ...

    @tdesc.setter
    def tdesc(self, value: System.Runtime.InteropServices.ComTypes.TYPEDESC) -> None:
        ...

    @property
    def desc(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC.DESCUNION:
        ...

    @desc.setter
    def desc(self, value: System.Runtime.InteropServices.ComTypes.ELEMDESC.DESCUNION) -> None:
        ...


class FUNCDESC:
    """This class has no documentation."""

    @property
    def memid(self) -> int:
        ...

    @memid.setter
    def memid(self, value: int) -> None:
        ...

    @property
    def lprgscode(self) -> System.IntPtr:
        ...

    @lprgscode.setter
    def lprgscode(self, value: System.IntPtr) -> None:
        ...

    @property
    def lprgelemdesc_param(self) -> System.IntPtr:
        ...

    @lprgelemdesc_param.setter
    def lprgelemdesc_param(self, value: System.IntPtr) -> None:
        ...

    @property
    def funckind(self) -> System.Runtime.InteropServices.ComTypes.FUNCKIND:
        ...

    @funckind.setter
    def funckind(self, value: System.Runtime.InteropServices.ComTypes.FUNCKIND) -> None:
        ...

    @property
    def invkind(self) -> System.Runtime.InteropServices.ComTypes.INVOKEKIND:
        ...

    @invkind.setter
    def invkind(self, value: System.Runtime.InteropServices.ComTypes.INVOKEKIND) -> None:
        ...

    @property
    def callconv(self) -> System.Runtime.InteropServices.ComTypes.CALLCONV:
        ...

    @callconv.setter
    def callconv(self, value: System.Runtime.InteropServices.ComTypes.CALLCONV) -> None:
        ...

    @property
    def c_params(self) -> int:
        ...

    @c_params.setter
    def c_params(self, value: int) -> None:
        ...

    @property
    def c_params_opt(self) -> int:
        ...

    @c_params_opt.setter
    def c_params_opt(self, value: int) -> None:
        ...

    @property
    def o_vft(self) -> int:
        ...

    @o_vft.setter
    def o_vft(self, value: int) -> None:
        ...

    @property
    def c_scodes(self) -> int:
        ...

    @c_scodes.setter
    def c_scodes(self, value: int) -> None:
        ...

    @property
    def elemdesc_func(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC:
        ...

    @elemdesc_func.setter
    def elemdesc_func(self, value: System.Runtime.InteropServices.ComTypes.ELEMDESC) -> None:
        ...

    @property
    def w_func_flags(self) -> int:
        ...

    @w_func_flags.setter
    def w_func_flags(self, value: int) -> None:
        ...


class VARKIND(IntEnum):
    """This class has no documentation."""

    VAR_PERINSTANCE = ...

    VAR_STATIC = ...

    VAR_CONST = ...

    VAR_DISPATCH = ...


class VARDESC:
    """This class has no documentation."""

    class DESCUNION:
        """This class has no documentation."""

        @property
        def o_inst(self) -> int:
            ...

        @o_inst.setter
        def o_inst(self, value: int) -> None:
            ...

        @property
        def lpvar_value(self) -> System.IntPtr:
            ...

        @lpvar_value.setter
        def lpvar_value(self, value: System.IntPtr) -> None:
            ...

    @property
    def memid(self) -> int:
        ...

    @memid.setter
    def memid(self, value: int) -> None:
        ...

    @property
    def lpstr_schema(self) -> str:
        ...

    @lpstr_schema.setter
    def lpstr_schema(self, value: str) -> None:
        ...

    @property
    def desc(self) -> System.Runtime.InteropServices.ComTypes.VARDESC.DESCUNION:
        ...

    @desc.setter
    def desc(self, value: System.Runtime.InteropServices.ComTypes.VARDESC.DESCUNION) -> None:
        ...

    @property
    def elemdesc_var(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC:
        ...

    @elemdesc_var.setter
    def elemdesc_var(self, value: System.Runtime.InteropServices.ComTypes.ELEMDESC) -> None:
        ...

    @property
    def w_var_flags(self) -> int:
        ...

    @w_var_flags.setter
    def w_var_flags(self, value: int) -> None:
        ...

    @property
    def varkind(self) -> System.Runtime.InteropServices.ComTypes.VARKIND:
        ...

    @varkind.setter
    def varkind(self, value: System.Runtime.InteropServices.ComTypes.VARKIND) -> None:
        ...


class DISPPARAMS:
    """This class has no documentation."""

    @property
    def rgvarg(self) -> System.IntPtr:
        ...

    @rgvarg.setter
    def rgvarg(self, value: System.IntPtr) -> None:
        ...

    @property
    def rgdispid_named_args(self) -> System.IntPtr:
        ...

    @rgdispid_named_args.setter
    def rgdispid_named_args(self, value: System.IntPtr) -> None:
        ...

    @property
    def c_args(self) -> int:
        ...

    @c_args.setter
    def c_args(self, value: int) -> None:
        ...

    @property
    def c_named_args(self) -> int:
        ...

    @c_named_args.setter
    def c_named_args(self, value: int) -> None:
        ...


class EXCEPINFO:
    """This class has no documentation."""

    @property
    def w_code(self) -> int:
        ...

    @w_code.setter
    def w_code(self, value: int) -> None:
        ...

    @property
    def w_reserved(self) -> int:
        ...

    @w_reserved.setter
    def w_reserved(self, value: int) -> None:
        ...

    @property
    def bstr_source(self) -> str:
        ...

    @bstr_source.setter
    def bstr_source(self, value: str) -> None:
        ...

    @property
    def bstr_description(self) -> str:
        ...

    @bstr_description.setter
    def bstr_description(self, value: str) -> None:
        ...

    @property
    def bstr_help_file(self) -> str:
        ...

    @bstr_help_file.setter
    def bstr_help_file(self, value: str) -> None:
        ...

    @property
    def dw_help_context(self) -> int:
        ...

    @dw_help_context.setter
    def dw_help_context(self, value: int) -> None:
        ...

    @property
    def pv_reserved(self) -> System.IntPtr:
        ...

    @pv_reserved.setter
    def pv_reserved(self, value: System.IntPtr) -> None:
        ...

    @property
    def pfn_deferred_fill_in(self) -> System.IntPtr:
        ...

    @pfn_deferred_fill_in.setter
    def pfn_deferred_fill_in(self, value: System.IntPtr) -> None:
        ...

    @property
    def scode(self) -> int:
        ...

    @scode.setter
    def scode(self, value: int) -> None:
        ...


class FUNCFLAGS(IntEnum):
    """This class has no documentation."""

    FUNCFLAG_FRESTRICTED = ...

    FUNCFLAG_FSOURCE = ...

    FUNCFLAG_FBINDABLE = ...

    FUNCFLAG_FREQUESTEDIT = ...

    FUNCFLAG_FDISPLAYBIND = ...

    FUNCFLAG_FDEFAULTBIND = ...

    FUNCFLAG_FHIDDEN = ...

    FUNCFLAG_FUSESGETLASTERROR = ...

    FUNCFLAG_FDEFAULTCOLLELEM = ...

    FUNCFLAG_FUIDEFAULT = ...

    FUNCFLAG_FNONBROWSABLE = ...

    FUNCFLAG_FREPLACEABLE = ...

    FUNCFLAG_FIMMEDIATEBIND = ...


class VARFLAGS(IntEnum):
    """This class has no documentation."""

    VARFLAG_FREADONLY = ...

    VARFLAG_FSOURCE = ...

    VARFLAG_FBINDABLE = ...

    VARFLAG_FREQUESTEDIT = ...

    VARFLAG_FDISPLAYBIND = ...

    VARFLAG_FDEFAULTBIND = ...

    VARFLAG_FHIDDEN = ...

    VARFLAG_FRESTRICTED = ...

    VARFLAG_FDEFAULTCOLLELEM = ...

    VARFLAG_FUIDEFAULT = ...

    VARFLAG_FNONBROWSABLE = ...

    VARFLAG_FREPLACEABLE = ...

    VARFLAG_FIMMEDIATEBIND = ...


class DESCKIND(IntEnum):
    """This class has no documentation."""

    DESCKIND_NONE = 0

    DESCKIND_FUNCDESC = ...

    DESCKIND_VARDESC = ...

    DESCKIND_TYPECOMP = ...

    DESCKIND_IMPLICITAPPOBJ = ...

    DESCKIND_MAX = ...


class BINDPTR:
    """This class has no documentation."""

    @property
    def lpfuncdesc(self) -> System.IntPtr:
        ...

    @lpfuncdesc.setter
    def lpfuncdesc(self, value: System.IntPtr) -> None:
        ...

    @property
    def lpvardesc(self) -> System.IntPtr:
        ...

    @lpvardesc.setter
    def lpvardesc(self, value: System.IntPtr) -> None:
        ...

    @property
    def lptcomp(self) -> System.IntPtr:
        ...

    @lptcomp.setter
    def lptcomp(self, value: System.IntPtr) -> None:
        ...


class ITypeComp(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def bind(self, sz_name: str, l_hash_val: int, w_flags: int, pp_t_info: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo], p_desc_kind: typing.Optional[System.Runtime.InteropServices.ComTypes.DESCKIND], p_bind_ptr: typing.Optional[System.Runtime.InteropServices.ComTypes.BINDPTR]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeInfo, System.Runtime.InteropServices.ComTypes.DESCKIND, System.Runtime.InteropServices.ComTypes.BINDPTR]:
        ...

    def bind_type(self, sz_name: str, l_hash_val: int, pp_t_info: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo], pp_t_comp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeInfo, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...


class ITypeLib(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def find_name(self, sz_name_buf: str, l_hash_val: int, pp_t_info: typing.List[System.Runtime.InteropServices.ComTypes.ITypeInfo], rg_mem_id: typing.List[int], pc_found: int) -> None:
        ...

    def get_documentation(self, index: int, str_name: typing.Optional[str], str_doc_string: typing.Optional[str], dw_help_context: typing.Optional[int], str_help_file: typing.Optional[str]) -> typing.Tuple[None, str, str, int, str]:
        ...

    def get_lib_attr(self, pp_t_lib_attr: typing.Optional[System.IntPtr]) -> typing.Tuple[None, System.IntPtr]:
        ...

    def get_type_comp(self, pp_t_comp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...

    def get_type_info(self, index: int, pp_ti: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def get_type_info_count(self) -> int:
        ...

    def get_type_info_of_guid(self, guid: System.Guid, pp_t_info: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def get_type_info_type(self, index: int, p_t_kind: typing.Optional[System.Runtime.InteropServices.ComTypes.TYPEKIND]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.TYPEKIND]:
        ...

    def is_name(self, sz_name_buf: str, l_hash_val: int) -> bool:
        ...

    def release_t_lib_attr(self, p_t_lib_attr: System.IntPtr) -> None:
        ...


class ITypeInfo(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def address_of_member(self, memid: int, inv_kind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, ppv: typing.Optional[System.IntPtr]) -> typing.Tuple[None, System.IntPtr]:
        ...

    def create_instance(self, p_unk_outer: typing.Any, riid: System.Guid, ppv_obj: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_containing_type_lib(self, pp_tlb: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeLib], p_index: typing.Optional[int]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeLib, int]:
        ...

    def get_dll_entry(self, memid: int, inv_kind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, p_bstr_dll_name: System.IntPtr, p_bstr_name: System.IntPtr, pw_ordinal: System.IntPtr) -> None:
        ...

    def get_documentation(self, index: int, str_name: typing.Optional[str], str_doc_string: typing.Optional[str], dw_help_context: typing.Optional[int], str_help_file: typing.Optional[str]) -> typing.Tuple[None, str, str, int, str]:
        ...

    def get_func_desc(self, index: int, pp_func_desc: typing.Optional[System.IntPtr]) -> typing.Tuple[None, System.IntPtr]:
        ...

    def get_i_ds_of_names(self, rgsz_names: typing.List[str], c_names: int, p_mem_id: typing.List[int]) -> None:
        ...

    def get_impl_type_flags(self, index: int, p_impl_type_flags: typing.Optional[System.Runtime.InteropServices.ComTypes.IMPLTYPEFLAGS]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IMPLTYPEFLAGS]:
        ...

    def get_mops(self, memid: int, p_bstr_mops: typing.Optional[str]) -> typing.Tuple[None, str]:
        ...

    def get_names(self, memid: int, rg_bstr_names: typing.List[str], c_max_names: int, pc_names: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def get_ref_type_info(self, h_ref: int, pp_ti: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def get_ref_type_of_impl_type(self, index: int, href: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def get_type_attr(self, pp_type_attr: typing.Optional[System.IntPtr]) -> typing.Tuple[None, System.IntPtr]:
        ...

    def get_type_comp(self, pp_t_comp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...

    def get_var_desc(self, index: int, pp_var_desc: typing.Optional[System.IntPtr]) -> typing.Tuple[None, System.IntPtr]:
        ...

    def invoke(self, pv_instance: typing.Any, memid: int, w_flags: int, p_disp_params: System.Runtime.InteropServices.ComTypes.DISPPARAMS, p_var_result: System.IntPtr, p_excep_info: System.IntPtr, pu_arg_err: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def release_func_desc(self, p_func_desc: System.IntPtr) -> None:
        ...

    def release_type_attr(self, p_type_attr: System.IntPtr) -> None:
        ...

    def release_var_desc(self, p_var_desc: System.IntPtr) -> None:
        ...


class CONNECTDATA:
    """This class has no documentation."""

    @property
    def p_unk(self) -> System.Object:
        ...

    @p_unk.setter
    def p_unk(self, value: System.Object) -> None:
        ...

    @property
    def dw_cookie(self) -> int:
        ...

    @dw_cookie.setter
    def dw_cookie(self, value: int) -> None:
        ...


class IEnumConnections(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnections]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumConnections]:
        ...

    def next(self, celt: int, rgelt: typing.List[System.Runtime.InteropServices.ComTypes.CONNECTDATA], pcelt_fetched: System.IntPtr) -> int:
        ...

    def reset(self) -> None:
        ...

    def skip(self, celt: int) -> int:
        ...


class IConnectionPoint(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def advise(self, p_unk_sink: typing.Any, pdw_cookie: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def enum_connections(self, pp_enum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnections]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumConnections]:
        ...

    def get_connection_interface(self, p_iid: typing.Optional[System.Guid]) -> typing.Tuple[None, System.Guid]:
        ...

    def get_connection_point_container(self, pp_cpc: typing.Optional[System.Runtime.InteropServices.ComTypes.IConnectionPointContainer]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IConnectionPointContainer]:
        ...

    def unadvise(self, dw_cookie: int) -> None:
        ...


class IEnumConnectionPoints(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]:
        ...

    def next(self, celt: int, rgelt: typing.List[System.Runtime.InteropServices.ComTypes.IConnectionPoint], pcelt_fetched: System.IntPtr) -> int:
        ...

    def reset(self) -> None:
        ...

    def skip(self, celt: int) -> int:
        ...


class IConnectionPointContainer(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def enum_connection_points(self, pp_enum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]:
        ...

    def find_connection_point(self, riid: System.Guid, pp_cp: typing.Optional[System.Runtime.InteropServices.ComTypes.IConnectionPoint]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.IConnectionPoint]:
        ...


class ITypeInfo2(System.Runtime.InteropServices.ComTypes.ITypeInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_all_cust_data(self, p_cust_data: System.IntPtr) -> None:
        ...

    def get_all_func_cust_data(self, index: int, p_cust_data: System.IntPtr) -> None:
        ...

    def get_all_impl_type_cust_data(self, index: int, p_cust_data: System.IntPtr) -> None:
        ...

    def get_all_param_cust_data(self, index_func: int, index_param: int, p_cust_data: System.IntPtr) -> None:
        ...

    def get_all_var_cust_data(self, index: int, p_cust_data: System.IntPtr) -> None:
        ...

    def get_cust_data(self, guid: System.Guid, p_var_val: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_documentation_2(self, memid: int, pbstr_help_string: typing.Optional[str], pdw_help_string_context: typing.Optional[int], pbstr_help_string_dll: typing.Optional[str]) -> typing.Tuple[None, str, int, str]:
        ...

    def get_func_cust_data(self, index: int, guid: System.Guid, p_var_val: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_func_index_of_mem_id(self, memid: int, inv_kind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, p_func_index: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def get_impl_type_cust_data(self, index: int, guid: System.Guid, p_var_val: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_param_cust_data(self, index_func: int, index_param: int, guid: System.Guid, p_var_val: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_type_flags(self, p_type_flags: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...

    def get_type_kind(self, p_type_kind: typing.Optional[System.Runtime.InteropServices.ComTypes.TYPEKIND]) -> typing.Tuple[None, System.Runtime.InteropServices.ComTypes.TYPEKIND]:
        ...

    def get_var_cust_data(self, index: int, guid: System.Guid, p_var_val: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_var_index_of_mem_id(self, memid: int, p_var_index: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...


class SYSKIND(IntEnum):
    """This class has no documentation."""

    SYS_WIN_16 = 0

    SYS_WIN_32 = ...

    SYS_MAC = ...

    SYS_WIN_64 = ...


class LIBFLAGS(IntEnum):
    """This class has no documentation."""

    LIBFLAG_FRESTRICTED = ...

    LIBFLAG_FCONTROL = ...

    LIBFLAG_FHIDDEN = ...

    LIBFLAG_FHASDISKIMAGE = ...


class TYPELIBATTR:
    """This class has no documentation."""

    @property
    def guid(self) -> System.Guid:
        ...

    @guid.setter
    def guid(self, value: System.Guid) -> None:
        ...

    @property
    def lcid(self) -> int:
        ...

    @lcid.setter
    def lcid(self, value: int) -> None:
        ...

    @property
    def syskind(self) -> System.Runtime.InteropServices.ComTypes.SYSKIND:
        ...

    @syskind.setter
    def syskind(self, value: System.Runtime.InteropServices.ComTypes.SYSKIND) -> None:
        ...

    @property
    def w_major_ver_num(self) -> int:
        ...

    @w_major_ver_num.setter
    def w_major_ver_num(self, value: int) -> None:
        ...

    @property
    def w_minor_ver_num(self) -> int:
        ...

    @w_minor_ver_num.setter
    def w_minor_ver_num(self, value: int) -> None:
        ...

    @property
    def w_lib_flags(self) -> System.Runtime.InteropServices.ComTypes.LIBFLAGS:
        ...

    @w_lib_flags.setter
    def w_lib_flags(self, value: System.Runtime.InteropServices.ComTypes.LIBFLAGS) -> None:
        ...


class IEnumVARIANT(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self) -> System.Runtime.InteropServices.ComTypes.IEnumVARIANT:
        ...

    def next(self, celt: int, rg_var: typing.List[System.Object], pcelt_fetched: System.IntPtr) -> int:
        ...

    def reset(self) -> int:
        ...

    def skip(self, celt: int) -> int:
        ...


class ITypeLib2(System.Runtime.InteropServices.ComTypes.ITypeLib, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_all_cust_data(self, p_cust_data: System.IntPtr) -> None:
        ...

    def get_cust_data(self, guid: System.Guid, p_var_val: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any]:
        ...

    def get_documentation_2(self, index: int, pbstr_help_string: typing.Optional[str], pdw_help_string_context: typing.Optional[int], pbstr_help_string_dll: typing.Optional[str]) -> typing.Tuple[None, str, int, str]:
        ...

    def get_lib_statistics(self, pc_unique_names: System.IntPtr, pcch_unique_names: typing.Optional[int]) -> typing.Tuple[None, int]:
        ...


