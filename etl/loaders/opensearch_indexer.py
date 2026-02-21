from opensearchpy import OpenSearch
import uuid


class OpenSearchIndexer:
    def __init__(self, host="localhost", port=9200, index_name="paragraphs"):
        self.index_name = index_name

        self.client = OpenSearch(
            hosts=[{"host": host, "port": port}],
            http_compress=True
        )

    def create_index_if_not_exists(self):
        if not self.client.indices.exists(index=self.index_name):
            self.client.indices.create(
                index=self.index_name,
                body={
                    "mappings": {
                        "properties": {
                            "content": {"type": "text"}
                        }
                    }
                }
            )

    def _normalize_doc(self, doc):
        """
        Convert ANY transformer output → valid dict with 'content'
        """

        # case 1 → already correct dict
        if isinstance(doc, dict) and "content" in doc:
            return doc

        # case 2 → tuple like (id, name, email)
        if isinstance(doc, (list, tuple)):
            return {"content": " ".join(map(str, doc))}

        # case 3 → single value (int/string/etc.)
        return {"content": str(doc)}

    def index_documents(self, documents: list):
        self.create_index_if_not_exists()

        responses = []

        for doc in documents:
            clean_doc = self._normalize_doc(doc)

            response = self.client.index(
                index=self.index_name,
                id=str(uuid.uuid4()),
                body=clean_doc
            )

            responses.append(response)

        return responses