# DjangoKickstarter

**DjangoKickstarter** is a preconfigured Django boilerplate designed to accelerate the development process. It includes essential tools like Django Allauth, Tailwind CSS, and prebuilt themes, providing a robust foundation for building web applications.

---

## Features

- **User Authentication**: Integrated with [Django Allauth](https://django-allauth.readthedocs.io/) for easy social and email-based authentication.
- **Tailwind CSS**: Simplifies styling with built-in support for [Tailwind CSS](https://tailwindcss.com/).
- **Prebuilt Themes**: Includes multiple ready-to-use themes for quick UI customization.
- **Simplified Development Workflow**: Start the server and Tailwind CSS watcher with a single command (`npm run dev`).
- **Template Library**: Includes templates for login, signup, and profile pages.
- **Responsive Design**: Optimized for various devices out of the box.

---

## Repository

Find the project on GitHub: [DjangoKickstarter Repository](https://github.com/Sayemahamed/DjangoKickstarter.git)

---

## Prerequisites

- Python 3.8+
- Node.js and npm
- Django (pre-installed via `requirements.txt`)
- A supported database (SQLite is the default)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sayemahamed/DjangoKickstarter.git
   cd DjangoKickstarter
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```bash
   npm install
   ```

4. Start the development server with Tailwind CSS live compilation:
   ```bash
   npm run dev
   ```

---

## Usage

### Switching Themes
Choose from the preconfigured themes by modifying the templates in the `themes/` directory or configuring them through the admin panel.

### Preconfigured Pages
- **Login**: `/accounts/login/`
- **Sign up**: `/accounts/signup/`
- **Profile**: `/profile/`

### Building Tailwind for Production
For production-ready CSS, you can run:
```bash
npm run build
```

---

## Folder Structure

```
DjangoKickstarter/
├── django_kickstarter/       # Main Django project folder
├── themes/                   # Preconfigured themes
├── templates/                # Templates for authentication and pages
├── static/                   # Static files for Tailwind and custom assets
├── tailwind.config.js        # Tailwind configuration
├── package.json              # Node.js dependencies
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## Contribution

We welcome contributions! Feel free to report issues, request features, or submit pull requests at our [GitHub repository](https://github.com/Sayemahamed/DjangoKickstarter.git).

---

## Author

**MD Iftaker Ahamed Sayem**

---

## License

This project is licensed under the [MIT License](LICENSE).

---

Kickstart your Django project effortlessly with DjangoKickstarter! 🚀
