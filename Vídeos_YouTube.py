from pytubefix import YouTube #Importando a biblioteca pytubefix para mexer com downloads do youtube
from moviepy import VideoFileClip, AudioFileClip #Importando as classes VideoFileClip e AudioFileClip do moviepy para trabalhar com vídeo e áudio

def VideoEmAltaResolucao(url): #Função para baixar os vídeos em alta resolução
    try:
        videoYoutube = YouTube(url) #Cria um objeto Youtube a partir da url fornecida pelo usuário

        print("Título do vídeo: ", videoYoutube.title) #Mostra o título do vídeo na tela/terminal

        #Aqui, o vídeo será baixado individualmente, sem áudio
        print("Baixando vídeo...") 

        video = videoYoutube.streams.filter(only_video=True, file_extension="mp4").order_by("resolution").desc().first() #Aqui, o vídeo terá a maior resolução possível 

        video.download(filename="Vídeo.mp4") #Realiza o download do vídeo, sem áudio

        print(f"Vídeo baixado com sucesso! Resolução: {video.resolution}") #Exibe a mensagem de sucesso na tela/terminal e a resolução do vídeo baixado

        #Aqui, o áudio será baixado individualmente, sem o vídeo
        print("Baixando áudio...")

        audio = videoYoutube.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first() #Aqui, o áudio terá um melhor "bitrate"

        audio.download(filename="Áudio.mp4") #Realiza o download do áudio, sem o vídeo

        print(f"Áudio baixado com sucesso! Aúdio (Bitrate): {audio.abr}") #Exibe a mensagem de sucesso na tela/terminal e o bitrate do áudio

        #Aqui, o áudio e o vídeo serão juntados em um só
        print("Aguarde, áudio e vídeo estão sendo juntados...")  

        videoClip = VideoFileClip("Vídeo.mp4") #Carregando o vídeo

        audioClip = AudioFileClip("Áudio.mp4") #Carregando o áudio

        videoFinal = videoClip.with_audio(audioClip) #Aqui, o aúdio é adicionado ao vídeo

        videoFinal.write_videofile(f"{videoYoutube.title}_em_Alta_Resolução.mp4") #Aqui, é salvado o vídeo final com o áudio

        print("Download concluído com sucesso!") #Exibe uma mensagem de sucesso na tela/terminal
    except Exception as erro: 
        print("Erro: ", str(erro)) #Mostrando o erro na tela/terminal (se tiver)

linkVideo = input("Digite ou cole uma url de um vídeo do youtube: ").strip().split("&")[0] #Aqui, o usuário vai inserir o vídeo. E depois será removido os parâmetros extras como &list= e tudo mais...

VideoEmAltaResolucao(linkVideo) #Chamando a função e passando a url que o usuário inseriu