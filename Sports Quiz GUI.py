import tkinter as tk
import requests
from tkinter import messagebox
score=0
url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple"
data = requests.get(url).json()
Data = {"response_code":0,"results":[{"type":"multiple","difficulty":"easy","category":"Sports","question":"Which of the following sports is not part of the triathlon?","correct_answer":"Horse-Riding","incorrect_answers":["Cycling","Swimming","Running"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"Which African American is in part responsible for integrating  Major League baseball?","correct_answer":"Jackie Robinson","incorrect_answers":["Curt Flood","Roy Campanella","Satchell Paige"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"What is the most common type of pitch thrown by pitchers in baseball?","correct_answer":"Fastball","incorrect_answers":["Slowball","Screwball","Palmball"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"Who won the 2017 Formula One World Drivers&#039; Championship?","correct_answer":"Lewis Hamilton","incorrect_answers":["Sebastian Vettel","Nico Rosberg","Max Verstappen"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"What team won the 2016 MLS Cup?","correct_answer":"Seattle Sounders","incorrect_answers":["Colorado Rapids","Toronto FC","Montreal Impact"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"How many players are there in an association football/soccer team?","correct_answer":"11","incorrect_answers":["10","9","8"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"Who won the 2016 Formula 1 World Driver&#039;s Championship?","correct_answer":"Nico Rosberg","incorrect_answers":["Lewis Hamilton","Max Verstappen","Kimi Raikkonen"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"What team did England beat to win in the 1966 World Cup final?","correct_answer":"West Germany","incorrect_answers":["Soviet Union","Portugal","Brazil"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"Which country hosted the 2022 FIFA World Cup?","correct_answer":"Qatar","incorrect_answers":["USA","Japan","Switzerland"]},{"type":"multiple","difficulty":"easy","category":"Sports","question":"This Canadian television sportscaster is known for his &quot;Hockey Night in Canada&quot; role, a commentary show during hockey games.","correct_answer":"Don Cherry","incorrect_answers":["Don McKellar","Don Taylor ","Donald Sutherland"]}]}

frame = tk.Tk()
frame.geometry("600x600")
frame.title("Sports Quiz")

Label1=tk.Label(frame,
                text="Sports Quiz",
                font=("Arial",50,"bold"),
                fg="yellow",
                bg="green",
                relief="raised",
                bd=10,
                padx=20,
                pady=20,
                width=10,
                anchor="center"
)
Label1.pack()
Label2=tk.Label(frame,
                text="Welcome!!",
                 font=("Arial",50,"bold","italic"),
                 fg="black",
                 width=10,
                 anchor="nw"
)
Label2.place(x=50,y=150)
Label3=tk.Label(frame,
                text="Enter Your UserName :",
                font=("Arial",10,"bold"),
                fg="black",
                bg="yellow",
                relief="raised",
                width=20,
                anchor="nw"
)
Label3.place(x=200,y=300)
name=tk.Entry(frame,
              width=50,
              bg="white",
)
name.place(x=450,y=300)

Label4=tk.Label(frame,
                text="Enter The Difficulty:",
                font=("Arial",10,"bold"),
                fg="black",
                bg="yellow",
                relief="raised",
                width=20,
                anchor="nw"
)
Label4.place(x=200,y=400)
difficulty=tk.Entry(frame,
                  width=50,
                  bg="white",
                  )
difficulty.place(x=450,y=400)

Label5=tk.Label(frame,
                text="Enter The Category :",
                font=("Arial",10,"bold"),
                fg="black",
                bg="yellow",
                relief="raised",
                width=20,
                anchor="nw"
)
Label5.place(x=200,y=500)
category=tk.Entry(frame,
                  width=50,
                  bg="white",
                  )
category.place(x=450,y=500)

class Newpage1:
    def __init__(self,master):
        new_page1 = tk.Toplevel(frame)
        new_page1.geometry("500x500")
        new_page1.title("page 1")
        New_Label1=tk.Label(new_page1,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
        New_Label1.pack()

        question1=(Data['results'][0]['question'])
        tk.Label(new_page1,font=("Arial",25,"bold"),text="Question 1").place(x=20,y=130)
        tk.Label(new_page1,
                 text=question1,
                 font=("Arial",25,"bold")
                 ).place(x=240,y=130)
        option1_A=(Data['results'][0]['incorrect_answers'][0])
        tk.Label(new_page1,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
        tk.Label(new_page1,
                 text=option1_A,
                 font=("Arial",25)
                 ).place(x=110,y=240)
        
        option1_B=(Data['results'][0]['incorrect_answers'][1])
        tk.Label(new_page1,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
        tk.Label(new_page1,
                 text=option1_B,
                 font=("Arial",25)
                 ).place(x=110,y=400)
        
        option1_C=(Data['results'][0]['correct_answer'])
        tk.Label(new_page1,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
        tk.Label(new_page1,
                 text=option1_C,
                 font=("Arial",25)
                 ).place(x=500,y=240)
        
        option1_D=(Data['results'][0]['incorrect_answers'][2])
        tk.Label(new_page1,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
        tk.Label(new_page1,
                 text=option1_D,
                 font=("Arial",25)
                 ).place(x=500,y=400)

        answer1=(Data['results'][0]['correct_answer'])
        tk.Label(new_page1,font=("Arial",25,"bold"),text="(Answer 1)").place(x=40,y=550)

        user_entry1 = tk.Entry(new_page1, font=("Arial",25),width=40,bg="white")
        user_entry1.place(x=400,y=550)

        def check_answer1():
            user_ans1=user_entry1.get().lower().strip()
            global score
            if user_ans1==answer1.lower():
                score=score+1
                messagebox.showinfo("result","your answer is correct")
                new_window2()
            else:
                messagebox.showinfo("result","your answer is wrong and correct ans is :Horse-Riding")
                new_window2()
        btn_submit=tk.Button(new_page1,
                                 text="SUBMIT",
                                 anchor="center",
                                 width=10,
                                 bg="blue",
                                 fg="yellow",
                                 font=("Arial",25,"bold"),
                                 command=check_answer1)
        btn_submit.place(x=500,y=600)
        btn_next1=tk.Button(new_page1,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window2
                            )
        btn_next1.place(x=750,y=600)


class Newpage2:
    def __init__(self,master):
         new_page2 = tk.Toplevel(frame)
         new_page2.geometry("500x500")
         new_page2.title("page 2")
         New_Label2=tk.Label(new_page2,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label2.pack()
         question2=(Data['results'][1]['question'])
         tk.Label(new_page2,font=("Arial",25,"bold"),text="Question 2").place(x=20,y=130)
         tk.Label(new_page2,
                  text=question2,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option2_A=(Data['results'][1]['correct_answer'])
        
         tk.Label(new_page2,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page2,
                  text=option2_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option2_B=(Data['results'][1]['incorrect_answers'][0])
         tk.Label(new_page2,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page2,
                  text=option2_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option2_C=(Data['results'][1]['incorrect_answers'][1])
         tk.Label(new_page2,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page2,
                  text=option2_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option2_D=(Data['results'][1]['incorrect_answers'][2])
         tk.Label(new_page2,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page2,
                  text=option2_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer2=(Data['results'][1]['correct_answer'])
         tk.Label(new_page2,font=("Arial",25,"bold"),text="(Answer 2)").place(x=40,y=550)

         user_entry2 = tk.Entry(new_page2, font=("Arial",25),width=40,bg="white")
         user_entry2.place(x=400,y=550)

         def check_answer2():
             user_ans2=user_entry2.get().lower().strip()
             global score
             if user_ans2==answer2.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window3()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :Jackie Robinson")
                 new_window3()
         btn_submit2=tk.Button(new_page2,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer2)
         btn_submit2.place(x=500,y=600)
         btn_next2=tk.Button(new_page2,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window3
                            )
         btn_next2.place(x=750,y=600)

class Newpage3:
    def __init__(self,master):
         new_page3 = tk.Toplevel(frame)
         new_page3.geometry("500x500")
         new_page3.title("page 3")
         New_Label3=tk.Label(new_page3,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label3.pack()
         question3=(Data['results'][2]['question'])
         tk.Label(new_page3,font=("Arial",25,"bold"),text="Question 3").place(x=20,y=130)
         tk.Label(new_page3,
                  text=question3,
                  font=("Arial",25,"bold")
                  ).place(x=240,y=130)
         option3_A=(Data['results'][2]['correct_answer'])
        
         tk.Label(new_page3,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page3,
                  text=option3_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option3_B=(Data['results'][2]['incorrect_answers'][0])
         tk.Label(new_page3,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page3,
                  text=option3_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option3_C=(Data['results'][2]['incorrect_answers'][1])
         tk.Label(new_page3,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page3,
                  text=option3_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option3_D=(Data['results'][2]['incorrect_answers'][2])
         tk.Label(new_page3,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page3,
                  text=option3_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer3=(Data['results'][2]['correct_answer'])
         tk.Label(new_page3,font=("Arial",25,"bold"),text="(Answer 3)").place(x=40,y=550)

         user_entry3 = tk.Entry(new_page3, font=("Arial",25),width=40,bg="white")
         user_entry3.place(x=400,y=550)

         def check_answer3():
             user_ans3=user_entry3.get().lower().strip()
             global score
             if user_ans3==answer3.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window4()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :Fastball")
                 new_window4()
         btn_submit3=tk.Button(new_page3,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer3)
         btn_submit3.place(x=500,y=600)
         btn_next3=tk.Button(new_page3,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window4
                            )
         btn_next3.place(x=750,y=600)


class Newpage4:
    def __init__(self,master):
         new_page4 = tk.Toplevel(frame)
         new_page4.geometry("500x500")
         new_page4.title("page 4")
         New_Label4=tk.Label(new_page4,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label4.pack()
         question4=(Data['results'][3]['question'])
         tk.Label(new_page4,font=("Arial",25,"bold"),text="Question 4").place(x=20,y=130)
         tk.Label(new_page4,
                  text=question4,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option4_A=(Data['results'][3]['correct_answer'])
        
         tk.Label(new_page4,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page4,
                  text=option4_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option4_B=(Data['results'][3]['incorrect_answers'][0])
         tk.Label(new_page4,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page4,
                  text=option4_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option4_C=(Data['results'][3]['incorrect_answers'][1])
         tk.Label(new_page4,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page4,
                  text=option4_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option4_D=(Data['results'][3]['incorrect_answers'][2])
         tk.Label(new_page4,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page4,
                  text=option4_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer4=(Data['results'][3]['correct_answer'])
         tk.Label(new_page4,font=("Arial",25,"bold"),text="(Answer 4)").place(x=40,y=550)

         user_entry4 = tk.Entry(new_page4, font=("Arial",25),width=40,bg="white")
         user_entry4.place(x=400,y=550)

         def check_answer4():
             user_ans4=user_entry4.get().lower().strip()
             global score
             if user_ans4==answer4.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window5()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :Lewis Hamilton")
                 new_window5()
         btn_submit4=tk.Button(new_page4,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer4)
         btn_submit4.place(x=500,y=600)
         btn_next4=tk.Button(new_page4,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window5
                            )
         btn_next4.place(x=750,y=600)

class Newpage5:
    def __init__(self,master):
         new_page5 = tk.Toplevel(frame)
         new_page5.geometry("500x500")
         new_page5.title("page 5")
         New_Label5=tk.Label(new_page5,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label5.pack()
         question5=(Data['results'][4]['question'])
         tk.Label(new_page5,font=("Arial",25,"bold"),text="Question 5").place(x=20,y=130)
         tk.Label(new_page5,
                  text=question5,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option5_A=(Data['results'][4]['correct_answer'])
        
         tk.Label(new_page5,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page5,
                  text=option5_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option5_B=(Data['results'][4]['incorrect_answers'][0])
         tk.Label(new_page5,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page5,
                  text=option5_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option5_C=(Data['results'][4]['incorrect_answers'][1])
         tk.Label(new_page5,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page5,
                  text=option5_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option5_D=(Data['results'][4]['incorrect_answers'][2])
         tk.Label(new_page5,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page5,
                  text=option5_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer5=(Data['results'][4]['correct_answer'])
         tk.Label(new_page5,font=("Arial",25,"bold"),text="(Answer 5)").place(x=40,y=550)

         user_entry5 = tk.Entry(new_page5, font=("Arial",25),width=40,bg="white")
         user_entry5.place(x=400,y=550)

         def check_answer5 ():
             user_ans5=user_entry5.get().lower().strip()
             global score
             if user_ans5==answer5.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window6()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :Seattle Sounders")
                 new_window6()
         btn_submit5=tk.Button(new_page5,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer5)
         btn_submit5.place(x=500,y=600)
         btn_next5=tk.Button(new_page5,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window6
                            )
         btn_next5.place(x=750,y=600)


class Newpage6:
    def __init__(self,master):
         new_page6 = tk.Toplevel(frame)
         new_page6.geometry("500x500")
         new_page6.title("page 6")
         New_Label6=tk.Label(new_page6,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label6.pack()
         question6=(Data['results'][5]['question'])
         tk.Label(new_page6,font=("Arial",25,"bold"),text="Question 6").place(x=20,y=130)
         tk.Label(new_page6,
                  text=question6,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option6_A=(Data['results'][5]['correct_answer'])
        
         tk.Label(new_page6,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page6,
                  text=option6_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option6_B=(Data['results'][5]['incorrect_answers'][0])
         tk.Label(new_page6,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page6,
                  text=option6_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option6_C=(Data['results'][5]['incorrect_answers'][1])
         tk.Label(new_page6,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page6,
                  text=option6_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option6_D=(Data['results'][5]['incorrect_answers'][2])
         tk.Label(new_page6,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page6,
                  text=option6_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer6=(Data['results'][5]['correct_answer'])
         tk.Label(new_page6,font=("Arial",25,"bold"),text="(Answer 6)").place(x=40,y=550)

         user_entry6 = tk.Entry(new_page6, font=("Arial",25),width=40,bg="white")
         user_entry6.place(x=400,y=550)

         def check_answer6 ():
             user_ans6=user_entry6.get().lower().strip()
             global score
             if user_ans6==answer6.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window7()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :11")
                 new_window7()
         btn_submit6=tk.Button(new_page6,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer6)
         btn_submit6.place(x=500,y=600)
         btn_next6=tk.Button(new_page6,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window7
                            )
         btn_next6.place(x=750,y=600)

class Newpage7:
    def __init__(self,master):
         new_page7 = tk.Toplevel(frame)
         new_page7.geometry("500x500")
         new_page7.title("page 7")
         New_Label7=tk.Label(new_page7,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label7.pack()
         question7=(Data['results'][6]['question'])
         tk.Label(new_page7,font=("Arial",25,"bold"),text="Question 7").place(x=20,y=130)
         tk.Label(new_page7,
                  text=question7,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option7_A=(Data['results'][6]['correct_answer'])
        
         tk.Label(new_page7,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page7,
                  text=option7_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option7_B=(Data['results'][6]['incorrect_answers'][0])
         tk.Label(new_page7,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page7,
                  text=option7_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option7_C=(Data['results'][6]['incorrect_answers'][1])
         tk.Label(new_page7,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page7,
                  text=option7_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option7_D=(Data['results'][6]['incorrect_answers'][2])
         tk.Label(new_page7,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page7,
                  text=option7_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer7=(Data['results'][6]['correct_answer'])
         tk.Label(new_page7,font=("Arial",25,"bold"),text="(Answer 7)").place(x=40,y=550)

         user_entry7 = tk.Entry(new_page7, font=("Arial",25),width=40,bg="white")
         user_entry7.place(x=400,y=550)

         def check_answer7 ():
             user_ans7=user_entry7.get().lower().strip()
             global score
             if user_ans7==answer7.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window8()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :Nico Rosberg")
                 new_window8()
         btn_submit7=tk.Button(new_page7,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer7)
         btn_submit7.place(x=500,y=600)
         btn_next7=tk.Button(new_page7,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window8
                            )
         btn_next7.place(x=750,y=600)

class Newpage8:
    def __init__(self,master):
         new_page8 = tk.Toplevel(frame)
         new_page8.geometry("500x500")
         new_page8.title("page 8")
         New_Label8=tk.Label(new_page8,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label8.pack()
         question8=(Data['results'][7]['question'])
         tk.Label(new_page8,font=("Arial",25,"bold"),text="Question 8").place(x=20,y=130)
         tk.Label(new_page8,
                  text=question8,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option8_A=(Data['results'][7]['correct_answer'])
        
         tk.Label(new_page8,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page8,
                  text=option8_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option8_B=(Data['results'][7]['incorrect_answers'][0])
         tk.Label(new_page8,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page8,
                  text=option8_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option8_C=(Data['results'][7]['incorrect_answers'][1])
         tk.Label(new_page8,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page8,
                  text=option8_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option8_D=(Data['results'][7]['incorrect_answers'][2])
         tk.Label(new_page8,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page8,
                  text=option8_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer8=(Data['results'][7]['correct_answer'])
         tk.Label(new_page8,font=("Arial",25,"bold"),text="(Answer 8)").place(x=40,y=550)

         user_entry8 = tk.Entry(new_page8, font=("Arial",25),width=40,bg="white")
         user_entry8.place(x=400,y=550)

         def check_answer8 ():
             user_ans8=user_entry8.get().lower().strip()
             global score
             if user_ans8==answer8.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window9()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :West Germary")
                 new_window9()
         btn_submit8=tk.Button(new_page8,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer8)
         btn_submit8.place(x=500,y=600)
         btn_next8=tk.Button(new_page8,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window9
                            )
         btn_next8.place(x=750,y=600)

class Newpage9:
    def __init__(self,master):
         new_page9 = tk.Toplevel(frame)
         new_page9.geometry("500x500")
         new_page9.title("page 9")
         New_Label9=tk.Label(new_page9,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label9.pack()
         question9=(Data['results'][8]['question'])
         tk.Label(new_page9,font=("Arial",25,"bold"),text="Question 9").place(x=20,y=130)
         tk.Label(new_page9,
                  text=question9,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option9_A=(Data['results'][8]['correct_answer'])
        
         tk.Label(new_page9,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page9,
                  text=option9_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option9_B=(Data['results'][8]['incorrect_answers'][0])
         tk.Label(new_page9,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page9,
                  text=option9_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option9_C=(Data['results'][8]['incorrect_answers'][1])
         tk.Label(new_page9,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page9,
                  text=option9_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option9_D=(Data['results'][8]['incorrect_answers'][2])
         tk.Label(new_page9,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page9,
                  text=option9_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer9=(Data['results'][8]['correct_answer'])
         tk.Label(new_page9,font=("Arial",25,"bold"),text="(Answer 9)").place(x=40,y=550)

         user_entry9 = tk.Entry(new_page9, font=("Arial",25),width=40,bg="white")
         user_entry9.place(x=400,y=550)

         def check_answer9 ():
             user_ans9=user_entry9.get().lower().strip()
             global score
             if user_ans9==answer9.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window10()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :Qatar")
                 new_window10()
         btn_submit9=tk.Button(new_page9,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer9)
         btn_submit9.place(x=500,y=600)
         btn_next9=tk.Button(new_page9,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window10
                            )
         btn_next9.place(x=750,y=600)

class Newpage10:
    def __init__(self,master):
         new_page10 = tk.Toplevel(frame)
         new_page10.geometry("500x500")
         new_page10.title("page 10")
         New_Label10=tk.Label(new_page10,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label10.pack()
         question10=(Data['results'][9]['question'])
         tk.Label(new_page10,font=("Arial",25,"bold"),text="Question 10").place(x=20,y=130)
         tk.Label(new_page10,
                  text=question10,
                  font=("Arial",20,"bold")
                  ).place(x=240,y=130)
         option10_A=(Data['results'][9]['correct_answer'])
        
         tk.Label(new_page10,font=("Arial",25,"bold"),text="(A)").place(x=40,y=240)
         tk.Label(new_page10,
                  text=option10_A,
                  font=("Arial",25)
                  ).place(x=110,y=240)
        
         option10_B=(Data['results'][9]['incorrect_answers'][0])
         tk.Label(new_page10,font=("Arial",25,"bold"),text="(B)").place(x=40,y=400)
         tk.Label(new_page10,
                  text=option10_B,
                  font=("Arial",25)
                  ).place(x=110,y=400)
        
         option10_C=(Data['results'][9]['incorrect_answers'][1])
         tk.Label(new_page10,font=("Arial",25,"bold"),text="(C)").place(x=450,y=240)
         tk.Label(new_page10,
                  text=option10_C,
                  font=("Arial",25)
                  ).place(x=500,y=240)
        
         option10_D=(Data['results'][9]['incorrect_answers'][2])
         tk.Label(new_page10,font=("Arial",25,"bold"),text="(D)").place(x=450,y=400)
         tk.Label(new_page10,
                  text=option10_D,
                  font=("Arial",25)
                  ).place(x=500,y=400)

         answer10=(Data['results'][9]['correct_answer'])
         tk.Label(new_page10,font=("Arial",25,"bold"),text="(Answer 10)").place(x=40,y=550)

         user_entry10 = tk.Entry(new_page10, font=("Arial",25),width=40,bg="white")
         user_entry10.place(x=400,y=550)

         def check_answer10 ():
             user_ans10=user_entry10.get().lower().strip()
             global score
             if user_ans10==answer10.lower():
                 score=score+1
                 messagebox.showinfo("result","your answer is correct")
                 new_window11()
             else:
                 messagebox.showinfo("result","your answer is wrong and correct ans is :Don Cherry")
                 new_window11()
         btn_submit10=tk.Button(new_page10,
                                  text="SUBMIT",
                                  anchor="center",
                                  width=10,
                                  bg="blue",
                                  fg="yellow",
                                  font=("Arial",25,"bold"),
                                  command=check_answer10)
         btn_submit10.place(x=500,y=600)
         btn_next10=tk.Button(new_page10,
                            text="NEXT",
                            anchor="center",
                            width=10,
                            bg="blue",
                            fg="yellow",
                            font=("Arial",25,"bold"),
                            command=new_window11
                            )
         btn_next10.place(x=750,y=600)

class Newpage11:
    def __init__(self,master):
         new_page11 = tk.Toplevel(frame)
         new_page11.geometry("500x500")
         new_page11.title("page 11")
         New_Label11=tk.Label(new_page11,
                            text="Sports Quiz",
                            font=("Arial",40,"bold"),
                            fg="black",
                            width=20,
                            anchor="center"
)
         New_Label11.pack()
         New_Label12=tk.Label(new_page11,
                            text="Thanks For Playing",
                            font=("Arial",65,"bold"),
                            fg="red",
                            bg="black",
                            relief="raised",
                            bd=10,
                            width=20,
                            anchor="center"
                              )
         New_Label12.pack()
         New_Label13=tk.Label(new_page11,
                              text="Great Job!!",
                              font=("Arial",60,"bold"),
                              fg="black",
                              width=20,
                              anchor="nw"
                              )
         New_Label13.place(x=60,y=300)
         btn_end=tk.Button(new_page11,
                            text="END",
                            anchor="center",
                            width=10,
                            bg="red",
                            fg="black",
                            font=("Arial",25,"bold"),
                            command=result
                            )
         btn_end.place(x=750,y=600)

def result():
    messagebox.showinfo("Quiz Completed",f"Your Final Score Is : {score}/10")


def new_window11():
    Newpage11(frame)


def new_window10():
    Newpage10(frame)


def new_window9():
    Newpage9(frame)


def new_window8():
    Newpage8(frame)


def new_window7():
    Newpage7(frame)

      
def new_window6():
    Newpage6(frame)


def new_window5():
    Newpage5(frame)


def new_window4():
    Newpage4(frame)

    
def new_window3():
    Newpage3(frame)

        
def new_window2():
     Newpage2(frame)
            
    
def new_window1():
    Newpage1(frame)
    
btn=tk.Button(frame,
              text="START",
              anchor="center",
              width=10,
              bg="red",
              fg="black",
              font=("Arial",15,"bold"),
              command=new_window1
)
btn.place(x=500,y=600)

