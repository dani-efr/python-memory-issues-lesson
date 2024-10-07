from converter import convert
from highscore import highscore

if __name__ == '__main__':
    try:
        convert()
        highscore()
    except Exception as e:
        print(e)
