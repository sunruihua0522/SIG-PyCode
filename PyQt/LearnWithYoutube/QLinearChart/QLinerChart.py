from PyQt5.QtChart import QChart, QLineSeries, QChartView
from PyQt5.QtWidgets import QMainWindow,QVBoxLayout,QWidget,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor

import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.InitGui()
        self.show()

    def InitGui(self):
        self.setWindowTitle("Line Chart")
        self.setGeometry(100,200,800,600)

        series = QLineSeries()
        series.setColor(QColor('red'))

        seriesA = QLineSeries()
        seriesA.setColor(QColor('green'))



        for i in range(1,20):
            series.append(10*i,20+i*i*8-3*i)
            seriesA.append(10*i, 6-i*i*2+5*i)


        chart = QChart()
        chart.addSeries(series)
        chart.addSeries(seriesA)
        chart.setAnimationOptions(chart.SeriesAnimations)
        chart.setAnimationDuration(1000)
        chart.setTitle("Line Chart")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)



        view = QChartView(chart)
        view.setRenderHint(QPainter.Antialiasing)




        vbox = QVBoxLayout()
        vbox.addWidget(view)
        root = QWidget()
        root.setLayout(vbox)

        self.setCentralWidget(root)
        pass

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(App.exec())



