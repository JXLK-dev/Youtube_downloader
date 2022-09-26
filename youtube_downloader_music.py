import os
import shutil
import yt_dlp
import fileinput
import os.path


def run(video_url: str):
    video_info = yt_dlp.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    # to check if music existed
    file_exists = os.path.exists(
        "C:\\Users\\Jerry\\Desktop\\AllApps\\Songs\\{}".format(filename))
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    if (not file_exists):
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
        shutil.move("C:\\Users\\Jerry\\Desktop\\AllApps\\somethingsus\\Youtube_downloader\\{}".format(
            filename), "C:\\Users\\Jerry\\Desktop\\AllApps\\Songs\\{}".format(filename))
    else:
        print("Failed to download file\nfilename : {} has existed".format(filename))
        filler = input("press enter to continue")


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
        print("3. Exit")
        method = input("Please select input method: ")
        if (method == "1"):
            download_all_script()
        if (method == "2"):
            os.system('cls')
            while (True):
                print("Type \"exit\" to go back")
                filename = input(
                    "Please input URL (Youtube Music) (Youtube) :\n")
                if (filename == "exit"):
                    break
                run(filename)
                os.system('cls')
        if (method == "3"):
            return
        os.system('cls')


if __name__ == '__main__':
    chooseDownloadMethod()
