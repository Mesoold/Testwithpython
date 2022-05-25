converter = True
while (converter == True):
    #หน้าหลัก ต้อนรับ และสำหรับใส่ค่าอุณหภูมิที่ต้องการ
    print("------------------------------------------------------")
    print("-------------temperature unit converter---------------")
    print("-------------MAIN MENU---------------")
    #ค่าอุณหภูมิที่ทั้งเซลเซียส,ฟาไรนไฮต์,เคลวิน,โรเมอร์ โดยใส่เพียงตัวย่อของแต่ละอุณหภูมิ จำเป็นต้องใส่ทั้งหน่วยของอุณหภูมิที่ต้องการจะะหา และค่าของอุณหภูมินั้นๆ
    print("degree Celsius : C, degree Fahrenheit : F, Kelvin : K, Réaumur : R, Exit : X")
    Tem_unit = str(input("temperature unit = "))
    Temper = float(input("temperature = "))
    print("------------------------------------------------------")
    if Tem_unit == 'C' or Tem_unit == 'c':
        f = (Temper*9/5)+32
        k = Temper+273.15
        r = Temper*0.8
        print("your degree Celsius is {:.2f}\ndegree Fahrenheit is {:.2f}\nKelvin is {:.2f}\nRéaumur is {:.2f}".format(Temper, f, k, r))
    elif Tem_unit == 'F' or Tem_unit == 'f':
        c = 5/9*(Temper-32)
        k = c+273.15
        r = c*0.8
        print("your degree Fahrenheit is {:.2f}\ndegree Celsius is {:.2f}\nKelvin is {:.2f}\nRéaumur is {:.2f}".format(Temper, c, k, r))
    elif Tem_unit == 'K' or Tem_unit == 'k':
        c = Temper-273.15
        f = (c*9/5)+32
        r = c*0.8
        print("your Kelvin is {:.2f}\ndegree Celsius is {:.2f}\ndegree Fahrenheit is {:.2f}\nRéaumur is {:.2f}".format(Temper, c, f, r))
    elif Tem_unit == 'R' or Tem_unit == 'r':
        c = Temper*1.25
        f = (c*9/5)+32
        k = c+273.15
        print("your Réaumur is {:.2f}\ndegree Celsius is {:.2f}\ndegree Fahrenheit is {:.2f}\nKelvin is {:.2f}".format(Temper, c, f, k))
    elif Tem_unit == 'x' or Tem_unit == 'X':
        converter = False
        print("EXIT ....") 
        exit(0)
    else :
        print("----------Please enter temperature unit again....---------") 
        continue


