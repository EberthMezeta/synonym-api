from fastapi import APIRouter
from pydantic import BaseModel
from utils.synonyms import synonyms_generator


router = APIRouter()


@router.get("/spa")
async def spanish_synonym(word: str):
    results = []
    synonyms_generator_object = synonyms_generator()
    results = synonyms_generator_object.get_synonyms(word, 'spa')
    return results


@router.get("/en")
async def english_synonym(word: str):
    results = []
    synonyms_generator_object = synonyms_generator()
    results = synonyms_generator_object.get_synonyms(word, 'eng')
    return results
