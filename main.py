import customtkinter
import pandas as pd
import os, sys
from PIL import Image

comiendoentokyo = os.path.join(os.path.dirname(os.path.realpath(__file__)), "comiendoentokyo.csv")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("english words")
        self.geometry("630x300")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "i")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "tokyot.png")), size=(45, 45))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "intro_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "intro_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "words_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "words_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "search_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "search_light.png")), size=(20, 20))
        self.edition_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "edition_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "edition_light.png")), size=(20, 20))
        self.delete_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "delete_dark.png")),
                                                dark_image=Image.open(os.path.join(image_path, "delete_light.png")), size=(20, 20))                                                

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" English Words", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(family="Helvetica",
                                                                                                         size=14, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.intro_button = customtkinter.CTkButton(self.navigation_frame, 
                                                    corner_radius=0, height=40, border_spacing=10, text="Intro",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), 
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.intro_button_event)
        self.intro_button.grid(row=1, column=0, sticky="ew")

        self.words_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                                    text="Words",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), 
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.chat_image, anchor="w", command=self.words_button_event)
        self.words_button.grid(row=2, column=0, sticky="ew")

        self.search_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                                    text="Search",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), 
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.add_user_image, anchor="w", command=self.search_button_event)
        self.search_button.grid(row=3, column=0, sticky="ew")

        self.edition_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, 
                                                    text="Edition",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), 
                                                    hover_color=("gray70", "gray30"),
                                                    image=self.edition_image, anchor="w", command=self.edition_button_event)
        self.edition_button.grid(row=4, column=0, sticky="ew")

        self.intro_frame_button_2 = customtkinter.CTkButton(self.navigation_frame, text="Exit", image=self.image_icon_image, 
                                                            compound="right", command=sys.exit)
        self.intro_frame_button_2.grid(row=5, column=0, padx=20, pady=10)

        # create Intro frame

        self.intro_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.intro_frame.grid_columnconfigure(0, weight=1)

        self.intro_frame_textbox = customtkinter.CTkTextbox(self.intro_frame, width=360, height=63)
        self.intro_frame_textbox.grid(row=2, column=0, padx=1, pady=1)
        self.intro_frame_textbox.focus_set() 
        self.intro_frame_textbox_label = customtkinter.CTkLabel(self.intro_frame, text="  Word, meaning...",
                                                              compound="left", font=customtkinter.CTkFont(family="Helvetica",
                                                                                                          size=12, weight="bold"))
        self.intro_frame_textbox_label.grid(row=1, column=0, padx=27, pady=18, sticky="w")

        self.intro_frame_button_1 = customtkinter.CTkButton(self.intro_frame, text="Save", image=self.image_icon_image, 
                                                            compound="right", command=self.on_submit)
        self.intro_frame_button_1.grid(row=3, column=0, padx=20, pady=10)

        self.save_label = customtkinter.CTkLabel(self.intro_frame, text="",
                                            padx=1, pady=1,
                                            compound="center", justify="center", 
                                            font=customtkinter.CTkFont(family="Helvetica",size=18, weight="bold"))
        self.save_label.grid(row=4, column=0, padx=1, pady=1)

        # create words frame
        self.words_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.words_textbox = customtkinter.CTkTextbox(self.words_frame, width=420, height=230,
                                            activate_scrollbars = True, scrollbar_button_color="gray75",
                                            fg_color="transparent",
                                            font=customtkinter.CTkFont(family="Helvetica", size=12, weight="bold"))
        self.words_textbox.grid(row=0, column=0, padx=1, pady=1)
        self.words_button_sort = customtkinter.CTkButton(self.words_frame, text="by Intro", width=20, height=30,
                                                            compound="left", command=self.words_refresh)
        self.words_button_sort.grid(row=2, column=0, padx=0, pady=0, sticky="ew")
        

        # create search frame
        self.search_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.search_entry = customtkinter.CTkEntry(self.search_frame,
                                            justify="left", font=customtkinter.CTkFont(family="Helvetica",
                                                                                     size=14, weight="bold"),
                                            fg_color="transparent",
                                            border_width=1,
                                            corner_radius=3,
                                            width=270)
        self.search_entry.grid(row=1, column=0, padx=81, pady=36)
        self.search_entry.bind('<Return>', self.search_word)

        self.search_frame_label = customtkinter.CTkLabel(self.search_frame, text="",
                                            compound="left", justify="left", 
                                            font=customtkinter.CTkFont(family="Helvetica", size=14, weight="normal"))
        self.search_frame_label.grid(row=0, column=0, padx=18, pady=18, sticky="ew")


        #create edition frame
        self.ed_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ed_frame.grid_rowconfigure(0, weight=1)

        self.edition_label = customtkinter.CTkLabel(self.ed_frame, text="",
                                            compound="left", justify="left", 
                                            font=customtkinter.CTkFont(family="Helvetica", size=14, weight="normal"))
        self.edition_label.grid(row=3, column=0, padx=18, pady=18, sticky="ew")
        self.deletion_label = customtkinter.CTkLabel(self.ed_frame, text="",
                                            compound="left", justify="left", 
                                            font=customtkinter.CTkFont(family="Helvetica", size=14, weight="normal"))
        self.deletion_label.grid(row=4, column=0, padx=18, pady=18, sticky="ew")
        self.ed_entry = customtkinter.CTkEntry(self.ed_frame,
                                            justify="left", font=customtkinter.CTkFont(family="Helvetica",
                                                                                     size=14, weight="bold"),
                                            fg_color="transparent",
                                            border_width=1,
                                            corner_radius=3,
                                            width=270)
        self.ed_entry.grid(row=1, column=0, padx=81, pady=18)

        self.info_label = customtkinter.CTkLabel(self.ed_frame, text=
                    "Until the moment the edition just refers to the delete words option,\nbe careful. Look up for the word, and mark the checkbox before\npressing the Delete button.",
                                            compound="left", justify="left", 
                                            font=customtkinter.CTkFont(family="Helvetica", size=12, weight="bold"))
        self.info_label.grid(row=0, column=0, padx=3, pady=3, sticky="ew")
        
        self.ed_button = customtkinter.CTkButton(self.ed_frame, text="Edit", image=self.edition_image, 
                                                            compound="right", command=self.word_edition)
        self.ed_button.grid(row=2, column=0, padx=0, pady=0)

        self.check_var = customtkinter.StringVar(value="off")

        #self.ed_entry.bind('<Return>', self.word_edition)
        self.selection_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.selection_frame.grid_columnconfigure(0, weight=1)

        self.change_button = customtkinter.CTkButton(self.selection_frame, text="Go to Edit", image=self.edition_image, 
                                                            compound="right", command=self.edition_update)
        self.change_button.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        #the update words section


        # select default frame
        self.select_frame_by_name("Intro")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.intro_button.configure(fg_color=("gray75", "gray25") if name == "Intro" else "transparent")
        self.words_button.configure(fg_color=("gray75", "gray25") if name == "Words" else "transparent")
        self.search_button.configure(fg_color=("gray75", "gray25") if name == "Search" else "transparent")
        self.edition_button.configure(fg_color=("gray75", "gray25") if name == "Edition" else "transparent")        

        # show selected frame
        if name == "Intro":
            self.intro_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.intro_frame.grid_forget()
        if name == "Words":
            self.words_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.words_frame.grid_forget()
        if name == "Search":
            self.search_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.search_frame.grid_forget()
        if name == "Edition":
            self.ed_frame.grid(row=0, column=1, sticky="new")
            self.selection_frame.grid(row=1, column=1, sticky="sew")
        else:
            self.ed_frame.grid_forget()
            self.selection_frame.grid_forget()

    def intro_button_event(self):
        self.select_frame_by_name("Intro")
        self.intro_frame_textbox.focus_set()    

    def exit_program(self):
        os.close

    def meanings(self, word):
        DELIMITER = '#'
        outs = ''
        words = word.split(DELIMITER)
        if len(words) > 1:  
            for mean in words:
                outs += mean + ' / '
        else:
            return word
        
        return outs[:-2]

    def words_refresh(self):
        self.words_textbox.delete(1.0, "end")
        if self.words_button_sort._text == "by Intro":
            self.update_words_list(False)
        else:
            self.words_button_sort.configure(text = "by A-Z")
            self.update_words_list(True)

    def update_words_list(self, sort):
        self.words_textbox.delete(1.0, 'end')
        self.app_words = pd.read_csv(comiendoentokyo, encoding='utf8', iterator=True, chunksize=1000)
 
        for chunk in self.app_words:
            if sort == True:
                chunk.sort_values(["word"],
                                    axis=0, 
                                    ascending=[True],  
                                    inplace=True)
                self.words_button_sort.configure(text = "by Intro")
            else:
                self.words_button_sort.configure(text = "by A-Z")
            for index, row in chunk.iterrows():
                    self.words_textbox.tag_config("bold", foreground="#ffffff")
                    self.words_textbox.tag_config("normal", foreground="#C0C0C0")
                    word_final = row["word"]
                    meaning = self.meanings(row["meaning"]) + "\n"
                    words_list = (word_final, "means:", meaning)
                    self.words_textbox.insert('end', word_final, "bold")
                    self.words_textbox.insert('end', " means: ", "normal")
                    self.words_textbox.insert('end', meaning, "\n")

    def words_button_event(self):
        self.select_frame_by_name("Words")
        self.update_words_list(True)

    def search_button_event(self):
        self.select_frame_by_name("Search")
        self.search_entry.focus_set()
    
    def edition_button_event(self):
        self.select_frame_by_name("Edition")
        self.ed_entry.focus_set()
    
    def clear_search_buttons(self, button):
        button.grid_forget()
    
    def deletion(self, word_to_delete):
        df = pd.read_csv(comiendoentokyo, encoding='utf8')
        df = df.drop(df[df.word == word_to_delete].index)
        df.to_csv(comiendoentokyo, encoding='utf8', index=False)
        self.deletion_label.configure(text=word_to_delete + " was deleted")
        self.b_delete.grid_forget() 

    def search_word(self, search_entry):
        self.word_to_search = self.search_entry.get()
        
        if not self.word_to_search:
            return
        
        df = pd.read_csv(comiendoentokyo, encoding='utf8')
        results_final = ''
        result = ''
        for x in df.itertuples():
            if x[1].find(self.word_to_search) != -1: 
                results_final = x[1], "means:", x[2], "\n"
                results_final = ' '.join(results_final)
                results_final = str.replace(results_final,"#"," / ")
                result += results_final
        if results_final == '':
            result = self.word_to_search, " does not appear in the system."
            result = ' '.join(result)

        self.search_frame_label.configure(text=result) 
    
    def check_event(self, word_to_delete):
        self.check_sum = 0
        self.ed_button.configure(image=self.edition_image)
        self.ed_button.update()
        if self.check_var.get() == "on":
            self.ed_button.configure(text="Delete")
            self.ed_button.update()
            df = pd.read_csv(comiendoentokyo, encoding='utf8')
            df = df.drop(df[df.word == word_to_delete].index)
            df.to_csv(comiendoentokyo, encoding='utf8', index=False)
            self.deletion_label.configure(text=word_to_delete + " was deleted")
            self.check_sum = 1
            return self.check_sum 
    
    def word_pass(self):
        w_entry = self.search_w_entry.get()
        self.word_to_pass = self.searching_ed(w_entry)
        return self.word_to_pass

    def edition_update(self):
    # Iterate through every widget inside the frame
        for widget in self.ed_frame.winfo_children():
            widget.destroy()  # deleting widget
        
        self.search_w_entry = customtkinter.CTkEntry(self.ed_frame,
                                            justify="left", font=customtkinter.CTkFont(family="Helvetica",
                                                                                     size=14, weight="bold"),
                                            fg_color="transparent",
                                            border_width=1,
                                            corner_radius=3,
                                            width=270)
        self.search_w_entry.grid(row=1, column=0, padx=81, pady=18)
        self.search_w_entry.focus_set()
        self.search_w_entry.bind('<Return>', self.edition_update)
        if self.search_w_entry.get() != '':
            w_entry = self.search_w_entry.get()
            word= self.searching_ed(w_entry)
            print(word)
         #return


    def searching_ed(self, x_word):
        df = pd.read_csv(comiendoentokyo, encoding='utf8')
        results_final = ''
        result = ''
        for x in df.itertuples():
            if x[1].find(x_word) != -1: 
                results_final = x[1], "means:", x[2], "\n"
                results_final = ' '.join(results_final)
                results_final = str.replace(results_final,"#"," / ")
                result += results_final            
        return result
        
    def word_edition(self):
        self.word_to_edit = self.ed_entry.get()
        if not self.word_to_edit:
            return
        word = self.searching_ed(self.word_to_edit)
        if word != '':        
            check_ed = customtkinter.CTkCheckBox(self.ed_frame, text="check to delete " + self.word_to_edit,
                                                     command=self.check_event(self.word_to_edit),
                                            variable=self.check_var, onvalue="on", 
                                            offvalue="off")
            if self.check_sum > 0:
                #check_ed.destroy()
                check_ed.grid_forget()
                self.ed_button.configure(text="Edit")
                self.ed_button.configure(image=self.edition_image)
                return
            else:
                check_ed.grid(row=4, padx=20, pady=0)
                self.ed_button.configure(text="Delete")
                self.ed_button.configure(image=self.delete_image)

        else:
                #self.clear_search_buttons(B1)
            word = self.word_to_edit, " does not appear in the system."
            word = ' '.join(word)
        
        self.edition_label.configure(text=word) 
            

    def on_submit(self):
        new_word = self.intro_frame_textbox.get(1.0, customtkinter.END)
        new_word = new_word.split(',')
        
        df = pd.read_csv(comiendoentokyo, encoding='utf8')
        df = pd.DataFrame(df)

        try:
            new_word[1] = new_word[1]
        except: #avoiding index error
            new_word = 'error'

        search = df.loc[df['word'] == new_word[0]]

        if search.size > 0:
            self.save_label.configure(text=new_word[0] + " is already in the system.")
        elif search.size == 0 and new_word != 'error' and new_word[1] != '\n':
            data = {'word':[new_word[0]],
                  'meaning':[new_word[1][:-1]],
                  'number_of_searches':[0]}
            df = pd.DataFrame(data)
            df.to_csv(comiendoentokyo, mode='a', encoding='utf8', index=False, header=False)
            self.save_label.configure(text=new_word[0] + " added")
        else:
            self.save_label.configure(text="Meaning of " +  new_word[0] + " can't be empty.")

        self.intro_frame_textbox.delete(1.0, 'end')
        self.len_word = len(new_word)


if __name__ == "__main__":
    app = App()
    app.mainloop()
