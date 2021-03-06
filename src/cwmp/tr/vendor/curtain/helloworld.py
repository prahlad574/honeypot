#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import digest
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(digest.DigestAuthMixin, tornado.web.RequestHandler):
    def getcreds(uname):
        creds = {'auth_username': 'jonesy', 'auth_password': 'foobar'}
        if uname == creds['auth_username']:
            return creds

    @digest.digest_auth('Authusers', getcreds)
    def get(self):
        self.write("Hello, world - Tornado %s" % tornado.version)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
