import pyautogui
import xlwings as xw
import time

# -- 엑셀파일 만들기 -- #
wb = xw.Book()
ws = wb.sheets.active

for i in range(2, 102):
    ws.range(i, 1).value = i
    ws.range(i, 2).value = f'part{i}'
    ws.range(i, 3).value = f'name{i}'
wb.save('example.xlsx')
wb.close()


# -- 엑셀 -> ppt 데이터 옮기기 -- #
wb = xw.Book('example.xlsx')
ws = wb.sheets.active

# ppt 클릭하여 활성화
pyautogui.click(x=1083, y=535)

for i in range(1, 10):
    num = str(int(ws.range(i, 1).value))
    part = ws.range(i, 2).value
    name = ws.range(i, 3).value

    # 번호
    pyautogui.click(x=1083, y=535)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write(num)

    # 소속
    pyautogui.click(x=848, y=657)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write(part)

    # 이름
    pyautogui.click(x=1283, y=664)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pyautogui.write(name)

    # 다음 페이지로 옮겨가기
    pyautogui.click(x=466, y=527)
    pyautogui.press('down')
