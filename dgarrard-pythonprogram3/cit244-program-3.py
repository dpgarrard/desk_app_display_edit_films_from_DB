
import wx
import sqlite3


class insert_dia(wx.Dialog):  #dialog window class takes wx.dialog as parent
    def __init__(self):    #class constructor
        wx.Dialog.__init__(self, None, title='Insert Data')  #parent constructor

        wx.StaticText(self, label='Enter movie information.', pos=(145,6))   #main label shows up when inserting

        self.title = wx.TextCtrl(self, id=-1, pos=(75,45),size=(100,-1)) #text entry assigned to appropriate labels
        wx.StaticText(self, id=-1, label='Title', pos=(100,30))  #Labels associated with text boxes located above text boxes

        self.rel_year = wx.TextCtrl(self, id=-1, pos=(75,85),size=(100,-1))
        wx.StaticText(self, id=-1, label='Release Year', pos=(100,70))

        self.lang = wx.TextCtrl(self, id=-1, pos=(75,125),size=(100,-1))
        wx.StaticText(self, id=-1, label='Language', pos=(100,110))

        self.rate = wx.TextCtrl(self, id=-1, pos=(240,45),size=(100,-1))
        wx.StaticText(self, id=-1, label='Rental Rate', pos=(265,30))

        self.length = wx.TextCtrl(self, id=-1, pos=(240,85),size=(100,-1))
        wx.StaticText(self, id=-1, label='Length', pos=(265,70))

        self.rating = wx.TextCtrl(self, id=-1, pos=(240,125),size=(100,-1))
        wx.StaticText(self, id=-1, label='Rating', pos=(265,110))

        wx.Button(self, id=wx.ID_OK, pos=(90,170))   #ok button @ bottom if insert box
        wx.Button(self, id=wx.ID_CANCEL, pos=(250,170))     #cancel button @ bottom of insert box

class delete_dia(wx.Dialog):  #dialog window for delete takes wx.dialog as parent
    def __init__(self): #class constructor
        wx.Dialog.__init__(self, None, title='Delete Data') #parent constructor

        wx.StaticText(self, label='Enter movie title to delete record.', pos=(100,6))

        self.title = wx.TextCtrl(self, id=-1, pos=(135,45),size=(100,-1))
        wx.StaticText(self, id=-1, label='movie title', pos=(150,30))

        wx.Button(self, id=wx.ID_OK, pos=(90, 145))  # ok button @ bottom if insert box
        wx.Button(self, id=wx.ID_CANCEL, pos=(250, 145))  # cancel button @ bottom of insert box

