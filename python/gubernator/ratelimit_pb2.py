# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ratelimit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ratelimit.proto',
  package='pb.gubernator',
  syntax='proto3',
  serialized_options=_b('Z\ngubernator\200\001\001'),
  serialized_pb=_b('\n\x0fratelimit.proto\x12\rpb.gubernator\x1a\x1cgoogle/api/annotations.proto\"4\n\x08Requests\x12(\n\x08requests\x18\x01 \x03(\x0b\x32\x16.pb.gubernator.Request\";\n\nRateLimits\x12-\n\x0brate_limits\x18\x01 \x03(\x0b\x32\x18.pb.gubernator.RateLimit\"\xb7\x01\n\x07Request\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\nunique_key\x18\x02 \x01(\t\x12\x0c\n\x04hits\x18\x03 \x01(\x03\x12\r\n\x05limit\x18\x04 \x01(\x03\x12\x10\n\x08\x64uration\x18\x05 \x01(\x03\x12+\n\talgorithm\x18\x06 \x01(\x0e\x32\x18.pb.gubernator.Algorithm\x12)\n\x08\x62\x65havior\x18\x07 \x01(\x0e\x32\x17.pb.gubernator.Behavior\"\xf0\x01\n\tRateLimit\x12%\n\x06status\x18\x01 \x01(\x0e\x32\x15.pb.gubernator.Status\x12\x15\n\rcurrent_limit\x18\x02 \x01(\x03\x12\x17\n\x0flimit_remaining\x18\x03 \x01(\x03\x12\x12\n\nreset_time\x18\x04 \x01(\x03\x12\r\n\x05\x65rror\x18\x05 \x01(\t\x12\x38\n\x08metadata\x18\x06 \x03(\x0b\x32&.pb.gubernator.RateLimit.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x10\n\x0eHealthCheckReq\"F\n\x0fHealthCheckResp\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\npeer_count\x18\x03 \x01(\x05*/\n\tAlgorithm\x12\x10\n\x0cTOKEN_BUCKET\x10\x00\x12\x10\n\x0cLEAKY_BUCKET\x10\x01*5\n\x08\x42\x65havior\x12\x0c\n\x08\x42\x41TCHING\x10\x00\x12\x0f\n\x0bNO_BATCHING\x10\x01\x12\n\n\x06GLOBAL\x10\x02*)\n\x06Status\x12\x0f\n\x0bUNDER_LIMIT\x10\x00\x12\x0e\n\nOVER_LIMIT\x10\x01\x32\xde\x01\n\x12RateLimitServiceV1\x12\x61\n\rGetRateLimits\x12\x17.pb.gubernator.Requests\x1a\x19.pb.gubernator.RateLimits\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/GetRateLimits:\x01*\x12\x65\n\x0bHealthCheck\x12\x1d.pb.gubernator.HealthCheckReq\x1a\x1e.pb.gubernator.HealthCheckResp\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/HealthCheckB\x0fZ\ngubernator\x80\x01\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_ALGORITHM = _descriptor.EnumDescriptor(
  name='Algorithm',
  full_name='pb.gubernator.Algorithm',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TOKEN_BUCKET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAKY_BUCKET', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=698,
  serialized_end=745,
)
_sym_db.RegisterEnumDescriptor(_ALGORITHM)

Algorithm = enum_type_wrapper.EnumTypeWrapper(_ALGORITHM)
_BEHAVIOR = _descriptor.EnumDescriptor(
  name='Behavior',
  full_name='pb.gubernator.Behavior',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BATCHING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_BATCHING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOBAL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=747,
  serialized_end=800,
)
_sym_db.RegisterEnumDescriptor(_BEHAVIOR)

Behavior = enum_type_wrapper.EnumTypeWrapper(_BEHAVIOR)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pb.gubernator.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDER_LIMIT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVER_LIMIT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=802,
  serialized_end=843,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
TOKEN_BUCKET = 0
LEAKY_BUCKET = 1
BATCHING = 0
NO_BATCHING = 1
GLOBAL = 2
UNDER_LIMIT = 0
OVER_LIMIT = 1



_REQUESTS = _descriptor.Descriptor(
  name='Requests',
  full_name='pb.gubernator.Requests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='pb.gubernator.Requests.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=116,
)


_RATELIMITS = _descriptor.Descriptor(
  name='RateLimits',
  full_name='pb.gubernator.RateLimits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rate_limits', full_name='pb.gubernator.RateLimits.rate_limits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=177,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='pb.gubernator.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pb.gubernator.Request.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unique_key', full_name='pb.gubernator.Request.unique_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hits', full_name='pb.gubernator.Request.hits', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='pb.gubernator.Request.limit', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='pb.gubernator.Request.duration', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='pb.gubernator.Request.algorithm', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='behavior', full_name='pb.gubernator.Request.behavior', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=363,
)


_RATELIMIT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='pb.gubernator.RateLimit.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pb.gubernator.RateLimit.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='pb.gubernator.RateLimit.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=606,
)

