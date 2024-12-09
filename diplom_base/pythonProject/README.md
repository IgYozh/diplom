# Сравнение подходов к реализации асинхронного программирования с использованием asyncio, threading и multiprocessing.


**Цель проекта:** 
Произвести оценку производительности и уместности использвоания трех ключевых подходов 
к асинхронному програмированию, а именно asyncio, threading, multiprocessing.

**Тема для проводимых задач:** Для реализации задач в формате дипломной работы,
мною была выбрана тема финансового рынка и её компонентов. В связи с личным интересом, а
также мотивацией реализовать полноценный проект-приложение в будущем. Также для чистоты сравнения
была использована CPU-bound задача требующая больших вычислений. 

**Количество задач с использованием 3 подходов:** 4 шт.

**Файловая структура проекта:**


```pythonProject
├── .idea
├── .venv
├── Task_1
│   ├── Async.py
│   ├── Multiproces.py
│   └── Thread.py
├── Task_2
│   ├── Async.py
│   ├── Multiproces.py
│   └── Thread.py
├── Task_3
│   ├── Async.py
│   ├── Multiproces.py
│   └── Thread.py
├── Task_4
│   ├── Async.py
│   ├── Multiproces.py
│   └── Thread.py
├── README.md
├── folders_structure.txt
└── requirements.txt
```
**Список необходимых библиотек:**

asyncio==3.4.3
aiohttp==3.11.9
requests==2.32.3
aiofiles==24.1.0
yfinance==0.2.50
beautifulsoup4==4.12.3
aiohttp_request==0.0.2
aiosignal==1.3.1
numpy==2.1.3
pandas==2.2.3
pillow==11.0.0

