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
        bestaudio = video.getbestaudio()
        self.pasta = p.LocalParaSalvar()
        self.arquivomp3 = self.pasta+"/"+str(video.title)+".mp3"
        try:
            bestaudio.download(self.arquivomp3)
            print("Download realizado com sucesso!")
        except:
            print("ERRO! Download não relizado")

class Path:
    def __init__(self,url):
        self.url = url
        self.video = pafy.new(self.url)
        self.PastaHome = os.path.expanduser("~")+"/"
        self.NovaPasta = ''

    def ValidaPasta(self,pasta):
        if os.path.exists(self.NovaPasta) == False:
            print(f"{pasta} é um diretório inexistente")
            pasta = input("Onde deseja salvar a música? ")
            return pasta

    def LocalParaSalvar(self):
        local = input("Onde deseja salvar a música? ")
        self.NovaPasta = str(self.PastaHome+local)
        p.ValidaPasta(local)
        return self.NovaPasta

link = sys.argv[1]
while True:
    d = Download(link)
    p = Path(link)
    d.GoDownload()
    repetição = input("Baixar mais uma música?[s/n]: ")
    if repetição =='n':
        print("Fechando programa")
        break
    elif repetição == 's':
        print("Digite um link: ")
        link = input()
    else:
        print("Não entendi")
        repetição = input("Baixar mais uma música?[s/n]: ")
