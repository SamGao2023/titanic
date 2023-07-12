# Function definitions and data processing
def getKidz(data):
    # Calculate the percentage of children who survived based on the data
    numkids = 0
    numsurv = 0
    for p in data:
        temp = p.split(',')
        if temp[6] != '':
            if float(temp[6]) < 16.0:
                numkids += 1
                if temp[1] == '1':
                    numsurv += 1
    return (numsurv / numkids) * 100

def getGrp(data, sex):
     # Calculate the percentage of survivors based on the data and sex
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(',')
        if temp[5] == sex:
            numgrp += 1
            if temp[1] == '1':
                numsurv += 1
    return (numsurv / numgrp) * 100

# Read data from the file
file = open('titanic.csv', 'r')
cols = file.readline()
data = file.readlines()
file.close()

k=getKidz(data)
w=getGrp(data,"female")
m=getGrp(data,"male")

# Open the results.html file for writing
fo = open('results.html', 'w')

# Write the HTML content with comments
fo.write("<html>\n")
fo.write("<head>\n")
fo.write("  <title>Women and Children first?</title>\n")
fo.write("  <link rel='stylesheet' href='result.css'>\n")
fo.write("</head>\n")
fo.write("<body>\n")
fo.write("  <div class='background'></div>\n")
fo.write("  <div class='banner'>\n")
fo.write("    <div class='navbar'>\n")
fo.write("      <a rel='link' href='index.html'><img src='SUS (1).png' class='logo' alt='home'></a>\n")
fo.write("      <ul>\n")
fo.write("        <li><a href='https://en.wikipedia.org/wiki/Titanic' target='_blank'>About Titanic</a></li>\n")
fo.write("        <li><a href='me.html'>About Me</a></li>\n")
fo.write("        <li><a href='https://github.com/SamGao2023/titanic/blob/main/write.py/' download target='_blank'>Download Source Code</a></li>\n")
fo.write("      </ul>\n")
fo.write("    </div>\n")
fo.write("  </div>\n")
fo.write("  <h1>Women and Children first?</h1>\n")
fo.write("  <div class='image-container'>\n")
fo.write("    <a href='https://en.wikipedia.org/wiki/Titanic' target='_blank'><img src='RMS_Titanic_3.jpg' alt='RMS Titanic'></a>\n")
fo.write("  </div>\n")
fo.write("  <p>This is the result of our Titanic analysis.</p>\n")
fo.write("  <svg width='1100' height='500'>\n")
fo.write("    <g class='rectangle-group'>\n")
fo.write("      <rect x='200' y='25' width='" + str(w * 10) + "' height='100' fill='#13293D' rx='15'></rect>\n")
fo.write("      <text x='560' y='75' fill='white'>Women</text>\n")
fo.write("      <text class='percentage-text' x='560' y='105'>74.2%</text>\n")
fo.write("    </g>\n")
fo.write("    <g class='rectangle-group'>\n")
fo.write("      <rect x='200' y='150' width='" + str(k * 10) + "' height='100' fill='#006494' rx='15'></rect>\n")
fo.write("      <text x='465' y='200' fill='white'>Children</text>\n")
fo.write("      <text class='percentage-text' x='465' y='230'>59.0%</text>\n")
fo.write("    </g>\n")
fo.write("    <g class='rectangle-group'>\n")
fo.write("      <rect x='200' y='275' width='" + str(m * 10) + "' height='100' fill='#247BA0' rx='15'></rect>\n")
fo.write("      <text x='275' y='325' fill='white'>Men</text>\n")
fo.write("      <text class='percentage-text' x='265' y='355'>18.9%</text>\n")
fo.write("    </g>\n")
fo.write("  </svg>\n")
fo.write("  <script src='result.js'></script>\n")
fo.write("</body>\n")
fo.write("</html>\n")
fo.close()


# Interactive section
keepgoing = True
while keepgoing:
    key = input("w for female, k for kids, m for men, q for quit")
    if key == 'q':
        keepgoing = False
        print('bye')
    elif key == 'w':
        result = getGrp(data, 'female')
        print(round(result, 1))
    elif key == 'm':
        result = getGrp(data, 'male')
        print(round(result, 1))
    elif key == 'k':
        result = getKidz(data)
        print(round(result, 1))
    else:
        print('umm follow instructions please')
