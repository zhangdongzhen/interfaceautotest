
ControlFocus("��","","Edit1")


WinWait("[CLASS:#32770]","",10)

ControlSetText("��","","Edit1",@ScriptDir&"\sms.xlsx")
Sleep(1000)


ControlClick("��","","Button1");