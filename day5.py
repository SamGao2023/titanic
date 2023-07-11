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
fo.write("      <a rel='link' href='index.html'><img src='SUS (1).png' class='logo'></a>\n")
fo.write("      <ul>\n")
fo.write("        <li><a href='https://en.wikipedia.org/wiki/Titanic' target='_blank'>About Titanic</a></li>\n")
fo.write("        <li><a href='Space.html'>About Me</a></li>\n")
fo.write("        <li><a href='titanic.csv'>Download Original Data</a></li>\n")
fo.write("      </ul>\n")
fo.write("    </div>\n")
fo.write("  </div>\n")
fo.write("  <h1>Women and Children first?</h1>\n")
fo.write("  <div class='image-container'>\n")
fo.write("    <img src='RMS_Titanic_3.jpg' alt='RMS Titanic'>\n")
fo.write("  </div>\n")
fo.write("  <p>This is the result of our Titanic analysis.</p>\n")
fo.write("  <svg width='800' height='500'>\n")
fo.write("    <g class='rectangle-group'>\n")
fo.write("      <rect x='0' y='25' width='740' height='100' fill='#ff0303'></rect>\n")
fo.write("      <text x='360' y='75' fill='white'>Women</text>\n")
fo.write("      <text class='percentage-text' x='360' y='105'>{}</text>\n".format(round(getGrp(data, 'female'), 1)))
fo.write("    </g>\n")
fo.write("    <g class='rectangle-group'>\n")
fo.write("      <rect x='0' y='150' width='590' height='100' fill='green'></rect>\n")
fo.write("      <text x='265' y='200' fill='white'>Children</text>\n")
fo.write("      <text class='percentage-text' x='265' y='230'>{}</text>\n".format(round(getKidz(data), 1)))
fo.write("    </g>\n")
fo.write("    <g class='rectangle-group'>\n")
fo.write("      <rect x='0' y='275' width='190' height='100' fill='blue'></rect>\n")
fo.write("      <text x='75' y='325' fill='white'>Men</text>\n")
fo.write("      <text class='percentage-text' x='65' y='355'>{}</text>\n".format(round(getGrp(data, 'male'), 1)))
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
