from app.database import client, COLLECTION_NAME

def match_job_description(job_desc):
    from core.embedder import get_embedding
    job_vector = get_embedding(job_desc)

    hits = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=job_vector,
        limit=5
    )

    return [
        {
            "filename": hit.payload["filename"],
            "score": hit.score
        } for hit in hits
    ]