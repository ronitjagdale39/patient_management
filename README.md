# 🏥 Patient Management System

A lightweight **Patient Management System** built using **Python and JSON-based data storage**.  
This project demonstrates **core backend fundamentals**, including CRUD operations, data validation, and file-based persistence — making it suitable for **internship interviews and FAANG-style evaluations**.

---

## 🚀 Project Overview

The **Patient Management System** allows users to manage patient records efficiently using a JSON file as the data source.  
It supports:

- Retrieving existing patient data
- Adding new patient records
- Updating specific patient details (all fields optional)
- Deleting patient records safely

All patient data is stored and managed inside a `patient.json` file, ensuring **persistent storage without a database**.

---

## 🧠 Key Concepts Demonstrated

- File handling in Python
- JSON-based data persistence
- CRUD operations (Create, Read, Update, Delete)
- Optional field updates (partial updates)
- Clean and modular code structure
- Edge case handling (patient not found, empty data, etc.)

---

## 📁 Project Structure
---

## 📌 Features

### ✅ Retrieve Patient Data
- Reads existing patient records from `patient.json`
- Displays all stored patient information

### ➕ Add New Patient
- Allows users to create a new patient entry
- Automatically appends data to `patient.json`
- Prevents accidental overwrites

### ✏️ Update Patient Details
- Update **only the fields you want**
- All update fields are optional
- Existing data remains unchanged if a field is skipped

### ❌ Delete Patient
- Removes a patient record if it exists in `patient.json`
- Handles invalid or missing patient IDs gracefully

---

## 🗃️ Sample Patient JSON Structure

```json
{
  'name':'ronit',
'city':'mumbai',
'age':19,
'weight':70.5,
'height':1.74
}
