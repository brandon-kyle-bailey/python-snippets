#/usr/bin/env python


def query_some_data():
    return {"name":1, "name":2, "name":3}


def raise_warning_dialog(QtGui):

    conflict_msg = "This is a warning"

    reply = QtGui.QMessageBox.question(QtGui.QMainWindow(),
                                       'Conflict found!',
                                        conflict_msg,
                                        QtGui.QMessageBox.YesToAll,
                                        QtGui.QMessageBox.Yes,
                                        QtGui.QMessageBox.No)

    return reply


def test():

    from PyQt4 import QtGui
    app = QtGui.QApplication([__name__])

    values_to_match = [1, 2, 3]

    results = query_some_data()
    used_names = {val for name, val in results.iteritems()}

    for name in values_to_match:
        
        if name in used_names:
            reply = raise_warning_dialog(QtGui)

            if reply == QtGui.QMessageBox.YesToAll:
                break
                
            elif reply == QtGui.QMessageBox.Yes:
                continue
                
            else:
                raise ValueError("This is a value error")


if __name__ == "__main__":
    test()
