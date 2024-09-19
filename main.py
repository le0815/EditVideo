import multiprocessing
import os
from edit_video_func import VideoFunc

def Edit(vid_func):
    temp_vid = vid_func.ResizeVideo(is_return=True)

    pos = ('center', 'bottom')
    vid_func.AddOverlay(pos=pos, main_video=temp_vid)



if __name__ == '__main__':
    count = 0

    input_path = '/home/ha/Videos/Tiktok/Nature/Original/'
    output_path = '/home/ha/Videos/Tiktok/Nature/Resized/'

    file_names = os.listdir(input_path)

    # check duplicate
    temp = os.listdir(output_path)
    for _ in temp:
        if file_names.count(_) > 0:
            print('ok')
            file_names.remove(_)

    while count < len(file_names):
        proc_use = 4

        vids_func = [VideoFunc(main_video_path=input_path+file_names[count + idx], output_path=output_path+file_names[count + idx], overlay_video_path='Video/moving_horse_resized.mp4') for idx in range(proc_use)]

        t1 = [multiprocessing.Process(target=Edit,
                               args=(vids_func[idx], ))
              for idx in range(proc_use)]

        # start thread
        procs = []
        for t in t1:
            procs.append(t)
            t.start()

        # wait for all task are done
        for proc in procs:
            proc.join()

        count += proc_use