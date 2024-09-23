def chatbot_response(user_input):
    user_input = user_input.lower()

    if "halo" in user_input or "hi" in user_input or "hei" in user_input:
        return "Halo! Ada yang bisa saya bantu?"
    elif "apa kabar" in user_input:
        return "Saya hanyalah program komputer, tapi saya baik-baik saja! Kamu bagaimana?"
    elif "nama kamu siapa" in user_input:
        return "Saya adalah chatbot sederhana yang siap membantu!"
    elif "terima kasih" in user_input or "makasih" in user_input:
        return "Sama-sama! Senang bisa membantu."
    elif "kamu bisa apa" in user_input:
        return "Saya bisa mengobrol denganmu dan menjawab beberapa pertanyaan sederhana!"
    elif "selamat tinggal" in user_input or "bye" in user_input:
        return "Sampai jumpa! Semoga harimu menyenangkan!"
    else:
        return "Maaf, saya tidak mengerti. Bisa kamu ulangi dengan pertanyaan yang berbeda?"

def start_chat():
    print("Chatbot: Halo! Saya adalah chatbot. Apa yang ingin kamu bicarakan?")
    while True:
        user_input = input("Kamu: ")
        
        if "selamat tinggal" in user_input.lower() or "bye" in user_input.lower():
            print("Chatbot: Sampai jumpa!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

start_chat()
