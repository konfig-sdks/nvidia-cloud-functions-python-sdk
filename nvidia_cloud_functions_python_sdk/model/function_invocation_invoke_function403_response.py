# coding: utf-8

"""
    Cloud Functions

    Since its founding in 1993, NVIDIA (NASDAQ: NVDA) has been a pioneer in accelerated computing. The company's invention of the GPU in 1999 sparked the growth of the PC gaming market, redefined computer graphics, ignited the era of modern AI and is fueling the creation of the metaverse. NVIDIA is now a full-stack computing company with data-center-scale offerings that are reshaping industry.

    The version of the OpenAPI document: 2.87.3
    Created by: https://www.nvidia.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from nvidia_cloud_functions_python_sdk import schemas  # noqa: F401


class FunctionInvocationInvokeFunction403Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            short = schemas.Int32Schema
            char = schemas.StrSchema
            _int = schemas.Int32Schema
            long = schemas.Int64Schema
            _float = schemas.Float32Schema
            double = schemas.Float64Schema
            direct = schemas.BoolSchema
            readOnly = schemas.BoolSchema
            __annotations__ = {
                "short": short,
                "char": char,
                "int": _int,
                "long": long,
                "float": _float,
                "double": double,
                "direct": direct,
                "readOnly": readOnly,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["short"]) -> MetaOapg.properties.short: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["char"]) -> MetaOapg.properties.char: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["int"]) -> MetaOapg.properties._int: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["long"]) -> MetaOapg.properties.long: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["float"]) -> MetaOapg.properties._float: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double"]) -> MetaOapg.properties.double: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direct"]) -> MetaOapg.properties.direct: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnly"]) -> MetaOapg.properties.readOnly: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["short", "char", "int", "long", "float", "double", "direct", "readOnly", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["short"]) -> typing.Union[MetaOapg.properties.short, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["char"]) -> typing.Union[MetaOapg.properties.char, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["int"]) -> typing.Union[MetaOapg.properties._int, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["long"]) -> typing.Union[MetaOapg.properties.long, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["float"]) -> typing.Union[MetaOapg.properties._float, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["double"]) -> typing.Union[MetaOapg.properties.double, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direct"]) -> typing.Union[MetaOapg.properties.direct, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnly"]) -> typing.Union[MetaOapg.properties.readOnly, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["short", "char", "int", "long", "float", "double", "direct", "readOnly", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        short: typing.Union[MetaOapg.properties.short, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        char: typing.Union[MetaOapg.properties.char, str, schemas.Unset] = schemas.unset,
        long: typing.Union[MetaOapg.properties.long, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        double: typing.Union[MetaOapg.properties.double, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        direct: typing.Union[MetaOapg.properties.direct, bool, schemas.Unset] = schemas.unset,
        readOnly: typing.Union[MetaOapg.properties.readOnly, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FunctionInvocationInvokeFunction403Response':
        return super().__new__(
            cls,
            *args,
            short=short,
            char=char,
            long=long,
            double=double,
            direct=direct,
            readOnly=readOnly,
            _configuration=_configuration,
            **kwargs,
        )
