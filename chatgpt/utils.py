import textwrap


def indent(text, amount, ch=' '):
    return textwrap.indent(text, amount * ch)





text = '''\
JAI SHREE RAM
- Jesus
'''




def main():
    print("USER:")
    print(indent(text, 4))

if __name__=="__main__":
	
	main()
