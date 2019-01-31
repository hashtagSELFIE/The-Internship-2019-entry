# Weather

โปรแกรมนี้จะอ่านไฟล์โจทย์นามสกุล .xml (Extensible Markup Language) และส่งออกข้อมูลเป็น .json (๋JavaScript Object Notation) ด้วย Python xmltodict package

# วิธีการรันโปรแกรม

1. เช็คดูให้แน่ใจว่า Path Terminal ของท่าน อยู่ที่โฟลเดอร์ที่ตั้งเดียวกันกับไฟล์ converter.py และโฟลเดอร์นั้นมีไฟล์ weather.xml
3. ติดตั้งแพ็คเกจ xmltodict (ในกรณีที่ยังไม่ได้ติดตั้ง) โดยสามารถติดตั้งได้โดยการพิมพ์คำสั่งดังกล่าว
```
pip3 install xmltodict
```
4. รันโปรแกรม โดย Windows OS สามารถรันได้ ดังนี้<br>

  ```
  py converter.py
  ```

  และ MacOS กับ Linux สามารถรันได้ ดังนี้<br>

  ```
  python3 converter.py
  ```

5. โปรแกรมจะสามารถรันได้ :smile: และสามารถใช้งานตัวโปรแกรม ผ่าน built-in menu ได้ทันท
6. เมื่อเข้าโปรแกรมมาแล้ว จะสามารถกด ```ENTER```เพื่อแปลงไฟล์ตัวอย่าง (weater.xml) ทันที <br> หรือสามารถพิมพ์ ```SUDO``` ตามด้วย Enter เพื่อทำการแปลงไฟล์ .xml ของท่านเอง (กรุณาเซฟไฟล์ .xml ของท่านไว้ในโฟลเดอร์เดียวกันกับ ไฟล์ converter.py นี้)

ี<br>

## สิ่งที่โปรแกรมสามารถทำได้

- สามารถแปลงไฟล์ .xml เป็น .json ได้
  - แปลงเป็นไฟล์ .json โดยที่มี indent 2 spaces
  - แปลงไฟล์ object ของ Current ได้ (Support ไฟล์ตัวอย่าง weather.xml เท่านั้น)

- มีระบบเมนู ที่ผู้ใช้สามารถเลือกโหมด, ยืนยัน โปรแกรมได้

- สามารถแสดงสถานะในการแปลงไฟล์ได้

- สามารถเรียกใช้งานได้ใน Windows, MacOS และ Linux

## แหล่งข้อมูลที่ใช้

- xmltodict package by martinblech <br>
  https://pypi.org/project/xmltodict/
- https://stackoverflow.com/questions/2084508/clear-terminal-in-python
- https://github.com/martinblech/xmltodict/issues/77
- https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
- https://medium.com/@MicroPyramid/how-to-convert-xml-content-into-json-using-xmltodict-3ab92bff913e
