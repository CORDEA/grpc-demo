# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_demo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc_demo.proto',
  package='grpcdemo',
  syntax='proto3',
  serialized_pb=_b('\n\x0fgrpc_demo.proto\x12\x08grpcdemo\"\xc3\x01\n\x07Request\x12\r\n\x05Nonce\x18\x01 \x01(\t\x12/\n\x07MapDemo\x18\x02 \x03(\x0b\x32\x1e.grpcdemo.Request.MapDemoEntry\x12\x14\n\nDoubleDemo\x18\x03 \x01(\x01H\x00\x12\x13\n\tFloatDemo\x18\x04 \x01(\x02H\x00\x1a@\n\x0cMapDemoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.grpcdemo.Object:\x02\x38\x01\x42\x0b\n\tOneOfDemo\"N\n\x08Response\x12\r\n\x05Nonce\x18\x01 \x01(\t\x12\x11\n\tBytesDemo\x18\x02 \x01(\x0c\x12 \n\x08\x45numDemo\x18\x03 \x01(\x0e\x32\x0e.grpcdemo.Enum\"\x1c\n\x06Object\x12\x12\n\nStringDemo\x18\x01 \x01(\t\"W\n\x0fRepeatedRequest\x12\r\n\x05Nonce\x18\x01 \x01(\t\x12\x0f\n\x07IntDemo\x18\x02 \x03(\x05\x12$\n\nObjectDemo\x18\x03 \x03(\x0b\x32\x10.grpcdemo.Object\"5\n\x10RepeatedResponse\x12\r\n\x05Nonce\x18\x01 \x01(\t\x12\x12\n\nStringDemo\x18\x02 \x03(\t\"1\n\rStreamRequest\x12\r\n\x05Nonce\x18\x01 \x01(\t\x12\x11\n\tFloatDemo\x18\x02 \x01(\x02\"A\n\x0eStreamResponse\x12\r\n\x05Nonce\x18\x01 \x01(\t\x12 \n\x08\x45numDemo\x18\x02 \x01(\x0e\x32\x0e.grpcdemo.Enum*\x1c\n\x04\x45num\x12\t\n\x05\x44\x45MO1\x10\x00\x12\t\n\x05\x44\x45MO2\x10\x01\x32\xcb\x01\n\x08GrpcDemo\x12/\n\x04\x44\x65mo\x12\x11.grpcdemo.Request\x1a\x12.grpcdemo.Response\"\x00\x12G\n\x0cRepeatedDemo\x12\x19.grpcdemo.RepeatedRequest\x1a\x1a.grpcdemo.RepeatedResponse\"\x00\x12\x45\n\nStreamDemo\x12\x17.grpcdemo.StreamRequest\x1a\x18.grpcdemo.StreamResponse\"\x00(\x01\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_ENUM = _descriptor.EnumDescriptor(
  name='Enum',
  full_name='grpcdemo.Enum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEMO1', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEMO2', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=599,
  serialized_end=627,
)
_sym_db.RegisterEnumDescriptor(_ENUM)

Enum = enum_type_wrapper.EnumTypeWrapper(_ENUM)
DEMO1 = 0
DEMO2 = 1



_REQUEST_MAPDEMOENTRY = _descriptor.Descriptor(
  name='MapDemoEntry',
  full_name='grpcdemo.Request.MapDemoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='grpcdemo.Request.MapDemoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='grpcdemo.Request.MapDemoEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=212,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='grpcdemo.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Nonce', full_name='grpcdemo.Request.Nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MapDemo', full_name='grpcdemo.Request.MapDemo', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DoubleDemo', full_name='grpcdemo.Request.DoubleDemo', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FloatDemo', full_name='grpcdemo.Request.FloatDemo', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_MAPDEMOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='OneOfDemo', full_name='grpcdemo.Request.OneOfDemo',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=30,
  serialized_end=225,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='grpcdemo.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Nonce', full_name='grpcdemo.Response.Nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BytesDemo', full_name='grpcdemo.Response.BytesDemo', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EnumDemo', full_name='grpcdemo.Response.EnumDemo', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=305,
)


_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='grpcdemo.Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StringDemo', full_name='grpcdemo.Object.StringDemo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=335,
)


