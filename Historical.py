import mysql.connector

class Db:
    connection = ""

    def __init__(self):
        self.connection = mysql.connector.connect(user= 'root',password='mysql',
                                                  host='localhost',database = 'python_program')

    def save_hist(self,historical_places):
        if historical_places.id > 0:
            try:
                cursor = self.connection.cursor()
                sql = ("UPDATE `historical_places` SET `name`=%s,`famous_for`=%s,`city`=%s,`price_ind`=%s,`price_foreign`=%s,`created_at`=%s WHERE id = %s")
                cursor.execute(sql,(historical_places.name,historical_places.famous_for,historical_places.city,historical_places.price_ind,historical_places.price_foreign,historical_places.created_at,str(hist.id)))
                self.connection.commit()
            except Exception as e:
                print(e)
        else:
            try:
                cursor = self.connection.cursor()
                sql = ("INSERT INTO `historical_places`(`id`, `name`, `famous_for`, `city`, `price_ind`, `price_foreign`, `created_at`) VALUES (null,%s,%s,%s,%s,%s,%s)")
                cursor.execute(sql,(historical_places.name,historical_places.famous_for,historical_places.city,historical_places.price_ind,historical_places.price_foreign,historical_places.created_at))
                self.connection.commit()
            except Exception as e:
                print(e)

    def select_hist(self,id = 0):
        if id == 0:
            try:
                cursor = self.connection.cursor()
                sql = ("SELECT * FROM `historical_places`")
                cursor.execute(sql)
                for (id,name,famous_for,city,price_ind,price_foreign,created_at) in cursor:
                    print(id,name,famous_for,city,price_ind,price_foreign,created_at)
            except Exception as e:
                print(e)
        else:
            try:
                cursor = self.connection.cursor()
                sql = ("SELECT * FROM `historical_places` WHERE id = %s")
                cursor.execute(sql,(id),)
                for (id, name, famous_for, city, price_ind, price_foreign, created_at) in cursor:
                    print(id, name, famous_for, city, price_ind, price_foreign, created_at)
            except Exception as e:
                print(e)

class History:
    id = 0
    name = ""
    famous_for = ""
    city = ""
    price_ind = ""
    price_foreign = ""
    created_at = ""

    def __init__(self,name="",famous="",city="",ind="",fore="",created="",id=0):
        self.id = id
        self.name = name
        self.famous_for = famous
        self.city = city
        self.price_ind = ind
        self.price_foreign =fore
        self.created_at = created

Hi = History("Red fort","History","Delhi","250","1300","1550-01-01")
db = Db()
db.save_hist(Hi)
db.select_hist()