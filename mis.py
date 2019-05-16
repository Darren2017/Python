class Bill:
    def __init__(self, id, name, part, ele, res):
        self.id = id
        self.name = name
        self.part = part
        self.ele = ele
        self.res = res


class GZKK:
    def __init__(self):
        self.count = 0
        self.bills = []

    def append(self, bill):
        self.bills.append(bill)

    def search(self, id):
        for i, value in  enumerate(self.bills):
            print(i)
            if value.id == id:
                return i
        return -1

def func(gzzk):
    id = input("请输入人员代码：(输入-1结束)")
    id = int(id)
    if id == -1:
        return
    re = gzkk.search(id)
    if re != -1:
        print("请输入扣款项目 1.扣电费  2.病事假条款")
        choose = input()
        choose = int(choose)
        if choose == 1:
            print("请输入扣款金额:")
            mon = input()
            mon = int(mon) 
            gzkk.bills[re].ele += mon
        elif choose == 2:
            print("请输入扣款金额:")
            mon = input()
            mon = int(mon) 
            gzkk.bills[re].res += mon
        else:
            print("选择有误")
    else:
        print("查无此人")
    func(gzzk)

if __name__ == '__main__':
    gzkk = GZKK()
    gzkk.append(Bill(1003, "刘一波", 1, 20.00, 12.00))
    gzkk.append(Bill(1008, "赵子英", 2, 20.00, 60.00))

    func(gzkk)