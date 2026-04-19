import json
import os

from documentcloud import DocumentCloud


def main() -> None:
    username = os.environ.get("DOCUMENTCLOUD_USERNAME")
    password = os.environ.get("DOCUMENTCLOUD_PASSWORD")
    client = DocumentCloud(username, password)

    # Look up the Documenters Network organization to get its integer ID,
    # which is required by the documents list filter.
    orgs = client.organizations.list(name="Documenters Network")
    org = next(iter(orgs), None)
    if org is None:
        raise ValueError("Could not find 'Documenters Network' organization")
    print(f"Organization: {org.name} (ID: {org.id})")

    # Fetch the first page of documents created from Jan 1 to Apr 1, 2026.
    # created_at__gt=2025-12-31 captures all of Jan 1 onwards.
    results = client.documents.list(
        organization=org.id,
        created_at__gt="2025-12-31",
        created_at__lt="2026-04-01",
        status="success",
    )

    print(f"Total documents: {results.count}")
    for doc in results.results:
        print(f"  [{doc.id}] {doc.title}  —  {doc.created_at:%Y-%m-%d}")

    # Inspect the first document: metadata + json_text with per-page links.
    first = results.results[0]
    print(f"\nInspecting: {first.title}")

    metadata = {
        "id": first.id,
        "title": first.title,
        "slug": first.slug,
        "description": first.description,
        "source": first.source,
        "language": first.language,
        "access": first.access,
        "status": first.status,
        "page_count": first.page_count,
        "created_at": first.created_at.isoformat(),
        "updated_at": first.updated_at.isoformat(),
        "publish_at": first.publish_at,
        "published_url": first.published_url,
        "related_article": first.related_article,
        "canonical_url": first.canonical_url,
        "asset_url": first.asset_url,
        "file_hash": first.file_hash,
        "user": first.user_id,
        "organization": first.organization_id,
        "data": first.data,
        "noindex": first.noindex,
    }

    json_text = first.json_text
    for page in json_text["pages"]:
        page["url"] = f"{first.canonical_url}#document/p{page['page'] + 1}"

    print(json.dumps({"metadata": metadata, "json_text": json_text}, indent=2))


if __name__ == "__main__":
    main()
