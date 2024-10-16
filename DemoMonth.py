def main() :
    month_no = 0;

    print("Jay Ganesh.....");

    month_names = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 
                   7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

    for i in range(1,21) :
        month_no = month_no +  1;
        
        if(month_no > 12):
            month_no = 1;

        month = month_names[month_no];

        print(month);

if __name__ == "__main__" :
    main();