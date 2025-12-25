from gtts import gTTS
from dotenv import load_dotenv
import os
load_dotenv()

def text_to_speech_with_gtts_old(text,output_filepath):
    language = 'hi'  # Hindi language code

    audioobj=gTTS(
        text=text, lang=language,slow=False
    )

    audioobj.save(output_filepath)





from elevenlabs.client import ElevenLabs

def text_to_speech_with_elevenlabs_old(input_text,output_filepath):
    client = ElevenLabs(
        api_key=os.environ.get("ELEVENLABS_API_KEY")  # Defaults to os.environ.get("ELEVEN_API_KEY")
    )
    
    # Get the audio stream
    audio_stream = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel - a standard voice ID
        output_format="mp3_22050_32",
        text=input_text
    )
    
    # Save the audio stream to file
    with open(output_filepath, "wb") as audio_file:
        for chunk in audio_stream:
            if chunk:
                audio_file.write(chunk)
    
    print(f"Audio saved to {output_filepath}")
     


import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language="hi"  # Hindi language code

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(
        api_key=os.environ.get("ELEVENLABS_API_KEY")  # Defaults to os.environ.get("ELEVEN_API_KEY")
    )
    
    # Get the audio stream
    audio_stream = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel - a standard voice ID
        output_format="mp3_22050_32",
        text=input_text,
        model_id="eleven_multilingual_v2"  # Using multilingual model for Hindi support
    )
    
    # Save the audio stream to file
    with open(output_filepath, "wb") as audio_file:
        for chunk in audio_stream:
            if chunk:
                audio_file.write(chunk)
    
    print(f"Audio saved to {output_filepath}")
    
    # Enable automatic audio playback after saving
    os_name = platform.system()
    try:
        if os_name == "Darwin": 
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  
            subprocess.run(['aplay', output_filepath])  
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    
    return output_filepath



