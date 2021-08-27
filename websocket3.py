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
"""Simplified chat demo for websockets.
Authentication, error handling, etc are left as an exercise for the reader :)
"""
import asyncio
import json
import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import uuid

# from tornado.options import define
from tornado import gen

from myjson import EnhancedJSONEncoder
from packet import DashPacket
from signal import TelemetryListener
from telemetry import UdpTelemetrySource


# define("port", default=5678, help="run on the given port", type=int)


class Looper:
    def __init__(self):
        self.listener: TelemetryListener = None

    async def minute_loop(self):
        source = UdpTelemetrySource([])
        source.init()
        while True:
            # print("before")
            packet = await source.receive2()
            if self.listener is not None:
                self.listener.receive(packet)
            # print("after")
            # await do_something()
            await gen.sleep(1 / 120)

    def register(self, listener: TelemetryListener):
        self.listener = listener


class Application(tornado.web.Application):
    def __init__(self, udpsource: Looper):
        # handlers = [(r"/", MainHandler), (r"/", ChatSocketHandler)]
        handlers = [(r"/", ChatSocketHandler, {"source": udpsource})]
        # settings = dict(
        #     cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
        #     static_path=os.path.join(os.path.dirname(__file__), "static"),
        #     xsrf_cookies=True,
        # )
        settings = dict()
        super().__init__(handlers, **settings)


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render("index.html", messages=ChatSocketHandler.cache)


class ChatSocketHandler(tornado.websocket.WebSocketHandler, TelemetryListener):
    def receive(self, data: DashPacket):
        self.send_updates(data)

    waiters = set()
    cache = []
    cache_size = 200

    def initialize(self, source: Looper):
        self.source = source
        print(source)
        self.source.register(self)

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self):
        logging.info("connected")
        ChatSocketHandler.waiters.add(self)

    def on_close(self):
        logging.info("closed")
        ChatSocketHandler.waiters.remove(self)

    @classmethod
    def update_cache(cls, chat):
        cls.cache.append(chat)
        if len(cls.cache) > cls.cache_size:
            cls.cache = cls.cache[-cls.cache_size:]

    @classmethod
    def send_updates(cls, chat: DashPacket):
        x = json.dumps(chat, cls=EnhancedJSONEncoder)

        print(f"Sending {chat.TimestampMS}", flush=True)
        for waiter in cls.waiters:
            try:
                waiter.write_message(x)
            except:
                logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        logging.info("got message %r", message)
        parsed = tornado.escape.json_decode(message)
        chat = {"id": str(uuid.uuid4()), "body": parsed["body"]}
        chat["html"] = tornado.escape.to_basestring(
            self.render_string("message.html", message=chat)
        )

        ChatSocketHandler.update_cache(chat)
        ChatSocketHandler.send_updates(chat)

    def check_origin(self, origin):
        return True


class X:
    def udp(self):
        print("callback")


def main():
    looper = Looper()
    x = X()
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    tornado.options.parse_command_line()
    app = Application(looper)
    app.listen(5678, "0.0.0.0")
    tornado.ioloop.IOLoop.current().spawn_callback(looper.minute_loop)
    # tornado.ioloop.IOLoop.instance().add_callback(callback=x.udp)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
