#
#
import tkinter as tk
from tkinter import messagebox, Label, Entry, Button
from tkinter import *
from tkinter import ttk
import pandas as pd
from datetime import datetime
import pymysql

# 连接数据库
def init_db():
    # 设置数据库连接参数
    db_params = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'caca*5521',
        'db': 'medicine',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }
    # 尝试连接数据库
    try:
        conn = pymysql.connect(**db_params)
        print("Database connection successful!")
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None

def waiting():
    messagebox.showinfo("ERROR", "正在开发，敬请期待。")

# 登录
def login(conn, entry_username, entry_password, var_role, windows):
    username = entry_username.get()
    password = entry_password.get()
    identity = var_role.get()
    cursor = conn.cursor()
    # 身份选择
    if identity == '患者':
        sql = "SELECT 患者账号,患者密码 FROM 账号密码患者 WHERE 患者账号=%s AND 患者密码=%s"
    if identity == '医生':
        sql = "SELECT 医生账号,医生密码 FROM 账号密码医生 WHERE 医生账号=%s AND 医生密码=%s"
    if identity == '管理员':
        sql = "SELECT 管理员账号,管理员密码 FROM 账号密码管理员 WHERE 管理员账号=%s AND 管理员密码=%s"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    if result:
        windows.destroy()
        messagebox.showinfo("Login Success", "You have successfully logged in!")
        if identity == '患者':
            main_ui_patient(username)
        if identity == '医生':
            main_ui_doctor(username)
        if identity == '管理员':
            main_ui_admin(username)
    else:
        messagebox.showerror("Login Failed", "Password incorrect, please try again.")

# 注册
def signup(patient_id, name, id_number, age, contact, password, password_again, sign_ui):
    if not patient_id or not name or not id_number or not age or not contact:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return
    if password != password_again:
        messagebox.showerror("错误", "两次输入密码不符，请重新填写。")
        return

    cursor = conn.cursor()
    cursor.execute("INSERT INTO 患者 (患者ID, 患者姓名, 身份证号, 年龄, 患者联系方式) VALUES (%s, %s, %s, %s, %s)",
                   (patient_id, name, id_number, age, contact))
    conn.commit()
    cursor.execute("INSERT INTO 账号密码患者 (患者账号, 患者密码) VALUES (%s, %s)",
                   (patient_id, password))
    conn.commit()
    messagebox.showinfo("成功", "注册成功。")
    sign_ui.destroy()

# 注册ui
def signup_ui(conn):
    sign_ui = tk.Tk()
    sign_ui.geometry('500x280')
    sign_ui.title("Sign up your account")

    # 患者信息
    patient_id_label = tk.Label(sign_ui, text="患者ID")
    patient_id_label.grid(row=0, column=0, sticky="w")
    patient_id_entry = tk.Entry(sign_ui)
    patient_id_entry.grid(row=0, column=1, sticky="w")

    name_label = tk.Label(sign_ui, text="患者姓名")
    name_label.grid(row=1, column=0, sticky="w")
    name_entry = tk.Entry(sign_ui)
    name_entry.grid(row=1, column=1, sticky="w")

    id_number_label = tk.Label(sign_ui, text="身份证号")
    id_number_label.grid(row=2, column=0, sticky="w")
    id_number_entry = tk.Entry(sign_ui)
    id_number_entry.grid(row=2, column=1, sticky="w")

    age_label = tk.Label(sign_ui, text="年龄")
    age_label.grid(row=3, column=0, sticky="w")
    age_entry = tk.Entry(sign_ui)
    age_entry.grid(row=3, column=1, sticky="w")

    contact_label = tk.Label(sign_ui, text="患者联系方式")
    contact_label.grid(row=4, column=0, sticky="w")
    contact_entry = tk.Entry(sign_ui)
    contact_entry.grid(row=4, column=1, sticky="w")

    password_label = tk.Label(sign_ui, text="密码")
    password_label.grid(row=5, column=0, sticky="w")
    password_entry = tk.Entry(sign_ui)
    password_entry.grid(row=5, column=1, sticky="w")

    password_again_label = tk.Label(sign_ui, text="确认密码")
    password_again_label.grid(row=6, column=0, sticky="w")
    password_again_entry = tk.Entry(sign_ui)
    password_again_entry.grid(row=6, column=1, sticky="w")

    # 创建提交按钮
    submit_button = tk.Button(sign_ui, text="   提交   ", command=lambda: add_patient_to_db(
        patient_id_entry.get(),
        name_entry.get(),
        id_number_entry.get(),
        age_entry.get(),
        contact_entry.get(),
        password_entry.get(),
        password_again_entry.get(),
        sign_ui
    ))
    submit_button.grid(row=7, column=1, sticky="w")

    sign_ui.mainloop()

