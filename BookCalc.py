#This calc in how much time you'll be completing the book,completed percentage,INPUTS-Book name,total pages,your avg personal best(in how much time you complete how many pages)
#Function - A= For converting time to minutes,B=Remaining pages of the book,
#Reading time Calc:(Find arithematic logic)
def Time_Converter (hours,mins) :
    h1 = 12 
    h = int(hours)
    m = int(mins)
    if h>=0 and h<h1 :
         h = h*60
         Total_mins = h+m
         return Total_mins
    else :
        h,m=input("Enter time taken to complete in 00:00 Format-").split(":")
        return Time_Converter(h,m)
    

    
def Remaining_pages (Total_no_of_pages, No_of_pages) :
     if No_of_pages<Total_no_of_pages :
          return Total_no_of_pages-No_of_pages
     else :
          Total_no_of_pages = int(input("Enter Total No. of pages-"))
          No_of_pages = int(input("pages you covered-"))
          return Remaining_pages (Total_no_of_pages, No_of_pages)
     

     
def Avg (NOP,Time_taken) :
     Avg_Time_Taken = Time_taken/NOP
    #  print (NOP,Time_taken)
     return Avg_Time_Taken


def Time_to_complete_Whole_Book_in_mins (Rp,Avg) :
     Total_Time = Rp*Avg
     return Total_Time


def Final_time (Whole_Book) :
    Final = Whole_Book/60
    return Final

def Main ():
       
    Book_name = input("Enter Book Name-")
    Total_no_of_pages = int(input("Enter Total No. of pages-"))
    print("Your Avg Personal Best")
    No_of_pages = int(input("pages you covered-"))
    a = str(No_of_pages)+" pages"
    print("Duration of completing",a) 


    h,m=input("Enter time taken to complete in 00:00 Format-").split(":")
    # print(f"{h}:{m}")
    total_mins = Time_Converter(h,m)

    micha_midhi = Remaining_pages (Total_no_of_pages, No_of_pages)
    Average = Avg (No_of_pages,total_mins)
    Time_in_mins = Time_to_complete_Whole_Book_in_mins(micha_midhi,Average)
    Expelliramus = Final_time(Time_in_mins)
    print(f"To complete {Book_name} of {Total_no_of_pages} pages will take {Expelliramus} hours")
    # print(total_mins,micha_midhi,Average,Time_in_mins)
    # print (Final_time(Time_in_mins))
#for i in range (5) :
  #      Main()
Main()


          




   
    
