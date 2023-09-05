#ver.2
import json
import time
import sys
import math
sleeptime = 0
class Subject:
    def __init__(self, name, time):
        self.name = name
        self.time = time
    def settime(self, t):
        self.time = t
    def output(self):
        print(self.name + "：" + str(self.time) + "h")
    def timer(self):
        input("エンターでタイマーを開始")
        timer_start = time.time()
        input("エンターでタイマーを停止")
        timer_end = time.time()
        span = math.floor((timer_end - timer_start) / 360) / 10
        while True:
            print(f"{span}h勉強しました。記録しますか？")
            input_line = input("はいorいいえ：")
            if input_line == "はい":
                self.time += span
                break
            elif input_line == "いいえ":
                break
            else:
                print("はいorいいえで答えてください")
    def self_addtime(self):
        study_time = 0
        while True:
            try:
                study_time = float(input("時間："))
            except ValueError:
                print("時間を整数または小数で入力してください")
                continue
            break
        print(f"記録：{self.name}を{study_time}時間学習")
        self.time += study_time
    def addtime(self):
        print("手動で記録するか、タイマーを使って記録することができます")
        operation = input("手動orタイマー：")
        while True:
            if operation == "手動":
                self.self_addtime()
                break
            elif operation == "タイマー":
                self.timer()
                break
            else:
                print("手動かタイマーで答えてください")
def studynote():
    try:
        f = open("json/data.json").read()
        subject_dic = json.loads(f)
        return subject_dic
    except Exception:
        print("ファイルエラー！")
        sys.exit()
def listsubject(subjects):
    print("保存された科目")
    view(subjects)
def addsubject(subjects):
    s = input("科目名：")
    subjects.append(Subject(s, 0))
def view(subjects):
    for e in subjects:
        e.output()
def save(subject_dic, subjects):
    d = {}
    for e in subjects:
        d[e.name] = e.time
    subject_dic["subject_data"] = d
    f = open( "json/data.json", "w")
    json.dump(subject_dic, f)
def delete(subjects):
    if len(subjects) == 1:
        print("消せません。一個以上のファイルが必要です")
        return subjects
    while True:
        operation = input("削除する科目：")
        if operation in [e.name for e in subjects]:
            id = [e.name for e in subjects].index(operation)
            del subjects[id]
            return subjects
        else:
            print("正しい科目を入力してください")
direction = """以下の操作が行えます。
科目名: 科目の勉強を開始
view: 学習時間を閲覧
add: 科目を追加
delete: 科目を削除
end: 終了
"""
subject_dic = studynote()
subjects = list()
for s, t in subject_dic["subject_data"].items():
    subjects.append(Subject(s, t))
while True:
    listsubject(subjects)
    print("----------------------")
    time.sleep(sleeptime)
    print(direction)
    operation = input("操作:")
    if operation in [e.name for e in subjects]:
        id = [e.name for e in subjects].index(operation)
        subjects[id].addtime()
        save(subject_dic, subjects)
    elif operation == "end":
        break
    elif operation == "add":
        addsubject(subjects)
        save(subject_dic, subjects)
    elif operation == "delete":
        subjects = delete(subjects)
        save(subject_dic, subjects)
    elif operation == "view":
        view(subjects)
    else:
        print("正しい操作を入力してください")
    print("----------------------")