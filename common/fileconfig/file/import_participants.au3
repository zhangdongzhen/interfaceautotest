
ControlFocus("��","","Edit1")


WinWait("[CLASS:#32770]","",10)

ControlSetText("��","","Edit1",@ScriptDir&"\import_participants.xlsx")
Sleep(2000)


ControlClick("��","","Button1");