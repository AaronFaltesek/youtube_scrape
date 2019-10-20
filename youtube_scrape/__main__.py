from __future__ import unicode_literals
from config import settings, __version__
import os
import random
import youtube_dl

def mp3_download(link, download_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_dir, '%(alt_title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '192',
    #     }],
    # }

    return_code = -1

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            return_code = ydl.download([link])

        random_file_name = random.randint(1, 100001)

        #os.rename('{}/_.mp3'.format(download_dir), '{}/{}.mp3'.format(download_dir, random_file_name))

    except Exception:
        return_code = 1

    return return_code

def create_download_directory(target_file_type):
    '''

    :param target_file_type:
    :return:
    '''
    download_dir_base = settings['{}_loc'.format(target_file_type)]
    # download_playlist_file_name = youtube_list_file_path
    return


def main():
    '''
    This will kick off the download process

    :return: None
    '''

    youtube_list_file_path = settings['youtube_list']
    target_file_type = settings['mp4_mp3_toggle']
    download_dir = create_download_directory(target_file_type)
    download_dir = settings['{}_loc'.format(target_file_type)]

    print("Beginning youtube scrape of videos and conversion to mp3/mp4 files stored in {}".format(download_dir))
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print("Directory created: {}".format(download_dir))

    # single link

    youtube_list_file = open(youtube_list_file_path, "r")
    youtube_links = youtube_list_file.readlines()

    [mp3_download(link, download_dir) for link in youtube_links if link.__contains__('www.youtube')]

    print('done')


if __name__ == '__main__':

    print("Youtube Scrape starting up")
    main()
    print("Version: {}".format(__version__))
