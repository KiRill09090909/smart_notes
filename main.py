import whisper

m = whisper.load_model('base')
result = m.transcribe('lesson.m4a')
print(result['text'])