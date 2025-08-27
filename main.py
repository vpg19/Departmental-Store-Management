import pandas as pd
import mysql.connector as mycon
import matplotlib.pyplot as pl

def main():
    conn = mycon.connect(host='localhost', user='root',
                        password='your_password', database='department', port=3306)
    cur = conn.cursor()

    while True:
        print('\n          ************DEPARMENTAL STORE MANAGEMENT SYSTEM************          ')
        print('          1. PRODUCTS        ')
        print('          2. CUSTOMER        ')
        print('          3. INVOICE         ')
        print('          4. DATA ANALYSIS   ')
        print('          5. EXIT            ')
        
        i = int(input('Enter a value: '))
        
        if i == 1:
            manage_products(conn, cur)
        elif i == 2:
            manage_customers(conn, cur)
        elif i == 3:
            manage_invoices(conn, cur)
        elif i == 4:
            data_analysis(conn)
        else:
            print('          THANK YOU            ')
            break

def manage_products(conn, cur):
    print('       PRODUCTS      ')
    print('1. View Products')
    print('2. Add Product')
    print('3. Remove Product')
    print('4. Modify Product')
    
    i1 = int(input('Enter a value: '))
    all_products = pd.read_sql('SELECT * FROM products', conn)
    
    if i1 == 1:
        pdt = pd.read_sql('SELECT * FROM products;', conn)
        print(pdt.to_string(index=False))
    elif i1 == 2:
        add_product(conn, cur, all_products)
    elif i1 == 3:
        remove_product(conn, cur, all_products)
    else:
        modify_product(conn, cur, all_products)

def add_product(conn, cur, all_products):
    a1 = input('Enter Item ID that is to be added: ')
    if a1 not in all_products['ItemID'].values:
        a2 = input('Enter Item Name: ')
        a3 = input('Enter Category: ')
        a4 = int(input('Enter Item price: '))
        a5 = int(input('Enter units available: '))
        add = 'INSERT INTO products (itemid, item_name, category, price, units_available) VALUES (%s, %s, %s, %s, %s);'
        val = (a1, a2, a3, a4, a5)
        cur.execute(add, val)
        conn.commit()
        print('Record inserted successfully!!')
    else:
        print('Item ID already exists.')

def remove_product(conn, cur, all_products):
    r1 = input('Enter ItemID that is to be removed: ')
    if r1 not in all_products['ItemID'].values:
        print('Invalid Item ID')
    else:
        rem = "DELETE FROM products WHERE itemid = (%s);"
        val = (r1,)
        cur.execute(rem, val)
        conn.commit()
        print('Record removed successfully!!')

def modify_product(conn, cur, all_products):
    it = input('Enter Item ID that is to be modified: ')
    if it not in all_products['ItemID'].values:
        print('Item ID does not exist.')
    else:
        nn = input('Enter new Item name: ')
        c = input('Enter new Category: ')
        p = int(input('Enter new price: '))
        ua = int(input('Enter new units available: '))
        up = 'UPDATE products SET item_name = (%s), category = (%s), price = (%s), units_available = (%s) WHERE itemid = (%s)'
        val = (nn, c, p, ua, it)
        cur.execute(up, val)
        conn.commit()
        print('Item updated successfully!!')

def manage_customers(conn, cur):
    print('       CUSTOMER')
    print('1. View Customers')
    print('2. Add Customer')
    print('3. Remove Customer')
    print('4. Modify Customer')
    
    i2 = int(input('Enter a number: '))
    all_customers = pd.read_sql('SELECT * FROM customer', conn)
    
    if i2 == 1:
        cus = pd.read_sql('SELECT * FROM customer;', conn)
        print(cus.to_string(index=False))
    elif i2 == 2:
        add_customer(conn, cur, all_customers)
    elif i2 == 3:
        remove_customer(conn, cur, all_customers)
    else:
        modify_customer(conn, cur, all_customers)

