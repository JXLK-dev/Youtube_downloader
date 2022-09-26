import os
from numpy import choose
import yt_dlp
import fileinput
import os.path


def run(video_url: str):
    video_info = yt_dlp.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    # to check if music existed
    file_exists = os.path.exists(filename)
    # print(file_exists)

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    if (not file_exists):
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
    else:
        print("Failed to download file\n filename : {} has existed".format(filename))


def extract_text_file():
    file = fileinput.input('list_of_songs.txt')
    listofsongs = []
    for line in file:
        listofsongs.append(line)
    return listofsongs


def download_all_script():
    listofsongs = extract_text_file()
    for song in listofsongs:
        run(song)
    deleteAllLinksInTextDocument("list_of_songs.txt")


def deleteAllLinksInTextDocument(textDocument: str):
    with open(textDocument, 'r+') as file:
        file.truncate(0)


def chooseDownloadMethod():
    while (True):
        print("1. Download music from the list_of_songs")
        print("2. Download music from input")
        method = input("Please select input method: ")
        if (method == "1"):
            download_all_script()
        if (method == "2"):
            filename = input("Please input URL (Youtube Music) (Youtube) :\n")
            run(filename)
        if (method == "3"):
            return
        os.system('cls')


if __name__ == '__main__':
    chooseDownloadMethod()