# 登录ui
def log_ui():
    #创建窗口500x280
    windows = tk.Tk()
    windows.geometry('500x280')
    windows.title("Medicine Management System")
    #用户名
    Label(windows, text="Username:").grid(row=0, column=0)
    entry_username = Entry(windows)
    entry_username.grid(row=0, column=1)
    #密码
    Label(windows, text="Password:").grid(row=1, column=0)
    entry_password = Entry(windows, show="*")
    entry_password.grid(row=1, column=1)
    #身份选择
    var_role = tk.StringVar(value="患者")
    label_role = tk.Label(windows, text="请选择您的身份:")
    label_role.grid(row=2, column=0)
    radiobutton_patient = tk.Radiobutton(windows, text="患者", variable=var_role, value="患者")
    radiobutton_doctor = tk.Radiobutton(windows, text="医生", variable=var_role, value="医生")
    radiobutton_admin = tk.Radiobutton(windows, text="管理员", variable=var_role, value="管理员")
    radiobutton_patient.grid(row=3, column=0)
    radiobutton_doctor.grid(row=3, column=1)
    radiobutton_admin.grid(row=3, column=2)
    #登录按钮
    Button(windows, text="     登录     ", command=lambda: login(conn, entry_username, entry_password, var_role, windows)).grid(row=4, column=1)
    Button(windows, text="     注册     ", command=lambda: signup_ui(conn)).grid(row=5, column=1)
    #主循环
    windows.mainloop()

# 查询患者信息
def get_patient_info(patient_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM 患者 WHERE 患者ID = %s", (patient_id,))
            result = cursor.fetchone()
            return result
    except Exception as e:
        messagebox.showerror("查询错误", str(e))
        return None

# 患者界面查询药品信息和处方信息（限制）
def get_patient_data(table_name):
    with conn.cursor() as cursor:
        if table_name == '药物信息':
            sql = "SELECT * FROM 药品患者"
            cursor.execute(sql)
        elif table_name == '处方信息':
            cursor.execute(
                "SELECT * FROM 处方 WHERE 患者ID = %s",
                (choose_pid))
        result = cursor.fetchall()
        return result
def load_patient_data():
    selected_table = table_selector.get()
    data = get_patient_data(selected_table)
    if selected_table == '药物信息':
        df = pd.DataFrame(data, columns=['药品名称', '批准文号', '药品类型', '保质期', '售价', '主要成分', '储存方式', '适用症状'])
    elif selected_table == '处方信息':
        df = pd.DataFrame(data, columns=['处方ID', '开具日期', '医生ID', '患者ID'])
    dataframe_to_treeview(tree, df)

# 患者修改信息
def modify_patient_info_to_db(patient_id, contact, mp):
    if not contact:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE `患者` SET `患者联系方式` = %s WHERE `患者ID` = %s",
        (contact, patient_id))
    conn.commit()
    messagebox.showinfo("成功", "修改成功。")

    mp.destroy()
def modify_patient_info(patient_id):
    mp = tk.Tk()
    mp.geometry('500x280')
    mp.title("Medicine Management System: Modify patient information")
    frame = tk.LabelFrame(mp)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    contact_label = tk.Label(frame, text="联系方式")
    contact_label.grid(row=0, column=0, sticky="w")
    contact_entry = tk.Entry(frame)
    contact_entry.grid(row=0, column=1, sticky="w")

    # 创建提交按钮
    submit_button = tk.Button(frame, text="   提交   ", command=lambda: modify_patient_info_to_db(
        patient_id,
        contact_entry.get(),
        mp
    ))
    submit_button.grid(row=1, column=1, sticky="w")

    mp.mainloop()

# 患者修改密码
def modify_patient_password_to_db(patient_id, old_password, new_password, new_password_again, mpp):
    if not old_password or not new_password or not new_password_again:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return

    cursor = conn.cursor(cursor=pymysql.cursors.Cursor)
    sql = "SELECT 患者密码 FROM 账号密码患者 WHERE 患者账号 = %s"
    cursor.execute(sql, (patient_id))
    result = cursor.fetchone()
    if result:

        stored_password = result[0]
        print(stored_password)
        if stored_password != old_password:
            messagebox.showerror("错误", "旧密码错误。")
            return

        if new_password != new_password_again:
            messagebox.showerror("错误", "两次输入密码不符，请重新填写。")
            return
        cursor.execute(
            "UPDATE `账号密码患者` SET `患者密码` = %s WHERE `患者账号` = %s",
            (new_password, patient_id))
        conn.commit()
        messagebox.showinfo("成功", "密码修改成功")
        mpp.destroy()
def modify_patient_password(patient_id):
    mpp = tk.Tk()
    mpp.geometry('500x280')
    mpp.title("Medicine Management System: Modify patient information")
    frame = tk.LabelFrame(mpp)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    old_password_label = tk.Label(frame, text="请输入旧密码")
    old_password_label.grid(row=0, column=0, sticky="w")
    old_password_entry = tk.Entry(frame)
    old_password_entry.grid(row=0, column=1, sticky="w")

    new_password_label = tk.Label(frame, text="请输入新密码")
    new_password_label.grid(row=1, column=0, sticky="w")
    new_password_entry = tk.Entry(frame)
    new_password_entry.grid(row=1, column=1, sticky="w")

    new_password_again_label = tk.Label(frame, text="请确认新密码")
    new_password_again_label.grid(row=2, column=0, sticky="w")
    new_password_again_entry = tk.Entry(frame)
    new_password_again_entry.grid(row=2, column=1, sticky="w")

    submit_button = tk.Button(frame, text="   提交   ", command=lambda: modify_patient_password_to_db(
        patient_id,
        old_password_entry.get(),
        new_password_entry.get(),
        new_password_again_entry.get(),
        mpp
    ))
    submit_button.grid(row=3, column=1, sticky="w")

    mpp.mainloop()

