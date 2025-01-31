from datetime import timedelta
import os
import whisper

def transcribe_audio(path):
    model = whisper.load_model("medium")  # Change this to your desired model
    print("Whisper model loaded.")
    
    # Add the 'language' parameter set to English ('en')
    transcribe = model.transcribe(audio=path, verbose=True, language="en")
    segments = transcribe['segments']

    for segment in segments:
        startTime = str(0) + str(timedelta(seconds=int(segment['start']))) + ',000'
        endTime = str(0) + str(timedelta(seconds=int(segment['end']))) + ',000'
        text = segment['text']
        segmentId = segment['id'] + 1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        # Ensure the directory "SrtFiles" exists
        os.makedirs("SrtFiles", exist_ok=True)
        
        srtFilename = os.path.join("SrtFiles", f"VIDEO_FILENAME.srt")
        with open(srtFilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)

    return srtFilename

# Call the function with your video file
transcribe_audio("video.mp4")
