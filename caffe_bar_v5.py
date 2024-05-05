def Output(d):
    for i in d:
        if i == 'name':
            name = d[i].upper()
        if i == 'sellPrice':
            sell = 'selling price: ' + str(d[i])
        if i == 'purchPrice':
            purch = 'purchase price: ' + str(d[i])
        if i == 'stock':
            stock = 'stock: ' + str(d[i])
        if i == 'minStock':
            minStock = 'minimal stock: ' + str(d[i])
        if i == 'less':
            if d[i] == True:
                less = 'there is less stock left than wanted!'
        if i == 'sales':
            sales = 'sales: ' + str(d[i])
    output = name + '\n' + sell + '\n' + purch + '\n' + stock + '\n' + minStock + '\n' + sales
    try:
        if d['less'] == True:
            output += '\n' + less
    except KeyError:
        pass
    return output

def output2Dict(output):
    D = dict()
    d = output.split('\n')
    for i in range(len(d)):
        if i == 0:
            D['name'] = str(d[i].lower())
        else:
            d1 = d[i].split(': ')
            if i == 1:
                D['sellPrice'] = float(d1[1])
            elif i == 2:
                D['purchPrice'] = float(d1[1])
            elif i == 3:
                D['stock'] = int(d1[1])
            elif i == 4:
                D['minStock'] = int(d1[1])
            elif i == 5:
                D['sales'] = int(d1[1])
            else:
                if D['stock'] < D['minStock']:
                    D['less'] = True
    return D

try:
    file = open('drinks.txt', 'r+')
    data = file.read()
    file.close()
except FileNotFoundError:
    pass

import os
from tkinter import *
from tkinter.messagebox import *

