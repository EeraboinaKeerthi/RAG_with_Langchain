# RAG_with_Langchain

LLM Limitations: Knowledge is constrained to what is included in training data.

RAG allows us to overcome this by integrating external data sources into LLM Applications.

RAG Workflow:

 1.Load : Load the documents to build the knowledge base

2. Split : Split them into chunks to be processed.

3. Embedding: Create numerical representations from text called embeddings

4. Store: These embeddings or vectors are stored in a vector database for future retrieval.


Load the documents using Langchain:
CSV- CSVLoader: a dependency for loading csv files in LangChain, pdf- PyPdf: a dependency for loading PDF documents in LangChain, html- UnstructuredHTMLLoader: a dependency for loading html files in LangChain
