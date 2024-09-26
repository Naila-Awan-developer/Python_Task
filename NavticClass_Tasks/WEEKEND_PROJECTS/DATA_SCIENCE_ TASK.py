import numpy as np
import matplotlib.pyplot as mpb
from matplotlib import style
import random


#Example: "xy axis"
def xy_axis():
    x_data = np.random.random(50) * 100
    y_data = np.random.random(50) * 100

    print(x_data)
    mpb.scatter(x_data, y_data)
    mpb.show()

    x_data = np.random.random(50) * 100
    y_data = np.random.random(50) * 100

    mpb.scatter(x_data, y_data , c = "red")
    mpb.show()

    x_data = np.random.random(50) * 100
    y_data = np.random.random(50) * 100

    mpb.scatter(x_data, y_data , c = "#000")
    mpb.show()

    x_data = np.random.random(50) * 100
    y_data = np.random.random(50) * 100

    mpb.scatter(x_data, y_data , c =  "#0f0", marker = "*", s= 150, alpha=0.3)
    mpb.show()

    x_data = np.random.random(50) * 100
    y_data = np.random.random(50) * 100

    mpb.scatter(x_data, y_data , c =  "#00f", s= 150)
    mpb.show()

#Example:2 "YW"
def YW():
    years = [2006 + x for x in range(16)]
    weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
           82, 82, 83, 81, 80, 79]

    print(len(years))
    print(len(weights))

    mpb.plot(years,weights,c = "red",lw = 3, linestyle = "--") #c = blue & green
    mpb.show()

    mpb.plot(years,weights, "g--", lw = 3)#c = blue & red
    mpb.show()

    mpb.scatter(years,weights)
    mpb.show()


#Example:3 "PL"
def PL():
    x = ["C++", "C#", "Python", "Java", "Go"]
    y = [20, 50, 140, 1, 45]

    mpb.bar(x, y,color = "r",align = "edge", width = 0.5, edgecolor = "g",lw = 6)
    mpb.show()

#Example:4 "ages"
def ages():
    ages = np.random.normal(20 , 1.5 ,1000)

    print(ages)
    mpb.hist(ages)
    mpb.show()

    mpb.hist(ages,
         bins=20,
         cumulative=True)
    mpb.show()


    ages = np.random.normal(20 , 1.5 ,1000)

    print(ages)
    mpb.hist(ages)
    mpb.show()
    mpb.hist(ages,
         bins=[ages.min(), 18, 21, ages.max()])
mpb.show()



#Example:5 "languages votes"
def languages_votes():
    langs = ["Python", "C++", "java", "C#", "Go"]
    votes = [50, 24, 14, 6, 17]

    mpb.pie(votes,  labels=langs)
    mpb.show()


    langs = ["Python", "C++", "java", "C#", "Go"]
    votes = [50, 24, 14, 6, 17]
    explodes = [0.3, 0, 0, 0, 0]

    mpb.pie(votes,  labels=langs, explode=explodes)
    mpb.show()

    langs = ["Python", "C++", "java", "C#", "Go"]
    votes = [50, 24, 14, 6, 17]
    explodes = [0.3, 0, 0, 0.2, 0]

    mpb.pie(votes,  labels=langs, explode=explodes)
    mpb.show()

    langs = ["Python", "C++", "java", "C#", "Go"]
    votes = [50, 24, 14, 6, 17]
    explodes = [0.3, 0, 0, 0.2, 0]

    mpb.pie(votes,  labels=langs, explode=explodes,
        autopct = "%.2f%%", pctdistance=1.3, startangle=90)
    mpb.show()



#Example:6 "heights"
def height():
    heights = np.random.normal(172, 8, 300)

    print(heights)
    mpb.boxplot(heights)
    mpb.show()


#Example:7 "linespaceConcatenation"
def linespace_Concatenation():
    first = np.linspace(0, 10, 25)
    second = np.linspace(10, 200, 25)
    third = np.linspace(200, 210, 25 )
    fourth = np.linspace(210, 230, 25)

    data = np.concatenate((first, second, third, fourth))
    mpb.boxplot(data)
    mpb.show()


#Example:8 "income ticks"
def income_ticks():
    years = [2014, 2015, 2016, 2017,
         2018, 2019, 2020, 2021]

    income = [55, 56, 62, 61,
          72, 72, 73, 75]

    income_ticks = list(range(50, 81, 2))

    mpb.plot(years, income)
    mpb.title("Income of John (in USD)", fontsize=25)
    mpb.xlabel("year")
    mpb.ylabel("yearly income in USD")
    mpb.yticks(income_ticks, [f"${x}k" for x in income_ticks])

