from math import ceil

def calcYuEBaoMin(s, expected):
  "s 万份收益；expected 预期收益（0.01倍数）"
  return ceil(100 / s * (expected-0.4))
  
def main():
  while True:
    try:
      s = float(input("输入万份收益"))
      expected = int(input("输入想要的收益（0.01的倍数）"))
      print(calcYuEBaoMin(s, expected))
    except e as ValueError:
      print("输入错误")
      continue


if __name__ == '__main__':
  main()
