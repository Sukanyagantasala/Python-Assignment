b1_price=499.00
b2_price=855.00
b3_price=645.00
gst=0.12
delivery_charges=250.00
print("Introducing to Python Programming : Rs%.2f"%b1_price)
print("Python Libraries Cookbook : Rs%.2f"%b2_price)
print("Data Science in Python : Rs%.2f"%b3_price)
print("GST : 12%")
print("Delivery Charges : Rs%.2f"%delivery_charges)
b1=int(input("Enter no of Introducing to Python Programming books : "))
b2=int(input("Enter no of Python Libraries Cookbook books : "))
b3=int(input("Enter no of Data Science in Python books : "))
sub_total=b1*b1_price+b2*b2_price+b3*b3_price
gst_amt=sub_total*(12/100)
invoice_amt=gst_amt+sub_total+delivery_charges
print("Invoice Amount=%.2f"%invoice_amt)

