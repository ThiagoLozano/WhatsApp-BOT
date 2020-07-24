# Bibliotecas.
from selenium import webdriver
import time


# Cria a classe.
class WhatsappBot:
    def __init__(self):
        # Mensagem que será enviada.
        self.mensagem = 'Olá, esta é uma mensagem gerada automaticamente por um BOT.'

        # Para quem está enviando.
        self.contatos = ["Insira o(s) contato(s) aqui"]

        # Configuração do Drive.
        config = webdriver.ChromeOptions()
        config.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=config)

    # Cria uma função para enviar a mensagem.
    def EnviarMensagem(self):
        # Entra no Site.
        self.driver.get('http://web.whatsapp.com')
        time.sleep(10)

        # Seleciona o grupo.
        for contato in self.contatos:
            campo_do_contato = self.driver.find_element_by_xpath("//span[@title='{}']".format(contato))
            time.sleep(3)
            campo_do_contato.click()

            # Seleciona a caixa de texto.
            caixa_de_texto = self.driver.find_element_by_class_name("_3uMse")
            time.sleep(3)
            caixa_de_texto.click()

            # Escreve a mensagem.
            caixa_de_texto.send_keys(self.mensagem)

            # Envia a mensagem.
            envia_mensagem = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            envia_mensagem.click()
            time.sleep(5)

        # Fecha o Chrome.
        self.driver.close()


bot = WhatsappBot()
bot.EnviarMensagem()

# HTML para o Campo do Grupo.
'''<span dir="auto" title="nome do contato" class="_3ko75 _5h6Y_ _3Whw5">'''

# HTML para a Caixa de Texto.
'''<div tabindex="-1" class="_3uMse">'''

# HTML para o Botão de Enviar.
'''<span data-testid="send" data-icon="send" class="">'''
