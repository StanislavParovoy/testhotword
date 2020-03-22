# testhotword
Тестируем hotrword с https://github.com/Picovoice/porcupine 

Для начала установим модули:

pip install numpy
pip install pyaudio
pip install soundfile
pip install pvporcupine
pip install speech_recognition

Далее запустим скрипт demohotword.py

В нашем случае используется ключевое слово "Амэрикано", произнесенное с английским акцентом

После произнесения ключевого слова через паузу в 1 сек можно говорить что-то вслух, тестовая программа распознает и напечатает вашу команду

https://github.com/Picovoice/porcupine/tree/master/resources/keyword_files/windows

Вы можете создать себе другое ключевое слово тут: https://console.picovoice.ai/

В этом репозитории лежит библиотека под win7x64, если у вас другая ОС, смотрите библиотеки на https://github.com/Picovoice/porcupine 


