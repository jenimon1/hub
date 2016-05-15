import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *


from SignUpPage import *
from CreateOrViewProjectPage import *


class LogInMainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout()
        self.vlayout.setStyleSheet("QVBoxLayout {background: rgba(0,255,0,0%)}")


        ##All neccessary Labels
        self.appNameLabel = QLabel("Engineer Hub")
        self.usernameLabel = QLabel("Username: ")
        self.passwordLabel = QLabel("Password: ")
        self.signUpLabel = QLabel("<A href='www.TutorialsPoint.com'>Sign Up</A>")

        ##All LineEdits
        self.usernameLine = QLineEdit()
        self.passwordLine = QLineEdit()

        ##All button
        self.loginBut = QPushButton("Login")




        # self.backgroundPic = QLabel()
        # self.backgroundPic.setPixmap(QPixmap("/Users/Chieh/Desktop/EngineerHub/loginPageBackEdit.jpg"))
        # # self.loginBut.setStyleSheet("QWidget {border: 20px; border-radius: 0px; background-color: #00FF00; left: -600px;}")
        # self.loginBut.setStyleSheet("QWidget {background-image: url(loginPageBackEdit.png)}")
        #
        # self.setStyleSheet("QWidget {background-image: url(/Users/Chieh/Desktop/EngineerHub/loginPageBackEdit.jpg)}")






        ##All LineEdits setup
        self.passwordLine.setEchoMode(QLineEdit.Password)


        ##Frame1 below Stretch() ,contain username Label and username line edit,with HorizontalBoxLayout as its layout
        row1hlayout = QHBoxLayout()
        row1hlayout.addStretch()
        row1hlayout.addWidget(self.usernameLabel)
        row1hlayout.addWidget(self.usernameLine)
        row1hlayout.addStretch()

        frame1 = QFrame()
        frame1.setLayout(row1hlayout)

        ##Frame2 below Stretch() ,contain password Label and password line edit,with HorizontalBoxLayout as its layout
        row2hlayout = QHBoxLayout()
        row2hlayout.addStretch()
        row2hlayout.addWidget(self.passwordLabel)
        row2hlayout.addWidget(self.passwordLine)
        row2hlayout.addStretch()

        frame2 = QFrame()
        frame2.setLayout(row2hlayout)





        ##Frame3 below Stretch() ,contain Signup Label and login button,with HorizontalBoxLayout as its layout
        row3hlayout = QHBoxLayout()
        row3hlayout.addStretch()
        row3hlayout.addWidget(self.signUpLabel)
        row3hlayout.addWidget(self.loginBut)
        row3hlayout.addStretch()

        frame3 = QFrame()
        frame3.setLayout(row3hlayout)









        ##Vertical layout as Login page main layout adding 1 stretch and all the 3 frames to its layout
        self.vlayout.addStretch()
        self.vlayout.addWidget(frame1)
        self.vlayout.addWidget(frame2)
        self.vlayout.addWidget(frame3)


        ##All Signal Handling function
        self.signUpLabel.linkActivated.connect(self.signUpLabelClicked)  ##when signup is clicked new SignUpPage(QDialog PopUpP)
        self.loginBut.clicked.connect(self.loginButClicked)



        ##LoginInPage window setup
        self.setGeometry(250,0,1000,800)
        self.setLayout(self.vlayout)


        self.show()

    def signUpLabelClicked(self):
        signUpWindow = SignUpMainWindow()



    def loginButClicked(self):
        print("Login button clicked")
        createOrViewProjWindow = CreateOrViewProjectMainWindow()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = LogInMainWindow()
    sys.exit(app.exec_())





