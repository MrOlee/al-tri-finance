import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

# =========================
# SETTING AWAL
# =========================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Aplikasi Keuangan Modern")
app.geometry("1400x800")

# =========================
# WARNA
# =========================
BG = "#0f172a"
CARD = "#1e293b"
SIDEBAR = "#111827"
WHITE = "#ffffff"

# =========================
# SIDEBAR
# =========================
sidebar = ctk.CTkFrame(app, width=250, fg_color=SIDEBAR, corner_radius=0)
sidebar.pack(side="left", fill="y")

title = ctk.CTkLabel(
    sidebar,
    text="💰 Finance App",
    font=("Poppins Bold", 24)
)
title.pack(pady=40)

menu1 = ctk.CTkButton(
    sidebar,
    text="Dashboard",
    height=45,
    corner_radius=12,
    font=("Poppins", 16)
)
menu1.pack(pady=10, padx=20, fill="x")

menu2 = ctk.CTkButton(
    sidebar,
    text="Transaksi",
    height=45,
    corner_radius=12,
    font=("Poppins", 16)
)
menu2.pack(pady=10, padx=20, fill="x")

menu3 = ctk.CTkButton(
    sidebar,
    text="Laporan",
    height=45,
    corner_radius=12,
    font=("Poppins", 16)
)
menu3.pack(pady=10, padx=20, fill="x")

menu4 = ctk.CTkButton(
    sidebar,
    text="Pengaturan",
    height=45,
    corner_radius=12,
    font=("Poppins", 16)
)
menu4.pack(pady=10, padx=20, fill="x")

# =========================
# MAIN CONTENT
# =========================
main = ctk.CTkFrame(app, fg_color=BG)
main.pack(side="right", fill="both", expand=True)

# =========================
# HEADER
# =========================
header = ctk.CTkFrame(main, fg_color="transparent")
header.pack(fill="x", padx=30, pady=20)

judul = ctk.CTkLabel(
    header,
    text="Dashboard Keuangan",
    font=("Poppins Bold", 30)
)
judul.pack(side="left")

tanggal = ctk.CTkLabel(
    header,
    text=datetime.now().strftime("%d %B %Y"),
    font=("Poppins", 16)
)
tanggal.pack(side="right")

# =========================
# CARD FRAME
# =========================
card_frame = ctk.CTkFrame(main, fg_color="transparent")
card_frame.pack(fill="x", padx=30)

def create_card(parent, title, value):
    card = ctk.CTkFrame(
        parent,
        fg_color=CARD,
        corner_radius=20,
        height=150
    )

    label_title = ctk.CTkLabel(
        card,
        text=title,
        font=("Poppins", 18)
    )
    label_title.pack(anchor="w", padx=20, pady=(20,5))

    label_value = ctk.CTkLabel(
        card,
        text=value,
        font=("Poppins Bold", 28)
    )
    label_value.pack(anchor="w", padx=20)

    return card

card1 = create_card(card_frame, "Total Saldo", "Rp 15.000.000")
card1.pack(side="left", expand=True, fill="x", padx=10)

card2 = create_card(card_frame, "Pemasukan", "Rp 8.000.000")
card2.pack(side="left", expand=True, fill="x", padx=10)

card3 = create_card(card_frame, "Pengeluaran", "Rp 3.000.000")
card3.pack(side="left", expand=True, fill="x", padx=10)

# =========================
# FORM INPUT
# =========================
form_frame = ctk.CTkFrame(
    main,
    fg_color=CARD,
    corner_radius=20
)
form_frame.pack(fill="x", padx=30, pady=25)

form_title = ctk.CTkLabel(
    form_frame,
    text="Tambah Transaksi",
    font=("Poppins Bold", 22)
)
form_title.pack(anchor="w", padx=20, pady=20)

input_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
input_frame.pack(fill="x", padx=20)

nama_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Nama Transaksi",
    height=45,
    corner_radius=12,
    font=("Poppins", 14)
)
nama_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

jumlah_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Jumlah",
    height=45,
    corner_radius=12,
    font=("Poppins", 14)
)
jumlah_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

kategori = ctk.CTkComboBox(
    input_frame,
    values=["Pemasukan", "Pengeluaran"],
    height=45,
    corner_radius=12,
    font=("Poppins", 14)
)
kategori.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_columnconfigure(1, weight=1)
input_frame.grid_columnconfigure(2, weight=1)

# =========================
# TABEL TRANSAKSI
# =========================
table_frame = ctk.CTkFrame(
    main,
    fg_color=CARD,
    corner_radius=20
)
table_frame.pack(fill="both", expand=True, padx=30, pady=(0,30))

table_title = ctk.CTkLabel(
    table_frame,
    text="Riwayat Transaksi",
    font=("Poppins Bold", 22)
)
table_title.pack(anchor="w", padx=20, pady=20)

columns = ("Tanggal", "Nama", "Kategori", "Jumlah")

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="#1e293b",
    foreground="white",
    rowheight=35,
    fieldbackground="#1e293b",
    borderwidth=0,
    font=("Poppins", 12)
)

style.configure(
    "Treeview.Heading",
    background="#334155",
    foreground="white",
    font=("Poppins Bold", 12)
)

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings"
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(fill="both", expand=True, padx=20, pady=20)

# =========================
# FUNCTION
# =========================
def tambah_data():
    tanggal = datetime.now().strftime("%d/%m/%Y")
    nama = nama_entry.get()
    jumlah = jumlah_entry.get()
    jenis = kategori.get()

    tree.insert("", "end", values=(
        tanggal,
        nama,
        jenis,
        f"Rp {jumlah}"
    ))

    nama_entry.delete(0, "end")
    jumlah_entry.delete(0, "end")

# =========================
# BUTTON
# =========================
btn = ctk.CTkButton(
    form_frame,
    text="Tambah Transaksi",
    height=50,
    corner_radius=15,
    font=("Poppins Bold", 16),
    command=tambah_data
)
btn.pack(padx=20, pady=20, fill="x")

# =========================
# RUN APP
# =========================
app.mainloop()
