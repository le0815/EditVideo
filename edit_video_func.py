from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.VideoClip import ImageClip


class VideoFunc:
    def __init__(self, main_video_path, output_path, overlay_video_path=""):
        self.main_video_path = main_video_path
        self.overlay_video_path = overlay_video_path
        self.output_path = output_path

    def AddOverlay(self, is_return=False, pos=("right", "bottom"), main_video=None):

        print('start add overlay to video')

        if main_video is None:
            main_video = VideoFileClip(self.main_video_path)
        # Load the video files

        overlay_video = VideoFileClip(self.overlay_video_path)

        # set duration of the overlay
        overlay_video = overlay_video.loop(duration=main_video.duration)

        # Set the position of the overlay video
        overlay_video = overlay_video.set_position(pos)

        # Create a composite video clip
        final_video = CompositeVideoClip([main_video, overlay_video])

        if is_return:
            return final_video

        # Write the final video to a file
        final_video.write_videofile(self.output_path, codec='libx264')

        #close opened video
        overlay_video.close()
        main_video.close()


    def ResizeVideo(self, is_return=False):
        print('start resize video')

        main_video = VideoFileClip(self.main_video_path)

        # Resize the video
        resized_clip = main_video.resize(height=720, )  # You can specify either height or width

        if is_return:
            return resized_clip

        # Write the final video to a file
        resized_clip.write_videofile(self.output_path, codec='libx264')

        # Close the video clips
        main_video.close()
        resized_clip.close()

    def GetAudio(self):
        # Load the video file
        video = VideoFileClip(self.main_video_path)

        # Extract the audio
        audio = video.audio

        # Write the audio to a file
        audio.write_audiofile(self.output_path)

    def RemoveWatermark(self, count, img_path):

        print(f'count: {count}')
        # Load the video
        video = VideoFileClip(self.main_video_path)

        # Load the image
        image = ImageClip(img_path)

        # Set the duration of the image clip to match the video duration
        image = image.set_duration(video.duration)

        # Set the position of the image (e.g., top-left corner)
        image = image.set_position(pos=(465, 55))  # You can adjust the position as needed

        # Overlay the image on the video
        composite = CompositeVideoClip([video, image])

        # Write the result to a file
        composite.write_videofile(self.output_path, codec='libx264')