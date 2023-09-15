﻿# 🐸	 My Test
- [My Test](#My-Test)
    - [1. Models](#1-Models)
    - [2. Page](#2-Page)
    - [3. เชื่อมต่อฐานข้อมูลไปยัง Supabase ใน settings.py](#3-เชื่อมต่อฐานข้อมูลไปยัง-supabase-ใน-settingspy)
    - [4. การแยกส่วนพัฒนา Projects](#4-การแยกส่วนพัฒนา-projects)
    - [5. deploy บน Vercel](#5-deploy-บน-Vercel)
    
## 1. Models
>**🐢	 Model Category**
```py
class Article(models.Model):
    head_line = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    pub_data = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE, default=1)
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Article"

    def __str__(self):
        return self.head_line + self.reporter

    def get_absolute_url(self):
        return reversed("Article_detail", kwargs={"pk": self.pk})
```
>**🐢	 Model Subject**
```py
class Subj(models.Model):
    subj_code = models.CharField(max_length=25)
    subj_name = models.CharField(max_length=255)
    credit = models.CharField(max_length=25)
    semester = models.CharField(max_length=25)
    year = models.CharField(max_length=25)
    cate =models.ForeignKey(Cate, on_delete=models.CASCADE,default=None)

    class Meta:
        verbose_name = "Subj"
        verbose_name_plural = "Subjs"

    def __str__(self):
        return self.subj_name
```
## 2. Page
![image](https://github.com/Porpathom/Test/blob/main/image/home.png)
>**🦎	 [index.html](https://github.com/Porpathom/Test/blob/main/templates/index.html)**


![image](https://github.com/Porpathom/Test/blob/main/image/details.png)
>**🦎	 [details.html](https://github.com/Porpathom/Test/blob/main/templates/details.html)**


![image](https://github.com/Porpathom/Test/blob/main/image/category.png)
>**🦎	 [category.html](https://github.com/Porpathom/Test/blob/main/templates/category.html)**


![image](https://github.com/Porpathom/Test/blob/main/image/details_category.png)
>**🦎	 [category_details.html](https://github.com/Porpathom/Test/blob/main/templates/details_cate.html)**


![image](https://github.com/Porpathom/Test/blob/main/image/about.png)
>**🦎	 [about.html](https://github.com/Porpathom/Test/blob/main/templates/about.html)**

## 3. เชื่อมต่อฐานข้อมูลไปยัง Supabase ใน [settings.py]()
```py
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER' :'postgres',
        'PASSWORD' :'pathom0966788627',
        'HOST' : 'db.exbttefhfhatmktvkfyj.supabase.co',
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
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Test.settings_dev')
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
## 5. deploy บน [Vercel](https://test-indol-three-90.vercel.app/)
![image]()
