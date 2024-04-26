from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit

from page.enrollPage import EnrollPage
from page.homePage import HomePage
from sql.tools import create_db
from ui.login_uipage import Ui_Form


class LoginPage(QWidget, Ui_Form):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.setupUi(self)
        self.init_slot()  # 初始化槽函数

    def init_slot(self):
        self.pushButton.clicked.connect(self.toenroll)
        self.loginBtn.clicked.connect(self.login)

    def toenroll(self):
        self.enrollpage = EnrollPage(self)
        self.enrollpage.show()
        self.close()

    def login(self):
        user_id = self.idlineEdit.text()  # 获取用户输入的账号
        user_pwd = self.pwdlineEdit.text()  # 获取用户输入的账号
        if user_id is not None and user_pwd is not None:
            print('开始登录')
            db, cursor = create_db(host='#', password='#', database='ldy',
                                   user='root', port=3306)
            try:
                sql = "SELECT user_class FROM users WHERE user_id = '{}' AND user_pwd = '{}' LIMIT 1".format(str(user_id), str(user_pwd))
                cursor.execute(sql)
                userdata = cursor.fetchone()
                if userdata:
                    print('登录成功')
                    user_class = userdata[0]
                    QMessageBox.information(self, '登录成功', '用户登录成功')
                    self.home = HomePage(user_class, self)
                    self.home.show()
                    self.close()
                    return
                else:
                    print('该用户不存在')
                    QMessageBox.warning(self, '登录失败', '该用户不存在')
            except BaseException as e:
                print('error:',str(e))
                cursor.close()
                db.close()
        QMessageBox.warning(self, '警告', '请输入您的账号密码')
        return