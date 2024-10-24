# **Sapphire (SAPP)** - Multi-OS System Administration Tool

## **Overview**
Sapphire (SAPP) is a cross-platform tool designed to manage users, groups, and system services on both **Windows** and **Linux** systems. It provides a convenient command-line interface (CLI) for system administrators, allowing them to perform tasks with ease. The tool leverages Python's `click` for CLI interactions and `rich` for beautiful console output.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/sapphire.git
   cd sapphire
   ```

2. **Install the Dependencies**:
   Install all required dependencies listed in the `setup.py` file:
   ```bash
   pip install -e .
   ```

3. **Make Sure the Environment is Set**:
   Ensure you have the required privileges (admin/root) when running the tool to execute system-level commands.

---

## **Available Commands**

### **User Management**

- **List All Users**:
  ```bash
  sapp list_users
  ```
  Displays all users on the system in a table format.

- **Add a New User**:
  ```bash
  sapp add_user <username> --password <password>
  ```
  Creates a new user on the system. The password is optional.

- **Delete a User**:
  ```bash
  sapp delete_user <username>
  ```
  Deletes the specified user from the system.

---

### **Group Management**

- **List All Groups**:
  ```bash
  sapp list_groups
  ```
  Displays all groups in the system in a table format.

- **Add a New Group**:
  ```bash
  sapp add_group <groupname>
  ```
  Creates a new group on the system.

- **Delete a Group**:
  ```bash
  sapp delete_group <groupname>
  ```
  Deletes the specified group from the system.

- **Add a User to a Group**:
  ```bash
  sapp add_user_to_group <username> <groupname>
  ```
  Adds the specified user to a group.

---

## **Examples**

1. **Create a User with Password**:
   ```bash
   sapp add_user johndoe --password secret123
   ```

2. **List All Users**:
   ```bash
   sapp list_users
   ```

3. **Add a User to the `admin` Group**:
   ```bash
   sapp add_user_to_group johndoe admin
   ```

4. **Delete a User**:
   ```bash
   sapp delete_user johndoe
   ```

---

## **Supported Platforms**

Sapphire supports the following platforms:
- **Windows**: Uses `net` commands for user and group management.
- **Linux**: Uses `useradd`, `groupadd`, `userdel`, and `groupdel` commands.

> Ensure that you run the tool with **administrator privileges** on Windows and **sudo/root privileges** on Linux.

---

## **Contributing**

If you'd like to contribute to the development of Sapphire, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m "Add new feature"`).
5. Push to the branch (`git push origin feature-name`).
6. Open a Pull Request.

---

## **License**

Sapphire is released under the [MIT License](LICENSE).

---

### **Developed by: Jacob Gallardo-Quintero**

**Enjoy Sapphire and make system management simpler!**

