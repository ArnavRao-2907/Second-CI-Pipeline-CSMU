def isp(text):
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    x = text.lower()
    return (alpha.issubset(x))
    
if __name__ == "__main__":
    isp("The quick brown fox jumps over the lazy dog")#True
    isp("Hello World")#False
    isp("QewrtYuioPLkjhgFDdSAZxcvvcvcbnm/.,m")#False

#Pangram is to be called when a sentence contains all 26 alphabets whether in uppercase or lowercase