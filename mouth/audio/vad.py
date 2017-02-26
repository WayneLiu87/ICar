from vad import VAD
detector = VAD(fs=16000)
speech = detector.detect_speech(sig, fs)