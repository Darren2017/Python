#coding=utf-8

from dbfpy import dbf
import dbfread

header = [["DM", "C", 4], ["Name", "C", 10], ["DF", "N", 7.2], ["BSJ", "N", 7.2]]
content = [["1003", "刘一波", 20.00, 12.00], ["1008", "赵子英", 20.00, 60.00]]
filename = "/Users/darren/Desktop/test.dbf"

def writeDbfFile(filename, header, content):
    db = dbf.Dbf(filename, new=True)
    for field in header:
        if type(field) == unicode:
            field[0] = field[0].encode('GBK')
        db.addField((field[0], field[1], field[2]))
    for record in content:
        rec = db.newRecord()
        for key, value in zip(header, record):
            if type(value) == unicode:
                value.encode('GBK')
                rec[key[0]] = value
            else:
                rec[key[0]] = value
            rec.store()
    db.close()

def search(id):
    table = dbfread.DBF(filename, encoding='UTF-8')
    for record in table:
        if record["DM"] == id:
            print(record['NAME'])
            return(str(id))
    return None

def editDF(id, num):
    table = dbfread.DBF(filename, encoding='UTF-8')
    for record in table:
        if record["DM"] == id:
            record['DF'] += num

def editBSJ(id, num):
    table = dbfread.DBF(filename, encoding='UTF-8')
    for record in table:
        if record["DM"] == id:
            record['BSJ'] += num

def func():
    id = input("请输入人员代码：(输入-1结束)")
    id = str(id)
    if id == "-1":
        return
    re = search(id)
    if re is not None:
        print("请输入扣款项目 1.扣电费  2.病事假条款")
        choose = input()
        choose = int(choose)
        if choose == 1:
            print("请输入扣款金额:")
            mon = input()
            mon = int(mon) 
            editDF(re[1], mon)
        elif choose == 2:
            print("请输入扣款金额:")
            mon = input()
            mon = int(mon) 
            editBSJ(re[1], mon)
        else:
            print("选择有误")
    else:
        print("查无此人")
    func()

if __name__ == '__main__':
    print("输入扣款文件GZKK.DBF, 使用默认文件输入1")
    ch = input()
    if ch != 1:
        filename = ch
    writeDbfFile(filename, header, content)
    func()