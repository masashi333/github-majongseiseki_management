#!/usr/bin/env python
# coding=utf-8

# 標準ライブラリをインポート
from datetime import datetime
from pickle import dump, load

# GUIライブラリをインポート
from Tkinter import *
import tkMessageBox



#OSをインポート
import os

#モジュール属性argvを取得するため
import sys

#コマンドライン引数を格納したリストの取得
argvs = sys.argv

#表をつくるためのクラスをインポート
import tktable

#文字置換を行うため
import re
#二次元配列を実現
from numpy import *

#全てのファイルを読み込むためのクラスをインポート
import glob

"""#文字化けしないようにするためのインポート
import sys
import codecs
enc = 'utf-8'
sys.stdin = codecs.getreader(enc)(sys.stdin)
sys.stdout = codecs.getwriter(enc)(sys.stdout)
sys.stderr = codecs.getwriter(enc)(sys.stdout)"""

# データ保存用ファイル名
DUMPFILE = argvs[1]


sub_win = None
class MajongApp(Frame):
    """
    Majong GUIアプリ用のクラス
    """
    def __init__(self, master=None):
        """
        初期化メソッド - ウィジェットやToDoのデータを初期化
        """
        Frame.__init__(self, master, padx=8, pady=4)
        self.pack()
        self.createwidgets()        # ウィジェットを作る
        t = self.winfo_toplevel()
        """t.resizable(False, False)   # Windowをサイズ変更できなくする"""
        self.load()                 # データをロードする

    def run_cmd():
        print var.get()

    def createwidgets(self):
        """
        ボタンなどウインドウの部品を作る
        """
        # スクロールバーつきListboxを作る
        self.frame1 = Frame(self)
        frame = self.frame1


        #タイトルラベル
        titleLabel = Label(frame, text = u"麻雀成績表",font=(u'ＭＳ ゴシック',18))
        titleLabel.grid(row = 0, column = 1, padx = 0, pady = 0)
        #テーブルを作る
        label = Label(frame, text="名前",font=(u'ＭＳ ゴシック',14))
        label.grid(row=1,column=1)
        tenbousyuushi_label = Label(frame, text="点棒収支",font=(u'ＭＳ ゴシック',14))
        tenbousyuushi_label.grid(row=2,column=0)

        self.tableVar = tktable.ArrayVar(frame)
        # we set initial table value
        """for x in range(0, 10):
            for y in range(0, 10):
                index = "%i,%i" % (y, x) # note that (row,col)
                self.tableVar.set(index,"1")"""
        table = tktable.Table(frame,resizeborders='none',titlecols=1,rows=20,cols=10,rowheight=2,maxheight=300,colwidth=15,maxwidth=2000,variable=self.tableVar)
        table.grid(row=2,column=1,sticky=NS)
        #スクロール機能を付ける
        self.yscroll = Scrollbar(frame, orient=VERTICAL)
        self.yscroll.grid(row=2, column=2, sticky=NS)
        self.yscroll.config(command=table.yview())
        table.config(yscrollcommand=self.yscroll.set)

        """self.table.bind("<ButtonRelease-1>", self.selectitem)"""
        self.frame1.grid(row=0, column=0)
        buttom_frame = Frame(self)
        #レート入力項目を作る
        rateLabel = Label(buttom_frame,text=u"レート",font=(u'ＭＳ ゴシック',18))
        rateLabel.grid(row=0,column=1)
        self.rateEntry = Entry(buttom_frame,justify=LEFT, width=20)
        self.rateEntry.grid(row=0,column=2,columnspan=2)
        quit_button = Button(buttom_frame, text="終了", command=sys.exit)
        quit_button.grid(row=1,column=0,padx=30)
        hozon_button = Button(buttom_frame,text="保存",command=self.hozon)
        hozon_button.grid(row=1,column=1,padx=30)
        update_button = Button(buttom_frame,text="更新",command=self.update)
        update_button.grid(row=1,column=2,padx=30)
        seiseki_button = Button(buttom_frame,text="成績表示",command=self.seisekihyouzi)
        seiseki_button.grid(row=1,column=3,padx=30)
        seisekisyuukei_button = Button(buttom_frame,text="成績総合計",command=self.seisekisyuukei)
        seisekisyuukei_button.grid(row=1,column=4,padx=30)
        buttom_frame.grid(row=1,column=0)



        """self.listbox = Listbox(frame, height=10, width=60,selectmode=SINGLE, takefocus=1)
        self.yscroll = Scrollbar(frame, orient=VERTICAL)"""
        # 成績表示画面を作る
        """self.seisekibox = Listbox(self,height=3,width=60,selectmode=SINGLE,takefocus=1)"""
        """title_name = argvs[1]
        title_name = title_name.replace('.dat','')
        #タイトルラベルを作る
        self.title_l =Label(frame,text="%s",%title_name)"""

        # 配置を決める
        """self.listbox.grid(row=0, column=0, sticky=NS)
        self.yscroll.grid(row=0, column=1, sticky=NS)"""
        """self.seisekibox.grid(row=1,column=0,sticky=NS,padx=8,pady=20)"""
        """self.listbox.grid_columnconfigure(0, weight = 1)
        self.seisekibox.grid_columnconfigure(1, weight = 1)
        self.title_l.grid(row=-1,column=0)"""

        # 動きとコードをつなげる
        """self.yscroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.yscroll.set)
        self.listbox.bind("<ButtonRelease-1>", self.selectitem)"""

        """self.frame1.grid(row=0, column=0)"""

        # 予定編集エリア，ボタンを作る
        """self.frame2 = Frame(self)
        frame = self.frame2
        self.tyakujyun_l = Label(frame, text="着順")
        self.tenbousyuushi_l = Label(frame, text="点棒収支")
        self.date_l = Label(frame, text="日付")
        self.rate_l = Label(frame,text="レート")
        self.Rating1_l = Label(frame,text="Rating1")
        self.Rating2_l = Label(frame,text="Rating2")
        self.tyakujyun_e = Entry(frame, justify=LEFT, width=20)
        self.tenbousyuushi_e = Entry(frame, justify=LEFT, width=20)
        self.date_e = Entry(frame, justify=LEFT, width=20)
        self.rate_e = Entry(frame,justify=LEFT,width=20)
        self.Rating1_e = Entry(frame,justify=LEFT,width=10)
        self.Rating2_e = Entry(frame,justify=LEFT,width=10)
        self.finished_v = IntVar()"""
        """self.finished_c = Checkbutton(frame, justify=LEFT, text=u"終了",
                                      variable=self.finished_v)"""
        """self.update_button = Button(frame, text=u"更新", state=DISABLED,
                                    command=self.updateitem)
        self.delete_button = Button(frame, text=u"削除", state=DISABLED,
                                    command=self.deleteitem)
        self.new_button = Button(frame, text=u"新規",
                                 command=self.createitem)
        self.save_button = Button(frame,text=u"保存",command=self.hozon)


        # 配置を決める
        self.tyakujyun_l.grid(row=0, column=0, columnspan=2)
        self.tyakujyun_e.grid(row=1, column=0, columnspan=2)
        self.tenbousyuushi_l.grid(row=2, column=0, columnspan=2)
        self.tenbousyuushi_e.grid(row=3, column=0, columnspan=2)
        self.date_l.grid(row=4, column=0, columnspan=2)
        self.date_e.grid(row=5, column=0, columnspan=2)
        self.rate_l.grid(row=6,column=0,columnspan=2)
        self.rate_e.grid(row=7,column=0,columnspan=2)"""
        """self.finished_c.grid(row=6, column=0, columnspan=2)"""
        """self.Rating1_l.grid(row=8,column=0)
        self.Rating2_l.grid(row=8,column=1)
        self.Rating1_e.grid(row=9,column=0)
        self.Rating2_e.grid(row=9,column=1)
        self.update_button.grid(row=10, column=0)
        self.delete_button.grid(row=10, column=1)
        self.new_button.grid(row=11, column=0)
        self.save_button.grid(row=11, column=1)

        self.frame2.grid(row=0, column=1)"""
    def seisekihyouzi(self):
        """
        麻雀の成績を表示する
        """
        global sub_win
        if sub_win is None or not sub_win.winfo_exists():
            sub_win = Toplevel()
            sub_win.geometry("900x500")
            sub_win.title("成績表示画面")
            self.seisekibox = Listbox(sub_win,height=20,width=100,selectmode=SINGLE,takefocus=1)
            self.seisekibox.grid(row=0,column=0,sticky=NS,padx=8,pady=20)
            """tenbousyuushi_sum = [0 for x in range(0,10)]
            name = ["" for y in range(0,10)]"""
            self.seisekilist=[]
            for i in range(1,10):
                if self.majong[0][i]=="":
                    break
                first = 0
                second = 0
                third = 0
                sikoukaisuu = 0
                jyuni_avarage = 0
                jyuni_sum = 0
                first_propability = 0
                second_propability = 0
                third_propability = 0
                tenbousyuushi_avarage = 0
                katigaku = 0
                myRating = 1500
                name = self.majong[0][i]
                tenbousyuushi_sum = 0
                for j in range(1,20):
                    if self.majong[j][i]!=0:
                        sikoukaisuu += 1
                    tenbousyuushi_sum += int(self.majong[j][i])
                    tyakujyunlist = ["" for x in range(0,3)]
                    for k in range(1,10):
                        if self.majong[j][k] != 0:
                            tyakujyunlist.append(int(self.majong[j][k]))
                            tyakujyunlist.sort()
                    if int(self.majong[j][i])==tyakujyunlist[2]:
                            first += 1
                            jyuni_sum += 1
                    elif int(self.majong[j][i])==tyakujyunlist[1]:
                            second += 1
                            jyuni_sum += 2
                    elif int(self.majong[j][i])==tyakujyunlist[0]:
                            third += 1
                            jyuni_sum += 3
                if sikoukaisuu == 0:
                    first_propability = 0
                    second_propability = 0
                    third_propability = 0
                    tenbousyuushi_avarage = 0
                    jyuni_avarage = 0
                else:
                    first_propability = first*1.0/sikoukaisuu
                    second_propability = second*1.0/sikoukaisuu
                    third_propability = third*1.0/sikoukaisuu
                    tenbousyuushi_avarage = tenbousyuushi_sum*1.0/sikoukaisuu
                    jyuni_avarage = jyuni_sum*1.0/sikoukaisuu
                first_propability =round(first_propability,2)
                second_propability = round(second_propability,2)
                third_propability = round(third_propability,2)
                tenbousyuushi_avarage = round(tenbousyuushi_avarage,2)
                jyuni_avarage = round(jyuni_avarage,2)
                if self.rateEntry.get()=="":
                    katigaku=0
                else:
                    katigaku = tenbousyuushi_sum * int(self.rateEntry.get()) * 10
                seiseki=["" for x in range(0,4)]
                seiseki[0] = ("名前:%s" %name)
                seiseki[1] = ("対局数:%d 順位 1位:%d 2位:%d 3位:%d" %(sikoukaisuu,first,second,third))
                seiseki[2]= ("順位率 1位:%3r 2位:%3r 3位:%3r 平均順位:%3r " %(first_propability,second_propability,third_propability,jyuni_avarage))
                seiseki[3]= ("平均収支:%3r 累計収支:%d 勝ち額:%d" %(tenbousyuushi_avarage,tenbousyuushi_sum,katigaku))
                self.seisekibox.insert(END,seiseki[0])
                self.seisekibox.insert(END,seiseki[1])
                self.seisekibox.insert(END,seiseki[2])
                self.seisekibox.insert(END,seiseki[3])
                self.seisekibox.insert(END,"")
                self.seisekilist.append("名前:%s" %name)
                self.seisekilist.append("対局数:%d 順位 1位:%d 2位:%d 3位:%d" %(sikoukaisuu,first,second,third))
                self.seisekilist.append("順位率 1位:%3r 2位:%3r 3位:%3r 平均順位:%3r " %(first_propability,second_propability,third_propability,jyuni_avarage))
                self.seisekilist.append("平均収支:%3r 累計収支:%d 勝ち額:%d" %(tenbousyuushi_avarage,tenbousyuushi_sum,katigaku))
            """for i in range(len(self.seisekilist)):  # lenでリストの要素数を求める, rangeにループ回数(回数分の要素のリストが戻り値), inはリストをとる
                print '%s' % (self.seisekilist[i]) # print文の末尾に「,」を付けると改行しない
                print '\n'"""
            title_name = argvs[1]
            title_name = title_name.replace('.dat','')
            seisekilist = title_name + "_seiseki.dat"
            f = open(seisekilist, 'w')
            dump(self.seisekilist, f)
            """for i in range(0,10):
                item[i] = "名前:%s 累計収支:%d" %(name[i],tenbousyuushi_sum[i])
            item[0] = ("麻雀成績　　　　　対局数:%d 　　　　平均順位:%3r　　　レート:%2r" %(sikoukaisuu,jyuni_avarage,myRating))
            item[1] = ("順位 1位:%3r 　　　2位:%3r 　　　3位:%3r" %(first_propability,second_propability,third_propability))
            item[2] = ("平均収支:%3r 　　　累計収支:%d 　　　勝ち額:%d" %(tenbousyuushi_avarage,tenbousyuushi_sum,katigaku))"""
            """for p in range(len(item)):
                self.seisekibox.insert(END,item[p])"""
    def seisekisyuukei(self):
        global sub_win
        if sub_win is None or not sub_win.winfo_exists():
            sub_win = Toplevel()
            sub_win.geometry("900x500")
            sub_win.title("成績総合計表示画面")
            self.seisekibox = Listbox(sub_win,height=20,width=100,selectmode=SINGLE,takefocus=1)
            self.seisekibox.grid(row=0,column=0,sticky=NS,padx=8,pady=20)
            d={}
            for file in glob.glob('*seiseki.dat'):
                f = open(file, 'r')
                self.seisekilist = load(f)
                """for i in range(len(self.seisekilist)):  # lenでリストの要素数を求める, rangeにループ回数(回数分の要素のリストが戻り値), inはリストをとる
                    print '%s' % (self.seisekilist[i]) # print文の末尾に「,」を付けると改行しない
                    print '\n'"""
                for i in range(len(self.seisekilist)):
                    name = re.search('名前:(.+)',self.seisekilist[i])
                    if name != None:
                        d.setdefault(str(name.group(1)),{})['sikoukaisuu']=0
                        d.setdefault(str(name.group(1)),{})['first']=0
                        d.setdefault(str(name.group(1)),{})['second']=0
                        d.setdefault(str(name.group(1)),{})['third']=0
                        d.setdefault(str(name.group(1)),{})['tenbousyuushi_sum']=0
            for file in glob.glob('*seiseki.dat'):
                f = open(file, 'r')
                self.seisekilist = load(f)
                for i in range(len(self.seisekilist)):
                    name = re.search('名前:(.+)',self.seisekilist[i])
                    if name != None:
                        sikoukaisuu = re.search('対局数:(.)',self.seisekilist[i+1])
                        first = re.search('1位:(.)',self.seisekilist[i+1])
                        second = re.search('2位:(.)',self.seisekilist[i+1])
                        third = re.search('3位:(.)',self.seisekilist[i+1])
                        tenbousyuushi_sum = re.search('累計収支:([-,0-9]+)',self.seisekilist[i+3])
                        sikoukaisuu_sum = int(sikoukaisuu.group(1)) + int(d[str(name.group(1))]['sikoukaisuu'])
                        first_sum = int(first.group(1)) + int(d[name.group(1)]['first'])
                        second_sum = int(second.group(1)) + int(d[name.group(1)]['second'])
                        third_sum = int(third.group(1)) + int(d[name.group(1)]['third'])
                        tenbousyuushi_sum_sum = int(tenbousyuushi_sum.group(1)) + int(d[name.group(1)]['tenbousyuushi_sum'])
                        d[name.group(1)]['sikoukaisuu']=sikoukaisuu_sum
                        d[name.group(1)]['first']=first_sum
                        d[name.group(1)]['second']=second_sum
                        d[name.group(1)]['third']=third_sum
                        d[name.group(1)]['tenbousyuushi_sum']=tenbousyuushi_sum_sum
            for name in d.keys(): # for/if文では文末のコロン「:」を忘れないように
                sikoukaisuu = d[name]['sikoukaisuu']
                first = d[name]['first']
                second = d[name]['second']
                third = d[name]['third']
                tenbousyuushi_sum = d[name]['tenbousyuushi_sum']
                if sikoukaisuu == 0:
                    first_propability = 0
                    second_propability = 0
                    third_propability = 0
                    tenbousyuushi_average = 0
                    jyuni_avarage = 0
                else:
                    first_propability = first*1.0/sikoukaisuu
                    second_propability = second*1.0/sikoukaisuu
                    third_propability = third*1.0/sikoukaisuu
                    tenbousyuushi_average = tenbousyuushi_sum*1.0/sikoukaisuu
                    jyuni_average = (first+second*2+third*3)*1.0/sikoukaisuu
                    first_propability =round(first_propability,2)
                    second_propability = round(second_propability,2)
                    third_propability = round(third_propability,2)
                    tenbousyuushi_average = round(tenbousyuushi_average,2)
                    jyuni_average = round(jyuni_average,2)
                if self.rateEntry.get()=="":
                    katigaku=0
                else:
                    katigaku = tenbousyuushi_sum * int(self.rateEntry.get()) * 10
                seiseki=["" for x in range(0,4)]
                seiseki[0] = ("名前:%s" %name)
                seiseki[1] = ("対局数:%d 順位 1位:%d 2位:%d 3位:%d" %(sikoukaisuu,first,second,third))
                seiseki[2]= ("順位率 1位:%3r 2位:%3r 3位:%3r 平均順位:%3r " %(first_propability,second_propability,third_propability,jyuni_average))
                seiseki[3]= ("平均収支:%3r 累計収支:%d 勝ち額:%d" %(tenbousyuushi_average,tenbousyuushi_sum,katigaku))
                self.seisekibox.insert(END,seiseki[0])
                self.seisekibox.insert(END,seiseki[1])
                self.seisekibox.insert(END,seiseki[2])
                self.seisekibox.insert(END,seiseki[3])
                self.seisekibox.insert(END,"")


    def hozon(self):
        """
        保存ボタンを押した時に指定の名前でファイルを保存
        """
        global sub_win
        if sub_win is None or not sub_win.winfo_exists():
            sub_win = Toplevel()
            sub_win.geometry("300x100")
            sub_win.title("保存ファイル名の指定")
            self.filename_l = Label(sub_win,text=u"保存ファイル名の指定")
            self.filename_e = Entry(sub_win,width=30)
            self.hozon_button = Button(sub_win,text=u"保存",command=self.rename)
            self.filename_l.grid(row=0, column=0,)
            self.filename_e.grid(row=1, column=0,)
            self.hozon_button.grid(row=3,column=0)
            self.save()


    def rename(self):
        f = open(DUMPFILE,'w')
        dump(self.majong,f)
        rename = self.filename_e.get()
        os.rename(DUMPFILE,rename)
        self.filename_e.delete(0,END)






    def load(self):
        """
        ToDoのデータをファイルから読み込む
        """
        try:
            f = open(DUMPFILE, 'r')
            self.majong = load(f)
        except IOError:
            self.majong = [['' for j in range(10)] for i in range(20)]
            for i in range(0,10):
                for j in range(1,20):
                    if i==0:
                        self.majong[j][0]=j
                    else:
                        self.majong[j][i]=0


    def save(self):
        """
        ToDoのデータをファイルに書き出す
        """
        f = open(DUMPFILE, 'w')
        dump(self.majong, f)



    def setlistitems(self):
        """
        配列を表に表示
        """
        for i in range(0,10):
            for j in range(0,20):
                index = "%i,%i" %(j,i)
                self.tableVar.set(index,self.majong[j][i])



    def refrectententries(self):
        """
        表に入力された要素を配列に反映
        """
        for i in range(0,10):
            for j in range(0,20):
                index = "%d,%d" %(j,i)
                self.majong[j][i]= self.tableVar.get(index)

    def update(self):
        """
        入力された要素を配列に反映して、表示する
        """
        self.refrectententries()
        self.setlistitems()
        self.save()




def main():
    """
    アプリケーションを動かす関数
    """
    root = Tk()
    title_name = argvs[1]
    title_name = title_name.replace('.dat','')
    root.title(u"麻雀成績管理アプリ %s " %title_name) #ウインドウにタイトルをつける
    app = MajongApp()         # ToDoAppインスタンスを作る
    app.setlistitems()      # Listboxの項目を揃える
    app.mainloop()          # アプリケーションの処理を開始する
    root.destroy()

if __name__ == '__main__':
    main()