mpb.show()


#Example:9 "legends"
def legends():
    stock_a = [100, 102, 99, 101, 101, 100, 102]
    stock_b = [90, 95, 102, 104, 105, 103, 109]
    stock_c  = [110, 115, 100, 105, 100, 98, 95]

    mpb.plot(stock_a, label="company1")
    mpb.plot(stock_b, label="company2")
    mpb.plot(stock_c, label="company3")

    mpb.legend(loc="lower right")
    mpb.legend(loc="lower center")

mpb.show()


#Example:10 "votes people"
def votes_people():
    style.use("ggplot")
    style.use("dark_background")


    votes = [10, 2, 5, 16, 22]
    people = (["A", "B", "C", "D", "E"])

    mpb.pie(votes, labels=None)
    mpb.legend(labels=people)

mpb.show()


#Example:11
def x1x2_y1y2():
    x1, y1 = np.random.random(100), np.random.random(100)
    x2, y2 = np.arange(100), np.random.random(100)

    mpb.figure(1)
    mpb.scatter(x1, y1)

    mpb.figure(2)
    mpb.plot(x2, y2)

mpb.show()


#Example:12
def x():
    x = np.arange(100)

    fig, axs = mpb.subplots(2, 2)

    axs[0,0].plot(x, np.sin(x))
    axs[0,0].set_title("Sine Wave")

    axs[0,1].plot(x, np.cos(x))
    axs[0,1].set_title("Cosine Wave")

    axs[1,0].plot(x, np.random.random(100))
    axs[1,0].set_title("Random Function")

    axs[1,1].plot(x, np.log(x))
    axs[1,1].set_title("Log Function")
    axs[1,1].set_xlabel("TEST")

    fig.suptitle("Fur Plots")

    mpb.tight_layout()

    mpb.savefig("furlpots.png", dpi=300)
    mpb.show()


#Example:13
def ax():
    ax = mpb.axes(projection="3d")

    x = np.random.random(100)
    y = np.random.random(100)
    z = np.random.random(100)

    ax.scatter(x, y, z)
    ax.set_title("3d Plot")
    ax.set_xlabel("test")
    mpb.show()



    ax = mpb.axes(projection="3d")

    x = np.arange(0, 50, 0.1)
    y = np.sin(x)
    z = np.cos(x)
    ax.plot(x, y, z)
    ax.set_title("3d Plot")
    ax.set_xlabel("test")
    mpb.show()
    ax = mpb.axes(projection="3d")

    x = np.arange(0, 50, 0.1)
    y = np.arange(0, 50, 0.1)
    z = np.cos(x + y)

    ax.plot(x, y, z)
    ax.set_title("3d Plot")
    ax.set_xlabel("test")
    mpb.show()

    ax = mpb.axes(projection="3d")

    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)

    x, y = np.meshgrid(x, y)

    z = np.sin(x) * np.cos(y)

    ax.plot_surface(x, y, z, cmap="Spectral")
    ax.set_title("3d Plot")
    ax.set_xlabel("test")
    ax.view_init(azim=0, elev=90)
mpb.show()


#Example:14(
def  heads_tails():
    heads_tails = [0, 0]
    for _ in range(100000):
        heads_tails[random.randint(0, 1)] +=1
        mpb.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
        mpb.pause(0.001)
        mpb.show()

print("*"*27)
print("|"" DIFFERENT type of GRAPHS""|")
print("*"*27)

while True:
    print(" 1.xy axis\n 2.YW \n 3.PL \n 4.ages\n 5.languages votes \n 6.height \n 7.linespace_Concatenation" 
           "\n 8.income ticks  \n 9.legends \n 10. votes people\n 11.x1x2_y1y2 \n 12.x \n 13.ax \n 14.heads_tails \n 15.exit_program")
    Choice=int(input("enter your choice"))
    if Choice==1:
        xy_axis()
    elif Choice==2:
         YW()
    elif Choice==3:
         PL()
    elif Choice == 4:
         ages()
    elif Choice == 3:
         languages_votes()
    elif Choice==6:
         height()
    elif Choice==7:
         linespace_Concatenation()
    elif Choice==8:
         income_ticks()
    elif Choice==9:
         legends()
    elif Choice==10:
         votes_people()
    elif Choice==11:
         x1x2_y1y2()
    elif Choice == 12:
          x()
    elif Choice == 13:
         ax()
    elif Choice == 14:
         heads_tails()
    elif Choice == 15:
         'exit_program'
    else:
        exit()

