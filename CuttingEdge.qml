import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12
import Qt.labs.platform 1.1
import QtQuick.Dialogs 1.3

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Cutting Edge")
    FolderDialog{
        id:inputfdialog
        folder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
        onAccepted: {
            inputfolderTextField.text=mainwinconnect.fpPathconv(inputfdialog.currentFolder)
        }
    }
    Component.onCompleted: {
        function onLoad(){
            mainwinconnect.success_dialogsignal.connect(
                        function lambdakun(stroniisan){
                            msgdialogsuc.open()
                        }

                        );
        }
        onLoad()
    }

    MessageDialog{
        id:msgdialogsuc
        title: "Success??"
        text:qsTr("I don't know....")

        onAccepted: {
            msgdialogsuc.close()
        }
        standardButtons: StandardButton.OK
    }

    Button {
        id: button24gakusei
        x: 551
        y: 42
        width: 52
        height: 40
        text: qsTr("...")
        onClicked: {
            inputfdialog.open()
        }
    }

    TextField {
        id: inputfolderTextField
        x: 97
        y: 42
        width: 428
        height: 40
        placeholderText: qsTr("Text Field")
    }
    FolderDialog{
        id:outputfdialog
        folder: StandardPaths.standardLocations(StandardPaths.PicturesLocation)[0]
        onAccepted: {
            outputfolderTextField.text=mainwinconnect.fpPathconv(outputfdialog.currentFolder)
        }
    }

    Button {
        id: outputbutton24gakusei
        x: 551
        y: 96
        width: 52
        height: 40
        text: qsTr("...")
        onClicked: {
            outputfdialog.open()
        }
    }

    TextField {
        id: outputfolderTextField
        x: 97
        y: 96
        width: 428
        height: 40
        placeholderText: qsTr("Text Field")
    }

    Label {
        id: label
        x: 27
        y: 55
        text: qsTr("Input:")
    }

    Label {
        id: label1
        x: 29
        y: 107
        text: qsTr("Output:")
    }

    Button {
        id: buttonrun
        x: 430
        y: 271
        text: qsTr("Running Process")
        onClicked: {
            mainwinconnect.running_process(inputfolderTextField.text,outputfolderTextField.text)
        }
    }
}
