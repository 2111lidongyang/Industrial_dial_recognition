import math
import random
from PyQt5.QtGui import QColor
import cv2

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox, QLineEdit, QFileDialog, QHeaderView

from infer import parse_args, infer
from page.minios import MinioCommand
from sql.tools import create_db
from ui.home_page import Ui_Form


class HomePage(QWidget, Ui_Form):
    def __init__(self, user_class, login):
        super(HomePage, self).__init__()
        self.setupUi(self)
        self.loginpage = login
        self.user_calss = user_class  # 获取到该用户的等级
        self.tabWidget.setCurrentIndex(0)  # 默认设置为普通用户的界面
        self.init_slot()  # 初始化槽函数
        self.init_data()  # 初始化图片检测的数据
        self.init_userdata()  # 初始化用户的数据

    def init_slot(self):
        self.tabWidget.currentChanged.connect(self.on_tab_changed)
        self.chooseBtn.clicked.connect(self.choose_file)  # 连接选择图片地址槽函数
        self.detectBtn.clicked.connect(self.detects)  # 连接图片检测槽函数
        self.delBtn.clicked.connect(self.deldata)  # 连接删除检测数据槽函数
        self.deluserBtn.clicked.connect(self.deluserdata)  # 连接删除用户数据槽函数
        self.upuserBtn.clicked.connect(self.upuserdata)  # 连接提升用户槽函数
        self.pushButton.clicked.connect(self.closeback)  # 连接退出登录槽函数

    def closeback(self):
        self.loginpage.idlineEdit.clear()
        self.loginpage.pwdlineEdit.clear()
        self.loginpage.show()

        self.close()

    def on_tab_changed(self, index):
        current_tab = self.tabWidget.widget(index)
        self.tabWidget.currentChanged.disconnect(self.on_tab_changed)
        print("Current Index:", index)

        if current_tab == self.tab:
            print("Switched to Tab 1")
            self.tabWidget.currentChanged.connect(self.on_tab_changed)
            return
        elif current_tab == self.tab_3:
            if self.user_calss == 0:
                QMessageBox.warning(self, '权限警告', '您没有权限进入该界面')
                print("Setting Index to 0")
                self.tabWidget.setCurrentIndex(0)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return
            else:
                print("Setting Index to 1")
                self.tabWidget.setCurrentIndex(1)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return
        elif current_tab == self.tab_2:
            if self.user_calss == 0:
                QMessageBox.warning(self, '权限警告', '您没有权限进入该界面')
                print("Setting Index to 0")
                self.tabWidget.setCurrentIndex(0)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return
            else:
                print("Setting Index to 2")
                self.tabWidget.setCurrentIndex(2)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return

    def deldata(self):
        # 获取选中的行索引
        selected_indexes = self.tableView.selectionModel().selectedRows()
        if selected_indexes:
            # 获取第一行最后一列的值
            last_column_index = self.tableView.model().columnCount() - 1
            first_selected_index = selected_indexes[0]
            last_column_value = self.tableView.model().index(first_selected_index.row(), last_column_index).data()

            # 在MySQL数据库中删除对应数据
            db, cursor = create_db(host='#', password='#', database='ldy',
                                   user='root', port=3306)
            sql = "DELETE FROM biaopan WHERE id = '{}'".format(last_column_value)
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
                QMessageBox.information(self, '删除成功', '数据删除成功')
                self.init_data()  # 刷新用户数据
            except BaseException as e:
                print('error', str(e))
                db.rollback()
                cursor.close()
                db.close()
                QMessageBox.warning(self, '删除失败', '请重试！！！')
        else:
            print("没有选中任何行。")
            QMessageBox.warning(self, '删除失败', '没有选中任何行！')

    def deluserdata(self):
        # 获取选中的行索引
        selected_indexes = self.tableView_2.selectionModel().selectedRows()
        if selected_indexes:
            # 获取第一行第一列的值
            first_selected_index = selected_indexes[0]
            first_column_value = self.tableView_2.model().data(first_selected_index)

            # 在MySQL数据库中删除对应数据
            db, cursor = create_db(host='#', password='#', database='ldy',
                                   user='root', port=3306)
            sql = "DELETE FROM users WHERE user_id = '{}'".format(str(first_column_value))
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
                QMessageBox.information(self, '删除成功', '数据删除成功')
                self.init_userdata()  # 刷新用户数据
                return
            except BaseException as e:
                print('error', str(e))
                db.rollback()
                cursor.close()
                db.close()
                QMessageBox.warning(self, '删除失败', '请重试！！！')
                return
        else:
            print("没有选中任何行。")
            QMessageBox.warning(self, '删除失败', '没有选中任何行！')

    def upuserdata(self):
        # 获取选中的行索引
        selected_indexes = self.tableView_2.selectionModel().selectedRows()
        if selected_indexes:
            # 获取第一行第一列的值
            first_selected_index = selected_indexes[-1]
            sec_selected_index = selected_indexes[0]
            first_column_value = self.tableView_2.model().data(first_selected_index)
            sec_column_value = self.tableView_2.model().data(sec_selected_index)

            # 在MySQL数据库中删除对应数据
            db, cursor = create_db(host='#', password='#', database='ldy',
                                   user='root', port=3306)
            sql = "UPDATE users SET user_class = '{}' WHERE user_id = '{}'".format(int(1), str(sec_column_value))
            try:
                cursor.execute(sql)
                db.commit()
                cursor.close()
                db.close()
                QMessageBox.information(self, '更新成功', '用户等级提升成功')
                self.init_userdata()  # 刷新用户数据
                return
            except BaseException as e:
                print('error', str(e))
                db.rollback()
                cursor.close()
                db.close()
                QMessageBox.warning(self, '更新失败', '请重试！！！')
                return
        else:
            print("没有选中任何行。")
            QMessageBox.warning(self, '更新失败', '没有选中任何行！')

    def init_data(self):
        from PyQt5.QtGui import QColor

        db, cursor = create_db(host='#', password='#', database='#', user='root', port=3306)
        sql = "SELECT * FROM biaopan"
        cursor.execute(sql)
        row = cursor.fetchall()

        if row:
            print(row)
            # 创建模型
            self.model1 = QStandardItemModel(len(row), 5)  # 几行几列数据
            self.model1.setHorizontalHeaderLabels(['时间', '检测结果', '图片url', '检测状态', '序号'])

            # 将数据填充到模型中
            for row_index, row_data in enumerate(row):
                for col_index, data in enumerate(row_data):
                    if col_index == 3:
                        if data == 1:
                            data = '正常'
                        else:
                            data = '异常'
                    item = QStandardItem(str(data).strip())  # 使用strip()去除可能存在的空白字符
                    self.model1.setItem(row_index, col_index, item)

                if row_data[-2] == 1:
                    for col_index in range(4):
                        if col_index == 3:
                            self.model1.item(row_index, col_index).setBackground(QColor('green'))
                        self.model1.item(row_index, col_index)
                elif row_data[-2] == 2:
                    for col_index in range(4):
                        if col_index == 3:
                            self.model1.item(row_index, col_index).setBackground(QColor('red'))
                        self.model1.item(row_index, col_index)

            # 将模型应用到表格视图中
            self.tableView.setModel(self.model1)
            # 调整列宽以适应内容
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            print('无该用户信息')
            QMessageBox.warning(self, '登录失败', '无该用户信息！')

    def init_userdata(self):
        db, cursor = create_db(host='#', password='#', database='#', user='root', port=3306)
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        row = cursor.fetchall()

        if row:
            print(row)
            # 创建模型
            self.model = QStandardItemModel(len(row), 3)  # 几行几列数据
            self.model.setHorizontalHeaderLabels(['用户账号', '用户密码', '用户等级'])

            # 将数据填充到模型中
            for row_index, row_data in enumerate(row):
                for col_index, data in enumerate(row_data):
                    if col_index == 2:
                        if data == 1:
                            data = '管理员'
                        else:
                            data = '普通用户'
                    item = QStandardItem(str(data).strip())  # 使用strip()去除可能存在的空白字符
                    self.model.setItem(row_index, col_index, item)

                if row_data[-1] == 1:
                    for col_index in range(4):
                        self.model.item(row_index, col_index)
                elif row_data[-1] == 2:
                    for col_index in range(4):
                        self.model.item(row_index, col_index)

            # 将模型应用到表格视图中
            self.tableView_2.setModel(self.model)
            # 调整列宽以适应内容
            self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            print('无该用户信息')
            QMessageBox.warning(self, '登录失败', '无该用户信息！')

    def choose_file(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, '选择图片', '', 'Image files (*.jpg *.png *.jpeg)',
                                                       options=options)
        if self.fileName:
            pixmap = QPixmap(self.fileName)
            pixmap = pixmap.scaled(self.label_8.size(), Qt.KeepAspectRatio)
            self.label_8.setPixmap(pixmap)

    def detects(self):
        print('开始表盘检测')
        self.low_temp = self.higspinBox.value()
        self.height_temp = self.lowspinBox.value()
        if self.low_temp == self.height_temp:
            QMessageBox.warning(self, '阈值错误', '您选择的高低阈值相同')
            return
        if self.low_temp and self.height_temp:
            try:
                if self.fileName:
                    self.label_7.setStyleSheet("background-color: #c8835c; border-radius: 20px;")
                    args = parse_args(self.fileName)
                    res = infer(args)
                    print('res', res[0])
                    res_number = len(res[0])
                    result = ''
                    maxs = 0
                    mins = 0
                    if res_number > 1:  # 2个以上数据
                        print('两')
                        print(type(res[0]))
                        maxs = max(res[0])
                        mins = min(res[0])
                        print('maxs:', maxs)
                        print('mins:', mins)
                        for r in res[0]:
                            result += str(math.ceil(r * 1000) / 1000)[:4] + '、'
                    else:
                        print('一')
                        result += str(math.ceil(res[0][0] * 1000) / 1000)[:4] + '、'
                        maxs = res[0][0]
                        mins = res[0][0]

                    self.numlineEdit_2.setText(str(result))
                    self.numlineEdit.setText(str(res_number))

                    pixmap = QPixmap(r'./output/result/rrr.jpg')
                    pixmap = pixmap.scaled(self.label_8.size(), Qt.KeepAspectRatio)
                    self.label_8.setPixmap(pixmap)

                    pixmap = QPixmap(r'./output/result\visualize_res.jpg')
                    pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatio)
                    self.label.setPixmap(pixmap)
                    # self.label_7.setStyleSheet("background-color: #b9c850,  border-radius: 20px;")
                    from datetime import datetime

                    current_time = datetime.now()
                    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")

                    # 将检测图片上传到数据库
                    m = MinioCommand(ip="#", api_port="9000", access_key="#",
                                     secret_key="#")
                    num = random.randint(0, 999999)
                    # print(num)
                    avatar_url = ''
                    db, cursor = create_db(host='#', password='#', database='ldy',
                                           user='root', port=3306)
                    if m.UploadObject('res_img{}.jpg'.format(str(num)), "taijiavatar", r'./output/result'
                                                                                       r'\visualize_res.jpg'):
                        avatar_url = 'http://43.143.229.40:9000/taijiavatar/' + 'res_img{}.jpg'.format(str(num))
                        print(avatar_url)
                    print('maxs = ', maxs)
                    print('mins = :', mins)
                    print('height_temp = ', self.height_temp)
                    print('low = :', self.low_temp)

                    if int(maxs) > int(self.height_temp):
                        QMessageBox.warning(self, '检测完成', '检测到阈值过高！！！！')
                        self.label_7.setStyleSheet("background-color: red;  border-radius: 20px;")

                        try:
                            sql = "INSERT INTO biaopan (time, res, img_url, status) VALUES ('{}', '{}', '{}', '{}')".format(
                                formatted_time, str(result), str(avatar_url), 2)
                            cursor.execute(sql)
                            db.commit()
                            cursor.close()
                            db.close()
                            self.init_data()
                            return
                        except BaseException as e:
                            print('error:', str(e))
                            db.rollback()
                            cursor.close()
                            db.close()
                            return

                    elif int(mins) < int(self.low_temp):
                        QMessageBox.warning(self, '检测完成', '检测到阈值过低！！！！')
                        self.label_7.setStyleSheet("background-color: red;  border-radius: 20px;")
                        try:
                            sql = "INSERT INTO biaopan (time, res, img_url, status) VALUES ('{}', '{}', '{}', '{}')".format(
                                formatted_time, str(result), str(avatar_url), 2)
                            cursor.execute(sql)
                            db.commit()
                            cursor.close()
                            db.close()
                            self.init_data()
                            return
                        except BaseException as e:
                            print('error:', str(e))
                            db.rollback()
                            cursor.close()
                            db.close()
                            return
                    else:
                        QMessageBox.information(self, '检测完成', '正常')
                        sql = "INSERT INTO biaopan (time, res, img_url, status) VALUES ('{}', '{}', '{}', '{}')".format(
                            formatted_time, str(result), str(avatar_url), 1)
                        cursor.execute(sql)
                        db.commit()
                        cursor.close()
                        db.close()
                        self.init_data()
                        self.label_7.setStyleSheet("background-color: #29b33b;  border-radius: 20px;")
                        return
                else:
                    QMessageBox.warning(self, '请选择您要检测的图片', '请选择您要检测的图片')
                    return
            except:
                return
        else:
            QMessageBox.warning(self, '请选择您的检测阈值', '请选择您的检测阈值')
            return
