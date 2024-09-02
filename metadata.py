import subprocess

def extract_image_metadata(image_path):
    '''
    Extracts metadata from an image using ExifTool.
    :param image_path: Path to the image file.
    :return: Metadata as a string.
    '''
    try:
        result = subprocess.run(['exiftool', image_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stderr:
            print("Error:", result.stderr.decode('utf-8'))
        metadata = result.stdout.decode('utf-8')
        return metadata
    except FileNotFoundError:
        return "ExifTool not found. Please ensure ExifTool is installed and in your PATH."

def extract_video_metadata(video_path):
    """
    Extracts metadata from a video using FFmpeg.
    :param video_path: Path to the video file.
    :return: Metadata as a string.
    """
    try:
        command = ['ffmpeg', '-i', video_path]
        result = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        # FFmpeg outputs metadata to stderr
        metadata = result.stderr.decode('utf-8')
        return metadata
    except FileNotFoundError:
        return "FFmpeg not found. Please ensure FFmpeg is installed and in your PATH."

def extract_video_frame(video_path, time, output_image):
    """
    Extracts a frame from a video at a specified time.
    :param video_path: Path to the video file.
    :param time: The timestamp in the video (e.g., '00:00:10' for 10 seconds).
    :param output_image: Path where the extracted frame will be saved.
    """
    try:
        command = ['ffmpeg', '-i', video_path, '-ss', time, '-vframes', '1', output_image]
        subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print(f"Frame extracted and saved to {output_image}")
    except FileNotFoundError:
        print("FFmpeg not found. Please ensure FFmpeg is installed and in your PATH.")

# Example usage:
if __name__ == "__main__":
    # Extract metadata from an image
    image_metadata = extract_image_metadata('C:\\Users\\RAIKAT\\OneDrive\\Documents\\rail-madad\\images.jpg')
    print("Image Metadata:\n", image_metadata)
    
    # Extract metadata from a video
    video_metadata = extract_video_metadata('C:\\Users\\RAIKAT\\OneDrive\\Documents\\rail-madad\\video.mp4')
    print("Video Metadata:\n", video_metadata)
    
    # Extract a frame from the video at the 10th second
    extract_video_frame('C:\\Users\\RAIKAT\\OneDrive\\Documents\\rail-madad\\video.mp4', '00:00:07', 'C:\\Users\\RAIKAT\\OneDrive\\Documents\\rail-madad\\frame.jpg')