def add_customer(conn, cur, all_customers):
    c1 = input('Enter Customer ID that is to be added: ')
    if c1 not in all_customers['CustID'].values:
        c2 = input('Enter First Name of the customer: ')
        c3 = input('Enter Last Name of the customer: ')
        while True:
            c4 = int(input('Enter Customer Phone number: '))
            if 1000000000 <= c4 <= 9999999999:
                c5 = input('Enter Customer Email address: ')
                addcus = 'INSERT INTO customer (custid, first_name, last_name, phone, email) VALUES (%s, %s, %s, %s, %s)'
                valcus = (c1, c2, c3, c4, c5)
                cur.execute(addcus, valcus)
                conn.commit()
                print('Customer Added Successfully!!')
                break
            else:
                print('Enter a 10 digit value !!')
    else:
        print('Customer already exists.')

def remove_customer(conn, cur, all_customers):
    re = input('Enter Customer ID that is to be removed: ')
    if re not in all_customers['CustID'].values:
        print('Invalid Customer ID')
    else:
        rev = 'DELETE FROM customer WHERE custid = (%s);'
        val = (re,)
        cur.execute(rev, val)
        conn.commit()
        print('Customer removed successfully!!')

def modify_customer(conn, cur, all_customers):
    ci = input('Enter Customer ID that is to be modified: ')
    if ci not in all_customers['CustID'].values:
        print('Invalid Customer ID')
    else:
        fn = input("Enter the new First name: ")
        ln = input("Enter the new Last name: ")
        ph = int(input('Enter new Phone number: '))
        em = input('Enter new Email ID: ')
        up = 'UPDATE customer SET first_name = (%s), last_name = (%s), phone=(%s), email=(%s) WHERE custid = (%s)'
        val = (fn, ln, ph, em, ci)
        cur.execute(up, val)
        conn.commit()
        print('Customer updated successfully')

def manage_invoices(conn, cur):
    print('       INVOICE')
    print('1. View Invoice of Customer')
    print('2. Create New Invoice')
    print('3. Delete Existing Invoice ')
    
    i3 = int(input('Enter a number: '))
    all_customers = pd.read_sql('SELECT * FROM customer', conn)
    all_invoices = pd.read_sql('SELECT * FROM invoice', conn)
    
    if i3 == 1:
        view_invoice(conn, all_invoices)
    elif i3 == 2:
        create_invoice(conn, cur, all_customers, all_invoices)
    else:
        delete_invoice(conn, cur, all_invoices)

def view_invoice(conn, all_invoices):
    inv = input('Enter Invoice ID: ')
    if inv not in all_invoices['InvoiceNO'].values:
        print('Invoice does not exist')
    else:
        val = (inv,)
        inv_df = pd.read_sql('SELECT invoiceno, custid FROM invoice WHERE invoiceno = (%s)', conn, params=val)
        c = str(inv_df.iloc[0, 1])
        cus = pd.read_sql('SELECT first_name, last_name, phone, email FROM customer WHERE custid = %s;', conn, params=(c,))
        dis = pd.read_sql('SELECT ItemID, Item_Name, Price, Quantity, Amount FROM products NATURAL JOIN invoice_line_item WHERE invoiceno=%s ORDER BY itemid;', conn, params=val)
        tamt = pd.read_sql('SELECT SUM(amount) FROM invoice_line_item WHERE invoiceno =(%s)', conn, params=val)
        date = pd.read_sql('SELECT sale_date FROM invoice WHERE invoiceno = (%s)', conn, params=val)
        
        print('\n')
        print('Invoice NO.: ', inv_df.iloc[0, 0])
        print('Sale Date: ', date.iloc[0, 0])
        print('First Name: ', cus.iloc[0, 0])
        print('Last Name: ', cus.iloc[0, 1])
        print('Email: ', cus.iloc[0, 3])
        print('Phone: ', cus.iloc[0, 2])
        print(dis.to_string(index=False))
        print('Total Amount: ', tamt.iloc[0, 0])
        print('\n')

