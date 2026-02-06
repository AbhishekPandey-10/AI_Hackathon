# Project Nexus 🚀

**Project Nexus** is a unified "Campus Super-App" designed to consolidate the fragmented digital experience of university students into a single, cohesive, and visually stunning dashboard.

Built with **Django** and **TailwindCSS**, it features a "Glassmorphism" design system and integrates core campus services into one seamless interface.

---

## 🌟 Features (v1.0)

### 1. Daily Pulse (The Core) ⚡
*   **Mess Menu**: View daily meals with descriptions.
*   **Live Feedback Loop**: Rate meals (Bad/Okay/Great) and view real-time sentiment graphs.
*   **Campus Feed**: AI-summarized notices categorized by urgency (Critical, Urgent, Standard).
*   **Weather**: Visual campus weather widget.

### 2. Academic Cockpit (The Brain) 🎓
*   **Smart Schedule**: Weekly timetable grid with "Next Class" prediction.
*   **Attendance Visualizer**: "Donut Chart" for overall attendance + subject-wise progress bars (Red/Green zones).
*   **Results**: CGPA tracking and grade cards.

### 3. Student Exchange (The Marketplace) 🤝
*   **Marketplace**: Buy/Sell used items (Books, Gadgets, etc.) with image uploads.
*   **Travel Board**: "Departure Board" style carpooling/cab-sharing list to find travel buddies.
*   **Lost & Found**: Backend support for reporting and tracking lost items.

### 4. Administrative Block (The Office) 🏛️
*   **Fee Status**: Widget showing fee dues with Red (Unpaid) / Green (Paid) status.
*   **RMS (Request Management System)**: Submit complaints (Hostel/Mess/Security) with images and track their resolution status.

---

## 🛠️ Tech Stack

*   **Backend**: Python, Django 5.2.5
*   **Frontend**: HTML5, TailwindCSS (CDN), Vanilla JavaScript
*   **Database**: SQLite (Dev), PostgreSQL (Ready for Prod)
*   **Authentication**: Custom User Model (Email/Phone support mockup)
*   **Design**: Custom "Nexus" Design System (Glassmorphism, Dark Mode)

---

## 🚀 Installation & Setup

### 1. Clone & Install
```bash
# Clone the repository
git clone https://github.com/yourusername/project-nexus.git
cd project-nexus

# Install Dependencies
pip install django
```

### 2. Configure Environment
Create a `.env` file (optional) or ensure `settings.py` has a valid `SECRET_KEY`.

### 3. Run Migrations
Initialize the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 5. Launch Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 📂 Project Structure

```text
w:/Ropar/
├── project_nexus/      # Main settings & URL routing
├── users/             # Auth, Dashboard, Profiles
├── daily_pulse/       # Mess Menu, Notices, Weather
├── student_exchange/  # Marketplace, Travel, Lost & Found
├── academic_cockpit/  # Timetable, Attendance, Results
├── administration/    # Fees, Complaints (RMS)
├── templates/         # Global HTML Templates (base.html, dashboard.html)
├── media/             # User uploaded content (Images)
└── manage.py          # Django CLI utility
```

---

## 🎨 Design System

The UI uses a custom **Glassmorphism** effect:
*   **Background**: Deep abstract gradients (`bg-nexus-dark`).
*   **Cards**: `.glass` utility (White opacity + Blur).
*   **Accents**: Violet/Blue gradients for primary actions.

---

**Developed by Abhishek Pandey** | Version 1.0 (Stable)
