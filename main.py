from mylib.signal_utils import modulate
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

def record_and_process():
    duration = 2
    sample_rate = 44100
    
    print("Recording in 3... 2... 1...")
    print("SPEAK NOW!")
    
    # Record audio
    audio = sd.rec(int(duration * sample_rate), 
                   samplerate=sample_rate, 
                   channels=1)
    sd.wait()
    
    print("Recording finished!")
    print(f"Audio shape: {audio.shape}")
    print(f"Audio max value: {np.max(np.abs(audio))}")
    
    # Check if audio was captured
    if np.max(np.abs(audio)) < 0.001:
        print("⚠️ No audio detected! Check microphone permissions.")
        return
    
    # Convert to 1D and take first 1000 samples
    audio = audio.flatten()[:1000]
    echo = audio * 0.5
    
    # Use your function
    result = modulate(audio.tolist(), echo.tolist(), 0, 100)
    
    print("Processing complete!")
    
    # Force plot to show
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(audio)
    plt.title('Your Voice')
    
    plt.subplot(2, 1, 2)
    plt.plot(result)
    plt.title('Voice × Echo Effect')
    
    plt.show(block=True)  # Force display
    print("Plot should be visible now!")

if __name__ == "__main__":
    record_and_process()