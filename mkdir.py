import os

def mkdir(path):
    folder = os.path.exists(path)

    if folder:
        os.remove(path)
        print("mkdir" + path)
    else:
        print("exist")

folders = ["如果是产品经理", "认识脸,不知道名字", "最难忘的一件事", "最想和谁上什么课", "最喜欢发什么表情包", "在团队的收获", "对团队的建议", "后悔加入团队和不后悔的理由", "最佳搭档", "想对张大大说的话", "新的一年对团队和自己的愿景", "总结自己的2018", "最想感谢的一个人", "除了现在的组想加入什么组", "有什么梦想", "为什么选择加入团队", "最想对新人说的一句话","最看好哪个学弟学妹","对导师的话和建议", "坚持留在团队的理由", "过生日想要什么生日礼物", "有压力会怎么办" ,"如何看待没了15寸MBP的张大大"]

for folder in folders:
    mkdir(folder)