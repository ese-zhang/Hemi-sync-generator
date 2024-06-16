# Hemi-sync-generator
把所爱的音乐，生成对应的双脑同步音频，有多种同步模式选择，仅仅支持WMV格式。
该Python程序允许您对多个音频文件应用双耳节拍处理。它支持三种双耳节拍处理模式：
1. 在左右声道上加载额外的频率。
2. 调整原有音轨的频率。
3. 通过相移生成双耳节拍。

This Python program allows you to apply binaural beat processing to multiple audio files. It supports three modes of binaural beat processing:
1. Adding extra frequencies to the left and right channels.
2. Modifying the original frequency of the audio track.
3. Generating beat frequencies by phase-shifting the left and right ears.

## 功能 | Features

- 支持选择多个音频文件进行处理。
- 三种双耳节拍处理模式：
  - **加载额外频率**：在左右声道添加不同频率的音频信号。
  - **直接修改原有频率**：调整原有音轨的频率来生成双耳节拍。
  - **左右耳相移产生拍频**：通过相移操作生成双耳节拍。
- 图形用户界面（GUI），使用方便。
- 显示处理进度的进度条。

- Select multiple audio files for processing.
- Three modes of binaural beat processing:
  - **Add Frequency**: Adds different frequencies to the left and right channels.
  - **Modify Frequency**: Adjusts the frequency of the original audio track.
  - **Phase Shift**: Generates binaural beats by phase-shifting the audio.
- Graphical User Interface (GUI) for ease of use.
- Progress bar to display processing status.

## 前提条件 | Prerequisites

确保您已安装以下Python库：

Make sure you have the following Python libraries installed:

pydub numpy scipy

确保您把ffmpeg放入路径

Make sure you have add your ffmpeg into the system path.

## 使用方法| Usage

1. 克隆仓库| Clone the repository

git clone https://github.com/ese-zhang/binaural-beats-audio-processor.git

cd binaural-beats-audio-processor

2. 编译代码|Make up

pyinstaller --onefile --windowed --name binaural_beat_generator binaural_beat_generator.py

pyinstaller binaural_beat_generator.spec

3. 运行|Run

在dist中运行exe文件。

run exe in folder dist.

4. 使用| Enjoy it.


## 代码解释 | Code Explanation

### 主要功能 | Main Functions

**load_files**: 允许用户选择多个音频文件进行处理。

**choose_output_folder**: 允许用户选择输出文件夹。

**process_files**: 根据用户选择的模式和频率差处理选定的文件。

**process_file**: 根据选择的双耳节拍处理模式处理单个音频文件。

**add_frequency**: 向音频通道添加指定频率。

**modify_frequency**: 修改音频通道的频率。

**phase_shift**: 通过相移操作生成双耳节拍。

**load_files**: Allows the user to select multiple audio files for processing.

**choose_output_folder**: Allows the user to choose the output folder.

**process_files**: Processes the selected files based on the chosen mode and frequency difference.

**process_file**: Applies the selected binaural beat processing mode to a single audio file.

**add_frequency**: Adds a specified frequency to the audio channel.

**modify_frequency**: Modifies the frequency of the audio channel.

**phase_shift**: Phase-shifts the left and right audio channels to create binaural beats.


## 贡献 | Contributing

欢迎贡献！请随时提交拉取请求。

Contributions are welcome! Please feel free to submit a Pull Request.
## 许可证 | License

此项目使用 MIT 许可证。详情请参阅 LICENSE 文件。

This project is licensed under the MIT License. See the LICENSE file for details.
## 致谢 | Acknowledgments

该程序使用了以下库：

pydub
numpy
scipy

This code is totally generated using chatgpt4o. The prompt is

需求说明

你需要一个 Python 程序，该程序能够对音频文件应用双耳节拍处理。具体需求包括以下几点：

功能描述：

支持选择多个音频文件进行处理。

支持三种模式的双耳节拍处理：

加载额外频率：在左右声道上加载额外的频率。

直接修改原有频率：调整原有音轨的频率。

左右耳相移产生拍频：通过相移生成双耳节拍。

GUI界面：

选择文件按钮：允许用户选择多个音频文件。

输出文件夹按钮：允许用户选择输出文件夹。

输入频率差的文本框：用户输入频率差。

模式选择菜单：用户选择三种模式中的一种。

导出按钮：执行音频处理并导出结果。

进度条：显示处理进度。

处理逻辑：

对于“加载额外频率”模式，分别在左右声道添加不同频率的音频信号。

对于“直接修改原有频率”模式，通过调整音轨的频率来生成双耳节拍。

对于“左右耳相移产生拍频”模式，通过相移操作生成双耳节拍，同时确保数组大小一致。

## 联系方式 | Contact

如果您有任何问题或建议，请提交问题或联系我：hectorzhang4253@gmail.com

If you have any questions or suggestions, please open an issue or contact me at hectorzhang4253@gmail.com
