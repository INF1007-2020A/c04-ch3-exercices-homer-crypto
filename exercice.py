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
    min_to_rad = angle_mins * (1/60) * (math.pi/180)
    sec_to_rad = angle_secs * (1/3600) * (math.pi/180)
    deg_to_rad = (angle_degs * (math.pi/180)) + min_to_rad + sec_to_rad

    return deg_to_rad


def to_degrees(angle_rads: float) -> tuple:
    return 0.0, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    to_celsius = (temperature - 32)/1.8
    return to_celsius


def to_farenheit(temperature: float) -> float:
    to_farenheit = (temperature * )
    return 0.0


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
