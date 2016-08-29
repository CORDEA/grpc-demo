#!/usr/bin/env python
# encoding:utf-8
#
# Copyright 2016 Yoshihiro Tanaka
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__Author__ =  "Yoshihiro Tanaka <contact@cordea.jp>"
__date__   =  "2016-08-28"

import random, string

import grpc_demo_pb2 as pb

def _create_nonce():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Object:
    def __init__(self, string_demo):
        self.string_demo = string_demo

    def to_data(self):
        obj = pb.Object()
        obj.StringDemo = self.string_demo
        return obj

    def set_to_data(self, obj):
        obj.StringDemo = self.string_demo

class Request:
    def __init__(self, map_demo, double_demo = None, float_demo = None):
        self.map_demo = map_demo
        self.double_demo = double_demo
        self.float_demo = float_demo

    def to_data(self):
        req = pb.Request()
        req.Nonce = _create_nonce()
        for k, v in self.map_demo.items():
            v.set_to_data(req.MapDemo[k])
        if self.double_demo:
            req.DoubleDemo = self.double_demo
        if self.float_demo:
            req.FloatDemo = self.float_demo
        return req

class Response:
    def __init__(self, nonce, bytes_demo, enum_demo):
        self.nonce = nonce
        self.bytes_demo = bytes_demo
        self.enum_demo = enum_demo

    def to_data(self):
        resp = pb.Response()
        resp.Nonce = self.nonce
        resp.BytesDemo = self.bytes_demo
        resp.EnumDemo = self.enum_demo
        return resp

class StreamRequest:
    def __init__(self, float_demo):
        self.float_demo = float_demo

    def to_data(self):
        req = pb.StreamRequest()
        req.Nonce = _create_nonce()
        req.FloatDemo = self.float_demo
        return req

class StreamResponse:
    def __init__(self, nonce, enum_demo):
        self.nonce = nonce
        self.enum_demo = enum_demo

    def to_data(self):
        resp = pb.StreamResponse()
        resp.Nonce = self.nonce
        resp.EnumDemo = self.enum_demo
        return resp

class RepeatedRequest:
    def __init__(self, int_demo, object_demo):
        self.int_demo = int_demo
        self.object_demo = object_demo

    def to_data(self):
        req = pb.RepeatedRequest()
        req.Nonce = _create_nonce()
        for i in self.int_demo:
            req.IntDemo.append(i)
        for i in self.object_demo:
            req.ObjectDemo.extend([i.to_data()])
        return req

class RepeatedResponse:
    def __init__(self, nonce, string_demo):
        self.nonce = nonce
        self.string_demo = string_demo

    def to_data(self):
        resp = pb.RepeatedResponse()
        resp.Nonce = self.nonce
        for i in self.string_demo:
            resp.StringDemo.append(i)
        return resp
