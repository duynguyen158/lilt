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
    )

    print(f"Total documents: {results.count}")
    for doc in results.results:
        print(f"  [{doc.id}] {doc.title}  —  {doc.created_at:%Y-%m-%d}")


if __name__ == "__main__":
    main()
