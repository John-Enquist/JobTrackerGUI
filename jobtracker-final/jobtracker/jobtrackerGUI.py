
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from jobtracker import *

display_Text = ""
state = ""
options = ["Standard","Case-Sensitive","Search by Line"]


class JobTracker:
    def __init__(self, master):
        self.master = master
        global display_Text # use global variable
        searchTypeSelected = tk.StringVar(master)
        searchTypeSelected.set(options[0])

        self.master.geometry("700x300")
        self.master.configure(bg= 'LightSteelBlue2')
        self.master.winfo_toplevel().title("Job Tracker")
        
        self.frame = tk.Frame(self.master, bg= 'LightSteelBlue2', borderwidth=1, width = 80, height = 50)

        self.text_read = scrolledtext.ScrolledText(self.master, state = 'disabled', font = ("Sans Seriff",10), borderwidth=1, bg="ghost white", width = 30, height = 10, undo=True)
        self.text_read['font'] = ('consolas', '12')
        self.text_read.place(x=50,y=20)
        self.text_read.pack(padx = 10, pady = 10, expand=False, fill='both')
        
        self.write_to_file = tk.Button(self.frame, font = ("Sans Seriff",10), text = 'Add Entry', activebackground = "steel blue", width = 10, command = lambda : self.input_window("Add", searchTypeSelected))
        self.write_to_file.pack(side = 'left', padx = 1, pady = 5)

        self.edit_file = tk.Button(self.frame, font = ("Sans Seriff",10), text = 'Edit File', activebackground = "steel blue", width = 10, command = lambda : self.input_window("Edit", searchTypeSelected))
        self.edit_file.pack(side = 'left', padx = 1, pady = 5)

        self.read_from_file = tk.Button(self.frame, font = ("Sans Seriff",10), text = 'Read File', activebackground = "steel blue", width = 10, command = lambda :  self.input_window("Read", searchTypeSelected))
        self.read_from_file.pack(side = 'left', padx = 1, pady = 5)

        self.find_in_file = tk.Button(self.frame, font = ("Sans Seriff",10), text = 'Search File', activebackground = "steel blue", width = 10, command = lambda :  self.input_window("Search", searchTypeSelected))
        self.find_in_file.pack(side = 'left', padx = 1, pady = 5)

        self.quit_button = tk.Button(self.frame, font = ("Sans Seriff",10), text = 'Quit', activebackground = "steel blue", width = 10, command = self.close_windows)
        self.quit_button.pack(side = 'right', padx = 1, pady = 5)

        self.frame.pack(side = 'bottom')

    #add input window for adding or searching file
    def input_window(self, inputType, searchTypeSelected):
        global display_Text #use global variable
        global state
        self.remove_input_frame()
        state = inputType
        self.input_frame = tk.Frame(self.master, bg= 'LightSteelBlue2', borderwidth=1, width = 70, height = 20)
        if (inputType == 'Search'):
            self.create_search_frame(searchTypeSelected)
        elif (inputType == 'Read'):
            self.display_file_contents()
        elif (inputType == 'Add'):
            self.display_file_contents()
            self.create_add_entry_frame()
        else:
            self.display_file_contents()
            self.text_read.configure(state = 'normal')
            self.enter = tk.Button(self.input_frame, font = ("Sans Seriff",10), text = "Save", width = 10, height = 1, activebackground = "steel blue", command = lambda : self.editFile())
            self.enter.pack(side = 'right', padx = 2)
        self.input_frame.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
        self.input_frame.pack()

    #creates objects for the add entry functionality   
    def create_add_entry_frame(self):
        self.add_entry_label_frame = tk.Frame(self.master, borderwidth=1, width = 70, height = 5, padx = 1, bg = "LightSteelBlue2")

        self.company_name_label = tk.Label(self.add_entry_label_frame, text = "Company Name", width = 20, height=1, padx= 2, bg = "LightSteelBlue2", justify=tk.LEFT)
        self.company_name_label.pack(side="left")

        self.job_title_label = tk.Label(self.add_entry_label_frame, text = "Job Title", width = 14, height=1, padx = 2, bg = "LightSteelBlue2", justify=tk.LEFT, anchor="w")
        self.job_title_label.pack(side="left")

        self.required_skills_label = tk.Label(self.add_entry_label_frame, text = "Req. Skills", width = 17, height=1, padx = 2, bg = "LightSteelBlue2", justify=tk.LEFT,  anchor="w")
        self.required_skills_label.pack(side="left")

        self.additional_notes_label = tk.Label(self.add_entry_label_frame, text = "Notes", width = 30, height = 1, padx = 2, bg = "LightSteelBlue2", justify=tk.LEFT, anchor="w")
        self.additional_notes_label.pack(side="left")

        self.add_entry_text_frame = tk.Frame(self.master, bg= 'LightSteelBlue2', borderwidth=1, width = 70, height = 5)

        self.company_name = tk.Entry(self.add_entry_text_frame, font = ("Sans Seriff",10), width = 15)
        self.company_name.pack(side = 'left', padx = 2, pady=1)

        self.job_title = tk.Entry(self.add_entry_text_frame, font = ("Sans Seriff",10), width = 15)
        self.job_title.pack(side = 'left', padx = 2, pady=1)
        
        self.required_skills = tk.Entry(self.add_entry_text_frame, font = ("Sans Seriff",10), width = 15)
        self.required_skills.pack(side = 'left', padx = 2, pady=1)
        
        self.additional_notes = tk.Entry(self.add_entry_text_frame, font = ("Sans Seriff",10), width = 15)
        self.additional_notes.pack(side = 'left', padx = 2, pady=1)
        
        self.enter = tk.Button(self.add_entry_text_frame, font = ("Sans Seriff",10), text = "Enter", width = 10, activebackground = "steel blue", command = lambda : self.add_entry_and_display())
        self.enter.pack(side = 'left', padx = 2, pady=1)

        self.add_entry_label_frame.pack()
        self.add_entry_text_frame.pack()

    #creates objects for the search functionality
    def create_search_frame(self, searchTypeSelected):
        self.text_entry = tk.Entry(self.input_frame, font = ("Sans Seriff",10))
        self.text_entry.pack(side = 'left', padx= 2, pady = 2)

        self.search_type = tk.OptionMenu(self.input_frame, searchTypeSelected, *options)
        self.search_type.pack(side = "left", padx = 2, pady = 2)

        self.enter = tk.Button(self.input_frame, font = ("Sans Seriff",10), text = "Search", width = 10, height = 1, activebackground = "steel blue", command = lambda : self.search_file(self.text_entry.get(), searchTypeSelected.get()))
        self.enter.pack(side = 'right', padx = 2)

    def search_file(self, keyword, searchType):
        global display_Text
        display_Text = searchFile(keyword, searchType)
        self.display_file_contents()
        self.remove_input_frame()


    def add_entry_and_display(self):
        global display_Text
        strJobName = self.company_name.get()
        strJobTitle = self.job_title.get()
        strSkills = self.required_skills.get()
        strNotes = self.additional_notes.get()
        addEntry(strJobName, strJobTitle, strSkills, strNotes)
        
        #addEntryToFile(self.text_entry.get())
        self.display_file_contents()
        self.remove_input_frame()

    def editFile(self):
        global display_Text
        display_Text = self.text_read.get("1.0", tk.END)
        overwriteFileContents(display_Text)
        self.display_file_contents()
        self.remove_input_frame()

    #Determines which frame removal method is necessary and does cleanup of objects
    def remove_input_frame(self):
        global state
        if (state == 'Edit'):
            self.remove_edit_frame()
        elif (state == 'Add'):
            self.remove_add_frame()
        elif (state == 'Search'):
            self.remove_search_frame()
        elif (state == 'Read'):
            self.remove_read_frame()
        state = ''

    #Removes objects associated with the "Edit" Functionality
    def remove_edit_frame(self):
        try:
           if (bool(self.input_frame.winfo_exists())):
                self.enter.pack_forget()
                self.input_frame.pack_forget()
        except:
            print("edit frame does not exist")

    #Removes objects associated with the "Read" Functionality
    def remove_read_frame(self):
        try:
           if (bool(self.input_frame.winfo_exists())):
                self.input_frame.pack_forget()
        except:
            print("edit frame does not exist")

    #Removes objects associated with the "Search" Functionality
    def remove_search_frame(self):    
        try:
            if (bool(self.input_frame.winfo_exists())):
                self.text_entry.pack_forget()
                self.enter.pack_forget()
                self.input_frame.pack_forget()
        except:
            print("search frame does not exist")

    #Removes objects associated with the "Add" Functionality
    def remove_add_frame(self):    
        try:
            if (bool(self.input_frame.winfo_exists())):
                self.company_name_label.pack_forget()
                self.job_title_label.pack_forget()
                self.required_skills_label.pack_forget()                
                self.additional_notes_label.pack_forget()               
                self.company_name.pack_forget()                
                self.job_title.pack_forget()            
                self.required_skills.pack_forget()             
                self.additional_notes.pack_forget()             
                self.enter.pack_forget()                
                self.add_entry_label_frame.pack_forget()
                self.add_entry_text_frame.pack_forget()
                self.input_frame.pack_forget()
        except:
            print("add frame does not exist")

    #display current text stored in display_text 
    #this function is used for displaying search results
    def display_stored_text(self):
        global state
        self.text_read.configure(state = 'normal')
        self.text_read.delete('1.0', tk.END)
        self.text_read.insert(tk.END, display_Text)
        self.text_read.configure(state = 'disabled')
        state = 'Search'

    #Displays the contents of the job file in a format viewable by the user
    #Displays search results as well when applicable
    def display_file_contents(self):
        global state
        if (state == 'Search'):
            self.display_stored_text()
        else:
            self.text_read.configure(state = 'normal')
            self.text_read.delete('1.0', tk.END)
            self.text_read.insert(tk.END, printFileContents())
            self.text_read.configure(state = 'disabled')

    def clear_text(self):
        self.text_read.configure(state = 'normal')
        self.text_read.delete('1.0', tk.END)
        self.text_read.configure(state = 'disabled')

    #Ends Application
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = JobTracker(root)
    root.mainloop()

if __name__ == '__main__':
    main()