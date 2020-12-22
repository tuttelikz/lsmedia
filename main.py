import os

def lsmedia(mypath):
    img_fm = (".tif", ".tiff", ".jpg", ".jpeg", ".gif", ".png", ".eps", 
          ".raw", ".cr2", ".nef", ".orf", ".sr2", ".bmp", ".ppm", ".heif")
    vid_fm = (".flv", ".avi", ".mp4", ".3gp", ".mov", ".webm", ".ogg", ".qt", ".avchd")
    aud_fm = (".flac", ".mp3", ".wav", ".wma", ".aac")
    media_fms = {"image": img_fm, "video": vid_fm, "audio": aud_fm}

    fns = lambda path, media : [fn for fn in os.listdir(path) if any(fn.endswith(media_fms[media]) for ext in media_fms[media])]
    img_fns, vid_fns, aud_fns = fns(mypath, "image"), fns(mypath, "video"), fns(mypath, "audio")

    print(f"State of media in '{mypath}'")
    print("Images: ", len(img_fns), " | Videos: ", len(vid_fns), "| Audios: ", len(aud_fns))
    
    return (img_fns, vid_fns, aud_fns)

mypath = "/home/DATA_Lia/data_02/sample" # define dir
(imgs, vids, auds) = lsmedia(mypath)