# 查询医生信息
def get_doctor_info(doctor_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM 医生 WHERE 医生ID = %s", (doctor_id,))
            result = cursor.fetchone()
            return result
    except Exception as e:
        messagebox.showerror("查询错误", str(e))
        return None

# 根据选择查询表格信息（患者/药品）：医生端
def get_all_info(table_name):
    with conn.cursor() as cursor:
        if table_name == '患者信息':
            sql = "SELECT * FROM 患者"
        elif table_name == '药物信息':
            sql = "SELECT * FROM 药品"
        elif table_name == '医生信息':
            sql = "SELECT * FROM 医生"
        elif table_name == '处方信息':
            sql = "SELECT * FROM 处方"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

# 信息表格及实现
def treeview_sort(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    try:
        l.sort(key=lambda t: int(t[0]), reverse=reverse)
    except ValueError:
        l.sort(reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort(tv, col, not reverse))
def dataframe_to_treeview(tree, dfs, column_name='序号'):
    tree.delete(*tree.get_children())
    a = dfs.columns.values.tolist()
    a.insert(0, column_name)
    b = [80 for nums in range(len(a) - 1)]
    b.insert(0, 50)
    df_titles = dict(zip(a, b))

    tree['columns'] = list(df_titles)
    for title in df_titles:
        tree.heading(title, text=title)
        tree.column(title, width=df_titles[title], anchor='center')
        tree.heading(title, command=lambda _col=title: treeview_sort(tree, _col, False))

    for index, row in dfs.iterrows():
        datas = row.tolist()
        datas.insert(0, index)
        tree.insert('', 'end', text='', values=datas)

# 开处方
def get_prescription_num():
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(处方ID) FROM 处方")
    result = cursor.fetchone()
    # 确保 result 不是 None 且至少包含一个元素
    if result:
        # 去除前导零，转换为整数，加1，然后再格式化为七位数字符串
        current_max_num = int(result[0].lstrip('0'))
        next_num = current_max_num + 1
        return '{:07d}'.format(next_num)
    else:
        return '0000001'

def add_prescription(prescription_id, patient_id, medicine_id , quantity, doctor_id, pu):
    if not patient_id or not medicine_id or not quantity or not prescription_id:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return

    # 获取当前日期和时间
    now = datetime.now()
    # 格式化输出年月日时分秒
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM 处方 WHERE 处方ID = %s",
        (prescription_id))
    result = cursor.fetchone()
    if result:
        cursor.execute("INSERT INTO 处方内容 (处方ID, 药品ID, 数量) VALUES (%s, %s, %s)",
                       (prescription_id, medicine_id, quantity))
        conn.commit()
    else:
        cursor.execute("INSERT INTO 处方 (处方ID, 开具日期, 医生ID, 患者ID) VALUES (%s, %s, %s, %s)",
                       (prescription_id, formatted_time, doctor_id, patient_id))
        conn.commit()
        cursor.execute("INSERT INTO 处方内容 (处方ID, 药品ID, 数量) VALUES (%s, %s, %s)",
                       (prescription_id, medicine_id, quantity))
        conn.commit()
    '''
    cursor.execute("INSERT INTO 药品销售记录 (记录ID, 药品ID, 医生ID, 患者ID, 数量, 销售日期) VALUES (%s, %s, %s, %s, %s, %s)",
                   (record_id, medicine_id, doctor_id, patient_id, quantity, formatted_time))
    conn.commit()
    record_id += 1
    '''
    messagebox.showinfo("成功", "药品已添加")

# 开处方ui
def prescription(doctor_id):
    pu = tk.Tk()
    pu.geometry('1080x720')
    pu.title("Medicine Management System: prescription")
    frame = tk.LabelFrame(pu)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    prescription_id_label = tk.Label(frame, text="处方ID")
    prescription_id_label.place(x=10, y=0)
    prescription_id_entry = tk.Entry(frame)
    prescription_id_entry.place(x=120, y=0)

    patient_id_label = tk.Label(frame, text="患者ID")
    patient_id_label.place(x=10, y=30)
    patient_id_entry = tk.Entry(frame)
    patient_id_entry.place(x=120, y=30)

    medicine_id_label = tk.Label(frame, text="药品ID")
    medicine_id_label.place(x=10, y=60)
    medicine_id_entry = tk.Entry(frame)
    medicine_id_entry.place(x=120, y=60)

    quantity_label = tk.Label(frame, text="数量")
    quantity_label.place(x=10, y=90)
    quantity_entry = tk.Entry(frame)
    quantity_entry.place(x=120, y=90)

    submit_button = tk.Button(frame, text="提交处方", command=lambda: add_prescription(
        prescription_id_entry.get(),
        patient_id_entry.get(),
        medicine_id_entry.get(),
        quantity_entry.get(),
        doctor_id,
        pu
    ))
    submit_button.place(x=120, y=120)

    global table_selector, tree
    table_selector = ttk.Combobox(frame, values=['处方信息', '药物信息'])
    table_selector.place(x=10, y=150, width=150)
    table_selector.set('处方信息')
    load_button = tk.Button(frame, text="加载数据", command=load_table_data)
    load_button.place(x=170, y=150, width=150)
    # 创建Treeview表格
    columns = []
    tree = ttk.Treeview(frame, show='headings', columns=columns)
    tree.place(x=10, y=200, width=1030, height=280)
    # 添加滚动条
    xbar = tk.Scrollbar(frame, orient='horizontal', command=tree.xview)
    xbar.place(x=10, y=480, width=1030)
    ybar = tk.Scrollbar(frame, orient='vertical', command=tree.yview)
    ybar.place(x=1030, y=200, height=280)
    tree.configure(xscrollcommand=xbar.set, yscrollcommand=ybar.set)
    # 初始加载患者表数据
    load_table_data()

    # 主循环
    pu.mainloop()

# 添加患者信息
def add_patient_to_db(patient_id, name, id_number, age, contact, password, password_again, ap):
    if not patient_id or not name or not id_number or not age or not contact:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return
    if password != password_again:
        messagebox.showerror("错误", "两次输入密码不符，请重新填写。")
        return

    cursor2 = conn.cursor(cursor=pymysql.cursors.Cursor)
    sql = "SELECT * FROM 患者 WHERE 患者ID = %s"
    cursor2.execute(sql, (patient_id))
    result = cursor2.fetchone()

    if result:
        messagebox.showerror("错误", "患者ID重复，请重新输入。")
        return

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO 患者 (患者ID, 患者姓名, 身份证号, 年龄, 患者联系方式) VALUES (%s, %s, %s, %s, %s)",
                       (patient_id, name, id_number, age, contact))
        conn.commit()
        cursor.execute("INSERT INTO 账号密码患者 (患者账号, 患者密码) VALUES (%s, %s)",
                       (patient_id, password))
        conn.commit()
        messagebox.showinfo("成功", "患者信息已添加")
    except pymysql.Error as e:
        messagebox.showerror("数据库错误", str(e))

    ap.destroy()
