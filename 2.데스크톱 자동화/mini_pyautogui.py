import pyautogui
import pyperclip
import time

# 메모장 프로그램 실행
pyautogui.press('win')
pyautogui.write('notepad')
pyautogui.press('enter')

# 3초 대기
time.sleep(3)

# "Hello, world!" 텍스트 입력
pyautogui.write('Hello, world!')

# "Ctrl + S" 키 입력하여 파일 저장 대화상자 열기
pyautogui.hotkey('ctrl', 's')

# 3초 대기
time.sleep(3)

# 파일 이름 입력 및 저장
file_path = 'example.txt'
pyperclip.copy(file_path)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# 프로그램 종료
pyautogui.hotkey('alt', 'f4')
