import tkinter as tk
from tkinter import messagebox
from src.crud_logic import CRUDLogic

class CRUDApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("CRUD Application")
        
        self.logic = CRUDLogic()
        
        # Labels and Entry fields
        tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry = tk.Entry(root, width=40)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        self.name_entry.bind("<Return>", self.focus_next_widget)
        
        tk.Label(root, text="Telefone:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.bind("<Return>", self.focus_next_widget)
        
        tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry = tk.Entry(root, width=40)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.email_entry.bind("<Return>", self.handle_enter_key)
        
        # Buttons for CRUD operations
        self.add_button = tk.Button(root, text="Adicionar", command=self.add_person)
        self.add_button.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.search_button = tk.Button(root, text="Buscar", command=self.search_person)
        self.search_button.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        
        self.update_button = tk.Button(root, text="Atualizar", command=self.update_person)
        self.update_button.grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)
        
        self.delete_button = tk.Button(root, text="Deletar", command=self.delete_person)
        self.delete_button.grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)
        
        # Listbox to display persons
        self.person_listbox = tk.Listbox(root, width=50)
        self.person_listbox.grid(row=4, column=0, columnspan=4, padx=10, pady=5, sticky=tk.W)
        
        self.update_person_listbox()
        
        # Bind double click event on listbox
        self.person_listbox.bind("<Double-Button-1>", self.fill_entry_fields)
    
    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return "break"
    
    def handle_enter_key(self, event):
        if self.add_button["state"] == tk.DISABLED:
            self.update_person()
        else:
            self.add_person()
        return "break"
    
    def fill_entry_fields(self, event):
        selected_index = self.person_listbox.curselection()
        
        if selected_index:
            selected_person = self.logic.get_persons()[selected_index[0]]
            
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, selected_person.name)
            
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, selected_person.phone)
            
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, selected_person.email)
            
            self.logic.set_editing_person_id(selected_person.id)
            self.add_button.config(state=tk.DISABLED)
    
    def update_person(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        
        error_message = self.logic.update_person(name, phone, email)
        if error_message:
            messagebox.showwarning("Erro", error_message)
        else:
            self.update_person_listbox()
            self.clear_entries()
            self.add_button.config(state=tk.NORMAL)
            self.name_entry.focus_set()  # Retorna o foco ao campo de nome
    
    def add_person(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        
        error_message = self.logic.add_person(name, phone, email)
        if error_message:
            messagebox.showwarning("Erro", error_message)
        else:
            self.update_person_listbox()
            self.clear_entries()
            self.name_entry.focus_set()  # Retorna o foco ao campo de nome
    
    def search_person(self):
        query = self.name_entry.get().strip().lower()
        results = self.logic.search_person(query)
        self.display_search_results(results)
    
    def display_search_results(self, results):
        self.person_listbox.delete(0, tk.END)
        for person in results:
            self.person_listbox.insert(tk.END, f"ID: {person.id} - {person.name} - {person.phone} - {person.email}")
    
    def delete_person(self):
        selected_index = self.person_listbox.curselection()
        if selected_index:
            confirmed = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esta pessoa?")
            if confirmed:
                selected_person = self.logic.get_persons()[selected_index[0]]
                self.logic.delete_person(selected_person.id)
                self.update_person_listbox()
                self.clear_entries()
    
    def update_person_listbox(self):
        self.person_listbox.delete(0, tk.END)
        for person in self.logic.get_persons():
            self.person_listbox.insert(tk.END, f"ID: {person.id} - {person.name} - {person.phone} - {person.email}")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.logic.set_editing_person_id(None)
        self.add_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    app = CRUDApplication(root)
    root.mainloop()
