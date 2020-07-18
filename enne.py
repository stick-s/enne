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

class Verifica:
    def validadeurl(self,link):
        if "https://www.youtube.com/" in link:
            return True
        else:
            print(f"{link} não é link do youtube")
            return False

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

    def MostrarDados(self):
        self.linksbaixados = open("baixados.txt")
        bancodelinks = self.linksbaixados.read()
        self.linksbaixados.close()
        print(bancodelinks)

    def VerificaUrlBd(self):
        with open("baixados.txt") as f:
            for verificar, linksbaixados in enumerate(f,1):
                if self.url in linksbaixados:
                    print("\nHá um download realizado de:\nNome: {}\nUrl: {}".format(self.video.title,self.url))
                    return True
            else:
                return False

class Operation:
    def finalizar(self):
        print("Fechando programa")
        for i in range(1,5):
            print('. .', end=' ', flush=True)
            sleep(1)
        print("\n")
        sys.exit()

    def menuhelp(self):
        print("-b [Mostrar músicas baixadas]")

    def repetir(self):
        repetição = input("Repetir processo de download? [S/N]: ")
        if repetição == ('n' or 'N'):
            op.finalizar()
        elif repetição == ('s' or 'S'):
            link = input("Digite um link: ")
            return link
        else:
            print("Falha em verificação")
            repetição = input("Repetir processo de download? [S/N]: ")

op = Operation()
try:
    arg = sys.argv[1]

except IndexError:
    print("Insira um link valido do YouTube como argumento.")
    op.menuhelp()
    op.finalizar()

v = Verifica()

if arg == '--help':
    op.menuhelp()
    op.finalizar()

elif v.validadeurl(arg) == True:
    while True:
        d = Download(arg)
        p = Path(arg)
        db = DataBase(arg)
        if db.VerificaUrlBd() == False:
            d.GoDownload()
            db.BancoDeDownloads()
            op.repetir()

else:
    op.finalizar()
