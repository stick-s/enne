from time import sleep
import pafy
import os
import shutil
import sys

class Download:
    def __init__(self,url):
        self.url = url
        self.video = pafy.new(self.url)
        self.arquivomp3 = ''
        self.pasta = ''
    def GoDownload(self):
        video = self.video
        try:
            bestaudio = video.getbestaudio()
            self.pasta = p.LocalParaSalvar()
            self.arquivomp3 = self.pasta+"/"+str(video.title)+".mp3"
            bestaudio.download(self.arquivomp3)
            print("Download realizado com sucesso!")
        except:
            print("ERRO! Download não realizado")

class Path:
    def __init__(self,url):
        self.url = url
        self.video = pafy.new(self.url)
        self.PastaHome = os.path.expanduser("~")+"/"
        self.NovaPasta = ''

    def ValidaPasta(self,pasta):
        if os.path.exists(self.NovaPasta) == False:
            print(f"{pasta} é um diretório inexistente")
            pasta = input("Salvar em: ")
            return pasta

    def LocalParaSalvar(self):
        local = input("Salvar em: ")
        self.NovaPasta = str(self.PastaHome+local)
        p.ValidaPasta(local)
        return self.NovaPasta

class DataBase:
    def __init__(self,url):
        self.url = url
        self.video = pafy.new(self.url)
        self.linksbaixados = open("baixados.txt")

    def BancoDeDownloads(self):
        self.linksbaixados = open("baixados.txt","a")
        self.linksbaixados.write("{}-{}\n".format(str(self.video.title),self.url))
        self.linksbaixados.close()

    def VerificaUrl(self):
        with open("baixados.txt") as f:
            for verificar, linksbaixados in enumerate(f,1):
                if self.url in linksbaixados:
                    print("\nHá um download realizado de:\nNome: {}\nUrl: {}".format(self.video.title,self.url))
                    return True
            else:
                return False

def finalizar():
    print("Fechando programa")
    for i in range(1,5):
        print('. .', end=' ', flush=True)
        sleep(1)
    print("\n")

link = sys.argv[1]
while True:
    d = Download(link)
    p = Path(link)
    db = DataBase(link)
    if db.VerificaUrl() == False:
        d.GoDownload()
        db.BancoDeDownloads()
        repetição = input("Repetir processo de download? [S/N]: ")
        if repetição == ('n' or 'N'):
            finalizar()
            break
        elif repetição == ('s' or 'S'):
            link = input("Digite um link: ")
        else:
            print("Falha em verificação")
            repetição = input("Repetir processo de download? [S/N]: ")
    else:
        finalizar()
        break
