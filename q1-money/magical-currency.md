+ محدودیت زمان: ۱ ثانیه
+ محدودیت حافظه: ۲۵۶ مگابایت

----------
حسن به تازگی صرافی خودش را باز کرده است. و می‌خواهد کارکنان بتوانند به راحتی مقادیر ارزی را به هم تبدیل کرده و با آن‌ها کار کنند. برای این کار او می‌خواهد پشتیبانی مقادیر مالی را به پایتون اضافه کند. برای این کار کلس Money را ایجاد کرده و امکانات خواسته شده را به آن اضافه کنید.

پایتون توابعی به نام توابع جادویی یا Magic Methods دارد که بر حسب نیاز در کارهایی که روی آبجکت انجام می‌شود آن‌ها را فراخوانی می‌کند. برای مثال وقتی عبارت 2 + 5 را حساب می‌کند در واقع مقدار `2.__add(5)__` را حساب می‌کند (می‌توانید عبارت دوم را هم در پایتون امتحان کنید.) یا برای `print(a)` در واقع `print(a.__str()__)` یا `print(str(a))` اجرا می‌شود (با کمی اغماض). حال ما می‌خواهیم با ویرایش و یا اضافه کردن این توابع به کلس خود ویژگی‌های معمول مثل جمع و تفریق را به آبجکت خود اضافه کنیم تا بتوان با این مقادیر پولی راحت کار کرد.

ابتدا ارزها و نرخ‌هایشان را به تومان را با این دیکشنری در کد خود ذخیره کنید:
```json
rates = {
    "IRT": 1,
    "USD": 59700,
    "EUR": 64550,
    "GBP": 75800,
    "CHF": 66450,
    "CAD": 43350,
    "TRY": 1845
}
```

# ویژگی‌ها
کلس شما باید دو متغییر ‍`amount` و ‍`currency` را به ترتیب هنگام ساخت گرفته و ذخیره کند که نشان می‌دهد چه میزان پول و به چه واحدی است.

مثلا برای ده دلار پول:
```python
a = Money(10, 'USD')
```

## امکان چاپ
باید بتوان آبجکتی از جنس پول را به درستی نمایش داد. برای این کار تابع ‍‍`__str__(self)`  و `__repr__(self)` را در کلس ایجاد و بازنویسی کنید تا در صورت چاپ شدن آبجکت یا تبدیل آن به رشته مقدار آن در کنار واحد پول نشان داده شود:
```python
>>> a = Money(100000, 'IRT')
>>> print(a)
>>> 10000 IRT
```

```python
>>> print([Money(100, "USD"), Money(2000, "IRT")])
print([Money(100, "USD"), Money(2000, "IRT")])
```

## جمع و تفریق پول
باید بتوانیم دو مقدار پول را به طور طبیعی در پایتون با هم جمع کنیم. حاصل از جنس Money است و واحد پول اولی را دارد (سمت چپ جمع). مقدار آن جمع مقدار اولی و مقدار معادل دومی است. دومی را با استفاده از نسبت نرخ‌ها به واحد پول اول تبدیل کنید. (یا به طور معادل می‌توانید همه را به تومان تبدیل کنید و نهایتا به واحد اولی تبدیل کنید.)

برای این قسمت باید توابع `__add__` و `__sub__` را بازنویسی کنید.

راهنمایی: از آنجایی که نرخ تومان برابر ۱ در نرخ‌ها وجود دارد هیچ گاه لازم نیست برای تومان در کدتان حالت خاص قائل شوید.

### مثال
```python
>>> a = Money(1, 'USD')
>>> b = Money(1, 'EUR')
>>> a + b
2.0812395309882747 USD
```


## ضرب پول در عدد
حاصل از جنس پول است و مقدار آن برابر با ضرب مقدار پول در عدد است.

### مثال
```python
>>> a = Money(10000, 'IRT')
>>> a * 2
20000 IRT
```


## تقسیم
در صورتی که پول بر پول تقسیم شود حاصل از جنس عدد و برابر با ارزش تومانی اولی تقسیم بر ارزش تومانی دومی است. در صورتی که پول بر عدد تقسیم شود حاصل از جنس پول و در واحد پول اولی است و مقدار آن مقدار پول تقسیم بر عدد است. تقسیم عدد بر پول ممکن نیست، البته کد شما لازم نیست این حالات را چک کند و تضمین می‌شود ورودی‌ها بدون خطا هستند.

### مثال
```python
>>> Money(2, 'GBP') / Money(1, 'USD')
2.539363484087102
>>> Money(2, 'USD') / 2
1.0 USD
```

## تقسیم صحیح
مشابه تقسیم معمولی ولی تقسیم صحیح.

### مثال
```python
>>> Money(2, 'GBP') // Money(1, 'USD')
151
>>> Money(2.1, 'USD') // 2
1.0 USD
```

## کوچک‌تری و بزرگ‌تری
توابع ‍`__lt__(self, other)` (کوچک‌تر)، `__le__(self, other)` (کوچک‌تر مساوی)، `__gt__(self, other)` (بزرگ‌تر)، و `__ge__(self, other)` را به کلس اضافه کنید تا بتوان بین پول‌ها مقایسه انجام داد. پول a وقتی از پول b بزرگ‌تر (مساوی) است که ارزش تومانی a از b بیشتر (مساوی) باشد. و برعکس برای کوچک‌تر.

### مثال
```python
>>> Money(2, 'GBP') > Money(1, 'USD')
True
>>> Money(1, 'USD') <= Money(40000, 'IRT')
False
>>> sorted([Money(1, 'USD'), Money(1, 'EUR'), Money(1, 'CHF'), Money(50000, 'IRT')])
[50000 IRT, 1 USD, 1 EUR, 1 CHF]
```

## تبدیل
تابع `convert(target)` را ایجاد کنید که خروجی آن از جنس پول و برابر با مقدار تبدیل شده با نرخ مقصد است.

### مثال
```python
>>> (Money(2, 'USD') - Money(30000, 'IRT')).convert('TRY') + Money(1, 'EUR')
83.44173441734418 TRY
```


# ورودی
در خط اول عدد صحیح n می‌آید که تعداد ورودی‌هایی که باید ارزیابی شوند را نشان می‌دهد. سپس در n خط بعدی در هر خط یک عبارت می‌آید که باید ارزیابی شوند. برای ارزیابی آن‌ها از تابع `eval()` پایتون استفاده کنید و خروجی را چاپ کنید.

راهنمایی: پس از پیاده سازی کلاس کد زیر را قرار دهید:
```python
for _ in range(int(input())):
    print(eval(input()))
```


## ورودی نمونه ۱
```python
9
Money(1, 'USD') + Money(10000, 'IRT')
Money(100, 'TRY') + Money(20, 'EUR')
(Money(2, 'USD') - Money(30000, 'IRT')).convert('EUR')
Money(20, 'CAD') / Money(1, 'USD')
Money(20, 'CAD') // Money(1, 'USD')
Money(20, 'CAD') / 3.5 + Money(10000, 'IRT')
Money(100, 'CAD') > Money(150, 'USD')
Money(100, 'CAD') < Money(150, 'USD')
sorted([Money(1, 'USD'), Money(1, 'EUR'), Money(1, 'CHF'), Money(10000, 'IRT')])
```

## خروجی نمونه ۱
```
1.16750418760469 USD
799.7289972899729 TRY
1.3849728892331525 EUR
14.522613065326633
14
5.944966221782831 CAD
False
True
[10000 IRT, 1 USD, 1 EUR, 1 CHF]
```