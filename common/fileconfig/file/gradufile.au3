
ControlFocus("��","","Edit1")


WinWait("[CLASS:#32770]","",10)

ControlSetText("��","","Edit1",@ScriptDir&"\gradufile.txt")
Sleep(2000)


ControlClick("��","","Button1");