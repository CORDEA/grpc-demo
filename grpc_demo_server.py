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

from concurrent import futures
from grpc_demo_common import *

import time
import grpc

import grpc_demo_pb2 as pb

class GrpcDemoServicer(pb.GrpcDemoServicer):

    def Demo(self, request, context):
        print('--- received demo request')
        print('nonce:', request.Nonce)
        resp = Response(request.Nonce, b'bytes', pb.DEMO1).to_data()
        return resp

    def RepeatedDemo(self, request, context):
        print('--- received repeated demo request')
        print('nonce:', request.Nonce)
        resp = RepeatedResponse(request.Nonce, ['string', 'string']).to_data()
        return resp

    def StreamDemo(self, requests, context):
        print('--- received stream demo request')
        for req in requests:
            print('nonce:', req.Nonce)
            resp = StreamResponse(req.Nonce, pb.DEMO2).to_data()
            yield resp

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb.add_GrpcDemoServicer_to_server(GrpcDemoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(24 * 60 * 60)
    except KeyboardInterrupt:
        server.stop(0)

if __name__=='__main__':
    serve()
