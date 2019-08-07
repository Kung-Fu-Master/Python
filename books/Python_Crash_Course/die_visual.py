from die import Die
import pygal
 
die = Die()
 
# 数据集合
results = []
count = 1
for roll_num in iter(lambda *args:die.roll(),None):
    results.append(roll_num)
    if count >= 1000:
        break
    count +=1
 
# 分析结果
frequencies= []
for value in range(1,die.num_sides+1):
    frequencie = results.count(value)
    frequencies.append(frequencie)
 
# 对结果进行可视化
hist = pygal.Bar()      # 生成实例
hist.title = 'Results of rolling one D6 1000 times'  # 标题
hist.x_labels = ['1','2','3','4','5','6']           # X轴数值坐标
hist.x_title = 'Result'                                 # X轴标题
hist.y_title = 'Frequency of Result'                # Y轴标题
 
hist.add('D6',frequencies)                             # 传入Y轴数据
hist.render_to_file('die_visual.svg')               # 文件生成路径，必须为svg格式文件

