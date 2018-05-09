# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/plugins/inference/utils/inference.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow_serving.apis import classification_pb2 as tensorflow__serving_dot_apis_dot_classification__pb2
from tensorflow_serving.apis import regression_pb2 as tensorflow__serving_dot_apis_dot_regression__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/plugins/inference/utils/inference.proto',
  package='tensorboard.plugins.inference.utils',
  syntax='proto3',
  serialized_pb=_b('\n3tensorboard/plugins/inference/utils/inference.proto\x12#tensorboard.plugins.inference.utils\x1a,tensorflow_serving/apis/classification.proto\x1a(tensorflow_serving/apis/regression.proto\"\x9b\x01\n\x0fInferenceResult\x12\x42\n\x0e\x63lassification\x18\x01 \x01(\x0b\x32(.tensorflow.serving.ClassificationResultH\x00\x12:\n\nregression\x18\x02 \x01(\x0b\x32$.tensorflow.serving.RegressionResultH\x00\x42\x08\n\x06resultb\x06proto3')
  ,
  dependencies=[tensorflow__serving_dot_apis_dot_classification__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_regression__pb2.DESCRIPTOR,])




_INFERENCERESULT = _descriptor.Descriptor(
  name='InferenceResult',
  full_name='tensorboard.plugins.inference.utils.InferenceResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classification', full_name='tensorboard.plugins.inference.utils.InferenceResult.classification', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regression', full_name='tensorboard.plugins.inference.utils.InferenceResult.regression', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='result', full_name='tensorboard.plugins.inference.utils.InferenceResult.result',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=181,
  serialized_end=336,
)

_INFERENCERESULT.fields_by_name['classification'].message_type = tensorflow__serving_dot_apis_dot_classification__pb2._CLASSIFICATIONRESULT
_INFERENCERESULT.fields_by_name['regression'].message_type = tensorflow__serving_dot_apis_dot_regression__pb2._REGRESSIONRESULT
_INFERENCERESULT.oneofs_by_name['result'].fields.append(
  _INFERENCERESULT.fields_by_name['classification'])
_INFERENCERESULT.fields_by_name['classification'].containing_oneof = _INFERENCERESULT.oneofs_by_name['result']
_INFERENCERESULT.oneofs_by_name['result'].fields.append(
  _INFERENCERESULT.fields_by_name['regression'])
_INFERENCERESULT.fields_by_name['regression'].containing_oneof = _INFERENCERESULT.oneofs_by_name['result']
DESCRIPTOR.message_types_by_name['InferenceResult'] = _INFERENCERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InferenceResult = _reflection.GeneratedProtocolMessageType('InferenceResult', (_message.Message,), dict(
  DESCRIPTOR = _INFERENCERESULT,
  __module__ = 'tensorboard.plugins.inference.utils.inference_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.plugins.inference.utils.InferenceResult)
  ))
_sym_db.RegisterMessage(InferenceResult)


# @@protoc_insertion_point(module_scope)