'''
Python3.8
PyCharm 2019.3.3 (Community Edition)
Build #PC-193.6494.30, built on February 6, 2020
Runtime version: 11.0.5+10-b520.38 amd64
VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
Windows 10 10.0
GC: ParNew, ConcurrentMarkSweep
Memory: 1459M
Cores: 8
Registry: 
Non-Bundled Plugins: com.kite.intellij
'''
# GUI：tkinter使用
# 小费计算
def resize(ev=None):
    '''改变label字体大小'''
    #label.config(font='Helvetica -%d bold' % scale.get())
    try:
        t=float(entry.get())
    except :
        label2.config(text='Wrong Value')
    else:
        label2.config(text='The fee is %.2f' % (t*(scale.get())/100))


top = tk.Tk()  # 实例化tkinter对象
top.geometry('400x200')  # 设置窗口大小
top.title('小费')  # 设置窗口标题

# # Label控件
# label = tk.Label(top, text='Hello World', font='Helvetica -12 bold', bg='yellow')
# label.pack(fill=tk.Y, expand=0)

# Label2控件
label2=tk.Label(top,text='')
label2.pack(side='bottom')


#Entry控件
entry=tk.Entry(top,bg='white')
entry.pack(side='right')

# scale滚动条，数值从5到20，水平滑动，命令是resize函数
scale = tk.Scale(top, from_=5, to=20, orient=tk.HORIZONTAL, command=resize)
scale.set(10)  # 设置初始值
scale.pack(fill=tk.X, expand=1)

# Button控件
# quit_btn = tk.Button(top, text='QUIT', command=top.quit,
#                      activeforeground='white', activebackground='red')
# quit_btn.pack()
#

#Button
button=tk.Button(top,text='Get the Fee!',command=resize)
button.pack()
tk.mainloop()
