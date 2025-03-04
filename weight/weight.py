##scoring mechanism for different keywords
from urllib.parse import urlparse

import spacy

nlp = spacy.load("en_core_web_md")
priority_keyword_weights = {
    "high_priority": (
        5,
        nlp(
            "bill law amendment vote resolution court supreme-court judiciary constitution parliament senate congress governor mayor treaty agreement"
        ),
    ),
    "medium_priority": (
        3,
        nlp(
            "health pandemic COVID-19 vaccine public-health security cybersecurity environment climate-change election voting national-security disaster-response"
        ),
    ),
    "low_priority": (
        1,
        nlp(
            "civil-rights justice human-rights democracy protests legislation laws regulations audit whistleblower public-comment news announcements"
        ),
    ),
    "baseline_priority": (0.5, nlp(".gov gov government")),
}


def findweight(url):
    parsed_url = urlparse(url)
    url_text = f"{parsed_url.netloc} {parsed_url.path} {parsed_url.query}".lower()
    total_weight = 0
    urlembedding = nlp(str(url_text))
    for key, value in priority_keyword_weights.items():
        similarity = urlembedding.similarity(value[1])
        total_weight += similarity * value[0]
    print(url, total_weight)
    return total_weight
