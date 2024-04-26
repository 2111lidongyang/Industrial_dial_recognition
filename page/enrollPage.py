from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit

from sql.tools import create_db
from ui.enroll_uipage import Ui_Form


class EnrollPage(QWidget, Ui_Form):
    def __init__(self, login):
        super(EnrollPage, self).__init__()
        self.setupUi(self)
        self.loginpage = login
        self.init_slot()  # 初始化槽函数

    def init_slot(self):
        self.pushButton.clicked.connect(self.tologin)
        self.enrollBtn.clicked.connect(self.enroll)

    def tologin(self):
        self.loginpage.show()
        self.close()

    def enroll(self):
        user_id = self.idlineEdit.text()
        user_pwd = self.pwdlineEdit.text()
        yzm = str(self.yzmlineEdit.text())
        if self.radioButton.isChecked():
            user_class = 0
        elif self.radioButton_2.isChecked():
            user_class = 1
        else:
            QMessageBox.warning(self,'警告','请选择您的身份')
            return
        if user_id is not None and user_pwd is not None:
            if user_class == 1 and yzm == '211166':

                db, cursor = create_db(host='#', password='#', database='ldy',
                                       user='root', port=3306)
                try:
                    sql = "SELECT * FROM users WHERE user_id = '{}'LIMIT 1".format(str(user_id))
                    cursor.execute(sql)
                    userdata = cursor.fetchone()
                    if userdata:
                        print('该用户已存在')
                        QMessageBox.warning(self, '注册失败', '该用户已存在')
                        return
                    else:
                        print('注册开始')
                        sql_insert = "INSERT INTO users (user_id, user_pwd, user_class) VALUES ('{}', '{}', '{}')".format(str(user_id), str(user_pwd), int(user_class))
                        try:
                            cursor.execute(sql_insert)
                            db.commit()
                            cursor.close()
                            db.close()
                            QMessageBox.information(self, '用户注册成功', '用户注册成功')
                            return
                        except BaseException as e:
                            print('error', str(e))
                            db.rollback()
                            cursor.close()
                            db.close()
                            return
                except BaseException as e:
                    print('error:', str(e))
                    cursor.close()
                    db.close()
                    return
            elif user_class == 1 and yzm != '2111':
                QMessageBox.warning(self, '注册失败', '验证码错误')
                return
            elif user_class == 0:
                db, cursor = create_db(host='#', password='#', database='ldy',
                                       user='root', port=3306)
                try:
                    sql = "SELECT * FROM users WHERE user_id = '{}'LIMIT 1".format(str(user_id))
                    cursor.execute(sql)
                    userdata = cursor.fetchone()
                    if userdata:
                        print('该用户已存在')
                        QMessageBox.warning(self, '注册失败', '该用户已存在')
                        return
                    else:
                        print('注册开始')
                        sql_insert = "INSERT INTO users (user_id, user_pwd, user_class) VALUES ('{}', '{}', '{}')".format(
                            str(user_id), str(user_pwd), int(user_class))
                        try:
                            cursor.execute(sql_insert)
                            db.commit()
                            cursor.close()
                            db.close()
                            QMessageBox.information(self, '用户注册成功', '用户注册成功')
                            return
                        except BaseException as e:
                            print('error', str(e))
                            db.rollback()
                            cursor.close()
                            db.close()
                            return
                except BaseException as e:
                    print('error:', str(e))
                    cursor.close()
                    db.close()
                    return
        QMessageBox.warning(self, '注册失败', '请输入您的账号密码')
        return
