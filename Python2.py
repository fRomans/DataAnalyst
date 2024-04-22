import pandas as pd

# df = pd.read_csv('R:\AProgr\data analyst\downloadfiles\lesson_1_data.csv', encoding = 'windows-1251',sep = ';')
# print(df.tail())
# print(df.head())
# print(df.shape)
# print(df.dtypes)
# df.shape
#
# df = df.rename(columns={'Номер': 'number',
#                         'Дата создания': 'create_date',
#                         'Дата оплаты': 'payment_date',
#                         'Title': 'tittle',
#                         'Статус': 'status',
#                         'Заработано': 'money',
#                         'Город': 'city',
#                         'Платежная система': 'payment_system'})
# print(df.columns)
#
# def send_product_report(file_path):
#     df = pd.read_csv(file_path,
#                      encoding='windows-1251', sep=';')
#     df = df.rename(columns={'Номер': 'number',
#                             'Дата создания': 'create_date',
#                             'Дата оплаты': 'payment_date',
#                             'Title': 'tittle',
#                             'Статус': 'status',
#                             'Заработано': 'money',
#                             'Город': 'city',
#                             'Платежная система': 'payment_system'})
#     all_money = df.money.sum()
#
#     money_title = df \
#         .query("status == 'Завершен'") \
#         .groupby(['tittle'], as_index=False) \
#         .aggregate({'money': 'sum', 'number': 'count'}) \
#         .sort_values('money', ascending=False) \
#         .rename(columns={'number': 'success_orders'})
#
#     today_day = datetime.today().strftime('%Y-%m-%d')
#     file_name = 'money_title_{}.csv'
#     file_name = file_name.format(today_day)
#
#     if int(money_title.money.sum()) == int(all_money):
#         print('OK! File {} is written.'.format(file_name))
#         money_title.to_csv(file_name, index=False)
#     else:
#         print('ERROR!')
#
#     return money_title
#
# _________________________________________________________________________________________

bookings = pd.read_csv('R:\AProgr\data analyst\downloadfiles\\bookings.csv', encoding = 'windows-1251',sep = ';')


# print(bookings)
#
# booking_list = bookings.columns.to_list()
# new_list = []
# for elbook in booking_list:
#
#     strng = str(elbook)
#     #     strng.trim()
#     strng = strng.lower()
#     strng = strng.replace(' ', '_')
#     new_list.append(strng)
# print(new_list)
#
#
# for new, boo in zip(new_list, booking_list):
#     bookings = bookings.rename(columns={boo : new})
#
#
# print(bookings.dtypes)
#
# bookings_head = bookings.head(7)
#
# print(bookings_head)
#
# country = bookings \
#     .query("is_canceled == 0") \
#     .groupby(['country'], as_index=False) \
#     .agg({'is_canceled': 'count'}) \
#     .sort_values('is_canceled')
#
# print(country.head(5))
#
# avrg = bookings \
#     .groupby(['hotel'], as_index=False) \
#     .agg({'stays_total_nights': 'mean'}) \
#
# print(avrg.round(2))
#
#
#
#
# ecuals = bookings \
#     .query("assigned_room_type != reserved_room_type") \
#
# print(ecuals.shape)
#
# arrivM = bookings \
#     .query("arrival_date_month == 'May'") \
#     .groupby(['arrival_date_year'], as_index=False) \
#     .agg({'arrival_date_month': 'count'}) \
#     .sort_values('arrival_date_month') \
#
# print(arrivM)
#
# arrivO = bookings \
#     .query("arrival_date_month == 'October'") \
#     .groupby(['arrival_date_year'], as_index=False) \
#     .agg({'arrival_date_month': 'count'}) \
#     .sort_values('arrival_date_month') \
#
# print(arrivO)
#
# arrivS = bookings \
#     .query("arrival_date_month == 'September'") \
#     .groupby(['arrival_date_year'], as_index=False) \
#     .agg({'arrival_date_month': 'count'}) \
#     .sort_values('arrival_date_month') \
#
# print(arrivS)
#
# canceled = bookings \
#     .query("hotel == 'City Hotel'") \
#     .query("is_canceled == 1") \
#     .groupby(['arrival_date_year','arrival_date_month'], as_index=False) \
#     .agg({'is_canceled': 'count'}) \
#     .sort_values('is_canceled', ascending=False) \
#
# print(canceled)
#
# znach = bookings \
#     .groupby(['adults','children','babies'], as_index=False) \
#     .agg({'adults': 'mean', 'children': 'mean', 'babies': 'mean'}) \
#
# print(znach.idxmax())
#
# bookings['total_kids'] = bookings['children'] + bookings['babies']
# child = bookings \
#     .groupby(['hotel'], as_index=False) \
#     .agg({'total_kids': 'mean'}) \
#     .sort_values('total_kids', ascending=False) \
#
# print(child.round(2))

# ___________________________________________________________________________

bookings['has_kids'] = bookings['total_kids'].astype(bollean)

cens = bookings \
    .query("has_kids == True") \
    .query("is_canceled == 1") \
    .groupby(['has_kids'], as_index=False) \
    .agg({'has_kids': 'sum'}) \
    .sort_values('has_kids', ascending=False) \

bookings.head(3)

cens

nocens = bookings \
    .query("has_kids == True") \
    .query("is_canceled == 0") \
    .groupby(['has_kids'], as_index=False) \
    .agg({'has_kids': 'sum'}) \
    .sort_values('has_kids', ascending=False) \

nocens

summa = cens + nocens
oneproc = summa/100
