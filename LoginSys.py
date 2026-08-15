import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Account")
        self.setFixedSize(1300, 700)

        #BACKGROUND
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap("w3school/wp8226555.jpg"))
        self.bg.setScaledContents(True)
        self.bg.resize(1300, 700)

        #CENTER ui
        self.ui = QFrame(self)
        self.ui.setFixedSize(400, 400)
        self.ui.move(450, 150)
        self.ui.setStyleSheet("""
            QFrame {
            background-color: rgba(255, 255, 255, 50);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 80);
            }
        """)

        # shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(10)
        self.ui.setGraphicsEffect(shadow)

        # inside ui
        layout = QVBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(30, 25, 40, 25)

        title = QLabel("Login")
        title.setFont(QFont("Segoe UI", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        title.setFixedHeight(35)
        title.setStyleSheet("""
            QFrame {
            color: #090164;
            background-color:None;
            border-radius: None;
            border: None;
            }
        """)
        

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.email.setFixedHeight(40)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setFixedHeight(40)

        email = QLabel("Email")
        email.setFixedHeight(15)
        email.setFont(QFont("Segoe UI",10))
        self.email.returnPressed.connect(self.login)
        email.setStyleSheet("""
            QFrame {
            background-color:None;
            border-radius: None;
            border: None;
            }
        """)
        

        password = QLabel("Password")
        password.setFixedHeight(15)
        password.setFont(QFont("Segoe UI",10))
        self.password.returnPressed.connect(self.login)
        password.setStyleSheet("""
            QFrame {
            background-color:None;
            border-radius: None;
            border: None;
            }
        """)

        register = QLabel("<span style='color:black;'>Don't have an account? "
               "<a href='#' style='color:white;'>Register here</a></span>")
        register.setFixedHeight(15)
        register.setStyleSheet("""
            QFrame {
            background-color:None;
            border-radius: None;
            border: None;
            }
        """)

        def clicked():
            print("Register clicked!")
        register.linkActivated.connect(lambda _: clicked())

        forget = QLabel("Forget Password?")
        forget.setFixedHeight(15)
        forget.setFont(QFont("Segoe UI",10))
        forget.setStyleSheet("""
            QFrame {
            background-color:None;
            border-radius: None;
            border: None;
            }
        """)

        btn = QPushButton("Sign in")
        btn.clicked.connect(self.login)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #090164;
                color: white;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3aa0ff;
            }
        """)
        btn.setFont(QFont("Segoe UI", 14))

        # input style
        input_style = """
        QLineEdit {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 8px;
            background: rgba(255,255,255,200);
        }
        """

        self.email.setStyleSheet(input_style)
        self.password.setStyleSheet(input_style)

        layout.addWidget(title)
        layout.addWidget(email)
        layout.addWidget(self.email)
        layout.addWidget(password)
        layout.addWidget(self.password)
        layout.addWidget(forget)
        layout.addWidget(btn)
        layout.addWidget(register)

        self.ui.setLayout(layout)

        self.bg.lower()
        self.ui.raise_()
    
    def login(self):
        email = self.email.text()
        password = self.password.text()

        if email == "Chhat" and password == "280605":
            self.dashboard = DashboardUI()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Wrong Username or Password")
            


class DashboardUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.setFixedSize(1000,700)
        self.setStyleSheet("""
            QWidget{
                background:white;
                font-family:Segoe UI;
            }
        """)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0,0,0,0)
        

        # SIDEBAR
        sidebar = QFrame()
        sidebar.setFixedSize(240,700)
        sidebar.setFixedWidth(240)
        sidebar.move(0,-100)
        sidebar.setContentsMargins(0,0,0,0)
        sidebar.setStyleSheet("""
            QFrame{
                background:#003347;
                border-radius:0px;
            }
        """)

        side_layout = QVBoxLayout(sidebar)

        side_title = QLabel("Student Menu")
        side_title.setFont(QFont("Segoe UI",12,QFont.Weight.Bold))
        side_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        side_title.setFixedHeight(50)

        side_title.setStyleSheet("""
            QLabel{
                color:white;
            }
            
        """)

        side_layout.addWidget(side_title)

        menus = [
            "⌂ Dashboard",
            "♙ Profile",
            "▣ Certificates",
            "☑ Tasks",
            "⚙ Settings",
            "? Help"
        ]

        for menu in menus:
            button = QPushButton(menu)
            button.setFixedHeight(40)
            button.setStyleSheet("""
                QPushButton{
                    background:#003347;
                    border:none;
                    text-align:left;
                    padding:12px;
                    color:white;
                }
                QPushButton:hover{
                    background:#004461;
                    border-radius:3px;
                }
                QFont("Segoe UI",12,QFont.Weight.Bold)
            """)
            side_layout.addWidget(button)

        side_layout.addStretch()

        logout = QPushButton("⇥ Logout")
        logout.setStyleSheet("""
            QPushButton{
                border:none;
                padding:12px;
                border-radius:6px;
                text-align:left;
            }
        """)

        side_layout.addWidget(logout)

        #MAIN CONTENT
        content = QVBoxLayout()
        content.setContentsMargins(20,20,50,50)
        title = QLabel("Projects")
        title.setFont(
            QFont("Segoe UI",20,QFont.Weight.Bold)
        )
        content.addWidget(title)

        #SKILL BOXES
        skill_layout = QHBoxLayout()
        skills = [
            ("🧮","Calculator"),
            ("🖥️","POS System"),
            ("🔃","N/A"),
            ("🔃","N/A")
        ]

        for icon,name in skills:
            card = QFrame()
            card.setFixedSize(200,130)
            card.setStyleSheet("""
                QFrame{
                    background:white;
                    border-radius:15px;
                }
            """)

            layout = QVBoxLayout(card)

            icon_label = QLabel(icon)
            icon_label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            icon_label.setFont(
                QFont("Arial",25)
            )

            name_label = QLabel(name)
            name_label.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            name_label.setFont(
                QFont("Segoe UI",11,QFont.Weight.Bold)
            )

            btn = QPushButton("Open")
            btn.setFixedSize(165,30)
            btn.setStyleSheet("""
                QPushButton{
                    background:#ff6845;
                    color:white;
                    border-radius:8px;
                    padding:5px;
                }
            """)

            layout.addWidget(icon_label)
            layout.addWidget(name_label)
            layout.addWidget(btn)

            skill_layout.addWidget(card)

        content.addLayout(skill_layout)

        # COURSES
        course_title = QLabel("My Courses")
        course_title.setFont(
            QFont("Segoe UI",20,QFont.Weight.Bold)
        )

        content.addWidget(course_title)
        course_layout = QHBoxLayout()
        courses = [
            ("HTML","80%"),
            ("CSS","50%"),
            ("JavaScript","30%")
        ]

        for name,progress in courses:
            card = QFrame()
            card.setFixedSize(250,150)
            card.setStyleSheet("""
                QFrame{
                    background:white;
                    border-radius:15px;
                }
            """)

            layout = QVBoxLayout(card)
            title = QLabel(name)
            title.setFont(
                QFont("Segoe UI",14,QFont.Weight.Bold)
            )
            percent = QLabel(
                progress+" Progress"
            )
            bar = QProgressBar()

            bar.setValue(
                int(progress.replace("%",""))
            )
        
            button = QPushButton("Continue")

            layout.addWidget(title)
            layout.addWidget(percent)
            layout.addWidget(bar)
            layout.addWidget(button)

            course_layout.addWidget(card)

        content.addLayout(course_layout)
        content.addStretch()

        main_layout.addWidget(sidebar)
        main_layout.addLayout(content)


# ================= RUN =================
app = QApplication(sys.argv)
window = LoginUI()
window.show()
sys.exit(app.exec())