def add_patient():
    ap = tk.Tk()
    ap.geometry('500x280')
    ap.title("Medicine Management System: Add patient")
    frame = tk.LabelFrame(ap)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    # 患者信息
    patient_id_label = tk.Label(frame, text="患者ID")
    patient_id_label.grid(row=0, column=0, sticky="w")
    patient_id_entry = tk.Entry(frame)
    patient_id_entry.grid(row=0, column=1, sticky="w")

    name_label = tk.Label(frame, text="患者姓名")
    name_label.grid(row=1, column=0, sticky="w")
    name_entry = tk.Entry(frame)
    name_entry.grid(row=1, column=1, sticky="w")

    id_number_label = tk.Label(frame, text="身份证号")
    id_number_label.grid(row=2, column=0, sticky="w")
    id_number_entry = tk.Entry(frame)
    id_number_entry.grid(row=2, column=1, sticky="w")

    age_label = tk.Label(frame, text="年龄")
    age_label.grid(row=3, column=0, sticky="w")
    age_entry = tk.Entry(frame)
    age_entry.grid(row=3, column=1, sticky="w")

    contact_label = tk.Label(frame, text="患者联系方式")
    contact_label.grid(row=4, column=0, sticky="w")
    contact_entry = tk.Entry(frame)
    contact_entry.grid(row=4, column=1, sticky="w")

    password_label = tk.Label(frame, text="密码")
    password_label.grid(row=5, column=0, sticky="w")
    password_entry = tk.Entry(frame)
    password_entry.grid(row=5, column=1, sticky="w")

    password_again_label = tk.Label(frame, text="确认密码")
    password_again_label.grid(row=6, column=0, sticky="w")
    password_again_entry = tk.Entry(frame)
    password_again_entry.grid(row=6, column=1, sticky="w")

    # 创建提交按钮
    submit_button = tk.Button(frame, text="   提交   ", command=lambda: add_patient_to_db(
        patient_id_entry.get(),
        name_entry.get(),
        id_number_entry.get(),
        age_entry.get(),
        contact_entry.get(),
        password_entry.get(),
        password_again_entry.get(),
        ap
    ))
    submit_button.grid(row=7, column=1, sticky="w")

    ap.mainloop()

