# ============================================
# Day 2 · Step 3：词频统计升级版 —— Top 10
#
# 今天三个新东西（我都写好了，你读注释理解）：
#   1. lower()   把大写统一成小写
#   2. items()   把本子拆成一排「(词, 次数)」对
#   3. sorted()  排序，按次数从多到少
#
# 复习的部分（切词 / 计数 / 打印）留给你自己写 —— 别照抄 step2.py
# ===============================================

# ---- 读文件（昨天学的）----
# 注意：这里做了个改动，让它不管从哪个目录运行都能找到文件
#
# __file__ = Python 自动建的变量，存着"这个脚本自己放在哪"
#            （前后各两个下划线，叫 dunder = double underscore 双下划线）
# os       = operating system 操作系统；os.path 专门管路径
# abspath  = absolute path 绝对路径（从盘符写全）
# dirname  = directory name 目录名，也就是去掉文件名、只留文件夹
# join     = 拼接，把文件夹和文件名拼成完整路径
import os
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, "sample_long.txt")

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

print(f"文件一共读进来 {len(text)} 个字符")


# ---- TODO 1：把 text 切成单词（复习，自己写）----
# 提示：split 是方法，要带 ()；结果要用 = 接住
# 变量名建议用复数 words，因为是一排东西
# ⚠️ 不许翻 step2.py —— 昨天刚复现过，先自己想
words =text.split()


print(f"一共切出 {len(words)} 个单词")


# ---- 今天新东西 1：统一小写 ----
# 问题：Python 和 python 会被算成两个不同的词
# lower = 降低、变小写（low「低的」的比较级 → 更低的）
# 它是**字符串的方法**，所以写法是：字符串.lower()
# 结果要用 = 接住（动作的结果！）
#
# 下面这行叫「列表推导式」list comprehension
#   comprehension = 理解、领悟 → 把一排东西挨个过一遍，生成新的一排
#   结构：[对每个东西做什么   for 每个东西 in 原来那排]
# 展开写就是：
#   new = []
#   for w in words:
#       new.append(w.lower())
#   words = new
words = [w.lower().strip(".?!,") for w in words]


# ---- TODO 2：统计词频（复习，自己写）----
# 提示一：空本子用 {} 不是 []（[] 是列表，{} 才是字典）
# 提示二：counts.get(w, 0) —— 查得到给真的，查不到给 0
# 提示三：for 后面有冒号，循环体要缩进
# ⚠️ 不许翻 step2.py —— 空本子用 {} 还是 []？昨天刚栽过
counts ={}
for w in words:
    counts[w]=counts.get(w,0)+1


print(f"一共有 {len(counts)} 个不同的单词")


# ---- 今天新东西 2：把本子拆成一排对子 ----
# items = 项目、条目（item 的复数）
# counts.items() 会把 {'python': 5, 'data': 3}
# 变成 [('python', 5), ('data', 3)]
#
# 为什么需要它：字典是"用钥匙查值"，**没有顺序**，没法直接排序
# 拆成一排对子之后，就能交给 sorted 排了
pairs = counts.items()


# ---- 今天新东西 3：排序 ----
# sorted = 排好序的（来自动词 sort，整理、分类）
# 三个参数（parameter 参数）：
#   sorted( 要排的东西 , key = 按什么排 , reverse = 是否反转 )
#   · key     = 钥匙 → 这里指"按哪一列排"
#   · reverse = 反转；True 表示从大到小（默认 False，从小到大）
#
# lambda = 一行没有名字的小函数（anonymous = 匿名的）
#   lambda p: p[1]  翻译："给我一个 p，我还给你 p 的第 2 项"
#   p[0] 是词，p[1] 是次数
sorted_pairs = sorted(pairs, key=lambda p:len(p[0]), reverse=True)


# ---- TODO 3：打印前 10 名（自己写）----
# 提示一：取前 10 个用切片 sorted_pairs[0:10]（方括号！）
# 提示二：对子可以拆开接收 —— for w, c in ...
#         这样 w 拿到词，c 拿到次数
print("\n出现次数最多的 10 个词：")
for w,c in sorted_pairs[0:10]:

    print(f"{w}: {c}")


# ============================================
# 验收：python step3.py
# 正确的话应该看到（数字必须完全一致）：
#   文件一共读进来 1123 个字符
#   一共切出 226 个单词
#   一共有 96 个不同的单词
#
#   出现次数最多的 10 个词：
#   you: 16
#   a: 14
#   to: 14
#   is: 11
#   code: 11
#   write: 9
#   can: 9
#   and: 8
#   python: 6
#   need: 5
# ============================================

# ---- 选做挑战（做完上面的再来）----
# 1. 现在 "code," 和 "code" 还是两个词（逗号粘在后面）
#    提示：字符串还有个方法叫 strip()，把两头的东西削掉
#          strip = 剥去、削掉。w.strip(".,!?") 削掉两头的 . , ! ?
#          想想该加在哪一行？
#
# 2. 打印出最长的 5 个词（不是出现最多的）
#    提示：key=lambda p: len(p[0])
#
# 3. 给排名加上序号 1. 2. 3.
#    提示：用 enumerate()，enumerate = 枚举、编号
#          for i, (w, c) in enumerate(sorted_pairs[0:10], start=1):
#              print(f"{i}. {w}: {c}")
for i,(w,c) in enumerate(sorted_pairs[0:10],start=1):
    print(f"{i},{w},{c}")