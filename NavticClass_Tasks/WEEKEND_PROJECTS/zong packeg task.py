def mobile_pakege_system():
    print("*"*15)
    print("|""zong packages""|")
    print("*"*15)
    while True:
        print("Dial: *6464#")
        print("1. Top Packages")
        print("2. All in One Packages")
        print("3. Internet Packages")
        print("4. SMS Packages")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            while True:
                print("\nTop Packages")
                print("1.200GB,2000ofRSfnet@RS1566 for30day")
                print("2.100GBoffnet@RS453 for7day")
                print("3.80GB,1000offnet@RS453 for 7 day")
                print("4.20GBsocial,@RS392 for30day")

                sub_choice = input("Select a top package (1-4): ")

                if sub_choice == '1':
                    print("\n 200GB,2000ofRSfnet@RS1566 for30day")
                    print("1.information")
                    print("subscribe ")
                    sub_choice=input("selesct option 200GB,2000ofRSfnet@RS1566 for30day(1-2")

                elif sub_choice == '1':
                    print("information")
                    print("enjoy 200GB,20,000 0n-net mins.,2000 Other operator \n Mins.,10,000SMS for 30 days@ Rs.1,800 load")
                elif sub_choice == '2':
                    print("subscribe")
                    print("your request has been submitted successfully")
                    break
                else:
                    print("Invalid option,try again ")


        elif choice == '2':
            while True:
                print("\nAll in One Packages")
                print("1. Mini")
                print("2. Weekly")
                print("3. Monthly ")
                print("4. Go back")

                sub_choice = input("Select an All in One package (1-4): ")

                if sub_choice == '1':
                    print("\nmini")
                    print("1. 1GB,1000onnet 3 days bundle@ RS.87")
                    print("2.Daily shandaar@ RS.17")
                    print("3.1GB,unlimited onnet 2 hour non-stop@ RS.14")
                    mini_choice = input("Select an option (1-3): ")
                    if mini_choice == '1':
                        print("You have selected 1GB,1000onnet 3 days bundle@ RS.8 ")
                    elif mini_choice == '2':
                        print("You have selectedDaily shandaar@ RS.17 ")
                    elif mini_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '2':
                    print("\nWeekly ")
                    print("1. 500MB + 50 mins + 200 SMS for $5")
                    print("2. 1GB + 100 mins + 500 SMS for $10")
                    print("3. Go back")
                    weekly_all_choice = input("Select an option (1-3): ")
                    if weekly_all_choice == '1':
                        print("You have selected 500MB + 50 mins + 200 SMS for $5")
                    elif weekly_all_choice == '2':
                        print("You have selected 1GB + 100 mins + 500 SMS for $10")
                    elif weekly_all_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '3':
                    print("\nMonthly")
                    print("1. 2GB + 200 mins + 1000 SMS for $15")
                    print("2. 5GB + 500 mins + 2000 SMS for $30")
                    print("3. Go back")
                    monthly_all_choice = input("Select an option (1-3): ")
                    if monthly_all_choice == '1':
                        print("You have selected 2GB + 200 mins + 1000 SMS for $15")
                    elif monthly_all_choice == '2':
                        print("You have selected 5GB + 500 mins + 2000 SMS for $30")
                    elif monthly_all_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid option, please try again")

        elif choice == '3':
            while True:
                print("\nInternet Packages")
                print("1. Daily Internet")
                print("2. Weekly Internet")
                print("3. Monthly Internet")
                print("4. Go back")

                sub_choice = input("Select an internet package (1-4): ")

                if sub_choice == '1':
                    print("\nDaily Internet")
                    print("1. 100MB for $1")
                    print("2. 500MB for $3")
                    print("3. Go back")
                    daily_net_choice = input("Select an option (1-3): ")
                    if daily_net_choice == '1':
                        print("You have selected 100MB for $1")
                    elif daily_net_choice == '2':
                        print("You have selected 500MB for $3")
                    elif daily_net_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '2':
                    print("\nWeekly Internet")
                    print("1. 1GB for $5")
                    print("2. 2GB for $8")
                    print("3. Go back")
                    weekly_net_choice = input("Select an option (1-3): ")
                    if weekly_net_choice == '1':
                        print("You have selected 1GB for $5")
                    elif weekly_net_choice == '2':
                        print("You have selected 2GB for $8")
                    elif weekly_net_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '3':
                    print("\nMonthly Internet")
                    print("1. 5GB for $20")
                    print("2. 10GB for $35")
                    print("3. Go back")
                    monthly_net_choice = input("Select an option (1-3): ")
                    if monthly_net_choice == '1':
                        print("You have selected 5GB for $20")
                    elif monthly_net_choice == '2':
                        print("You have selected 10GB for $35")
                    elif monthly_net_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '4':
                    break
                else:
                    print("Invalid option, please try again")

        elif choice == '4':
            while True:
                print("\nSMS Packages")
                print("1. Daily SMS")
                print("2. Weekly SMS")
                print("3. Go back")

                sub_choice = input("Select an SMS package (1-4): ")

                if sub_choice == '1':
                    print("\nDaily SMS")
                    print("1. 100 SMS for $1")
                    print("2. 500 SMS for $3")
                    print("3. Go back")
                    daily_sms_choice = input("Select an option (1-3): ")
                    if daily_sms_choice == '1':
                        print("You have selected 100 SMS for $1")
                    elif daily_sms_choice == '2':
                        print("You have selected 500 SMS for $3")
                    elif daily_sms_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '2':
                    print("\nWeekly SMS")
                    print("1. 700 SMS for $5")
                    print("2. 1500 SMS for $8")
                    print("3. Go back")
                    weekly_sms_choice = input("Select an option (1-3):")
                    if weekly_sms_choice == '1':
                        print("You have selected 700 SMS for $5")
                    elif weekly_sms_choice == '2':
                        print("You have selected 1500 SMS for $8")
                    elif weekly_sms_choice == '3':
                        break
                    else:
                        print("Invalid option, please try again")
                elif sub_choice == '3':
                  break
                else:
                    print("Invalid option, please try again")
mobile_pakege_system()