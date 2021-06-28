# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kodama_msg.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kodama_msg.proto',
  package='kodama',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10kodama_msg.proto\x12\x06kodama\x1a\x1fgoogle/protobuf/timestamp.proto\"t\n\x0bRequestData\x12\x0e\n\x06tag_id\x18\x01 \x01(\x05\x12\t\n\x01v\x18\x02 \x01(\x05\x12\t\n\x01w\x18\x03 \x01(\x05\x12\x0b\n\x03tau\x18\x04 \x01(\x05\x12\x10\n\x08scenario\x18\x06 \x01(\x05\x12\x0f\n\x07targetX\x18\x07 \x01(\x05\x12\x0f\n\x07targetY\x18\x08 \x01(\x05\"\xac\x02\n\nSensorData\x12\'\n\x04pose\x18\x01 \x01(\x0b\x32\x19.kodama.SensorData.Pose2D\x12\x35\n\x12nearby_robot_poses\x18\x02 \x03(\x0b\x32\x19.kodama.SensorData.Pose2D\x12>\n\x17nearby_target_positions\x18\x03 \x03(\x0b\x32\x1d.kodama.SensorData.Position2D\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\"\n\nPosition2D\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x1a+\n\x06Pose2D\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0b\n\x03yaw\x18\x03 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_REQUESTDATA = _descriptor.Descriptor(
  name='RequestData',
  full_name='kodama.RequestData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tag_id', full_name='kodama.RequestData.tag_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v', full_name='kodama.RequestData.v', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='kodama.RequestData.w', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tau', full_name='kodama.RequestData.tau', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scenario', full_name='kodama.RequestData.scenario', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetX', full_name='kodama.RequestData.targetX', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetY', full_name='kodama.RequestData.targetY', index=6,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=61,
  serialized_end=177,
)


_SENSORDATA_POSITION2D = _descriptor.Descriptor(
  name='Position2D',
  full_name='kodama.SensorData.Position2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='kodama.SensorData.Position2D.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='kodama.SensorData.Position2D.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=401,
  serialized_end=435,
)

_SENSORDATA_POSE2D = _descriptor.Descriptor(
  name='Pose2D',
  full_name='kodama.SensorData.Pose2D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='kodama.SensorData.Pose2D.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='kodama.SensorData.Pose2D.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='kodama.SensorData.Pose2D.yaw', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=437,
  serialized_end=480,
)

_SENSORDATA = _descriptor.Descriptor(
  name='SensorData',
  full_name='kodama.SensorData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pose', full_name='kodama.SensorData.pose', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nearby_robot_poses', full_name='kodama.SensorData.nearby_robot_poses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nearby_target_positions', full_name='kodama.SensorData.nearby_target_positions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='kodama.SensorData.timestamp', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SENSORDATA_POSITION2D, _SENSORDATA_POSE2D, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=480,
)

_SENSORDATA_POSITION2D.containing_type = _SENSORDATA
_SENSORDATA_POSE2D.containing_type = _SENSORDATA
_SENSORDATA.fields_by_name['pose'].message_type = _SENSORDATA_POSE2D
_SENSORDATA.fields_by_name['nearby_robot_poses'].message_type = _SENSORDATA_POSE2D
_SENSORDATA.fields_by_name['nearby_target_positions'].message_type = _SENSORDATA_POSITION2D
_SENSORDATA.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['RequestData'] = _REQUESTDATA
DESCRIPTOR.message_types_by_name['SensorData'] = _SENSORDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestData = _reflection.GeneratedProtocolMessageType('RequestData', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTDATA,
  __module__ = 'kodama_msg_pb2'
  # @@protoc_insertion_point(class_scope:kodama.RequestData)
  ))
_sym_db.RegisterMessage(RequestData)

SensorData = _reflection.GeneratedProtocolMessageType('SensorData', (_message.Message,), dict(

  Position2D = _reflection.GeneratedProtocolMessageType('Position2D', (_message.Message,), dict(
    DESCRIPTOR = _SENSORDATA_POSITION2D,
    __module__ = 'kodama_msg_pb2'
    # @@protoc_insertion_point(class_scope:kodama.SensorData.Position2D)
    ))
  ,

  Pose2D = _reflection.GeneratedProtocolMessageType('Pose2D', (_message.Message,), dict(
    DESCRIPTOR = _SENSORDATA_POSE2D,
    __module__ = 'kodama_msg_pb2'
    # @@protoc_insertion_point(class_scope:kodama.SensorData.Pose2D)
    ))
  ,
  DESCRIPTOR = _SENSORDATA,
  __module__ = 'kodama_msg_pb2'
  # @@protoc_insertion_point(class_scope:kodama.SensorData)
  ))
_sym_db.RegisterMessage(SensorData)
_sym_db.RegisterMessage(SensorData.Position2D)
_sym_db.RegisterMessage(SensorData.Pose2D)


# @@protoc_insertion_point(module_scope)