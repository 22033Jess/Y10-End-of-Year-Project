import tkinter as tk
#Asthetics 
    #Main
bg_color = '#7DA3CA' 
fg_color = '#0D1821' 
button_bg_color = '#B4CDED' 
button_fg_color = '#0D1821'   
    #labels
custom_label_style = {'bg': button_bg_color, 'fg': fg_color, 'font': ('Georgia', 24, 'normal'), 'pady': 20}
    #buttons
custom_button_style = {'bg': button_bg_color, 'fg': button_fg_color, 'font': ('Georgia', 24, 'normal')}

#Question Windows
def open_new_window():
  global new_window

  # Close the main window
  root.withdraw()
  # Open a new window
  new_window = tk.Toplevel(root)
  new_window.title("Question 1")
  new_window.overrideredirect(True)
  new_window.configure(bg=bg_color)  # Set background color

  # Question
  question_label = tk.Label(new_window, text="Which Pattern Comes Next?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
  question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

  # Image Question
  image_path = "Images/Question1.png"
  question_image = tk.PhotoImage(file=image_path)
  image_label = tk.Label(new_window, image=question_image, **custom_label_style)
  image_label.grid(row=1, column=0, columnspan=5, pady=20)

  # Option Images
  option_images = []
  for i in range(1, 5):
      image_path = f"Images/Q1Option{i}.png"
      option_image = tk.PhotoImage(file=image_path)
      option_images.append(option_image)
      image_label = tk.Label(new_window, image=option_image)
      image_label.grid(row=2, column=i - 1, padx=35)

  # Radio Buttons
  radio_var = tk.StringVar()
  radio_buttons = []
  for i, option in enumerate(["A", "B", "C", "D"]):
      radio_button = tk.Radiobutton(new_window, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
      radio_button.grid(row=3, column=i, padx=35)
      radio_buttons.append(radio_button)



  # Next Button
  next_button = tk.Button(new_window, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window2()), **custom_button_style)
  next_button.grid(row=4, column=4, pady=10)



  # Check Answer
  def check_answer(selected_option):
    global score
    global answer1
    if selected_option == "Option 1":
      answer1 = "A"
    elif selected_option == "Option 2":
      answer1 = "B"
    elif selected_option == "Option 3":
      answer1 = "C"
      score += 1
    elif selected_option == "Option 4":
      answer1 = "D"
  
  new_window.mainloop()
def open_new_window2():
  global new_window2
  # Close the main window
  new_window.withdraw()
  # Open a new window
  new_window2 = tk.Toplevel(root)
  new_window2.title("Question 2")
  new_window2.overrideredirect(True)
  new_window2.configure(bg=bg_color)  # Set background color

  # Question
  question_label = tk.Label(new_window2, text="Which Pattern Comes Next?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
  question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

  # Image Question
  image_path = "Images/Question2.png"
  question_image = tk.PhotoImage(file=image_path)
  image_label = tk.Label(new_window2, image=question_image, **custom_label_style)
  image_label.grid(row=1, column=0, columnspan=5, pady=20)

  # Option Images
  option_images = []
  for i in range(1, 5):
      image_path = f"Images/Q2Option{i}.png"
      option_image = tk.PhotoImage(file=image_path)
      option_images.append(option_image)
      image_label = tk.Label(new_window2, image=option_image)
      image_label.grid(row=2, column=i - 1, padx=35)

  # Radio Buttons
  radio_var = tk.StringVar()
  radio_buttons = []
  for i, option in enumerate(["A", "B", "C", "D"]):
      radio_button = tk.Radiobutton(new_window2, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
      radio_button.grid(row=3, column=i, padx=35)
      radio_buttons.append(radio_button)



  # Next Button
  next_button = tk.Button(new_window2, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window3()), **custom_button_style)
  next_button.grid(row=4, column=4, pady=10)



  # Check Answer
  def check_answer(selected_option):
    global score
    global answer2
    if selected_option == "Option 1":
      answer2 = "A"
      score += 1
    elif selected_option == "Option 2":
      answer2 = "B"
    elif selected_option == "Option 3":
      answer2 = "C"
    elif selected_option == "Option 4":
      answer2 = "D"

  new_window2.mainloop()
def open_new_window3():
  global new_window3
  # Close the main window
  new_window2.withdraw()
  # Open a new window
  new_window3 = tk.Toplevel(root)
  new_window3.title("Question 3")
  new_window3.overrideredirect(True)
  new_window3.configure(bg=bg_color)  # Set background color

  # Question
  question_label = tk.Label(new_window3, text="Which Pattern Fits In The Gap?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
  question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

  # Image Question
  image_path = "Images/Question3.png"
  question_image = tk.PhotoImage(file=image_path)
  image_label = tk.Label(new_window3, image=question_image, **custom_label_style)
  image_label.grid(row=1, column=0, columnspan=5, pady=20)

  # Option Images
  option_images = []
  for i in range(1, 5):
      image_path = f"Images/Q3Option{i}.png"
      option_image = tk.PhotoImage(file=image_path)
      option_images.append(option_image)
      image_label = tk.Label(new_window3, image=option_image)
      image_label.grid(row=2, column=i - 1, padx=35)

  # Radio Buttons
  radio_var = tk.StringVar()
  radio_buttons = []
  for i, option in enumerate(["A", "B", "C", "D"]):
      radio_button = tk.Radiobutton(new_window3, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
      radio_button.grid(row=3, column=i, padx=35)
      radio_buttons.append(radio_button)



  # Next Button
  next_button = tk.Button(new_window3, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window4()), **custom_button_style)
  next_button.grid(row=4, column=4, pady=10)



  # Check Answer
  def check_answer(selected_option):
    global score
    global answer3
    if selected_option == "Option 1":
      answer3 = "A"
    elif selected_option == "Option 2":
      answer3 = "B"
      score += 1
    elif selected_option == "Option 3":
      answer3 = "C"
    elif selected_option == "Option 4":
      answer3 = "D"
  new_window3.mainloop()
def open_new_window4():
  global new_window4
  # Close the main window
  new_window3.withdraw()
  # Open a new window
  new_window4 = tk.Toplevel(root)
  new_window4.title("Question 4")
  new_window4.overrideredirect(True)
  new_window4.configure(bg=bg_color)  # Set background color

  # Question
  question_label = tk.Label(new_window4, text=
        """Which Letter Has Something In Common 
  With This Group?""", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
  question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

  # Image Question
  image_path = "Images/Question4.png"
  question_image = tk.PhotoImage(file=image_path)
  image_label = tk.Label(new_window4, image=question_image, **custom_label_style)
  image_label.grid(row=1, column=0, columnspan=5, pady=20)

  # Option Images
  option_images = []
  for i in range(1, 5):
      image_path = f"Images/Q4Option{i}.png"
      option_image = tk.PhotoImage(file=image_path)
      option_images.append(option_image)
      image_label = tk.Label(new_window4, image=option_image)
      image_label.grid(row=2, column=i - 1, padx=35)

  # Radio Buttons
  radio_var = tk.StringVar()
  radio_buttons = []
  for i, option in enumerate(["A", "B", "C", "D"]):
      radio_button = tk.Radiobutton(new_window4, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
      radio_button.grid(row=3, column=i, padx=35)
      radio_buttons.append(radio_button)



  # Next Button
  next_button = tk.Button(new_window4, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window5()), **custom_button_style)
  next_button.grid(row=4, column=4, pady=10)



  # Check Answer
  def check_answer(selected_option):
    global score
    global answer4
    if selected_option == "Option 1":
      answer4 = "A"
    elif selected_option == "Option 2":
      answer4 = "B"
    elif selected_option == "Option 3":
      answer4 = "C"
      score += 1
    elif selected_option == "Option 4":
      answer4 = "D"

  root.mainloop()
def open_new_window5():
 global new_window5
 # Close the main window
 new_window4.withdraw()
 # Open a new window
 new_window5 = tk.Toplevel(root)
 new_window5.title("Question 5")
 new_window5.overrideredirect(True)
 new_window5.configure(bg=bg_color)  # Set background color

 # Question
 question_label = tk.Label(new_window5, text="How Many Triangles Are In The 6th Shape?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
 question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

 # Image Question
 image_path = "Images/Question5.png"
 question_image = tk.PhotoImage(file=image_path)
 image_label = tk.Label(new_window5, image=question_image, **custom_label_style)
 image_label.grid(row=1, column=0, columnspan=5, pady=20)

 # Option Images
 option_images = []
 for i in range(1, 5):
     image_path = f"Images/Q5Option{i}.png"
     option_image = tk.PhotoImage(file=image_path)
     option_images.append(option_image)
     image_label = tk.Label(new_window5, image=option_image)
     image_label.grid(row=2, column=i - 1, padx=35)

 # Radio Buttons
 radio_var = tk.StringVar()
 radio_buttons = []
 for i, option in enumerate(["A", "B", "C", "D"]):
     radio_button = tk.Radiobutton(new_window5, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
     radio_button.grid(row=3, column=i, padx=35)
     radio_buttons.append(radio_button)



 # Next Button
 next_button = tk.Button(new_window5, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window6()), **custom_button_style)
 next_button.grid(row=4, column=4, pady=10)



 # Check Answer
 def check_answer(selected_option):
   global score
   global answer5
   if selected_option == "Option 1":
     answer5 = "A"
   elif selected_option == "Option 2":
     answer5 = "B"
   elif selected_option == "Option 3":
     answer5 = "C"
     score += 1
   elif selected_option == "Option 4":
     answer5 = "D"

  
 new_window5.mainloop()
def open_new_window6():
 global new_window6
 # Close the main window
 new_window5.withdraw()
 # Open a new window
 new_window6 = tk.Toplevel(root)
 new_window6.title("Question 6")
 new_window6.overrideredirect(True)
 new_window6.configure(bg=bg_color)  # Set background color

 # Question
 question_label = tk.Label(new_window6, text="Which Pattern Fits In The Gap?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
 question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

 # Image Question
 image_path = "Images/Question6.png"
 question_image = tk.PhotoImage(file=image_path)
 image_label = tk.Label(new_window6, image=question_image, **custom_label_style)
 image_label.grid(row=1, column=0, columnspan=5, pady=20)

 # Option Images
 option_images = []
 for i in range(1, 5):
     image_path = f"Images/Q6Option{i}.png"
     option_image = tk.PhotoImage(file=image_path)
     option_images.append(option_image)
     image_label = tk.Label(new_window6, image=option_image)
     image_label.grid(row=2, column=i - 1, padx=35)

 # Radio Buttons
 radio_var = tk.StringVar()
 radio_buttons = []
 for i, option in enumerate(["A", "B", "C", "D"]):
     radio_button = tk.Radiobutton(new_window6, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
     radio_button.grid(row=3, column=i, padx=35)
     radio_buttons.append(radio_button)



 # Next Button
 next_button = tk.Button(new_window6, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window7()), **custom_button_style)
 next_button.grid(row=4, column=4, pady=10)



 # Check Answer
 def check_answer(selected_option):
   global score
   global answer6
   if selected_option == "Option 1":
     answer6 = "A"
   elif selected_option == "Option 2":
     answer6 = "B"
     score += 1
   elif selected_option == "Option 3":
     answer6 = "C"
   elif selected_option == "Option 4":
     answer6 = "D"
 new_window6.mainloop()
def open_new_window7():
 global new_window7
 # Close the main window
 new_window6.withdraw()
 # Open a new window
 new_window7 = tk.Toplevel(root)
 new_window7.title("Question 7")
 new_window7.overrideredirect(True)
 new_window7.configure(bg=bg_color)  # Set background color

 # Question
 question_label = tk.Label(new_window7, text="What Number Comes Next?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
 question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

 # Image Question
 image_path = "Images/Question7.png"
 question_image = tk.PhotoImage(file=image_path)
 image_label = tk.Label(new_window7, image=question_image, **custom_label_style)
 image_label.grid(row=1, column=0, columnspan=5, pady=20)

 # Option Images
 option_images = []
 for i in range(1, 5):
     image_path = f"Images/Q7Option{i}.png"
     option_image = tk.PhotoImage(file=image_path)
     option_images.append(option_image)
     image_label = tk.Label(new_window7, image=option_image)
     image_label.grid(row=2, column=i - 1, padx=35)

 # Radio Buttons
 radio_var = tk.StringVar()
 radio_buttons = []
 for i, option in enumerate(["A", "B", "C", "D"]):
     radio_button = tk.Radiobutton(new_window7, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
     radio_button.grid(row=3, column=i, padx=35)
     radio_buttons.append(radio_button)



 # Next Button
 next_button = tk.Button(new_window7, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window8()), **custom_button_style)
 next_button.grid(row=4, column=4, pady=10)



 # Check Answer
 def check_answer(selected_option):
   global score
   global answer7
   if selected_option == "Option 1":
     answer7 = "A"
     score += 1
   elif selected_option == "Option 2":
     answer7 = "B"
   elif selected_option == "Option 3":
     answer7 = "C"
   elif selected_option == "Option 4":
     answer7 = "D"
 new_window3.mainloop()
def open_new_window8():
  global new_window8
  # Close the main window
  new_window7.withdraw()
  # Open a new window
  new_window8 = tk.Toplevel(root)
  new_window8.title("Question 8")
  new_window8.overrideredirect(True)
  new_window8.configure(bg=bg_color)  # Set background color

  # Question
  question_label = tk.Label(new_window8, text="What Are The Missing Letters?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
  question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

  # Image Question
  image_path = "Images/Question8.png"
  question_image = tk.PhotoImage(file=image_path)
  image_label = tk.Label(new_window8, image=question_image, **custom_label_style)
  image_label.grid(row=1, column=0, columnspan=5, pady=20)

 

  # Radio Buttons
  radio_var = tk.StringVar()
  radio_buttons = []
  for i, option in enumerate(["A", "B", "C", "D"]):
      radio_button = tk.Radiobutton(new_window8, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
      radio_button.grid(row=3, column=i, padx=35)
      radio_buttons.append(radio_button)



  # Next Button
  next_button = tk.Button(new_window8, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window9()), **custom_button_style)
  next_button.grid(row=4, column=4, pady=10)



  # Check Answer
  def check_answer(selected_option):
    global score
    global answer8
    if selected_option == "Option 1":
      answer8 = "A"
    elif selected_option == "Option 2":
      answer8 = "B"
    elif selected_option == "Option 3":
      answer8 = "C"
      score += 1
    elif selected_option == "Option 4":
      answer8 = "D"
  new_window8.mainloop()
def open_new_window9():
  global new_window9
  # Close the main window
  new_window8.withdraw()
  # Open a new window
  new_window9 = tk.Toplevel(root)
  new_window9.title("Question 9")
  new_window9.overrideredirect(True)
  new_window9.configure(bg=bg_color)  # Set background color

  # Question
  question_label = tk.Label(new_window9, text="""Which 3 Shapes Can Be Put Togeather 
  To Make A Square?""", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
  question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

  # Image Question
  image_path = "Images/Question9.png"
  question_image = tk.PhotoImage(file=image_path)
  image_label = tk.Label(new_window9, image=question_image, **custom_label_style)
  image_label.grid(row=1, column=0, columnspan=5, pady=20)

  # Option Images
  option_images = []
  for i in range(1, 4):
      image_path = f"Images/Q9Option{i}.png"
      option_image = tk.PhotoImage(file=image_path)
      option_images.append(option_image)
      image_label = tk.Label(new_window9, image=option_image)
      image_label.grid(row=2, column=i - 1, padx=35, pady= 10)

  # Radio Buttons
  radio_var = tk.StringVar()
  radio_buttons = []
  for i, option in enumerate(["A", "B", "C",]):
      radio_button = tk.Radiobutton(new_window9, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
      radio_button.grid(row=3, column=i, padx=35)
      radio_buttons.append(radio_button)



  # Next Button
  next_button = tk.Button(new_window9, text="Next", command=lambda: (check_answer(radio_var.get()), open_new_window10()), **custom_button_style)
  next_button.grid(row=4, column=4, pady=10)



  # Check Answer
  def check_answer(selected_option):
    global score
    global answer9
    if selected_option == "Option 1":
      answer9 = "A"
    elif selected_option == "Option 2":
      answer9 = "B"
      score += 1
    elif selected_option == "Option 3":
      answer9 = "C"
  
  new_window9.mainloop()
def open_new_window10():
  global new_window10
  # Close the main window
  new_window9.withdraw()
  # Open a new window
  new_window10 = tk.Toplevel(root)
  new_window10.title("Question 10")
  new_window10.overrideredirect(True)
  new_window10.configure(bg=bg_color)  # Set background color

  # Question
  question_label = tk.Label(new_window10, text="Who Is Pictured In The Photograph?", bg=button_bg_color, fg=fg_color, font=('Georgia', 24, 'normal'), pady=20)
  question_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='ew')  # Add padx, pady, and sticky

  # Image Question
  image_path = "Images/Question10.png"
  question_image = tk.PhotoImage(file=image_path)
  image_label = tk.Label(new_window10, image=question_image, **custom_label_style)
  image_label.grid(row=1, column=0, columnspan=5, pady=20)

  

  # Radio Buttons
  radio_var = tk.StringVar()
  radio_buttons = []
  for i, option in enumerate(["A", "B", "C", "D"]):
      radio_button = tk.Radiobutton(new_window10, text=option, variable=radio_var, value=f"Option {i + 1}", **custom_button_style)
      radio_button.grid(row=3, column=i, padx=35)
      radio_buttons.append(radio_button)



  # Next Button
  next_button = tk.Button(new_window10, text="Next", command=lambda: (check_answer(radio_var.get()), open_end_window()), **custom_button_style)
  next_button.grid(row=4, column=4, pady=10)



  # Check Answer
  def check_answer(selected_option):
    global score
    global answer10
    if selected_option == "Option 1":
      answer10 = "A"
      score += 1
    elif selected_option == "Option 2":
      answer10 = "B"
    elif selected_option == "Option 3":
      answer10 = "C"
    elif selected_option == "Option 4":
      answer10 = "D"
  new_window10.mainloop()

# End Window
def open_end_window():
  global end_window
# Close the main window
  new_window10.withdraw()
 # Open a new window
  end_window = tk.Toplevel(root)
  end_window.title("Finish")
  end_window.overrideredirect(True)
  end_window.geometry("800x480")
  end_window.configure(bg=bg_color)  
#Show Score
  congrats_label = tk.Label(end_window, text="Congratulations!",pady=30, font=('Georgia', 40, 'normal'), bg=bg_color, fg=fg_color)
  congrats_label.pack()
  score_label = tk.Label(end_window, text=f"You scored {score}/10" , bg=bg_color, fg= fg_color, font= ('Georgia', 24, 'normal'),pady=15)
  score_label.pack()
#see answers
  next_button = tk.Button(end_window, text="Click here to see answers to each question.", command=open_answer_window, bg=bg_color, fg=fg_color, font=('Georgia', 15, 'normal'),)
  next_button.pack()
#restart
  
def close():
  end_window.withdraw()

#Answer Window
def open_answer_window():
  global answer_window
  answer_window= tk.Toplevel(root)
  answer_window.title("Finish")
  answer_window.geometry("800x480")
  answer_window.overrideredirect(True)
  answer_window.configure(bg=bg_color)
  end_window.withdraw()
  text = tk.Label(answer_window, text = "Answers", font=('Georgia', 40, 'normal'), bg=bg_color, fg=fg_color)
  text.pack()
  question1 = tk.Label(answer_window, text= "Question 1 - The correct answer was C you put "+ answer1,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady = 5)
  question1.pack()

  question2 = tk.Label(answer_window, text= "Question 2 - The correct answer was A you put "+ answer2,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady = 5)
  question2.pack()
  
  question3 = tk.Label(answer_window, text= "Question 3 - The correct answer was B you put "+ answer3,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question3.pack()
  
  question4 = tk.Label(answer_window, text= "Question 4 - The correct answer was C you put "+ answer4,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question4.pack()

  question5 = tk.Label(answer_window, text= "Question 5 - The correct answer was C you put "+ answer5,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question5.pack()

  question6 = tk.Label(answer_window, text= "Question 6 - The correct answer was B you put "+ answer6,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question6.pack()

  question7 = tk.Label(answer_window, text= "Question 7 - The correct answer was A you put "+ answer7,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question7.pack()

  question8 = tk.Label(answer_window, text= "Question 8 - The correct answer was C you put "+ answer8,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question8.pack()

  question9 = tk.Label(answer_window, text= "Question 9 - The correct answer was B you put "+ answer9,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question9.pack()

  question10 = tk.Label(answer_window, text= "Question 10 - The correct answer was A you put "+ answer10,font=('Georgia', 15, 'normal'), bg=bg_color, fg=fg_color, pady=5)
  question10.pack()

  back = tk.Button(answer_window, text="Back", command=open_end_window, **custom_button_style)
  back.pack()
  answer_window.mainloop()

#Start Window
def open_start_window():
  global root
  global score
  score = 0

# Beginning screen
  root = tk.Tk()
  root.title("Welcome!")
  root.geometry("800x480")
  root.overrideredirect(True)
  root.configure(bg=bg_color)  # Set background color

# Text
  Greeting = tk.Label(root, text="Welcome", pady=30, font=('Georigia', 40, 'normal'), bg=bg_color, fg=fg_color)
  Greeting.pack()

  next_button = tk.Button(root, text="Click to Start", command=open_new_window, **custom_button_style)
  next_button.pack()

  root.mainloop()

open_start_window()
