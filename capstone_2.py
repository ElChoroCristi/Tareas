#hacer un combinador de nombres

def name_swap(first1, first2, largo1, largo2):
    largoa = int(largo1 / 2)
    largob = int(largo2 / 2)
    first = first1[0:largoa:1] + first2[largob:largo2:1]
    return first



first_last1 = str(input("Ingrese Nombre y Apellido"))
first_last2 = str(input("Ingrese otro Nombre y Apellido"))

space1 = int(first_last1.find(" "))
space2 = int(first_last2.find(" "))

largo_total1 = len(first_last1)
largo_total2 = len(first_last2)

first1 = first_last1[0:space1:1]
first2 = first_last2[0:space2:1]
largo_f1 = len(first1)
largo_f2 = len(first2)

last1 = first_last1[space1:largo_total1:1]
last2 = first_last2[-1:space2:-1]
largo_l1 = len(last1)
largo_l2 = len(last2)

new_first = str(name_swap(first1, first2, largo_f1, largo_f2))
new_last = str(name_swap(last1, last2, largo_l1, largo_l2))
print(new_first + " " + new_last)