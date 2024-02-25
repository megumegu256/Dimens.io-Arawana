import sys
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import rotation  as r


# PySide6にグラフを表示するためのクラス
class GraphCanvas(FigureCanvasQTAgg):

  # コンストラクタ
  def __init__(self, parent=None, width=5, height=4, dpi=100):
    # グラフの設定
    fig = Figure(figsize=(width, height), dpi=dpi) 
    self.axes = fig.add_subplot(1, 1, 1, projection='3d')
    super(GraphCanvas, self).__init__(fig)


  # データをグラフにプロットする関数
  def data_plot(self):
    # x, yのデータ
    x_data = [180,211,224,235,247,256,265,271,275,279,284,287,289]
    y_data = [357,337,329,322,315,311,305,301,298,295,293,293,290]
    z_data = [279,278,279,279,281,281,282,282,284,285,286,288,290]

    self.axes.scatter(x_data , y_data, z_data)  # 散布図作成

    self.axes.set_title("3d_test_title") # グラフタイトル
    self.axes.set_xlim(min(x_data)-10, max(x_data)+10) # x軸の最小値、最大値を設定
    self.axes.set_ylim(min(y_data)-10, max(y_data)+10) # y軸の最小値、最大値を設定
    self.axes.set_zlim(min(z_data)-10, max(z_data)+10) # z軸の最小値、最大値を設定
    self.axes.set_xlabel("x_data") # x軸の名前を設定
    self.axes.set_ylabel("y_data") # y軸の名前を設定
    self.axes.set_zlabel("z_data") # y軸の名前を設定

    # self.axes.axis("off") # これを設定するとグラフタイトル以外の軸線などが全てクリアされる


# PySide6のGUIのクラス
class MainWindow(QMainWindow):

  # コンストラクタ
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    self.setWindowTitle("PySide6 GUI")

    # matplotlibのグラフのクラスオブジェクト
    graph_canvas = GraphCanvas(self, width=5, height=4, dpi=100)
    graph_canvas.data_plot() # データからグラフを作成

    # GUIレイアウト作成
    layout = QVBoxLayout()
    layout.addWidget(graph_canvas)
    toolbar = NavigationToolbar(graph_canvas, self) # matplotlibのツールバーを作成
    layout.addWidget(toolbar)                       # matplotlibのツールバー追加

    # GUI画面全体のレイアウトを作成
    widget = QWidget()
    widget.setLayout(layout)
    self.setCentralWidget(widget)


if __name__ == '__main__':
  # Qtアプリケーションの作成
  app = QApplication(sys.argv)

  # フォームを作成して表示
  form = MainWindow()
  form.show()

  # 画面表示のためのループ
  sys.exit(app.exec())