# 修改患者信息
def d_modify_patient_info_to_db(patient_id, name, id_number, age, contact, password, dmp):
    if not patient_id or not name or not id_number or not age or not contact or not password:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE `患者` SET `患者ID` = %s WHERE `患者ID` = %s",
        (contact, patient_id))
    conn.commit()
    cursor.execute(
        "UPDATE `患者` SET `患者联系方式` = %s WHERE `患者ID` = %s",
        (contact, patient_id))
    conn.commit()
    cursor.execute(
        "UPDATE `患者` SET `患者联系方式` = %s WHERE `患者ID` = %s",
        (contact, patient_id))
    conn.commit()
    cursor.execute(
        "UPDATE `患者` SET `患者联系方式` = %s WHERE `患者ID` = %s",
        (contact, patient_id))
    conn.commit()
    cursor.execute(
        "UPDATE `账号密码患者` SET `患者密码` = %s WHERE `患者ID` = %s",
        (password, patient_id))
    conn.commit()
    messagebox.showinfo("成功", "修改成功。")

    dmp.destroy()
def d_modify_patient_info():
    dmp = tk.Tk()
    dmp.geometry('500x280')
    dmp.title("Medicine Management System: Modify patient information")
    frame = tk.LabelFrame(dmp)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    patient_id_label = tk.Label(frame, text="患者ID")
    patient_id_label.grid(row=0, column=0, sticky="w")
    patient_id_entry = tk.Entry(frame)
    patient_id_entry.grid(row=0, column=1, sticky="w")

    name_label = tk.Label(frame, text="患者姓名")
    name_label.grid(row=1, column=0, sticky="w")
    name_entry = tk.Entry(frame)
    name_entry.grid(row=1, column=1, sticky="w")

    id_number_label = tk.Label(frame, text="身份证号")
    id_number_label.grid(row=2, column=0, sticky="w")
    id_number_entry = tk.Entry(frame)
    id_number_entry.grid(row=2, column=1, sticky="w")

    age_label = tk.Label(frame, text="年龄")
    age_label.grid(row=3, column=0, sticky="w")
    age_entry = tk.Entry(frame)
    age_entry.grid(row=3, column=1, sticky="w")

    contact_label = tk.Label(frame, text="患者联系方式")
    contact_label.grid(row=4, column=0, sticky="w")
    contact_entry = tk.Entry(frame)
    contact_entry.grid(row=4, column=1, sticky="w")

    new_password_label = tk.Label(frame, text="密码")
    new_password_label.grid(row=1, column=0, sticky="w")
    new_password_entry = tk.Entry(frame)
    new_password_entry.grid(row=1, column=1, sticky="w")

    # 创建提交按钮
    submit_button = tk.Button(frame, text="   提交   ", command=lambda: add_patient_to_db(
        patient_id_entry.get(),
        name_entry.get(),
        id_number_entry.get(),
        age_entry.get(),
        contact_entry.get(),
        new_password_entry.get(),
        dmp
    ))
    submit_button.grid(row=5, column=1, sticky="w")

    dmp.mainloop()

# 表格选择（列）
def load_table_data():
    selected_table = table_selector.get()
    data = get_all_info(selected_table)
    if selected_table == '患者信息':
        df = pd.DataFrame(data, columns=['患者ID', '患者姓名', '身份证号', '年龄', '患者联系方式'])
    elif selected_table == '药物信息':
        df = pd.DataFrame(data, columns=['药品ID', '药品名称', '批准文号', '供应商ID', '药品类型', '库存地址', '保质期', '售价', '库存数量', '主要成分', '储存方式', '适用症状'])
    elif selected_table == '医生信息':
        df = pd.DataFrame(data, columns=['医生ID', '医生姓名', '科室', '联系方式'])
    elif selected_table == '处方信息':
        df = pd.DataFrame(data, columns=['处方ID', '开具日期', '医生ID', '患者ID'])
    dataframe_to_treeview(tree, df)

# 查询管理员信息
def get_admin_info(admin_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM 账号密码管理员 WHERE 管理员账号 = %s", (admin_id,))
            result = cursor.fetchone()
            return result
    except Exception as e:
        messagebox.showerror("查询错误", str(e))
        return None

def delete_patient_to_db(patient_id, dp):
    if not patient_id:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM 患者 WHERE 患者ID = %s",
        (patient_id))
    conn.commit()
    messagebox.showinfo("成功", "删除成功。")

    dp.destroy()
def delete_patient():
    dp = tk.Tk()
    dp.geometry('500x280')
    dp.title("Medicine Management System: Delete patient information")
    frame = tk.LabelFrame(dp)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    patient_id_label = tk.Label(frame, text="请输入患者ID")
    patient_id_label.grid(row=0, column=0, sticky="w")
    patient_id_entry = tk.Entry(frame)
    patient_id_entry.grid(row=0, column=1, sticky="w")

    # 创建提交按钮
    submit_button = tk.Button(frame, text="   提交   ", command=lambda: delete_patient_to_db(
        patient_id_entry.get(),
        dp
    ))
    submit_button.grid(row=2, column=1, sticky="w")

    dp.mainloop()

