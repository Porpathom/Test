﻿﻿﻿﻿# 🐸	 My Test
- [My Test](#My-Test)
    - [1. Models](#1-Models)
    - [2. Page](#2-Page)
    - [3. เชื่อมต่อฐานข้อมูลไปยัง Supabase ใน settings.py](#3-เชื่อมต่อฐานข้อมูลไปยัง-supabase-ใน-settingspy)
    - [4. การแยกส่วนพัฒนา Projects](#4-การแยกส่วนพัฒนา-projects)
    - [5. deploy บน Vercel](#5-deploy-บน-Vercel)
    
## 1. Models
>**🐢	 Model Employ**
```py
class Employ(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.IntegerField(choices=SEX_CHOICES, default=1)
    age = models.CharField(max_length=25)
    education = models.IntegerField(choices=EDUCATION_CHOICES, default=None)
    dep =models.ForeignKey(Department, on_delete=models.CASCADE,default=None)
    
    class Meta:
        verbose_name = "Employ"
        verbose_name_plural = "Employs"

    def __str__(self):
        return self.first_name + " "+self.last_name
```
>**🐢	 Model Department**
```py
class Department(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name
```
>**🐢	 Choices**
```py
SEX_CHOICES = [
    (1,'ชาย'),
    (2,'หญิง'),
]

EDUCATION_CHOICES = [
    (1,'ปวช.'),
    (2,'ปวส.'),
    (3,'ปริญญาตรี'),
    (4,'สูงกว่าปริญญาตรี')
]

```
## 2. Page
![image]()
>**🦎	 [index.html](https://github.com/Porpathom/Fntest/blob/main/templates/index.html)**


![image]()
>**🦎	 [details.html](https://github.com/Porpathom/Fntest/blob/main/templates/details.html)**


![image]()
>**🦎	 [department.html](https://github.com/Porpathom/Fntest/blob/main/templates/department.html)**


![image]()
>**🦎	 [department_details.html](https://github.com/Porpathom/Fntest/blob/main/templates/details_dep.html)**


![image]()
>**🦎	 [about.html](https://github.com/Porpathom/Fntest/blob/main/templates/about.html)**

![image]()
>**🦎	 [admin](https://fntest.vercel.app/admin)**


>**🐛	 user: admin**
>**🐛	 password: admin**
        

## 3. เชื่อมต่อฐานข้อมูลไปยัง Supabase ใน [settings.py]()
```py
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER' :'postgres',
        'PASSWORD' :'???',
        'HOST' : '???',
        'PORT' : ''
    }
}   
```
>**🐍 โดยจะมีการใช้คำสั่ง dumpdata ให้ข้อมูลอยู่ในรูปแบบของ JSON และ loaddata เพื่อย้ายไปยังฐานข้อมูลใหม่**

```sh
python manage.py dumpdatautf8 --output data.json
```

>**🐍 dumpdata การ copy ฐานข้อมูลเดิมออกมา**
```sh
python manage.py loaddatautf8 data.json
```
>**🐍 loaddata การนำฐานข้อมูลลงไปยังฐานข้อมูลใหม่**

## 4. การแยกส่วนพัฒนา Projects
>**🔺 การแยกส่วนพัฒนาโดยมีการเพิ่มไฟล์ [manage_dev.py]() เพื่อเรียกใช้ [settings_dev.py]() สำหรับการพัฒนา Projects โดยแยกออกจาก Deploy**

```py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fntest.settings_dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```
## 5. deploy บน [Vercel](https://fntest.vercel.app/)
![image]()