class table_frame(wx.Frame):  #main panel
    def __init__(self, parent, id_, title):
        wx.Frame.__init__(self, parent, id_, title=title, ) # parent, id, title, size of table size=(800,800)
        self.SetSize((675,400)) #sets frame size
        table_panel = wx.Panel(self,id_) #creates panel



                #horizontal & vertical sizer's

        h_box = wx.BoxSizer(wx.HORIZONTAL)
        v_box = wx.BoxSizer(wx.VERTICAL)

        content_label = wx.StaticText(table_panel,label= 'Film Data') #label set to content_label variable

            # setting up buttons

        display = wx.Button(table_panel, label='Display Data')  # Display button at bottom of main page
        insert = wx.Button(table_panel, label='Insert Data')  # Insert button at bottom of main page
        cancel = wx.Button(table_panel, label='Cancel')  # Cancel button at bottom of main page
        rem = wx.Button(table_panel, label='delete entry')  # remove button at bottom of main page below insert

        # bind buttons to appropriate functions
        display.Bind(wx.EVT_BUTTON, self.display_table)
        insert.Bind(wx.EVT_BUTTON, self.insert_to_table)
        cancel.Bind(wx.EVT_BUTTON, self.cancel_program)
        rem.Bind(wx.EVT_BUTTON, self.delete_record)

        #setting up table

        self.list = wx.ListCtrl(table_panel, -1, style = wx.LC_REPORT,) # pos=(70,30), size=(650,600)) # setting up table & assign to self.list,

        #setting up columns

        self.list.InsertColumn(0, 'film_id', width=60)
        self.list.InsertColumn(1, 'title', width=195)
        self.list.InsertColumn(2, 'release_year', width=80)
        self.list.InsertColumn(3, 'language', width=90)
        self.list.InsertColumn(4, 'rental_rate', width=80)
        self.list.InsertColumn(5, 'length', width=60)
        self.list.InsertColumn(6, 'rating', width=60)

                    # add widgets to specific sizer's

        v_box.Add(content_label, 0, wx.ALL | wx.ALIGN_CENTER, border=10)
        v_box.Add(self.list, 1, wx.EXPAND | wx.LEFT | wx.RIGHT, border=15)
        h_box.Add(display, 1, wx.EXPAND | wx.ALL, border=5)
        h_box.Add(insert, 1, wx.EXPAND | wx.ALL, border=5)
        h_box.Add(cancel, 1, wx.EXPAND | wx.ALL, border=5)
        h_box.Add(rem, 1, wx.EXPAND | wx.ALL, border=5)

        v_box.Add(h_box, 0, wx.EXPAND | wx.ALL, border=10) # add button row to bottom of vertical sizer '0' keeps height expand stretches across width.

        table_panel.SetSizer(v_box) #add vertical sizer to panel
        self.Centre()  # center the window when loaded up

    def show_all_data(self):  #used to display the whole table

        self.list.DeleteAllItems() #used to empty the list control
        con = sqlite3.connect('movies.db') #connect to database & assign to con variable
        cur = con.cursor() # assign database to cursor to execute SQL's & assign to cur variable

        sql = 'SELECT * FROM afilms'
        cur.execute(sql)
        data = cur.fetchall()       # grab everthing from executed SQL statement
        for row in data:        # cycle through all data and assign to row
            self.list.Append(row) # add to self.list everything that is cycled through

        cur.close()
        con.close()

    def display_table(self,event):
        try:
            self.show_all_data()

        except sqlite3.Error as error:
            dlg = wx.MessageDialog(self, str(error), 'error occured')
            dlg.ShowModal()
    
    def cancel_program(self,event):
        self.Close()   # exit program
        
    def delete_record(self,event):

        d_b = delete_dia() #call delete_dia class assign to d_b for delete box
        btn_id = d_b.ShowModal() #only allow button presses or close by x in corner, assign to btn_id

        if btn_id != wx.ID_OK: # test to see if ok button isn't pressed
            d_b.Destroy()  #closes the windows
            return

        title = d_b.title.GetValue() #get data that's inserted into text box if ok button is pressed.
        if title != '':
            con = sqlite3.connect('movies.db')  # connect to database & assign to con variable
            cur = con.cursor()  # assign database to cursor to execute SQL's & assign to cur variable
            sql_select = 'SELECT * FROM afilms WHERE title = ?'
            cur.execute(sql_select, (title,))  # enter variables into parameters in sql statement
            name = cur.fetchone() #if title in database assign to name

            if name is not None:  #if name variable has title in it delete, if not error
                sql_delete = 'DELETE FROM afilms WHERE title = ?'  # sql statement with parameterized query
                cur.execute(sql_delete,(title,))  # enter variables into parameters in sql statement
                con.commit()  # save changes
            else:
                dlg = wx.MessageDialog(self,'Title not found in database. Must be exactly as written out',caption = 'error')
                dlg.ShowModal()
                self.show_all_data()  # get all data again
        else:
            dlg = wx.MessageDialog(self,'title not found in database. Put something in the box please.',caption = 'error')
            dlg.ShowModal()
            self.show_all_data()  # get all data again


    def insert_to_table(self, event):  # used to insert data to table

        i_b = insert_dia()  #call dialog class assign i_b for insert box
        btn_id = i_b.ShowModal()  #only allow button presses or close by x in corner, assign to btn_id

                                 
        if btn_id != wx.ID_OK: # test to see if ok button isn't pressed
            i_b.Destroy()  #closes the windows
            return

        title = i_b.title.GetValue()  #get data that's inserted into TextCtrl boxes if ok button is pressed
        r_year = i_b.rel_year.GetValue()
        lang = i_b.lang.GetValue()
        rate = i_b.rate.GetValue()
        length = i_b.length.GetValue()
        rating = i_b.rating.GetValue()


            
        if title != '' and r_year != '' and lang != '' and rate != '' and length != '' and rating != '':  # check if empty values
            try:
                r_year == int(r_year)  #see if data type is correct
            except:
                dlg = wx.MessageDialog(None,'release year must be a 4 digit number.', 'error', wx.OK | wx.ICON_ERROR)  #throw this error if not correct data type
                dlg.ShowModal()
                dlg.Destroy()
                
                
            try:
                lang == int(lang)
            except:
                dlg = wx.MessageDialog(None,'language must be a number indicating the total number of languages.', 'error', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                
            try:
                rate == float(rate)
            except:
                dlg = wx.MessageDialog(None,'rent rate must include a decimal number.', 'error', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                

            try:
                length == int(length)
            except:
                dlg = wx.MessageDialog(None,'length must be a number in minutes please.', 'error', wx.OK | wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                              
                 
                           
            
        else:               #if not everything is entered into textboxes throw this error
            dlg = wx.MessageDialog(None,'all fields are required', 'error', wx.OK | wx.ICON_ERROR)
            dlg.ShowModal()
            dlg.Destroy()

            
            
        if type(r_year and lang and length) == int and type(rate) == float:
            try:
                
                con = sqlite3.connect('movies.db') #connect to database & assign to con variable
                cur = con.cursor() # assign database to cursor to execute SQL's & assign to cur variable

                sql = 'INSERT INTO afilms VALUES (?,?,?,?,?,?,?)' #sql statement with parameterized query
                cur.execute(sql, (None, title, r_year, lang, rate, length, rating)) # enter variables into parameters in sql statement
                con.commit() #save changes

                self.show_all_data() # get all data again
            except:
                dlg = wx.MessageDialog(None,'couldnt load file', 'error', wx.OK | wx.ICON_ERROR) #error statement
                dlg.ShowModal()
                i_b.Destroy()
         

        i_b.Destroy()
            
app = wx.App()  #bring wxpython into existence
tf = table_frame(None, -1, 'Movie Night')  #insatantiate parent frame
tf.Show()   #make frame visible
app.MainLoop()  #loop looking for events
