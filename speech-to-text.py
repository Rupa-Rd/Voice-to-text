
from PIL import Image
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = '<YOUR_SPEECH_KEY>'
SPEECH_REGION = '<LOCATION>'
#IMAGE PATH IMPORT

def words_separation(words_list) :
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "for",
                       "are", "was", "were", "be", "been", "being", "in", "have", "has", "had", "do", "does", "did",
                       "but", "at", "by", "with", "from", "here", "when", "where", "how", "down", "all", "any",
                       "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",
                       "into", "one",  "could", "would", "should", "here", "there", "about", "on", "upon",
                       "so", "up", "down", "above", "under", "so", "then", "than", "may","."]
    numbers = '0123456789'
    word1 = words_list.replace('.','').replace(',','')
    word = word1.split(' ')
    for i in word:
        i.lower()
        for j in i :
            if j in numbers:
                yield j
            else:

                yield i
                break



def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        word_list = str(speech_recognition_result.text)
        print("Recognized: {}".format(word_list))
        print("Words : ")
        obj = words_separation(word_list)
        for i in obj:
            # img = Image.open(f"E:/pythonProject/cfg-week-1/venv/Sign_language/{i}.jpeg")
            # img.show()
            print(i)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone()
