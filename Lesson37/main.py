import tornado.web
import tornado.ioloop


class Mainhandler(tornado.web.RequestHandler):
    async def get (self):
        self.write("Start<br>")
        await self.number_writer()
        self.write("End")
    async def number_writer(self):
        for i in range(1,11):
            self.write(f"Processing....{i}<br>")
            await tornado.gen.sleep(1)
class Posthandler(tornado.web.RequestHandler):
    def get(self):
        self.write('PostHandler Get Request')

    def post(self):
        self.write('PostHandler Post Request')

def make_app():
    return tornado.web.Application([
        (r"/", Mainhandler),
        (r"/post", Posthandler)
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()