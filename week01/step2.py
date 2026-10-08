# ============================================
# Day 1 · Step 2：真正的词频统计 CLI
#
# 和 Step 1 的区别只有一处：
#   文本来源从「用户敲键盘」改成「读文件」
# 下面三步（切词 → 计数 → 打印）你已经会了
# ============================================

# ---- 今天唯一的新东西：读文件 ----
# open     = 打开
# "r"      = read，读模式
# encoding = 编码，utf-8 才能读中文
# with     = 带着，用完自动把文件关上
# as f     = 给打开的文件起个名字叫 f
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(f"文件一共读进来 {len(text)} 个字符")


# ---- TODO 1：把 text 切成单词列表 ----
# 提示：和 Step 1 一模一样，只是变量从 sentence 换成 text
# 注意：split 是方法，要带 ()
word=text.split()



# ---- TODO 2：统计每个词出现几次，存进 counts ----
# 提示：先准备空本子，再 for 循环（记得冒号），算完写回本子
counts={}
for w in word:
    counts[w]=counts.get(w,0)+1


# ---- TODO 3：把统计结果打印出来 ----
print(counts)


# ============================================
# 验收：python step2.py
# 应该看到 counts 里 python 是 3，love 是 2
# ============================================

# ---- 选做挑战（做完上面的再来）----
# 让结果按次数从多到少排列：
#   items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
#   for w, c in items:
#       print(f"{w}: {c}")
# sorted  = 排序（sort 的过去式，排好的）
# reverse = 反转
# lambda  = 一行小函数
