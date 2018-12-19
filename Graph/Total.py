"""carsales"""
import pandas as pd
import matplotlib.pyplot as plt
def main():
    """carsalespermonth"""
    df = pd.read_csv('car.csv')
    df.set_index("Brand", inplace=True)
    ax = df["Total"].plot(kind="bar", figsize=(10, 10));
    ax.set_title('ยอดขายรถยนต์ทั้งหมดในปี2018(เดือนมกราคม-กันยายน)',fontname='Circular',fontsize='22')
    ax.set_ylabel("จำนวนยอดขายรถยนต์(คัน)", fontname='Circular', fontsize='20')
    ax.set_xlabel("ยี่ห้อรถยนต์", fontname='Circular', fontsize='20')
    plt.show()

main()
