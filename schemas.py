"""
Pydantic schemas/model to validate/parse request and replies
"""
import re
from pydantic import BaseModel, validator, ValidationError

year_regex = re.compile("^(19|20)\d{2}$")  # i hate regex


class Movie(BaseModel):
    """
    A 'simple' movie as per ...
    """

    movie_title_search_string: str
    release_year: str
    mtype: str # todo enum

    # @validator("release_year")
    # def release_year_must_be_a_valid_year(cls, v):
    #     """
    #     we make sure the year string we receive as input is valid
    #     :param v:
    #     :return:
    #     """
    #     if not year_regex.match(v):
    #         raise ValidationError(f"Invalid year : {v}")
