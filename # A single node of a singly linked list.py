class Node: #کلاس نود یک لینکد لیست
  def __init__(self, data = None, next=None): #تابع ایجاد کلاس
    self.data = data #داده های نود
    self.next = next #نود بعدی
class LinkedList: #کلاس لینکد لیست
  def __init__(self):  
    self.head = None #اولین نود
  def insert(self, data): #تابع ایجاد نود
    newNode = Node(data) #ایجاد نود جدید
    if(self.head): #اگر اولین نود نبود
      current = self.head #نود جاری اولین نود
      while(current.next): #اگر نود بعدی وجود داشت
        current = current.next #نود جاری بعدی
      current.next = newNode #نود بعدی نود جاری نود جدید
    else: #اگر اولین نود بود
      self.head = newNode #اولین نود نود جدید
  def printLL(self): #تابع چاپ لینکد لیست
    current = self.head #نود جاری اولین نود
    while(current): #اگر نود جاری وجود داشت
      print(current.data) #چاپ داده های نود جاری
      current = current.next #نود جاری بعدی
def open_file(): # تابعی که فایل را باز میکند
    file = open("text.txt", "r") # باز کردن فایل
    read = file.readlines() # خواندن فایل
    maze1 = [] # ایجاد یک لیست برای ذخیره مسیر
    for line in read:
      #کوچک کردن حروف
      line=line.lower()
      if line[-1] == "\n": # حذف کردن \n از انتهای هر خط
          line = line[:-1]
      #جدا کردن هر کلمه 
      line = line.split(" "or"-"or"_"or"="or"("or")"or"["or"]"or"{"or"}"or"|"or"\""or"'"or"#"or"@"or"!"or"?"or"%"or"^"or"&"or"*"or"~"or"`"or","or"."or";"or":"or"/")
      if line[-1] == "":
          line = line[:-1]
      maze1.append(line) # اضافه کردن مسیر به لیست
    return maze1 # برگرداندن مسیر
text=open_file() # اجرای تابع
LL = LinkedList() #ایجاد لینکد لیست
def A_Z(): #تابع ایجاد لینکد لیست حروف الفبا
  A=["A"]
  B=["B"]
  C=["C"]
  D=["D"]
  E=["E"]
  F=["F"]
  G=["G"]
  H=["H"]
  I=["I"]
  J=["J"]
  K=["K"]
  L=["L"]
  M=["M"]
  N=["N"]
  O=["O"]
  P=["P"]
  Q=["Q"]
  R=["R"]
  S=["S"]
  T=["T"]
  U=["U"]
  V=["V"]
  W=["W"]
  X=["X"]
  Y=["Y"]
  Z=["Z"]
  LL.insert(A)
  LL.insert(B)
  LL.insert(C)
  LL.insert(D)
  LL.insert(E)
  LL.insert(F)
  LL.insert(G)
  LL.insert(H)
  LL.insert(I)
  LL.insert(J)
  LL.insert(K)
  LL.insert(L)
  LL.insert(M)
  LL.insert(N)
  LL.insert(O)
  LL.insert(P)
  LL.insert(Q)
  LL.insert(R)
  LL.insert(S)
  LL.insert(T)
  LL.insert(U)
  LL.insert(V)
  LL.insert(W)
  LL.insert(X)
  LL.insert(Y)
  LL.insert(Z)
A_Z()#اجرای تابع
#اضافه کردن داده به لیست A

for i in text:
  for j in i:
    if j[0]=="a":
      
      LL.head.data.append(j)
#اضافه کردن داده به لیست B
for i in text:
  for j in i:
    if j[0]=="b":
      LL.head.next.data.append(j)
#اضافه کردن داده به لیست C
for i in text:
  for j in i:
    if j[0]=="c":
      LL.head.next.next.data.append(j)
#اضافه کردن داده به لیست D
for i in text:
  for j in i:
    if j[0]=="d":
      LL.head.next.next.next.data.append(j)
#اضافه کردن داده به لیست E
for i in text:
  for j in i:
    if j[0]=="e":
      LL.head.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست F
for i in text:
  for j in i:
    if j[0]=="f":
      LL.head.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست G
for i in text:
  for j in i:
    if j[0]=="g":
      LL.head.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست H
for i in text:
  for j in i:
    if j[0]=="h":
      LL.head.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست I
for i in text:
  for j in i:
    if j[0]=="i":
      LL.head.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست J
for i in text:
  for j in i:
    if j[0]=="j":
      LL.head.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست K
for i in text:
  for j in i:
    if j[0]=="k":
      LL.head.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست L
for i in text:
  for j in i:
    if j[0]=="l":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست M
for i in text:
  for j in i:
    if j[0]=="m":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست N
for i in text:
  for j in i:
    if j[0]=="n":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست O
for i in text:
  for j in i:
    if j[0]=="o":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست P
for i in text:
  for j in i:
    if j[0]=="p":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست Q
for i in text:
  for j in i:
    if j[0]=="q":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست R
for i in text:
  for j in i:
    if j[0]=="r":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست S
for i in text:
  for j in i:
    if j[0]=="s":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست T
for i in text:
  for j in i:
    if j[0]=="t":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست U
for i in text:
  for j in i:
    if j[0]=="u":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست V
for i in text:
  for j in i:
    if j[0]=="v":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست W
for i in text:
  for j in i:
    if j[0]=="w":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست X
for i in text:
  for j in i:
    if j[0]=="x":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست Y
for i in text:
  for j in i:
    if j[0]=="y":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)
#اضافه کردن داده به لیست Z
for i in text:
  for j in i:
    if j[0]=="z":
      LL.head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.data.append(j)

LL.printLL()