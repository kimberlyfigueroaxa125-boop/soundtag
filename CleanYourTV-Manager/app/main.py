from pathlib import Path
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication

ROOT = Path(__file__).resolve().parent
UI = ROOT / "ui" / "MainWindow.ui"


def main():
    app = QApplication(sys.argv)
    loader = QUiLoader()
    window = loader.load(str(UI))
    if window is None:
        raise RuntimeError(f"Unable to load UI: {UI}")
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
