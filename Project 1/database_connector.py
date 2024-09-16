import mysql.connector
from tkinter import messagebox

class DB_connect:
    def __init__(self) :
        try:
            self.conn= mysql.connector.connect(host='localhost', user='your_user_name',       # make the suitable changes as required
                                               password='your_password', database='database name')
            self.mycursor=self.conn.cursor()
        except:
            messagebox.showerror("Couldn't connect", "Some error occured. Could not connect to the database. Try again")                         

    def register(self, ID, name, add, phn, DoB, LicNo, issue_date, expiry_date, aadhar_no, experience, duty, password):
        exp=''
        if (experience==1):
            exp= "Beginner"
        elif(experience==2):
            exp= "Intermediate"
        else:
            exp= "Advanced"


        dty=''
        if (duty==1):
            dty= "Linked"    
        else:
            dty= "Unlinked"    


        try:
            self.mycursor.execute(f'''INSERT INTO drivers VALUES ({ID}, "{name}", "{add}", {phn}, "{DoB}",
                                  {LicNo}, "{issue_date}", "{expiry_date}", {aadhar_no}, "{exp}", "{dty}", "{password}");''')
            self.conn.commit()
        except:
            messagebox.showerror("Couldn't register", "Some error occured. Could not register. Try again")

        else:
            messagebox.showinfo("Saved Successfully", "Your credentials has been saved successfully\nPlease wait while we redirect you")

        return    
    
    def get_values(self,ID):
        try:    
            self.mycursor.execute(f'''SELECT * FROM drivers WHERE ID= {ID} ;''')
            results = self.mycursor.fetchall()  # Fetch all results
            self.conn.commit()
            # print(results[0][0])   # first index is to access the row, second index is to access the
                                   # column in that particular row
            return (results)   

        except:
            messagebox.showerror('Unable to process the request',
                                 'Some error occured. Could not load the data') 
            
            return
        
    def delete_info(self, ID):
        try:
            self.mycursor.execute(f'''DELETE FROM drivers WHERE ID= {ID};''')    
            self.conn.commit()
            messagebox.showinfo("Deletion Done", "Your data has been deleted permanently")
            return

        except:
            messagebox.showerror('Unable to process the request',
                                 'Some error occured. Could not delete the data')
            return
        
    def get_info(self):
        self.mycursor.execute(f'''SELECT * FROM drivers;''')    
        print(self.mycursor.fetchall())
        self.conn.commit()

if __name__== "__main__":
    d= DB_connect()
    d.get_info()   
