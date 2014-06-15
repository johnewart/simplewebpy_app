import web
import view, config
from view import render

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.base(view.listing())

    if __name__ == "__main__":
      try:
        config.DB.query("CREATE TABLE items (id serial primary key,body text)")
        config.DB.query("INSERT INTO items(body) values('Item 1')")
        config.DB.query("INSERT INTO items(body) values('Item 2')")
        config.DB.query("INSERT INTO items(body) values('Item 3')")
        config.DB.query("INSERT INTO items(body) values('Item 4')")
        config.DB.query("INSERT INTO items(body) values('Item 5')")
      except:
        print "Already created data..."

      app = web.application(urls, globals())
      app.internalerror = web.debugerror
      app.run()