_REPEATEDREQUEST = _descriptor.Descriptor(
  name='RepeatedRequest',
  full_name='grpcdemo.RepeatedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Nonce', full_name='grpcdemo.RepeatedRequest.Nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='IntDemo', full_name='grpcdemo.RepeatedRequest.IntDemo', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ObjectDemo', full_name='grpcdemo.RepeatedRequest.ObjectDemo', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=337,
  serialized_end=424,
)


_REPEATEDRESPONSE = _descriptor.Descriptor(
  name='RepeatedResponse',
  full_name='grpcdemo.RepeatedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Nonce', full_name='grpcdemo.RepeatedResponse.Nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StringDemo', full_name='grpcdemo.RepeatedResponse.StringDemo', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=479,
)


_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='grpcdemo.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Nonce', full_name='grpcdemo.StreamRequest.Nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FloatDemo', full_name='grpcdemo.StreamRequest.FloatDemo', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=481,
  serialized_end=530,
)


_STREAMRESPONSE = _descriptor.Descriptor(
  name='StreamResponse',
  full_name='grpcdemo.StreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Nonce', full_name='grpcdemo.StreamResponse.Nonce', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EnumDemo', full_name='grpcdemo.StreamResponse.EnumDemo', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=597,
)

_REQUEST_MAPDEMOENTRY.fields_by_name['value'].message_type = _OBJECT
_REQUEST_MAPDEMOENTRY.containing_type = _REQUEST
_REQUEST.fields_by_name['MapDemo'].message_type = _REQUEST_MAPDEMOENTRY
_REQUEST.oneofs_by_name['OneOfDemo'].fields.append(
  _REQUEST.fields_by_name['DoubleDemo'])
_REQUEST.fields_by_name['DoubleDemo'].containing_oneof = _REQUEST.oneofs_by_name['OneOfDemo']
_REQUEST.oneofs_by_name['OneOfDemo'].fields.append(
  _REQUEST.fields_by_name['FloatDemo'])
_REQUEST.fields_by_name['FloatDemo'].containing_oneof = _REQUEST.oneofs_by_name['OneOfDemo']
_RESPONSE.fields_by_name['EnumDemo'].enum_type = _ENUM
_REPEATEDREQUEST.fields_by_name['ObjectDemo'].message_type = _OBJECT
_STREAMRESPONSE.fields_by_name['EnumDemo'].enum_type = _ENUM
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['RepeatedRequest'] = _REPEATEDREQUEST
DESCRIPTOR.message_types_by_name['RepeatedResponse'] = _REPEATEDRESPONSE
DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['StreamResponse'] = _STREAMRESPONSE
DESCRIPTOR.enum_types_by_name['Enum'] = _ENUM

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(

  MapDemoEntry = _reflection.GeneratedProtocolMessageType('MapDemoEntry', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST_MAPDEMOENTRY,
    __module__ = 'grpc_demo_pb2'
    # @@protoc_insertion_point(class_scope:grpcdemo.Request.MapDemoEntry)
    ))
  ,
  DESCRIPTOR = _REQUEST,
  __module__ = 'grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:grpcdemo.Request)
  ))
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.MapDemoEntry)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:grpcdemo.Response)
  ))
_sym_db.RegisterMessage(Response)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), dict(
  DESCRIPTOR = _OBJECT,
  __module__ = 'grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:grpcdemo.Object)
  ))
_sym_db.RegisterMessage(Object)

RepeatedRequest = _reflection.GeneratedProtocolMessageType('RepeatedRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPEATEDREQUEST,
  __module__ = 'grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:grpcdemo.RepeatedRequest)
  ))
_sym_db.RegisterMessage(RepeatedRequest)

RepeatedResponse = _reflection.GeneratedProtocolMessageType('RepeatedResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPEATEDRESPONSE,
  __module__ = 'grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:grpcdemo.RepeatedResponse)
  ))
_sym_db.RegisterMessage(RepeatedResponse)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMREQUEST,
  __module__ = 'grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:grpcdemo.StreamRequest)
  ))
_sym_db.RegisterMessage(StreamRequest)