# 添加医生信息
def add_doctor_to_db(doctor_id, name, department, contact, password, password_again, ad):
    if not doctor_id or not name or not department or not contact:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return
    if password != password_again:
        messagebox.showerror("错误", "两次输入密码不符，请重新填写。")
        return

    cursor2 = conn.cursor(cursor=pymysql.cursors.Cursor)
    sql = "SELECT 医生ID FROM 医生 WHERE 医生ID = %s"
    cursor2.execute(sql, (doctor_id))
    result = cursor2.fetchone()
    if result:
        messagebox.showerror("错误", "医生ID已存在，请使用其他ID。")
        return

    cursor = conn.cursor()
    cursor.execute("INSERT INTO 医生 (医生ID, 医生姓名, 科室, 联系方式) VALUES (%s, %s, %s, %s)",
                   (doctor_id, name, department, contact))
    conn.commit()
    cursor.execute("INSERT INTO 账号密码医生 (医生账号, 医生密码) VALUES (%s, %s)",
                   (doctor_id, password))
    conn.commit()
    messagebox.showinfo("成功", "医生信息已添加")
    ad.destroy()

def add_doctor():
    ad = tk.Tk()
    ad.geometry('500x280')
    ad.title("Medicine Management System: Add doctor")
    frame = tk.LabelFrame(ad)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    # 医生信息
    doctor_id_label = tk.Label(frame, text="医生ID")
    doctor_id_label.grid(row=0, column=0, sticky="w")
    doctor_id_entry = tk.Entry(frame)
    doctor_id_entry.grid(row=0, column=1, sticky="w")

    name_label = tk.Label(frame, text="医生姓名")
    name_label.grid(row=1, column=0, sticky="w")
    name_entry = tk.Entry(frame)
    name_entry.grid(row=1, column=1, sticky="w")

    department_label = tk.Label(frame, text="科室")
    department_label.grid(row=2, column=0, sticky="w")
    department_entry = tk.Entry(frame)
    department_entry.grid(row=2, column=1, sticky="w")

    contact_label = tk.Label(frame, text="联系方式")
    contact_label.grid(row=3, column=0, sticky="w")
    contact_entry = tk.Entry(frame)
    contact_entry.grid(row=3, column=1, sticky="w")

    password_label = tk.Label(frame, text="密码")
    password_label.grid(row=4, column=0, sticky="w")
    password_entry = tk.Entry(frame)
    password_entry.grid(row=4, column=1, sticky="w")

    password_again_label = tk.Label(frame, text="确认密码")
    password_again_label.grid(row=5, column=0, sticky="w")
    password_again_entry = tk.Entry(frame)
    password_again_entry.grid(row=5, column=1, sticky="w")

    # 创建提交按钮
    submit_button = tk.Button(frame, text="   提交   ", command=lambda: add_doctor_to_db(
        doctor_id_entry.get(),
        name_entry.get(),
        department_entry.get(),
        contact_entry.get(),
        password_entry.get(),
        password_again_entry.get(),
        ad
    ))
    submit_button.grid(row=6, column=1, sticky="w")

    ad.mainloop()

# 修改供应商信息
def modify_provider_info_to_db(old_provider_id, new_provider_id, name, responsible_person, contact, mp):
    if not old_provider_id or not name or not new_provider_id or not responsible_person or not contact:
        messagebox.showerror("错误", "存在空值，请重新填写。")
        return

    cursor2 = conn.cursor(cursor=pymysql.cursors.Cursor)
    sql = "SELECT 供应商ID FROM 供应商 WHERE 供应商ID = %s"
    cursor2.execute(sql, (new_provider_id))
    result1 = cursor2.fetchone()
    sql = "SELECT 供应商ID FROM 供应商 WHERE 供应商ID = %s"
    cursor2.execute(sql, (old_provider_id))
    result2 = cursor2.fetchone()

    if result2:
        if not result1 or old_provider_id == new_provider_id:
            cursor = conn.cursor()
            cursor.execute("UPDATE `供应商` SET `供应商名称` = %s WHERE `供应商ID` = %s",
                           (name, old_provider_id))
            conn.commit()

            cursor.execute("UPDATE `供应商` SET `负责人` = %s WHERE `供应商ID` = %s",
                           (responsible_person, old_provider_id))
            conn.commit()

            cursor.execute("UPDATE `供应商` SET `联系方式` = %s WHERE `供应商ID` = %s",
                           (contact, old_provider_id))
            conn.commit()

            cursor.execute("UPDATE `供应商` SET `供应商ID` = %s WHERE `供应商ID` = %s",
                           (new_provider_id, old_provider_id))
            conn.commit()

            messagebox.showinfo("成功", "修改成功。")
        else:
            messagebox.showerror("错误", "请检查供应商ID。")
    else:
        messagebox.showerror("错误", "请检查供应商ID。")

    mp.destroy()
    return

