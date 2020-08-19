from time import sleep
import pafy
import os
import shutil
import sys
import re

class Download:
    def __init__(self,url):
        self.url = url
        self.video = pafy.new(self.url)
        self.arquivo_mp3 = ''
        self.pasta = ''

    def go_download(self):
        video = self.video
        try:
            bestaudio = video.getbestaudio()
            self.pasta = path.save_location()
            self.arquivo_mp3 = self.pasta + self.video.title + ".mp3"
            bestaudio.download(self.arquivo_mp3)
            print("Download realizado com sucesso!")
        except:
            print("ERRO! Download não realizado")

class Validates:
    def validates_url(self, link):
        if re.findall(r"https://www\.youtube\.com/watch\?v=.{11}", link)
            return True
        else:
            print(f"{link} não é link do youtube")
            return False

class Path:
    def __init__(self):
        self.url = url
        self.video = pafy.new(self.url)
        self.home_folder = os.path.expanduser("~") + os.sep
        self.new_folder = ''

    def validates_folder(self, folder):
        if os.path.exists(self.new_folder) == False:
            print(f"{folder} é um diretório inexistente")
            folder = input("Salvar em: ")
            return folder

    def save_location(self):
        local = input("Salvar em: ")
        self.new_folder = str(self.home_folder + local)
        path.validates_folder(local)
        return self.new_folder

class DataBase:
    def __init__(self,url):
        self.video = pafy.new(url)
        self.file_download_links = open("enne.conf", "a+")

    def data_downloads(self):
        self.file_download_links = open("enne.conf","a")
        self.file_download_links.write("{}-{}\n".format(self.video.title, self.url))
        self.file_download_links.close()

    def show_data(self):
        self.download_links = open("enne.conf", "a+")
        self.download_links.seek(os.SEEK_SET, 0)
        data_link = self.download_links.read()
        self.download_links.close()
        print(data_link)

    def check_data_url(self):
        with open("enne.conf","a") as f:
            for check, self.download_links in enumerate(f,1):
                if self.url in self.download_links:
                    print("\nHá um download realizado de:\nNome: {}\nUrl: {}".format(self.video.title,self.url))
                    return True
            else:
                return False

class Operation:
    def finish(self):
        print("Fechando programa")
        for i in range(1,5):
            print('. .', end=' ', flush=True)
            sleep(1)
        print("\n")
        sys.exit(0)

    def menuhelp(self):
        print("-b [Mostrar músicas baixadas]")
        print("-h [Exibir esse menu]")

    def repeat(self):
       repetition = input("Repetir processo de download? [S/N]: ")
        if repetition == ('n' or 'N'):
            op.finish()
        elif repetition == ('s' or 'S'):
            link = input("Digite um link: ")
            return True
        else:
            print("Falha em verificação")
            repetition = input("Repetir processo de download? [S/N]: ")


operation = Operation()
try:
    video_url = sys.argv[1]
    local_salvar = sys.argv[2]

except IndexError:
    print("Insira um link valido do YouTube como argumento.")
    operation.menuhelp()
    operation.finish()

validates = Validates()

if arg == '--help':
    operation.menuhelp()
    operation.finish()

elif validates.validates_url(video_url):
    while True:
        download = Download(video_url)
        path = Path()
        data = DataBase(video_url)
        if not data.check_data_url():
            download.go_download()
            data.data_downloads()
            operation.repeat()

else:
    operation.menuhelp()
    operation.finish()
