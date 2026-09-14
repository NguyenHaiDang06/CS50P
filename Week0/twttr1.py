def main():
  a=input("Input: ")
  chuoi_moi=shorten(a)
  print(f"Output: {chuoi_moi}")
  pass
def shorten(word):
  ket_qua=""
  x="ueoaiUEOAI"
  for b in word:
    if b in x:
      continue
      ket_qua+=b
  return ket_qua

if __name__=="__main__":
  main()