def modify_provider_info():
    mp = tk.Tk()
    mp.geometry('500x280')
    mp.title("Medicine Management System: Add doctor")
    frame = tk.LabelFrame(mp)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    # 医生信息
    old_provider_id_label = tk.Label(frame, text="请输入想要修改的原供应商ID")
    old_provider_id_label.grid(row=0, column=0, sticky="w")
    old_provider_id_entry = tk.Entry(frame)
    old_provider_id_entry.grid(row=0, column=1, sticky="w")

    label = tk.Label(frame, text="请修改信息：")
    label.grid(row=1, column=0, sticky="w")

    new_provider_id_label = tk.Label(frame, text="请输入想要修改的新供应商ID")
    new_provider_id_label.grid(row=2, column=0, sticky="w")
    new_provider_id_entry = tk.Entry(frame)
    new_provider_id_entry.grid(row=2, column=1, sticky="w")

    name_label = tk.Label(frame, text="供应商名称")
    name_label.grid(row=3, column=0, sticky="w")
    name_entry = tk.Entry(frame)
    name_entry.grid(row=3, column=1, sticky="w")

    responsible_person_label = tk.Label(frame, text="负责人")
    responsible_person_label.grid(row=4, column=0, sticky="w")
    responsible_person_entry = tk.Entry(frame)
    responsible_person_entry.grid(row=4, column=1, sticky="w")

    contact_label = tk.Label(frame, text="联系方式")
    contact_label.grid(row=5, column=0, sticky="w")
    contact_entry = tk.Entry(frame)
    contact_entry.grid(row=5, column=1, sticky="w")

    # 创建提交按钮
    submit_button = tk.Button(frame, text="   提交   ", command=lambda: modify_provider_info_to_db(
        old_provider_id_entry.get(),
        new_provider_id_entry.get(),
        name_entry.get(),
        responsible_person_entry.get(),
        contact_entry.get(),
        mp
    ))
    submit_button.grid(row=6, column=1, sticky="w")

    mp.mainloop()


# 患者主界面
def main_ui_patient(patient_id):
    patient_info = get_patient_info(patient_id)
    if not patient_info:
        messagebox.showerror("患者信息错误", "未找到患者信息")
        return
    mup = tk.Tk()
    mup.geometry('1080x720')
    mup.title("Medicine Management System: patient")
    basic_info_frame = tk.LabelFrame(mup, text="基本信息")
    basic_info_frame.place(x=10, y=10, width=1060, height=200)

    tk.Label(basic_info_frame, text=f"患者ID: {patient_info['患者ID']}").grid(row=0, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"患者姓名: {patient_info['患者姓名']}").grid(row=1, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"身份证号: {patient_info['身份证号']}").grid(row=2, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"年龄: {patient_info['年龄']}").grid(row=3, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"患者联系方式: {patient_info['患者联系方式']}").grid(row=4, column=0, sticky="w")
    modification_button = tk.Button(basic_info_frame, text="修改信息", command=lambda: modify_patient_info(patient_id))
    modification_button.grid(row=5, column=0, sticky="w")
    modification_password_button = tk.Button(basic_info_frame, text="修改密码", command=lambda: modify_patient_password(patient_id))
    modification_password_button.grid(row=5, column=1, sticky="w")
    # 选择框
    choose_info_frame = tk.LabelFrame(mup, text="操作")
    choose_info_frame.place(x=10, y=220, width=1060, height=490)

    global table_selector, tree, choose_pid
    choose_pid = patient_id
    table_selector = ttk.Combobox(choose_info_frame, values=['处方信息', '药物信息'])
    table_selector.place(x=10, y=0, width=150)
    table_selector.set('处方信息')
    load_button = tk.Button(choose_info_frame, text="加载数据", command=load_patient_data)
    load_button.place(x=170, y=0, width=150)
    # 创建Treeview表格
    columns = []
    tree = ttk.Treeview(choose_info_frame, show='headings', columns=columns)
    tree.place(x=10, y=50, width=1030, height=280)
    # 添加滚动条
    xbar = tk.Scrollbar(choose_info_frame, orient='horizontal', command=tree.xview)
    xbar.place(x=10, y=330, width=1030)
    ybar = tk.Scrollbar(choose_info_frame, orient='vertical', command=tree.yview)
    ybar.place(x=1030, y=50, height=280)
    tree.configure(xscrollcommand=xbar.set, yscrollcommand=ybar.set)
    # 初始加载患者表数据
    load_patient_data()

    mup.mainloop()

