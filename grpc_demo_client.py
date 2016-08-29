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

from grpc_demo_common import *

import grpc

import grpc_demo_pb2 as pb

def demo(stub):
    o = Request({'key': Object('test')}, 1.0).to_data()
    resp = stub.Demo(o)
    print('nonce:', resp.Nonce)

def stream_demo_requests():
    for i in range(10):
        o = StreamRequest(1.0).to_data()
        yield o

def stream_demo(stub):
    resps = stub.StreamDemo(stream_demo_requests())
    for resp in resps:
        print('nonce:', resp.Nonce)

def repeated_demo(stub):
    o = RepeatedRequest([1, 2, 3, 4, 5], [Object('string'), Object('string')]).to_data()
    resp = stub.RepeatedDemo(o)
    print('nonce:', resp.Nonce)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb.GrpcDemoStub(channel)

    print('--- demo request')
    demo(stub)
    print('--- repeated demo request')
    repeated_demo(stub)
    print('--- stream demo request')
    stream_demo(stub)

if __name__=='__main__':
    run()