_RATELIMIT = _descriptor.Descriptor(
  name='RateLimit',
  full_name='pb.gubernator.RateLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pb.gubernator.RateLimit.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_limit', full_name='pb.gubernator.RateLimit.current_limit', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit_remaining', full_name='pb.gubernator.RateLimit.limit_remaining', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reset_time', full_name='pb.gubernator.RateLimit.reset_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='pb.gubernator.RateLimit.error', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pb.gubernator.RateLimit.metadata', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RATELIMIT_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=606,
)


_HEALTHCHECKREQ = _descriptor.Descriptor(
  name='HealthCheckReq',
  full_name='pb.gubernator.HealthCheckReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=624,
)


_HEALTHCHECKRESP = _descriptor.Descriptor(
  name='HealthCheckResp',
  full_name='pb.gubernator.HealthCheckResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pb.gubernator.HealthCheckResp.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='pb.gubernator.HealthCheckResp.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peer_count', full_name='pb.gubernator.HealthCheckResp.peer_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=626,
  serialized_end=696,
)

_REQUESTS.fields_by_name['requests'].message_type = _REQUEST
_RATELIMITS.fields_by_name['rate_limits'].message_type = _RATELIMIT
_REQUEST.fields_by_name['algorithm'].enum_type = _ALGORITHM
_REQUEST.fields_by_name['behavior'].enum_type = _BEHAVIOR
_RATELIMIT_METADATAENTRY.containing_type = _RATELIMIT
_RATELIMIT.fields_by_name['status'].enum_type = _STATUS
_RATELIMIT.fields_by_name['metadata'].message_type = _RATELIMIT_METADATAENTRY
DESCRIPTOR.message_types_by_name['Requests'] = _REQUESTS
DESCRIPTOR.message_types_by_name['RateLimits'] = _RATELIMITS
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['RateLimit'] = _RATELIMIT
DESCRIPTOR.message_types_by_name['HealthCheckReq'] = _HEALTHCHECKREQ
DESCRIPTOR.message_types_by_name['HealthCheckResp'] = _HEALTHCHECKRESP
DESCRIPTOR.enum_types_by_name['Algorithm'] = _ALGORITHM
DESCRIPTOR.enum_types_by_name['Behavior'] = _BEHAVIOR
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Requests = _reflection.GeneratedProtocolMessageType('Requests', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTS,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.Requests)
  ))
_sym_db.RegisterMessage(Requests)

RateLimits = _reflection.GeneratedProtocolMessageType('RateLimits', (_message.Message,), dict(
  DESCRIPTOR = _RATELIMITS,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimits)
  ))
_sym_db.RegisterMessage(RateLimits)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.Request)
  ))
_sym_db.RegisterMessage(Request)

RateLimit = _reflection.GeneratedProtocolMessageType('RateLimit', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _RATELIMIT_METADATAENTRY,
    __module__ = 'ratelimit_pb2'
    # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimit.MetadataEntry)
    ))
  ,
  DESCRIPTOR = _RATELIMIT,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.RateLimit)
  ))
_sym_db.RegisterMessage(RateLimit)
_sym_db.RegisterMessage(RateLimit.MetadataEntry)

HealthCheckReq = _reflection.GeneratedProtocolMessageType('HealthCheckReq', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKREQ,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.HealthCheckReq)
  ))
_sym_db.RegisterMessage(HealthCheckReq)

HealthCheckResp = _reflection.GeneratedProtocolMessageType('HealthCheckResp', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHCHECKRESP,
  __module__ = 'ratelimit_pb2'
  # @@protoc_insertion_point(class_scope:pb.gubernator.HealthCheckResp)
  ))
_sym_db.RegisterMessage(HealthCheckResp)


DESCRIPTOR._options = None
_RATELIMIT_METADATAENTRY._options = None

_RATELIMITSERVICEV1 = _descriptor.ServiceDescriptor(
  name='RateLimitServiceV1',
  full_name='pb.gubernator.RateLimitServiceV1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=846,
  serialized_end=1068,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRateLimits',
    full_name='pb.gubernator.RateLimitServiceV1.GetRateLimits',
    index=0,
    containing_service=None,
    input_type=_REQUESTS,
    output_type=_RATELIMITS,
    serialized_options=_b('\202\323\344\223\002\026\"\021/v1/GetRateLimits:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='HealthCheck',
    full_name='pb.gubernator.RateLimitServiceV1.HealthCheck',
    index=1,
    containing_service=None,
    input_type=_HEALTHCHECKREQ,
    output_type=_HEALTHCHECKRESP,
    serialized_options=_b('\202\323\344\223\002\021\022\017/v1/HealthCheck'),
  ),
])
_sym_db.RegisterServiceDescriptor(_RATELIMITSERVICEV1)

DESCRIPTOR.services_by_name['RateLimitServiceV1'] = _RATELIMITSERVICEV1

# @@protoc_insertion_point(module_scope)
