from etl.extractors.extractor import UserExtractor
from etl.transformers.json_transformer import JSONTransformer
from etl.loaders.opensearch_indexer import OpenSearchIndexer


def main():
    # ---------------------------
    # Extract
    # ---------------------------
    extractor = UserExtractor()
    rows = extractor.extract()

    # ---------------------------
    # Transform
    # ---------------------------
    transformer = JSONTransformer()
    output = transformer.transform(rows)

    print("Transformed Output:")
    print(output)

    # ---------------------------
    # Load → OpenSearch (using loader method)
    # ---------------------------
    indexer = OpenSearchIndexer()

    responses = indexer.index_users(output)

    print("\nIndexed Documents:")
    for res in responses:
        print(res)


if __name__ == "__main__":
    main()