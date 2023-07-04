# Speech to Text Conversion with Azure Cognitive Services

This repository contains a Python script that utilizes Azure Cognitive Services for converting speech/voice into text and breaking it into words. The script makes use of Azure's Speech to Text service, which provides accurate and real-time transcription capabilities.

## Prerequisites

To run the script, ensure you have the following:

- Python 3.x installed on your machine
- Azure Cognitive Services subscription key and endpoint. You can obtain these by creating a Speech resource in the Azure portal.

## Setup and Usage

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install azure-cognitiveservices-speech`.
3. Open the `convert_speech_to_text.py` script and replace `<YOUR_SUBSCRIPTION_KEY>` and `<YOUR_ENDPOINT>` with your actual subscription key and endpoint values.
4. Run the script using `python convert_speech_to_text.py`.
5. Provide the path to the audio file or specify the audio input source.
6. The script will connect to Azure Cognitive Services, transcribe the speech, and display the resulting text along with the individual words.

Feel free to modify the script as per your specific requirements or integrate it into your existing projects.

## Resources

- [Azure Cognitive Services Documentation](https://docs.microsoft.com/azure/cognitive-services/)
- [Azure Speech Service Documentation](https://docs.microsoft.com/azure/cognitive-services/speech-service/)

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.
