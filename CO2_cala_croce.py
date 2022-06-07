from matplotlib import pyplot as plt
import math
import random


dis_casa_scuola = [4, 3.4, 0.35, 1.7, 1.1, .23, .63, .55, .75, .7, 13, .65, .7, 2.5, .09, .8, 1, 1.7, .55, 2.8, 1.5]
kilometri_per_litro = {'gpl': 10, 'benzina': 13, 'diesel': 26.3, 'metano': 22.7}
c02_prodotta_per_litro = {'gpl': 1610, 'benzina': 2380, 'diesel': 2650, 'metano': 2750} # as grams per liter
school_days_per_month = 20
months_of_school = 8


def distance_over_one_month(distance, school_days_per_month):
    tot_distance = sum(distance) * 2 * school_days_per_month
    return math.ceil(tot_distance)


def grams_to_kilos(n):
    return n / 1000


distance_over_one_month = distance_over_one_month(dis_casa_scuola, school_days_per_month)

# if all the distance was covered with disel, the CO2 produced per liter is:
c02_per_litro_diesel = c02_prodotta_per_litro['diesel'] / kilometri_per_litro['diesel'] * distance_over_one_month
c02_per_litro_benzina = c02_prodotta_per_litro['benzina'] / kilometri_per_litro['benzina'] * distance_over_one_month
c02_per_litro_metano = c02_prodotta_per_litro['metano'] / kilometri_per_litro['metano'] * distance_over_one_month
c02_per_litro_gpl = c02_prodotta_per_litro['gpl'] / kilometri_per_litro['gpl'] * distance_over_one_month

all_gasses = [c02_per_litro_benzina, c02_per_litro_diesel, c02_per_litro_metano, c02_per_litro_gpl]
for value, gas_name in zip(all_gasses, kilometri_per_litro.keys()):
    value = grams_to_kilos(value)
    print(f'{gas_name}\t : {value=:.2f}')


# median of kilos of co2 produced each month
c02_kili_mese = sum(all_gasses) / len(all_gasses)
print(f'{c02_kili_mese=:.2f}')


# co2 of class per school year, as a function
def co2_per_school_year(c02_kili_mese, months_of_school):
    return c02_kili_mese * months_of_school


# c02 of each student per month
def c02_per_student_per_month(dis_casa_scuola, gas_type, school_days_per_month) -> list:
    c02_per_student_per_month = []
    for distance in dis_casa_scuola:
        c02_per_student_per_month.append(distance * 2 * school_days_per_month * kilometri_per_litro[gas_type] / 1000)
    return c02_per_student_per_month


# c02 of each student per year
def c02_per_student_per_year(c02_per_student_per_month, months_of_school):
    c02_per_student_per_year = []
    for c02 in c02_per_student_per_month:
        c02_per_student_per_year.append(c02 * months_of_school)
    return c02_per_student_per_year


# plot the values of c02 per student per year
def plot_c02_per_student_per_year(c02_per_student_per_year):
    plt.plot(c02_per_student_per_year)
    plt.show()


# plot the values of c02 per student per month
def plot_c02_per_student_per_month(c02_per_student_per_month):
    plt.plot(c02_per_student_per_month)
    plt.show()


plot_c02_per_student_per_month(c02_per_student_per_month(dis_casa_scuola, 'benzina', school_days_per_month))
plot_c02_per_student_per_year(c02_per_student_per_year(c02_per_student_per_month(dis_casa_scuola, 'benzina', school_days_per_month), months_of_school))