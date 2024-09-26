def Moon_star():
  print("                    *      ","\n")
  print("                * *","\n")
  print("             *  *  ","\n")
  print("          *  *          ","\n")
  print("         *  *          *","\n")
  print("        * *        ***   ***","\n")
  print("        * *            *","\n")
  print("         * *   ","\n")
  print("           * *","\n")
  print("             * *","\n")
  print("                * *  ","\n")
  print("                   *")

def arrow():
    print("        *                                    *","\n")
    print("        * *                                  *  *","\n")
    print("          ************************************      *","\n")
    print("          *                                            *",'\n')
    print("          ************************************      *","\n")
    print("        * *                                  *  *","\n")
    print("        *                                    *","\n")
while True:
    print("1.Moon_star \n 2.arrow \n 3.exist")
    choice=int(input("enter your choice:"))
    if choice==1:
        Moon_star()
    elif choice==2:
        arrow()
    else:
     exit()
