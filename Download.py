from pytubefix import YouTube 
from moviepy import VideoFileClip, AudioFileClip 
import os
import re

# Criando as pastas, caso elas sejam apagadas sem querer, são criadas novamente
os.makedirs("Vídeos", exist_ok=True)
os.makedirs("Áudios", exist_ok=True)
os.makedirs("Vídeo_Final", exist_ok=True)

def download_video(url): 
    try:
        videoYoutube = YouTube(url)
        # Removendo caracteres especiais e trocando-os por underline
        tituloVideo = re.sub(r'[\\/*?:"<>|()\n]', "", videoYoutube.title)
        tituloVideo = tituloVideo.replace(" ", "_")
        
        print("\nTítulo do vídeo: ", videoYoutube.title) 

        #Aqui, o vídeo será baixado individualmente, sem áudio e com a maior resolução possível
        print("\nBaixando vídeo...")
        video = videoYoutube.streams.filter(only_video=True, file_extension="mp4").order_by("resolution").desc().first()  
        video.download(output_path="Vídeos", filename=f"{tituloVideo}_Vídeo.mp4") 
        print(f"Vídeo baixado com sucesso! Resolução: {video.resolution}")

        #Aqui, o áudio será baixado individualmente, sem o vídeo e com o maior bitrate possível
        print("\nBaixando áudio...")
        audio = videoYoutube.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first()
        audio.download(output_path="Áudios", filename=f"{tituloVideo}_Áudio.mp4") 
        print(f"Áudio baixado com sucesso! Aúdio (Bitrate): {audio.abr}")

        #Aqui, o áudio e o vídeo serão juntados em um só
        print("\nJuntando vídeo e áudio...")

        # Criando os caminhos para o vídeo e para o áudio
        caminhoVideo = f"Vídeos/{tituloVideo}_Vídeo.mp4"
        caminhoAudio = f"Áudios/{tituloVideo}_Áudio.mp4"
        caminhoVideoFinal = f"Vídeo_Final/{tituloVideo}_Vídeo_Final.mp4"

        # Juntando áudio e vídeo...
        videoClip = VideoFileClip(caminhoVideo)
        audioClip = AudioFileClip(caminhoAudio)
        videoFinal = videoClip.with_audio(audioClip)
        videoFinal.write_videofile(caminhoVideoFinal)

        print("\nDownload concluído com sucesso! Aproveite! 😉")
    except Exception as erro: 
        print("\nErro: ", str(erro))

print("Olá, seja bem-vindo(a) à DownLucas! Aqui você pode baixar um vídeo do YouTube a partir da URL do vídeo! 😁")

# Removendo parâmetros extras como espaço, além de dividir o vídeo em substrings após o &
linkVideo = input("\nCole o link de um vídeo do YouTube: ").strip().split("&")[0] 

download_video(linkVideo)