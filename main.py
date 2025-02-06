from src.Controllers.SpeechController import SpeechController

def main():
    controller = SpeechController()
    result = controller.process_speech()
    print("Final Output:", result)

if __name__ == "__main__":
    main()