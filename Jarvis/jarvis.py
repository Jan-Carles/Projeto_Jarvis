import pyttsx3  # Biblioteca para conversão de texto em fala (TTS - Text-to-Speech)
import datetime  # Fornece classes para manipular datas e horas
import speech_recognition as sr  # Biblioteca para reconhecimento de voz e conversão de fala em texto
import pause  # Usada para pausar o código por um tempo ou até um momento específico
import pyautogui as pa  # Permite automação de interação com a interface gráfica, como cliques e digitação
import time  # Oferece funções relacionadas ao tempo, como atrasos e manipulação de timestamps
import pyperclip  # Fornece suporte para copiar e colar texto usando a área de transferência do sistema


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
        if 'abrir' in comando:

            falar("Tudo bem")
            pa.PAUSE = 1
            pa.press('win') #pa.press é uma função para apertar ('win') é o teclado
            pa.write('Edge') #função para escrever
            pa.press('ENTER') #função para apertar
            pa.write('youtube.com') #função para escrever
            pa.press('ENTER') #função para apertar
            time.sleep(8) #função para intervalo em segundos
            falar("E agora? o que eu faço?")
            continue
        
        if 'coloque' in comando:

            falar("Você que manda!")
            time.sleep(5)
            pa.click(x=1032, y=123) # coordenadas para o click
            pa.write("Black in Black")
            pa.press('ENTER')
            time.sleep(3)
            pa.click(x=1157, y=322) #coordnadas para o click
            time.sleep(5)
            pa.press('ENTER')

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