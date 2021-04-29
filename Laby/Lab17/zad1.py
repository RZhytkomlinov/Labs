from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
class Base:
    def __init__(self,name):
        self.engine = create_engine('sqlite:///{}.db'.format(name), echo = True)
        self.meta = MetaData()
        self.table = Table(
            '{}'.format(name), self.meta,
            Column('id', Integer, primary_key = True,),
            Column('title', String),
            Column('director', String),
            Column('actors', String),
            Column('vod', String),
            sqlite_autoincrement = True,
        )
        self.meta.create_all(self.engine)
        # print("these are columns in our table %s" %(self.films.columns.keys()))

    def delete_film(self,title):
        conn = self.engine.connect()
        dels = self.table.delete().where(self.table.c.title == title)
        conn.execute(dels)
        s = self.table.select()
        conn.execute(s).fetchall()

    def add_film(self, title, dirc, actor, vod):
        conn = self.engine.connect()
        insert = self.table.insert().values(title == title, director = dirc, actors = actor, vod = vod)
        conn.execute(insert)

    def show_film(self):
        conn = self.engine.connect()
        show = self.table.select()
        results = conn.execute(show)
        for x in results:
            print(f"Film: {x[1]}, Reżyser: {x[2]}, Aktorzy: {x[3]}, VOD: {x[4]}")

    def update_film(self,title, newtitle, newdir, newactors, newvod):
        conn = self.engine.connect()
        stat = self.table.update().where(self.table.c.title == title).values(title = newtitle, director = newdir, actors = newactors, vod = newvod)
        conn.execute(stat)
        s = self.table.select()
        conn.execute(s).fetchall()


t = Base('films')

t.add_film('title', 'director', 'actors', 'vod')
t.show_film()
t.update_film('tytul', 'nowy tytul', 'nowy rezyser', 'nowi aktorzy', 'nowe vod')
t.show_film()
t.delete_film('tytul')



