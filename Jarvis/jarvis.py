import pyttsx3
import datetime
import speech_recognition as sr
import pause

# Inicializa o TTS
texto_fala = pyttsx3.init()

def falar(audio):
    texto_fala.setProperty("rate", 195)  # Ajusta a velocidade da fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[0].id)  # 0 = Masculina, 1 = Feminina
    texto_fala.say(audio)
    texto_fala.runAndWait()

# Função para obter a hora atual
def tempo():
    hora_atual = datetime.datetime.now().strftime("%I:%M")
    falar(f"Agora são, {hora_atual}")
    print(f"Hora: {hora_atual}")

# Função para obter a data atual
def data():
    # Lista com os meses por extenso
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    agora = datetime.datetime.now()
    dia = agora.day
    mes = meses[agora.month - 1]  # Obtém o nome do mês correspondente
    ano = agora.year
    falar(f"Hoje é dia {dia} de {mes}, de {ano}!")
    print(f"Data: {dia} de {mes} de {ano}")

# Função para saudar o usuário com base na hora
def bem_vindo():
    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        saudacao = "Bom dia senhor! Bem vindo de volta!"
    elif 12 <= hora < 18:
        saudacao = "Boa tarde senhor! Bem vindo de volta!"
    else:
        saudacao = "Boa noite senhor! Bem vindo de volta!"
    falar(saudacao)

# Função para capturar comandos de voz
def microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando sua fala...")
        r.pause_threshold = 1  # Tempo de pausa antes de processar a fala
        try:
            audio = r.listen(source)  # Escuta o áudio do usuário
            print("Processando...")
            comando = r.recognize_google(audio, language='pt-BR')  # Converte áudio para texto
            print(f"Você disse: {comando}")
            return comando.lower()  # Retorna o texto reconhecido em minúsculas
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Erro na conexão: {e}")
            falar("Houve um problema na conexão. Por favor, tente novamente.")
            return None

# Função principal para processar comandos
if __name__ == "__main__":
    bem_vindo()
    while True:
        print("Escutando...")
        comando = microfone()

        # Verifica se o comando não é nulo
        if comando is None:
            continue

        # Se o usuário disser "Jarvis", o programa responde "Estou lhe ouvindo"
        if 'jar' in comando:
            falar("Estou lhe ouvindo!")
            continue  # Volta para escutar mais comandos

        # Responde a outros comandos
        if 'como' in comando:
            falar("Estou bem! Obrigado por perguntar.")
            falar("O que posso fazer para ajudá-lo?")
        elif 'horas' in comando:
            tempo()
        elif 'data' in comando:
            data()
        elif 'volte' in comando:
            falar("Por quanto tempo devo esperar?")
            while True:
                resposta = microfone()
                if resposta and resposta.isdigit():
                    segundos = int(resposta)
                    falar(f"Ok, voltarei em {segundos} segundos.")
                    pause.seconds(segundos)
                    falar("Estou de volta, senhor!")
                    break
                else:
                    falar("Por favor, diga um número válido.")
        elif 'obrigado' in comando:
            falar("Tudo bem! Se precisar estou aqui!")
            quit()
        else:
            falar("Desculpe, não entendi o comando. Pode repetir?")