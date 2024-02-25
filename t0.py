import sys
import PySide6.QtWidgets as Qw

# PySide6.QtWidgets.MainWindow を継承した MainWindow クラスの定義
class MainWindow(Qw.QMainWindow):
  
  # コンストラクタ(初期化)
  def __init__(self):

    # 親クラスのコンストラクタの呼び出し
    super().__init__() 

    # ウィンドウタイトル設定
    self.setWindowTitle('MainWindow') 

    # ウィンドウのサイズ(640x240)と位置(X=100,Y=50)の設定
    self.setGeometry(100, 50, 640, 240) 

    #「実行」ボタンの生成と設定
    self.btn_run = Qw.QPushButton('実行',self)
    self.btn_run.setGeometry(10,10,100,20)

    #「クリア」ボタンの生成と設定
    self.btn_clear = Qw.QPushButton('クリア',self)
    self.btn_clear.setGeometry(120,10,100,20)

    # テキストボックス
    self.tb_log = Qw.QTextEdit('',self)
    self.tb_log.setGeometry(10,40,620,170)
    self.tb_log.setPlaceholderText('(ここに実行ログを表示します)')

    # ステータスバー
    self.sb_status = Qw.QStatusBar()
    self.setStatusBar(self.sb_status)
    self.sb_status.setSizeGripEnabled(False)
    self.sb_status.showMessage('プログラムを起動しました。')

# 本体
if __name__ == '__main__':
  app = Qw.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.show()
  sys.exit(app.exec())