from PyQt6 import QtWidgets, uic
import qrcode

# Initialize application
app = QtWidgets.QApplication([])

# Load UI
w = uic.loadUi('UIQRcodeProject.ui')

# Define QR code generation function
def CreateQRCode():
    link = w.link.toPlainText()
    if not link.strip():  # Check for empty input
        QtWidgets.QMessageBox.warning(w, "Input Error", "Please enter a valid link.")
        return

    # Open a file dialog for the user to choose the save location
    file_dialog = QtWidgets.QFileDialog()
    save_path, _ = file_dialog.getSaveFileName(
        w, 
        "Save QR Code",  # Dialog title
        "qrcode.png",    # Default file name
        "Images (*.png *.jpg *.bmp)"  # File types
    )
    
    if not save_path:  # If the user cancels the dialog
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    try:
        img.save(save_path)
        QtWidgets.QMessageBox.information(w, "Success", f"QR Code saved as '{save_path}'.")
    except Exception as e:
        QtWidgets.QMessageBox.critical(w, "Error", f"Failed to save QR Code: {str(e)}")

# Connect button to the function
w.pushButton.clicked.connect(CreateQRCode)

# Start application
if __name__ == '__main__':
    w.show()
    app.exec()
