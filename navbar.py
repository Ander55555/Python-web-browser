from PyQt5.QtWidgets import QToolBar, QAction, QLineEdit
from PyQt5.QtCore import QUrl

class NavBar(QToolBar):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.back_btn = QAction("←", self)
        self.back_btn.triggered.connect(lambda: self.parent.current_browser().back())
        self.addAction(self.back_btn)

        self.forward_btn = QAction("→", self)
        self.forward_btn.triggered.connect(lambda: self.parent.current_browser().forward())
        self.addAction(self.forward_btn)

        self.reload_btn = QAction("⟳", self)
        self.reload_btn.triggered.connect(lambda: self.parent.current_browser().reload())
        self.addAction(self.reload_btn)

        self.home_btn = QAction("🏠", self)
        self.home_btn.triggered.connect(lambda: self.parent.current_browser().setUrl(QUrl("https://www.google.com")))
        self.addAction(self.home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.addWidget(self.url_bar)

    def navigate_to_url(self):
        text = self.url_bar.text()
        url = QUrl(text if "." in text else f"https://www.google.com/search?q={text}")
        if not url.scheme():
            url.setScheme("http")
        self.parent.current_browser().setUrl(url)

    def update_url(self, url):
        self.url_bar.setText(url)
