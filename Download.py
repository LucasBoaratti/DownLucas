from pytubefix import YouTube 
from moviepy import VideoFileClip, AudioFileClip 

def download_video(url): 
    try:
        videoYoutube = YouTube(url)
        print("\nTítulo do vídeo: ", videoYoutube.title) 

        #Aqui, o vídeo será baixado individualmente, sem áudio e com a maior resolução possível
        print("\nBaixando vídeo...")
        video = videoYoutube.streams.filter(only_video=True, file_extension="mp4").order_by("resolution").desc().first()  
        video.download(filename="Vídeo.mp4") 
        print(f"Vídeo baixado com sucesso! Resolução: {video.resolution}") 

        #Aqui, o áudio será baixado individualmente, sem o vídeo e com o maior bitrate possível
        print("\nBaixando áudio...")
        audio = videoYoutube.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first()
        audio.download(filename="Áudio.mp4") 
        print(f"Áudio baixado com sucesso! Aúdio (Bitrate): {audio.abr}")

        #Aqui, o áudio e o vídeo serão juntados em um só
        print("\nJuntando vídeo e áudio...")
        videoClip = VideoFileClip("Vídeo.mp4")
        audioClip = AudioFileClip("Áudio.mp4")
        videoFinal = videoClip.with_audio(audioClip)
        videoFinal.write_videofile(f"{videoYoutube.title}_Vídeo_Final.mp4")

        print("\nDownload concluído com sucesso! Aproveite! 😉")
    except Exception as erro: 
        print("Erro: ", str(erro))

print("Olá, seja bem-vindo(a) à DownLucas! Aqui você pode baixar um vídeo do YouTube a partir da URL do vídeo! 😁")

# Removendo parâmetros extras como espaço, além de dividir o vídeo em substrings após o &
linkVideo = input("\nCole o link de um vídeo do YouTube: ").strip().split("&")[0] 

download_video(linkVideo)