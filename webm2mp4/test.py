from moviepy.editor import VideoFileClip


input_file = "/home/hongyu/SETUP/laposte/1.webm"



output_file = "/home/hongyu/SETUP/laposte/1.mp4"

# 使用VideoFileClip加载视频文件

video = VideoFileClip(input_file)

# 保存为MP4格式

video.write_videofile(output_file)
