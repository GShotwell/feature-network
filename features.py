from decorators import feature
from pandas import DataFrame
from typing import Callable, Union
import datetime


@feature
def date(date: DataFrame) -> None:
    return None


@feature
def dob(data: DataFrame) -> datetime.date:
    return None


@feature
def age(
    data,
    date: Union[Callable, datetime.date] = date,
    dob: Union[Callable, datetime.date] = dob,
):
    return date(data) - dob(data)


@feature
def state(data: DataFrame) -> None:
    return None


@feature
def age_in_years(data: DataFrame, age: int = age) -> int:
    return age(data) / 365


@feature
def is_florida(data: DataFrame, state: Union[Callable, str] = state):
    return state == "FL"
