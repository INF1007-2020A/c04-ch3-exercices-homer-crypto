#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    Result_sqrt_root = math.sqrt(a)
    return Result_sqrt_root


def square(a: float) -> float:
    Result_sqrt = a*a
    return Result_sqrt


def average(a: float, b: float, c: float) -> float:
    Result_avrg = (a + b + c)/3
    return Result_avrg


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    min_to_deg = angle_mins * (1/60)
    sec_to_deg = angle_secs * (1/3600)
    to_radians = (angle_degs + min_to_deg + sec_to_deg) * (math.pi/180)
    return to_radians


def to_degrees(angle_rads: float) -> tuple:
    rad_to_deg = math.degrees(angle_rads)
    minutes = rad_to_deg % 1
    return 0.0, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    to_celsius = (temperature - 32)/1.8
    return to_celsius


def to_farenheit(temperature: float) -> float:
    to_farenheit = (temperature * 1.8 + 32)
    return to_farenheit


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
