import streamlit as st
import sqlite3
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT
)
""")
conn.commit()
st.title("📞 Contact Book")

menu = ["Add Contact", "View Contacts", "Update Contact", "Delete Contact"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Add Contact":
    st.subheader("Add New Contact")
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    
    if st.button("Save Contact"):
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        st.success(f"✅ Contact {name} added successfully!")
elif choice == "View Contacts":
    st.subheader("📋 Contact List")
    cursor.execute("SELECT * FROM contacts")
    data = cursor.fetchall()
    
    for contact in data:
        st.write(f"👤 {contact[1]} | 📞 {contact[2]} | ✉️ {contact[3]}")
elif choice == "Update Contact":
    st.subheader("✏️ Update Contact")
    contact_name = st.text_input("Enter Contact Name to Update")
    new_name = st.text_input("New Name")
    new_phone = st.text_input("New Phone")
    new_email = st.text_input("New Email")
    
    if st.button("Update"):
        cursor.execute("UPDATE contacts SET phone=?, email=? WHERE name=?", 
                       (new_phone, new_email, contact_name))
        conn.commit()
        st.success(f"✅ Contact '{contact_name}' updated successfully!")

elif choice == "Delete Contact":
    st.subheader("❌ Delete Contact")
    contact_name = st.text_input("Enter Contact Name to Delete")
    
    if st.button("Delete"):
        cursor.execute("DELETE FROM contacts WHERE name=?", (contact_name,))
    conn.commit()
    st.success(f"✅ Contact '{contact_name}' deleted successfully!")

