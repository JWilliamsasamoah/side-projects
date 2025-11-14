# Grizzly Assistant

Grizzly Assistant is a **desktop launcher app** built with Python and Tkinter.  
It gives you a simple GUI with big buttons to quickly open:

- Social media
- Entertainment sites
- Anime streaming
- Food delivery
- Shopping sites
- Productivity / finance tools
- PC games installed on your machine

Think of it as a personal **homepage/launcher**, but as a desktop app.

---

## 🖥 Features

### 1. Main Menu

When you run the app, you get a main window with a custom image and a big button.  
Clicking it opens the main menu with categories:

- **Social media**
- **Entertainment**
- **Anime**
- **Ordering food**
- **Shopping**
- **Productivity and Finance**
- **Games**
- **Exit**

Each category opens in its own Tkinter `Toplevel` window.

---

### 2. Social Media Launcher

Opens popular sites in your browser:

- Google  
- Instagram  
- Snapchat  
- Facebook  
- Twitter  
- TikTok  
- Discord (desktop app via `subprocess` and your local path)

---

### 3. Entertainment

Opens streaming platforms:

- YouTube  
- Twitch  
- Netflix  
- Disney+  
- Prime Video  

---

### 4. Anime

Anime streaming shortcuts:

- Funimation  
- Crunchyroll  

---

### 5. Food Delivery

Quick access to food apps:

- Uber Eats  
- Foodora  
- SkipTheDishes  
- DoorDash  

---

### 6. Shopping

Opens shopping sites:

- Amazon  
- Best Buy  
- Walmart  
- Apple  
- Microsoft  
- Foot Locker  
- Costco  

---

### 7. Productivity & Finance

Productivity and finance tools:

- TD Bank  
- Scotiabank  
- LinkedIn  
- Gmail  
- Outlook  
- Google Docs / Slides / Forms / Sheets  
- Placeholder: “Other application coming soon!”

---

### 8. Games Launcher (Windows)

Launches installed PC games and launchers via `subprocess` (using your local paths):

- Overwatch  
- Call of Duty: Black Ops Cold War  
- GTA V  
- Warzone  
- Fortnite  
- Steam  
- Epic Games Launcher  
- Battle.net  

> These all use **hardcoded file paths** like `E://Games//Overwatch//Overwatch Launcher.exe`.  
> You’ll need to update these to match where your games are installed.

---

## 🛠 Tech Stack

**Language**

- Python

**Libraries**

- `tkinter` – GUI (buttons, windows, images)
- `webbrowser` – Open websites
- `subprocess` – Launch local apps and games

**Assets**

- `gazz.png` – Main background/logo image
- `bs.png` – Button image on the splash screen

Make sure these image files are in the **same directory** as the script.

---

## 📦 Setup & Installation

1. **Install Python** (if you don’t already have it)

   - Windows from python.org  
   - Tkinter is included in standard Python installs.

2. **Project structure example**

   ```text
   grizzly-assistant/
   ├─ grizzly_assistant.py   # your script
   ├─ gazz.png
   └─ bs.png
