from fastapi import APIRouter
from pydantic import BaseModel
from nltk.corpus import wordnet
import traceback

router = APIRouter()


@router.get("/spa")
async def spanish_synonym(word: str):
    try:
        results = []
        for syn in wordnet.synsets(word, lang=('spa')):
            for name in syn.lemma_names('spa'):
                results.append(name)
        return results
    except BaseException as ex:
        print(traceback.format_exc())
        return []


@router.get("/en")
async def english_synonym(word: str):
    try:
        results = []
        for syn in wordnet.synsets(word):
            for name in syn.lemma_names():
                results.append(name)
        return results
    except:
        return []
