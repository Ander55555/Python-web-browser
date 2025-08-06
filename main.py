import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget
from browser_tab import BrowserTab
from navbar import NavBar

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Pro Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        self.navbar = NavBar(self)
        self.addToolBar(self.navbar)

        self.add_new_tab("https://www.google.com", "Home")

    def add_new_tab(self, url, label):
        tab = BrowserTab(url)
        tab.browser.urlChanged.connect(lambda q: self.navbar.update_url(q.toString()))
        i = self.tabs.addTab(tab, label)
        self.tabs.setCurrentIndex(i)

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def current_browser(self):
        return self.tabs.currentWidget().browser

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