def create_invoice(conn, cur, all_customers, all_invoices):
    n = input('Enter New Invoice NO. (I00x): ')
    if n not in all_invoices['InvoiceNO'].values:
        c = input('Enter Customer ID: ')
        if c not in all_customers['CustID'].values:
            print('Invalid Customer ID')
        else:
            d1 = pd.read_sql('SELECT DATE(NOW())', conn)
            d = str(d1.iloc[0, 0])
            pm = input('Enter Payment Mode: ')
            i = int(input('Enter number of goods purchased: '))
            b = 1
            while b <= i:
                a = input('Enter Item ID Purchased: ')
                q = int(input('Enter number of units purchased: '))
                s = pd.read_sql('SELECT units_available FROM products WHERE itemid = (%s)', conn, params=(a,))
                sa = int(s.iloc[0, 0])
                if sa > q:
                    stock = 'UPDATE products SET units_available = units_available - (%s) WHERE itemid = (%s);'
                    vals = (q, a)
                    cur.execute(stock, vals)
                    am = pd.read_sql('SELECT price * (%s) FROM products WHERE itemid = (%s)', conn, params=(q, a))
                    amt = int(am.iloc[0, 0])
                    val = (n, a, q, amt)
                    ins = 'INSERT INTO invoice_line_item VALUES(%s, %s, %s, %s)'
                    cur.execute(ins, val)
                    conn.commit()
                    b += 1
                else:
                    print('Insufficient Stock')
            val2 = (n, c, d, pm)
            inv = 'INSERT INTO invoice VALUES (%s, %s, %s, %s)'
            cur.execute(inv, val2)
            conn.commit()
            print('Invoice added successfully!!')
    else:
        print('Invoice already exists')

def delete_invoice(conn, cur, all_invoices):
    r = input('Enter Invoice no That is to be removed: ')
    val = (r,)
    if r not in all_invoices['InvoiceNO'].values:
        print('Invalid Invoice')
    else:
        pq = pd.read_sql('SELECT itemid, quantity FROM invoice_line_item WHERE invoiceno =(%s)', conn, params=(r,))
        c = pd.read_sql('SELECT COUNT(itemid) FROM invoice_line_item WHERE invoiceno = (%s)', conn, params=(r,))
        cv = int(c.iloc[0, 0])
        i = 0
        while i < cv:
            pi = str(pq.iloc[i, 0])
            q = int(pq.iloc[i, 1])
            stock = 'UPDATE products SET units_available = units_available + (%s) WHERE itemid = (%s);'
            vals = (q, pi)
            cur.execute(stock, vals)
            conn.commit()
            i = i + 1
        rem = 'DELETE FROM invoice_line_item WHERE invoiceno = (%s)'
        rem2 = 'DELETE FROM invoice WHERE invoiceno = (%s)'
        cur.execute(rem, val)
        cur.execute(rem2, val)
        conn.commit()
        print('Invoice removed successfully !!')

def data_analysis(conn):
    print('     DATA ANALYSIS      ')
    print('1. Product Analysis')
    print('2. Payment Mode Analysis')
    
    i4 = int(input('Enter a number: '))
    
    if i4 == 1:
        u = pd.read_sql('SELECT DISTINCT(category), SUM(units_available) AS "Units Available" FROM products GROUP BY category', conn)
        u.plot(kind='bar', x='category')
        pl.xlabel('Category')
        pl.ylabel('Units Available')
        pl.show()
    else:
        p = pd.read_sql('SELECT DISTINCT(payment_mode), COUNT(payment_mode) AS "No. of times used" FROM invoice GROUP BY payment_mode', conn)
        p.plot(x='payment_mode', marker='o')
        pl.xlabel('Payment Mode')
        pl.ylabel('No. of times used')
        pl.show()
    
    input("Press any key to continue...")

if __name__ == "__main__":
    main()