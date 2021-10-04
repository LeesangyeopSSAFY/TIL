CREATE TABLE countries (
id INTEGER PRIMARY KEY,
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER
);

INSERT INTO countries VALUES
(1, 'B203', '2019-12-31', '2020-01-03', 'suite', 900),
(2, '1102', '2020-01-04', '2020-01-08', 'suite', 850),
(3, '303', '2020-01-01', '2020-01-03', 'deluxe', 500),
(4, '807', '2020-01-04', '2020-01-07', 'superior', 300);

ALTER TABLE countries RENAME TO hotels;

SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

SELECT grade, COUNT(*) FROM hotels ORDER BY COUNT(*) DESC GROUP BY grade;

SELECT * FROM hotels WHERE room_num='B%' OR grade='deluxe';

SELECT * FROM hotels WHERE NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price;


User.objects.all()

User.objects.filter(id=19).values('age')

User.objects.all().values('age')

User.objects.filter(age__lte=40).values('id', 'balance')

User.objects.filter(last_name='김', balance__gte=500).values('first_name')

User.objects.filter(first_name__endswith='수', country='경기도').values('balance')

User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()

User.objects.filter(phone__startswith='010-').count()

user = User.objects.get(first_name='옥자', last_name='김')
user.country = '경기도'
user.save()

User.objects.get(first_name='옥자', last_name='김').update(country='경기도')

User.objects.get(first_name='진호', last_name='백').delete()

User.objects.order_by('-balance')[:4].values('first_name', 'last_name', 'balance')

User.objects.filter(phone__contains='123', age__lt=30)

User.objects.filter(phone__startswith='010').values('country').distinct()

User.objects.all().aggregate(Avg('age'))

User.objects.filter(last_name='박').aggregate(Avg('balance'))

User.objects.filter(country='경상북도').aggregate(Max('balance'))

User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[0]