StreamResponse = _reflection.GeneratedProtocolMessageType('StreamResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMRESPONSE,
  __module__ = 'grpc_demo_pb2'
  # @@protoc_insertion_point(class_scope:grpcdemo.StreamResponse)
  ))
_sym_db.RegisterMessage(StreamResponse)


_REQUEST_MAPDEMOENTRY.has_options = True
_REQUEST_MAPDEMOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class GrpcDemoStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Demo = channel.unary_unary(
        '/grpcdemo.GrpcDemo/Demo',
        request_serializer=Request.SerializeToString,
        response_deserializer=Response.FromString,
        )
    self.RepeatedDemo = channel.unary_unary(
        '/grpcdemo.GrpcDemo/RepeatedDemo',
        request_serializer=RepeatedRequest.SerializeToString,
        response_deserializer=RepeatedResponse.FromString,
        )
    self.StreamDemo = channel.stream_stream(
        '/grpcdemo.GrpcDemo/StreamDemo',
        request_serializer=StreamRequest.SerializeToString,
        response_deserializer=StreamResponse.FromString,
        )


class GrpcDemoServicer(object):

  def Demo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RepeatedDemo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamDemo(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GrpcDemoServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Demo': grpc.unary_unary_rpc_method_handler(
          servicer.Demo,
          request_deserializer=Request.FromString,
          response_serializer=Response.SerializeToString,
      ),
      'RepeatedDemo': grpc.unary_unary_rpc_method_handler(
          servicer.RepeatedDemo,
          request_deserializer=RepeatedRequest.FromString,
          response_serializer=RepeatedResponse.SerializeToString,
      ),
      'StreamDemo': grpc.stream_stream_rpc_method_handler(
          servicer.StreamDemo,
          request_deserializer=StreamRequest.FromString,
          response_serializer=StreamResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpcdemo.GrpcDemo', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaGrpcDemoServicer(object):
  def Demo(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def RepeatedDemo(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def StreamDemo(self, request_iterator, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaGrpcDemoStub(object):
  def Demo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Demo.future = None
  def RepeatedDemo(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  RepeatedDemo.future = None
  def StreamDemo(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()


def beta_create_GrpcDemo_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('grpcdemo.GrpcDemo', 'Demo'): Request.FromString,
    ('grpcdemo.GrpcDemo', 'RepeatedDemo'): RepeatedRequest.FromString,
    ('grpcdemo.GrpcDemo', 'StreamDemo'): StreamRequest.FromString,
  }
  response_serializers = {
    ('grpcdemo.GrpcDemo', 'Demo'): Response.SerializeToString,
    ('grpcdemo.GrpcDemo', 'RepeatedDemo'): RepeatedResponse.SerializeToString,
    ('grpcdemo.GrpcDemo', 'StreamDemo'): StreamResponse.SerializeToString,
  }
  method_implementations = {
    ('grpcdemo.GrpcDemo', 'Demo'): face_utilities.unary_unary_inline(servicer.Demo),
    ('grpcdemo.GrpcDemo', 'RepeatedDemo'): face_utilities.unary_unary_inline(servicer.RepeatedDemo),
    ('grpcdemo.GrpcDemo', 'StreamDemo'): face_utilities.stream_stream_inline(servicer.StreamDemo),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_GrpcDemo_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('grpcdemo.GrpcDemo', 'Demo'): Request.SerializeToString,
    ('grpcdemo.GrpcDemo', 'RepeatedDemo'): RepeatedRequest.SerializeToString,
    ('grpcdemo.GrpcDemo', 'StreamDemo'): StreamRequest.SerializeToString,
  }
  response_deserializers = {
    ('grpcdemo.GrpcDemo', 'Demo'): Response.FromString,
    ('grpcdemo.GrpcDemo', 'RepeatedDemo'): RepeatedResponse.FromString,
    ('grpcdemo.GrpcDemo', 'StreamDemo'): StreamResponse.FromString,
  }
  cardinalities = {
    'Demo': cardinality.Cardinality.UNARY_UNARY,
    'RepeatedDemo': cardinality.Cardinality.UNARY_UNARY,
    'StreamDemo': cardinality.Cardinality.STREAM_STREAM,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'grpcdemo.GrpcDemo', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
