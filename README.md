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

## Auto Deployment on a VPS
1. Create a file in   ```.github/workflows/<file_name>.yml``` and add the provided code snippet to it.
```
name: Deploy on Push

on:
  push:
    branches:
      - main # Adjust to your desired branch

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v3

    - name: Install sshpass
      run: sudo apt-get update && sudo apt-get install -y sshpass

    - name: Deploy using rsync
      env:
        SSH_USERNAME: ${{ secrets.SSH_USERNAME }}
        SSH_IPADDRESS: ${{ secrets.SSH_IPADDRESS }}
        SSH_PASSWORD: ${{ secrets.SSH_PASSWORD }}
      run: |
        sshpass -p "$SSH_PASSWORD" rsync -rv \
          -e "ssh -o StrictHostKeyChecking=no" \
          ./ "$SSH_USERNAME@$SSH_IPADDRESS:<destination_path>" --exclude .git
```
2. Configure the following secrets in your GitHub repository:
 * ```SSH_USERNAME```: Your VPS username
 * ```SSH_PASSWORD```: Your VPS password
 * ```SSH_IPADDRESS```: The IP address of your VPS
3. Update the ```destination_path``` in the code to specify where your project should be deployed on the server.
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