# 医生主界面
def main_ui_doctor(doctor_id):
    doctor_info = get_doctor_info(doctor_id)
    if not doctor_info:
        messagebox.showerror("医生信息错误", "未找到医生信息")
        return
    mud = tk.Tk()
    mud.geometry('1080x720')
    mud.title("Medicine Management System: doctor")
    # 基本信息框
    basic_info_frame = tk.LabelFrame(mud, text="基本信息")
    basic_info_frame.place(x=10, y=10, width=1060, height=200)
    # 医生基本信息
    tk.Label(basic_info_frame, text=f"医生ID: {doctor_info['医生ID']}").grid(row=0, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"医生姓名: {doctor_info['医生姓名']}").grid(row=1, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"科室: {doctor_info['科室']}").grid(row=2, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"联系方式: {doctor_info['联系方式']}").grid(row=3, column=0, sticky="w")
    # 选择框
    choose_info_frame = tk.LabelFrame(mud, text="操作")
    choose_info_frame.place(x=10, y=220, width=1060, height=490)
    # 选择操作
    tk.Button(choose_info_frame, text="开药", command=lambda: prescription(doctor_id)).place(x=330, y=0, width=150)
    tk.Button(choose_info_frame, text="添加患者信息", command=lambda: add_patient()).place(x=490, y=0, width=150)
    tk.Button(choose_info_frame, text="修改患者信息", command=lambda: d_modify_patient_info()).place(x=490, y=0, width=150)
    global table_selector, tree
    table_selector = ttk.Combobox(choose_info_frame, values=['患者信息', '药物信息'])
    table_selector.place(x=10, y=0, width=150)
    table_selector.set('患者信息')
    load_button = tk.Button(choose_info_frame, text="加载数据", command=load_table_data)
    load_button.place(x=170, y=0, width=150)
    # 创建Treeview表格
    columns = []
    tree = ttk.Treeview(choose_info_frame, show='headings', columns=columns)
    tree.place(x=10, y=50, width=1030, height=280)
    # 添加滚动条
    xbar = tk.Scrollbar(choose_info_frame, orient='horizontal', command=tree.xview)
    xbar.place(x=10, y=330, width=1030)
    ybar = tk.Scrollbar(choose_info_frame, orient='vertical', command=tree.yview)
    ybar.place(x=1030, y=50, height=280)
    tree.configure(xscrollcommand=xbar.set, yscrollcommand=ybar.set)
    # 初始加载患者表数据
    load_table_data()

    mud.mainloop()

# 管理员主界面
def main_ui_admin(admin_id):
    admin_info = get_admin_info(admin_id)
    if not admin_info:
        messagebox.showerror("管理员信息错误", "未找到管理员信息")
        return
    mua = tk.Tk()
    mua.geometry('1080x720')
    mua.title("Medicine Management System: admin")
    basic_info_frame = tk.LabelFrame(mua, text="基本信息")
    basic_info_frame.place(x=10, y=10, width=1060, height=100)

    tk.Label(basic_info_frame, text=f"管理员ID: {admin_info['管理员账号']}").grid(row=0, column=0, sticky="w")
    tk.Label(basic_info_frame, text=f"管理员姓名: {admin_info['管理员姓名']}").grid(row=1, column=0, sticky="w")
    # 选择框
    choose_info_frame = tk.LabelFrame(mua, text="操作")
    choose_info_frame.place(x=10, y=120, width=1060, height=590)
    # 选择操作
    tk.Button(choose_info_frame, text="添加患者信息", command=lambda: add_patient()).place(x=10, y=0, width=150)
    tk.Button(choose_info_frame, text="修改患者信息", command=lambda: d_modify_patient_info()).place(x=170, y=0, width=150)
    tk.Button(choose_info_frame, text="删除患者信息", command=lambda: delete_patient()).place(x=330, y=0, width=150)
    tk.Button(choose_info_frame, text="添加医生信息", command=lambda: add_doctor()).place(x=490, y=0, width=150)
    tk.Button(choose_info_frame, text="修改医生信息", command=lambda: waiting()).place(x=650, y=0, width=150)
    tk.Button(choose_info_frame, text="删除医生信息", command=lambda: waiting()).place(x=810, y=0, width=150)
    tk.Button(choose_info_frame, text="修改供应商信息", command=lambda: modify_provider_info()).place(x=330, y=40, width=150)
    tk.Button(choose_info_frame, text="添加药物信息", command=lambda: waiting()).place(x=490, y=40, width=150)
    tk.Button(choose_info_frame, text="修改药物信息", command=lambda: waiting()).place(x=650, y=40, width=150)
    tk.Button(choose_info_frame, text="删除药物信息", command=lambda: waiting()).place(x=810, y=40, width=150)

    global table_selector, tree
    table_selector = ttk.Combobox(choose_info_frame, values=['患者信息', '医生信息', '药物信息'])
    table_selector.place(x=10, y=40, width=150)
    table_selector.set('患者信息')
    load_button = tk.Button(choose_info_frame, text="加载数据", command=load_table_data)
    load_button.place(x=170, y=40, width=150)
    # 创建Treeview表格
    columns = []
    tree = ttk.Treeview(choose_info_frame, show='headings', columns=columns)
    tree.place(x=10, y=90, width=1030, height=280)
    # 添加滚动条
    xbar = tk.Scrollbar(choose_info_frame, orient='horizontal', command=tree.xview)
    xbar.place(x=10, y=370, width=1030)
    ybar = tk.Scrollbar(choose_info_frame, orient='vertical', command=tree.yview)
    ybar.place(x=1030, y=90, height=280)
    tree.configure(xscrollcommand=xbar.set, yscrollcommand=ybar.set)
    # 初始加载患者表数据
    load_table_data()

# 主函数
if __name__ == '__main__':
    conn = init_db()
    log_ui()
    conn.close()