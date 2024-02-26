import rotation  as r
import display as d

import math
import sys
import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# レイアウト設定用変数
sp_exp = Qw.QSizePolicy.Policy.Expanding

class MainWindow(Qw.QMainWindow):

    # コンストラクタ(初期化
    def __init__(self):

        super().__init__() 
        self.setWindowTitle('Dimens.io-Arowana') 
        self.rp = []

        rect = Qc.QRect()
        rect.setSize(Qc.QSize(640,160))
        rect.moveCenter(app.primaryScreen().availableGeometry().center())
        self.setGeometry(rect) 

        # メインレイアウトの設定
        central_widget = Qw.QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = Qw.QVBoxLayout(central_widget) # 垂直レイアウト

        # ボタン配置の水平レイアウトを作成します。
        button_layout = Qw.QHBoxLayout()
        button_layout.setAlignment(Qc.Qt.AlignmentFlag.AlignLeft) # 左寄せ
        main_layout.addLayout(button_layout) # メインレイアウトにボタンレイアウトを追加

        #「実行」ボタンの生成と設定
        self.btn_run = Qw.QPushButton('実行')
        self.btn_run.setSizePolicy(sp_exp,sp_exp)
        self.btn_run.setGeometry(320, 100, 320, 100)
        button_layout.addWidget(self.btn_run)

        self.btn_run.clicked.connect(self.btn_run_clicked) 

        # テキストボックス
        self.textbox = Qw.QTextEdit(self)
        self.textbox.setPlaceholderText("次元数n＿座標(n個の要素数スペース区切り)＿軸周りの回転(comb(n,2)の要素数スペース区切り)")
        self.textbox.setGeometry(0, 0, 640, 50)
        self.textbox.toPlainText()

        # ステータスバー
        self.sb_status = Qw.QStatusBar()
        self.setStatusBar(self.sb_status)
        self.sb_status.setSizeGripEnabled(False)
        self.sb_status.showMessage('')


        self.edit = Qw.QLineEdit("")
        self.button = Qw.QPushButton("出力")

        layout = Qw.QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)


    def btn_run_clicked(self):
        A = [float(i) for i in self.textbox.toPlainText().split()]
        # (2<=n<=12)
        n = int(A[0])

        # points n 初期座標
        ps = [[]]

        for i in range(len(ps)):
            while len(ps[i]) != n:
                dfc = n-len(ps[i])
                if dfc > 0:
                    ps[i].append(0)
                elif dfc < 0:
                    ps[i].pop()
                
        for a in range(n):
            ps[0][a] = A[1+a]
        # thetas comb(n,2) 初期回転角度
            

        ths = []

        while len(ths) != math.comb(n,2):
            dfc = math.comb(n,2)-len(ths)
            if dfc > 0:
                ths.append(0)
            elif dfc < 0:
                ths.pop()

        for b in range(math.comb(n,2)):
            ths[b] = A[n+b]


        # # phis comb(n,2) 軸回転角度
        # phs = []
        # # rotation variation comb(n,2) 回転速度
        # rv = []
        # # psi comb(n,2) 
        # pss = []

        # # lines 2 線入力
        # ls = []


        # rotation points position 回転後座標
        self.rp = []


        # # rotation points new 回転後座標(速度変化あり)
        # rn = []
        # # rotation points graphic 回転後座標(速度、軸変化あり)
        # rg = []








        # while len(phs) != math.comb(n,2):
        #     dfc = math.comb(n,2)-len(phs)
        #     if dfc > 0:
        #         phs.append(0)
        #     elif dfc < 0:
        #         phs.pop()

        # while len(rv) != math.comb(n,2):
        #     dfc = math.comb(n,2)-len(rv)
        #     if dfc > 0:
        #         rv.append(0)
        #     elif dfc < 0:
        #         rv.pop()

        # while len(pss) != math.comb(n,2):
        #     dfc = math.comb(n,2)-len(pss)
        #     if dfc > 0:
        #         pss.append(0)
        #     elif dfc < 0:
        #         pss.pop()

        # for m in range(math.comb(n,2)):
        #     pss[m] += rv[m]

        # for j in range(len(ls)):
        #     while len(ls[j]) != 2:
        #         dfc = 2-len(ls[j])
        #         if dfc > 0:
        #             ls[j].append(0)
        #         elif dfc < 0:
        #             ls[j].pop()


        while len(self.rp) != len(ps):
            dfc = len(ps)-len(self.rp)
            if dfc > 0:
                self.rp.append(0)
            elif dfc < 0:
                self.rp.pop()

        # while len(rn) != len(ps):
        #     dfc = len(ps)-len(rn)
        #     if dfc > 0:
        #         rn.append(0)
        #     elif dfc < 0:
        #         rn.pop()

        # while len(rg) != len(ps):
        #     dfc = len(ps)-len(rg)
        #     if dfc > 0:
        #         rg.append(0)
        #     elif dfc < 0:
        #         rg.pop()


        for k in range(len(ps)):
            self.rp[k] = r.rot(n,ps[k],ths)

        # for o in range(len(ps)):
        #     rn[o] = r.rot(n,ps[o],r.lisumnew(n,ths,phs))

        # for l in range(len(ps)):
        #     rg[l] = r.rot(n,ps[l],r.lisum(n,ths,phs,pss))

        # vr = r.lisum(n,ths,phs,pss) #最終角度



        # x_data = []
        # y_data = []


        # while len(x_data) != len(rg):
        #     dfc = len(rg)-len(x_data)
        #     if dfc > 0:
        #         x_data.append(0)
        #     elif dfc < 0:
        #         x_data.pop()

        # while len(y_data) != len(rg):
        #     dfc = len(rg)-len(y_data)
        #     if dfc > 0:
        #         y_data.append(0)
        #     elif dfc < 0:
        #         y_data.pop()


        # for n in range(len(rg)):
        #     x_data[n] = rg[n][0]
        #     y_data[n] = rg[n][1]



        


        # print(rg)
        # print(x_data)
        # print(y_data)


        msg = ''
        msg += (f"{self.rp[0][0],self.rp[0][1],self.rp[0][2]}")
        self.sb_status.showMessage(msg)


        d.main(self.rp)




if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())