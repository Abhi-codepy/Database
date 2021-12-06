import mysql.connector

class History:

    def __init__(self,name="",price_ind="",price_foreign=""):
        self.name = name
        self.price_ind= price_ind
        self.price_foreign = price_foreign

    def __repr__(self):
        return str(self.name).center(20) + "|"+ str(self.price_ind).center(12) + "|"+ str(self.price_foreign).center(13)

class Ticket:

    def __init__(self,id="",customer_name="",mobile_no="",hid="",origin="",person_count="",Total="",date=""):
        self.id =id
        self.customer_name=customer_name
        self.mobile_no = mobile_no
        self.hid = hid
        self.person_count = person_count
        self.origin = origin
        self.date= date
        self.Total = Total

    def __repr__(self):
        data = ""
        data += "|" + str(self.id).center(10) + "|" + str(self.customer_name).center(20) + "|" + str(self.mobile_no).center(10) +"|"+str(self.hid).center(10)+ "|" + str(self.person_count).center(12) + "|" + str(self.origin).center(10) + "|"+  str(self.Total).center(10)+ "|"+ str(self.date).center(20) + "|"
        return data

class Db:
    connection = ""
    def __init__(self):
        self.tlist = []
        self.connection = mysql.connector.connect(user = 'root',password = 'mysql',
                                                  host='localhost',database = 'python_program')

    def select_all(self):
        try:
            cursor = self.connection.cursor()
            sql = ("SELECT t.id AS tid,t.customer_name,t.mobile_no,hi.name,hi.price_ind,hi.price_foreign,t.Origin,t.person_count,t.Total,t.date FROM ticket AS t INNER JOIN historical_places AS hi ON t.hid = hi.id")
            cursor.execute(sql)
            print("----------------------------E-TICKET---------------------------------")
            print("|"+"Ticket_id".center(10)+"|"+"Customer_name".center(20)+"|"+"Mobile_no".center(10)+"|"+"Place_name".center(20)+"|"+"Indian_price".center(10)+"|"+"Foreign_price".center(10)+"|"+"Person_count".center(10)+"|"+"Origin".center(10)+"|"+"Total".center(10)+"|"+"Date".center(20)+"|")
            print("*"*148)
            for (tid,customer_name,mobile_no,name,price_ind,price_foreign,Origin,person_count,Total,date) in cursor:
                hi = History(name,price_ind,price_foreign)
                if Origin == "Indian":
                    Ti = Ticket(tid,customer_name,mobile_no,hi,Origin,person_count,int(person_count)*int(price_ind),date)
                else:
                    Ti = Ticket(tid, customer_name, mobile_no,hi,Origin,person_count,int(person_count) * int(price_foreign),date)
                self.tlist.append(Ti)
            for ans in self.tlist:
                print(ans)
        except Exception as e:
            print(e)

db = Db()
tl = db.select_all()
print(tl)