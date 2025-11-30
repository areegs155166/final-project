cars = [
    ["تويوتا كامري", 95000],
    ["هيونداي سوناتا", 85000],
    ["كيا سبورتاج", 105000],
    ["هوندا أكورد", 110000],
    ["مازدا 6", 90000]
]

print("اختر رقم السيارة:")
for i in range(len(cars)):
    print(f"{i+1} - {cars[i][0]}")

choice = input("اكتب الرقم: ")

if not choice.isdigit():
    print("خطأ: الرجاء إدخال رقم فقط.")
else:
    index = int(choice) - 1

    if 0 <= index < len(cars):
        name = cars[index][0]
        price = cars[index][1]

        tax = price * 0.15
        total = price + tax

        print("اسم السيارة:", name)
        print("السعر شامل الضريبة:", total)
    else:
        print("خطأ: رقم السيارة غير موجود.")
