from edit_video_func import VideoFunc

test = VideoFunc(main_video_path='Video/YOUCC2-7397001293203557659.mp4', output_path='test.mp4', overlay_video_path='Video/moving_horse_resized.mp4')

pos = ('center', 'bottom')

test.AddOverlay(pos)