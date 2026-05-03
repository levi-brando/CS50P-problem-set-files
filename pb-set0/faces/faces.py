def main():
    convert(input())

def convert(msg):
    converted_msg = msg.replace(":)", "🙂").replace(":(", "🙁")
    print(converted_msg)

main()

