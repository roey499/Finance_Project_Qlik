#משתמשים ב־ image רשמי של Python (קטן וקל).
FROM python:3.11-slim

#מגדיר את תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

#מתקין ספריות Python הדרושות ל־Excel.
RUN pip install pandas openpyxl

#מעתיק את קובץ הקוד מהמחשב לתוך ה־ image. 
COPY TestPandas.py .

CMD ["python", "TestPandas.py"]
