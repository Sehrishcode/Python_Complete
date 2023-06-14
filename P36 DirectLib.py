from pathlib import Path
path1 = Path("e_commerce")
path2 = Path("ecommerce")
path3 = Path("shipping.py")
path4 = Path("P10 Logic.Opr.py")
path5 = Path("emails")
print(path5.mkdir()) 
print(path5.rmdir())


print(path1.exists())
print(path2.exists()) 
print(path3.exists())
print(path4.exists())
path = Path()
for file in path.glob("*"):
    print(file)
for file in path.glob("*.*"):
    print(file)
for file in path.glob("*e_commerce"):
    print(file)
