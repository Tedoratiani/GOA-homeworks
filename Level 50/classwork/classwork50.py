# Nameerror როცა დასახელებული ცვლადი არ არის დადგენლი/შექმნილი
# Taberror როცა შეცდომა ინდენტაციაშა
# indexerror როცა ისეთი ინდექსი დავასახელეთ ან გამოვიძახეთ რომელის სიაში/სტრინგში არ არის
# valueerror როცა ცვლადის მნიშვნელობა არ შეესაბამება იმ ფუნქციის ლოგიკას
try:
    print(abc)
except:
    print("ცვლადი არ არის შედგენილი")


list=[1,2,3]
try:
    print(list[3])
except:
    print("ეს ინდექსი არ მოიძებნა")


try:
    abc=int("abc")
except:
    print("ასოებს ციფრებად ვერ გადააქცევ")