class App(Frame):

    def __init__(self, tt):
        self.win = tt
        self.win.title('caffe bar')
        super().__init__(self.win)
        self.bn1_clicks = 0
        self.drinks_clicks = 0
        self.pack(expand = True)
        self.config(height = 1000, width = 500)
        self.Main()
        return

    def Main(self):
        self.win.title('Main menu')
        self.b1 = Button(self, text = 'drinks', command = self.Drinks)
        self.b1.place(x = 10, y = 10)
        self.b0 = Button(self, text = 'finance', command = self.Finance)
        self.b0.place(x = 100, y = 10)
        self.b4 = Button(self, text = 'exit', command = self.Exit)
        self.b4.place(x = 200, y = 10)
        return

    def Exit(self):
        try:
            self.all
            self.l2['text']
            if len(self.all) == 0 and len(self.l2['text']) == 0:
                raise NameError
        except AttributeError:
            if os.path.exists('drinks.txt'):
                save = askyesno('exit', 'would you like to save entered data?\nif you save it, the next time you run the program, the data will be the same,\nif you do not save it, you will have to enter all data again')
                if not save:
                    os.remove('drinks.txt')
            else:
                pass
        except NameError:
            try:
                os.remove('drinks.txt')
            except FileNotFoundError:
                pass
        else:
            save = askyesno('exit', 'would you like to save entered data?\nif you save it, the next time you run the program, the data will be the same,\nif you do not save it, you will have to enter all data again')
            if save:
                if os.path.exists('drinks.txt'):
                    os.remove('drinks.txt')
                    file = open('drinks.txt', 'w+')
                    file.write(self.l2['text'])
                    file.close()
                else:
                    file = open('drinks.txt', 'w+')
                    file.write(self.l2['text'])
                    file.close()
            else:
                if os.path.exists('drinks.txt'):
                    os.remove('drinks.txt')
        finally:
            self.win.destroy()

    def Drinks(self):
        self.drinks_clicks += 1
        if self.drinks_clicks == 1:
            self.b3 = Button(self, text = 'enter new drink', command = self.NewDrink)
            self.b3.place(x = 15, y = 90)
        try:
            self.l2
        except AttributeError:
            self.l2 = Label(self)
            self.l2.place(x = 10, y = 120)
        else:
            if 'expense' in self.l2['text']:
                self.l2.config(text = '')
        try:
            if len(self.all) > 0:
                self.l2.config(text = self.all)
            try:
                self.b2
                self.b5
            except AttributeError:
                self.b2 = Button(self, text = 'edit', command = self.Edit)
                self.b2.place(x = 180, y = 90)
                self.b5 = Button(self, text = 'delete', command = self.Delete)
                self.b5.place(x = 250, y = 90)
            try:
                if self.finance_clicks == 1:
                    self.b2.place(x = 180, y = 90)
                    self.b5.place(x = 250, y = 90)
                    self.finance_clicks = 0
            except AttributeError:
                pass
        except AttributeError:
            try:
                data
                self.l2.config(text = data)
                self.b2 = Button(self, text = 'edit', command = self.Edit)
                self.b2.place(x = 180, y = 90)
                self.b5 = Button(self, text = 'delete', command = self.Delete)
                self.b5.place(x = 250, y = 90)
            except NameError:
                pass
        self.all = self.l2['text']
        return

    def Finance(self):
        self.drinks_clicks = 0
        expense = 0
        income = 0
        try:
            if 'expense' not in self.l2['text'] and len(self.all) > 0:
                self.all = self.l2['text']
                for i in self.all.split('\n\n'):
                    purchPrice = float(output2Dict(i)['purchPrice'])
                    stock = int(output2Dict(i)['stock'])
                    sellPrice = float(output2Dict(i)['sellPrice'])
                    sales = int(output2Dict(i)['sales'])
                    expense += purchPrice*(stock + sales)
                    income += sellPrice*sales
            else:
                if self.finance_clicks == 1:
                    for i in self.all.split('\n\n'):
                        purchPrice = float(output2Dict(i)['purchPrice'])
                        stock = int(output2Dict(i)['stock'])
                        sellPrice = float(output2Dict(i)['sellPrice'])
                        sales = int(output2Dict(i)['sales'])
                        expense += purchPrice*(stock + sales)
                        income += sellPrice*sales
        except AttributeError:
            self.l2 = Label(self)
            self.l2.place(x = 10, y = 120)
        try:
            self.b3.place_forget()
            self.b2.place_forget()
            self.b5.place_forget()
        except AttributeError:
            pass
        finally:
            self.l2.config(text = 'expense: ' + str(expense) + ' eur\nincome: ' + str(income) + ' eur\nresult: ' + str(income - expense) + ' eur')
        self.finance_clicks = 1
        return

    def NewDrink(self):
        try:
            if self.all.count('\n\n') == 6:
                raise NameError
        except NameError:
            showinfo('message', 'unfortunately, there are already too many drinks in the menu. you cannot enter new drinks unless you delete already existing ones.')
        else:
            self.win.withdraw()
            self.top = Toplevel()
            self.top.config(height = 200, width = 350)
            self.top.title('new drink')
            self.top.wn0 = Label(self.top, text = 'all fields are mandatory!')
            self.top.wn0.place(x = 10, y = 10)
            self.top.wn1 = Label(self.top, text = 'name of drink item')
            self.top.wn1.place(x = 10, y = 30)
            self.top.en1 = Entry(self.top)
            self.top.en1.place(x = 190, y = 30)
            self.top.wn2 = Label(self.top, text = 'selling price of item')
            self.top.wn2.place(x = 10, y = 50)
            self.top.en2 = Entry(self.top)
            self.top.en2.place(x = 190, y = 50)
            self.top.wn6 = Label(self.top, text = 'eur')
            self.top.wn6.place(x = 320, y = 50)
            self.top.wn7 = Label(self.top, text = 'purchase price of item')
            self.top.wn7.place(x = 10, y = 70)
            self.top.en5 = Entry(self.top)
            self.top.en5.place(x = 190, y = 70)
            self.top.wn8 = Label(self.top, text = 'eur')
            self.top.wn8.place(x = 320, y = 70)
            self.top.wn3 = Label(self.top, text = 'stock')
            self.top.wn3.place(x = 10, y = 90)
            self.top.en3 = Entry(self.top)
            self.top.en3.place(x = 190, y = 90)
            self.top.wn4 = Label(self.top, text = 'minimal stock')
            self.top.wn4.place(x = 10, y = 110)
            self.top.en4 = Entry(self.top)
            self.top.en4.place(x = 190, y = 110)
            self.top.wn5 = Label(self.top, text = 'sales - starting value: 0')
            self.top.wn5.place(x = 10, y = 130)
            self.top.bn1 = Button(self.top, text = 'create new item', command = self.CreateNew)
            self.top.bn1.place(x = 200, y = 170)
            self.top.bn2 = Button(self.top, text = 'quit', command = self.Quit)
            self.top.bn2.place(x = 40, y = 170)
        return

    def Quit(self):
        self.top.destroy()
        self.win.deiconify()
        return

    def CreateNew(self):
        try:
            if len(self.top.en1.get()) == 0 or len(self.top.en2.get()) == 0 or len(self.top.en3.get()) == 0 or len(self.top.en4.get()) == 0 or len(self.top.en5.get()) == 0:
                raise SyntaxError
            else:
                if len(self.top.en1.get()) > 29:
                    raise TabError
                for i in self.top.en1.get():
                    if ord(i) < 65 or 90 < ord(i) < 97 or ord(i) > 122:
                        if i != ' ':
                            raise NameError
                if float(self.top.en2.get()) < 0 or float(self.top.en5.get()) < 0:
                    raise ValueError
                for j in self.top.en3.get():
                    if ord(j) < 48 or ord(j) > 57:
                        raise TypeError
                for k in self.top.en4.get():
                    if ord(k) < 48 or ord(k) > 57:
                        raise IndexError
                if float(self.top.en2.get()) < float(self.top.en5.get()):
                    raise AttributeError
        except TabError:
            showerror('error', 'name of item cannot contain more than 29 characters')
        except SyntaxError:
            showerror('error', 'if you want to create a new item, first fill in all fields and then click "create new item"\nif you want to go back to the Main menu, click on "quit"')
        except NameError:
            showerror('error', 'you can use only english alphabet letters in the name field')
        except ValueError:
            showerror('error', 'you can use only positive real numbers and decimal point in the price field')
        except TypeError:
            showerror('error', 'you can use only whole numbers in the stock field')
        except IndexError:
            showerror('error', 'you can use only whole numbers in the minimal stock field')
        except AttributeError:
            result = askyesno('message', 'entered selling price of item is less than the purchase price\nare you sure you want to continue?')
            if result:
                D = {'name': self.top.en1.get(),
                     'sellPrice': float(self.top.en2.get()),
                     'purchPrice': float(self.top.en5.get()),
                     'stock': int(self.top.en3.get()),
                     'minStock': int(self.top.en4.get()),
                     'sales': 0,
                     'less': False}
                if D['minStock'] > D['stock']:
                    D['less'] = True
                self.top.destroy()
                self.win.deiconify()
                self.bn1_clicks += 1
                if self.bn1_clicks == 1:
                    self.l2.config(text = Output(D))
                    self.b2 = Button(self, text = 'edit', command = self.Edit)
                    self.b2.place(x = 180, y = 90)
                    self.b5 = Button(self, text = 'delete', command = self.Delete)
                    self.b5.place(x = 250, y = 90)
                else:
                    self.l2.config(text = self.all + '\n\n' + Output(D))
                self.all = self.l2['text']
        else:
            D = {'name': self.top.en1.get(),
                 'sellPrice': float(self.top.en2.get()),
                 'purchPrice': float(self.top.en5.get()),
                 'stock': int(self.top.en3.get()),
                 'minStock': int(self.top.en4.get()),
                 'sales': 0,
                 'less': False}
            if D['minStock'] > D['stock']:
                D['less'] = True
            self.top.destroy()
            self.win.deiconify()
            self.bn1_clicks += 1
            if self.bn1_clicks == 1:
                try:
                    data
                    self.l2.config(text = self.all + '\n\n' + Output(D))
                except NameError:
                    self.l2.config(text = Output(D))
                    self.b2 = Button(self, text = 'edit', command = self.Edit)
                    self.b2.place(x = 180, y = 90)
                    self.b5 = Button(self, text = 'delete', command = self.Delete)
                    self.b5.place(x = 250, y = 90)
            else:
                self.l2.config(text = self.all + '\n\n' + Output(D))
            self.all = self.l2['text']
        return

    def Edit(self):
        self.win.withdraw()
        self.top = Toplevel()
        self.top.config(height = 210, width = 300)
        self.a = 0
        if self.all.count('\n\n') == 0:
            showinfo('message', 'only one item currently exists in the databases, you can only edit values for that item')
            self.wp2 = Label(self.top, text = 'editing values for item ' + self.all.split('\n')[0].split(': ')[-1])
            self.wp2.place(x = 50, y = 10)
        else:
            self.wp0 = Label(self.top, text = 'choose item which you want to edit')
            self.wp0.place(x = 20, y = 10)
            self.rbv = IntVar()
            for e in self.all.split('\n\n'):
                self.a += 1
                name = e.split('\n')[0].split(': ')[-1]
                self.r1 = Radiobutton(self.top, text = name, variable = self.rbv, value = self.a)
                self.r1.place(x = 10, y = self.a*20 + 10)
        if self.a != 0:
            self.top.config(height = self.a*20 + 210)
        self.wp1 = Label(self.top, text = 'choose which value you want to edit')
        self.wp1.place(x = 10, y = self.a*20 + 40)
        self.cbv1 = BooleanVar()
        self.cbv2 = BooleanVar()
        self.cbv3 = BooleanVar()
        self.cbv4 = BooleanVar()
        self.cbv5 = BooleanVar()
        self.cp1 = Checkbutton(self.top, text = 'selling price', variable = self.cbv1)
        self.cp1.place(x = 5, y = self.a*20 + 65)
        self.cp5 = Checkbutton(self.top, text = 'purchase price', variable = self.cbv5)
        self.cp5.place(x = 5, y = self.a*20 + 85)
        self.cp2 = Checkbutton(self.top, text = 'stock', variable = self.cbv2)
        self.cp2.place(x = 5, y = self.a*20 + 105)
        self.cp3 = Checkbutton(self.top, text = 'minimal stock', variable = self.cbv3)
        self.cp3.place(x = 5, y = self.a*20 + 125)
        self.cp4 = Checkbutton(self.top, text = 'sales', variable = self.cbv4)
        self.cp4.place(x = 5, y = self.a*20 + 145)
        self.bp1 = Button(self.top, text = 'next', command = self.Next)
        self.bp1.place(x = 200, y = self.a*20 + 180)
        self.bp2 = Button(self.top, text = 'quit', command = self.Quit)
        self.bp2.place(x = 50, y = self.a*20 + 180)
        return

    def Next(self):
        try:
            if self.all.count('\n\n') != 0:
                if self.rbv.get() == 0:
                    raise IndexError
            if self.cbv1.get() == 0 and self.cbv2.get() == 0 and self.cbv3.get() == 0 and self.cbv4.get() == 0 and self.cbv5.get() == 0:
                raise TypeError
        except IndexError:
            showerror('error', 'choose item which you want to edit')
        except TypeError:
            showerror('error', 'choose at least one field or click quit')
        else:
            self.top.config(width = 400)
            b = 0
            if self.cbv1.get():
                self.top.config(height = self.a*20 + 280 + b*20)
                self.lp1 = Label(self.top, text = 'new selling price:')
                self.lp1.place(x = 5, y = self.a*20 + 220 + b*20)
                self.ep1 = Entry(self.top)
                self.ep1.place(x = 150, y = self.a*20 + 220 + b*20)
                b += 1
            if self.cbv5.get():
                self.top.config(height = self.a*20 + 280 + b*20)
                self.lp5 = Label(self.top, text = 'new purchase price:')
                self.lp5.place(x = 5, y = self.a*20 + 220 + b*20)
                self.ep5 = Entry(self.top)
                self.ep5.place(x = 150, y = self.a*20 + 220 + b*20)
                b += 1
            if self.cbv2.get():
                self.top.config(height = self.a*20 + 280 + b*20)
                self.lp2 = Label(self.top, text = 'how many new items arrived:')
                self.lp2.place(x = 5, y = self.a*20 + 220 + b*20)
                self.ep2 = Entry(self.top)
                self.ep2.place(x = 200, y = self.a*20 + 220 + b*20)
                b += 1
            if self.cbv3.get():
                self.top.config(height = self.a*20 + 280 + b*20)
                self.lp3 = Label(self.top, text = 'new minimal amount of item in stock:')
                self.lp3.place(x = 5, y = self.a*20 + 220 + b*20)
                self.ep3 = Entry(self.top)
                self.ep3.place(x = 250, y = self.a*20 + 220 + b*20)
                b += 1
            if self.cbv4.get():
                self.top.config(height = self.a*20 + 280 + b*20)
                self.lp4 = Label(self.top, text = 'enter amount of item sold')
                self.lp4.place(x = 5, y = self.a*20 + 220 + b*20)
                self.ep4 = Entry(self.top)
                self.ep4.place(x = 200, y = self.a*20 + 220 + b*20)
                b += 1
            self.bp2 = Button(self.top, text = 'edit', command = self.EditAndReturn)
            self.bp2.place(x = 50, y = self.a*20 + 230 + b*20)
        return

    def EditAndReturn(self):
        q = 1
        if self.all.count('\n\n') != 0:
            q = self.rbv.get()
        y = output2Dict(self.all.split('\n\n')[q-1])
        try:
            if self.cbv1.get():
                if float(self.ep1.get()) < 0:
                    raise ValueError
            if self.cbv5.get():
                if float(self.ep5.get()) < 0:
                    raise ValueError
            if self.cbv2.get():
                if len(self.ep2.get()) == 0:
                    raise NameError
                for i in self.ep2.get():
                    if ord(i) < 48 or ord(i) > 57:
                        raise NameError
            if self.cbv3.get():
                if len(self.ep3.get()) == 0:
                    raise IndexError
                for j in self.ep3.get():
                    if ord(j) < 48 or ord(j) > 57:
                        raise IndexError
            if self.cbv4.get():
                for k in self.ep4.get():
                    if ord(k) < 48 or ord(k) > 57:
                        raise SyntaxError
                if self.cbv3.get():
                    if int(self.ep4.get()) > int(y['stock']) + int(self.ep2.get()):
                        raise AttributeError
                else:
                    if int(self.ep4.get()) > int(y['stock']):
                        raise AttributeError
        except ValueError:
            showerror('error', 'you can use only positive real numbers and decimal point in the price field')
        except NameError:
            showerror('error', 'you can use only whole numbers in the stock field')
        except IndexError:
            showerror('error', 'you can use only whole numbers in the minimal stock field')
        except SyntaxError:
            showerror('error', 'you can use only whole numbers in the sold items field')
        except AttributeError:
            showerror('error', 'sales cannot be bigger than current stock\nenter sales again or edit stock')
        else:
            if self.cbv1.get():
                y['sellPrice'] = float(self.ep1.get())
            if self.cbv5.get():
                y['purchPrice'] = float(self.ep5.get())
            if self.cbv2.get():
                y['stock'] = int(y['stock']) + int(self.ep2.get())
                if y['minStock'] < y['stock']:
                    y['less'] = False
            if self.cbv3.get():
                y['minStock'] = int(self.ep3.get())
                if y['minStock'] > y['stock']:
                    y['less'] = True
                else:
                    y['less'] = False
            if self.cbv4.get():
                y['sales'] = int(y['sales']) + int(self.ep4.get())
                y['stock'] = int(y['stock']) - int(self.ep4.get())
                if y['minStock'] > y['stock']:
                    y['less'] = True
                else:
                    y['less'] = False
            x = self.all.split('\n\n')
            x[q-1] = str(Output(y))
            self.top.destroy()
            self.win.deiconify()
            self.l2.config(text = '\n\n'.join(x))
            self.all = self.l2['text']
        return

    def Delete(self):
        self.win.withdraw()
        if self.all.count('\n\n') == 0:
            showinfo('message', 'only one item currently exists in the databases, you can only delete that item')
            odg = askyesno('delete?', 'are you sure you want to delete item ' + self.all.split('\n')[0])
            if odg:
                self.l2.config(text = '')
                self.all = self.l2['text']
                self.b2.place_forget()
                self.b5.place_forget()
                self.obrisano = 1
                self.win.deiconify()
            else:
                self.win.deiconify()
        else:
            self.top = Toplevel()
            self.top.title('delete')
            self.a = 0
            self.wi1 = Label(self.top, text = 'choose item you want to delete')
            self.wi1.place(x = 10, y = 5)
            self.rbv = IntVar()
            for e in self.all.split('\n\n'):
                self.a += 1
                name = e.split('\n')[0]
                self.r1 = Radiobutton(self.top, text = name, variable = self.rbv, value = self.a)
                self.r1.place(x = 10, y = self.a*20 + 10)
            self.top.config(height = self.a*40 + 40, width = 200)
            self.bi1 = Button(self.top, text = 'delete', command = self.DeleteProceed)
            self.bi1.place(x = 10, y = self.a*20 + 40)
            self.bi2 = Button(self.top, text = 'odustani', command = self.Quit)
            self.bi2.place(x = 70, y = self.a*20 + 40)
        return

    def DeleteProceed(self):
        q = self.rbv.get()
        try:
            if q == 0:
                raise ValueError
        except ValueError:
            showerror('error', 'you have to choose one field, or click quit')
        else:
            jedan = '\n\n'.join(self.all.split('\n\n')[:q-1])
            dva = '\n\n'.join(self.all.split('\n\n')[q:])
            if q == 1:
                self.l2.config(text = dva)
            elif q == self.a:
                self.l2.config(text = jedan)
            else:
                self.l2.config(text = jedan + '\n\n' + dva)
            showinfo('message', 'item ' + self.all.split('\n\n')[q-1].split('\n')[0] + ' is deleted')
            self.all = self.l2['text']
            self.top.destroy()
            self.win.deiconify()
        return

t = Tk()
app = App(t)
t.mainloop()
