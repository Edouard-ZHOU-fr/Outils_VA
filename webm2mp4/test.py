from moviepy.editor import VideoFileClip
import time
import taichi as ti

# ti.init(arch=ti.gpu)
# @ti.kernel
def main():
    input_file = "/home/hongyu/SETUP/larochelle/1.webm"
    output_file = "/home/hongyu/SETUP/larochelle/1.mp4"

    # 使用VideoFileClip加载视频文件

    video = VideoFileClip(input_file)

    # 保存为MP4格式
    video.write_videofile(output_file)


main()