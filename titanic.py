def exData(blist, num_entries):
    for i in range(num_entries):
        line = blist[i]
        temp = line.split(",")
        a = " "
        if temp[1] == "1":
            a = "yes"
        elif temp[1] == "0":
            a = "no"
        print(f"Did {temp[3]} survive? {a} (Gender: {temp[5]})")

fi = open("titanic.csv", "r")
biglist = fi.readlines()
fi.close()

print(f"Total lines: {len(biglist)}")
print("First line:", biglist[0])
num = int(input("Please input the amount of data you want to see: "))
exData(biglist, num)
