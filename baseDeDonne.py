import mysql.connector
from db_manager import*
from tkinter import*
from tkinter import ttk
import datetime

class Gestion_base_de_donnee(FrameMultijoueur):
    def __init__(self, fenetre):
        super().__init__(fenetre)
        
        
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="jeu_memoire"
        )
        self.cursor = self.conn.cursor()
        
       
        

    
        
    def creeTable(self):
        
        def Utilisateurs():
            def Envoyer():
                nom = entry_nom.get()
                age = entry_email.get()
                mail =  entry_mdp.get()
                
                self.cursor.execute("INSERT INTO utilisateur (pseudo,email) VALUES(%s,%s)",(nom,mail))
                self.conn.commit()
                
                
                self.cursor.execute("SELECT * FROM utilisateur ")
                res = self.cursor.fetchall()
                liste = []
                for u in res:
                    if u not in liste:
                        liste.append(u)
                
                print(liste)
                for _ in liste:
                    self.tree.insert("","end",values=(_))
                        
                
                self.conn.commit()
            app = CTk()
            app.title("Formulaire Stylé")
            app.geometry("400x400")

            titre = CTkLabel(app, text="Formulaire de contact", font=("Arial", 22, "bold"))
            titre.pack(pady=20)

            entry_nom = CTkEntry(app, placeholder_text="Nom")
            entry_nom.pack(pady=10, ipadx=10, ipady=5)

            entry_email = CTkEntry(app, placeholder_text="Email")
            entry_email.pack(pady=10, ipadx=10, ipady=5)

            entry_mdp = CTkEntry(app, placeholder_text="Mot de passe", show="*")
            entry_mdp.pack(pady=10, ipadx=10, ipady=5)

            btn_envoyer = CTkButton(app, text="Envoyer" ,command=Envoyer)
            btn_envoyer.pack(pady=20)

            app.mainloop()    
            
        self.nomUtilisateur = CTkLabel(self.frameHaut,width=5,text="Toha" ,font=("",30),text_color="white")
        self.nomUtilisateur.place(x=610,y=70)
        self.Utilisateur = CTkButton(self.frameHaut,width=50,height=50,text="🧑",fg_color="blue",font=("",30))
        self.Utilisateur.place(x=630,y=10)
      
        self.Utilisateur.configure(command= Utilisateurs)
        requettes = [
       
        """
        CREATE TABLE IF NOT EXISTS utilisateur (
            id_utilisateur INT AUTO_INCREMENT PRIMARY KEY,
            pseudo VARCHAR(50) NOT NULL,
            email VARCHAR(100)
        );
            """,
        """
            CREATE TABLE IF NOT EXISTS Partie (
            id_partie INT AUTO_INCREMENT PRIMARY KEY,
            date_heure DATETIME DEFAULT CURRENT_TIMESTAMP,
            mode ENUM('solo', 'multijoueur', 'vs_ordi') NOT NULL
        );
        """,
        """
            CREATE TABLE IF NOT EXISTS Score (
                id_score INT AUTO_INCREMENT PRIMARY KEY,
                id_utilisateur INT,
                id_partie INT,
                score_obtenu INT,
                temps_ecoule TIME,
                erreur INT,
                coups INT,
                FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur),
                FOREIGN KEY(id_partie) REFERENCES Partie(id_partie)
        );
        """]
        self.conn.commit()
        
        for requette in requettes:
            self.cursor.execute(requette)
        self.conn.commit()
        
        
        
        
       
            
    def Afficher(self):
        
        self.tree = ttk.Treeview(self.t,columns=("identifient","nom","email"), show="headings")
        self.tree.heading("identifient",text="joueurs")
        self. tree.heading("nom",text="pseaudo")
        self.tree.heading("email",text="email")
        self.tree.pack()
        
        self.cursor.execute("SELECT * FROM utilisateur ")
        res = self.cursor.fetchall()
        
        for _ in res:
            self.tree.insert("","end",values=(_))
        
        tree2 = ttk.Treeview(self.t,columns=("id","mode","heure"), show="headings")
        tree2.heading("id",text="partie-jouer")
        tree2.heading("mode",text="mode")
        tree2.heading("heure",text="heure")
        tree2.pack()
   
if __name__=='__main__':
    jeu = CTk()
    #fenetre = Memory_game(jeu)
    fenetre = Gestion_base_de_donnee(jeu)
    fenetre.frameMultijoueur()
    fenetre.frame1()
    fenetre.frame2()
    fenetre.frame3()
    fenetre.Afficher()
    fenetre.creeTable()
    #fenetre.insertion_des_donnee()
    jeu.resizable(width=False,height=False)
    fenetre.run()