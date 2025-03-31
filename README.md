# RAG_with_Langchain

LLM Limitations: Knowledge is constrained to what is included in training data.

RAG allows us to overcome this by integrating external data sources into LLM Applications.

RAG Workflow:

 1.Load : Load the documents to build the knowledge base

2. Split : Split them into chunks to be processed.

3. Embedding: Create numerical representations from text called embeddings

4. Store: These embeddings or vectors are stored in a vector database for future retrieval.


**Load the documents using Langchain:**
CSV- CSVLoader: a dependency for loading csv files in LangChain, pdf- PyPdf: a dependency for loading PDF documents in LangChain, html- UnstructuredHTMLLoader: a dependency for loading html files in LangChain

**Splitting or Chunking**

Documents are splitted in chunks that contain sufficient context useful to LLM's.If the chunks are huge, retrieval will be slow and LLM may struggle to extract the most relevant context from the chunk to respond to query. 

chunk_size parameter is used to control this balance. Another parameter chunk_overlap is used to capture important information that may be lost around the boundaries between the chunk.

1. Charactertextsplitter: This method was also unable to create chunks that were all below the chunk_size by splitting by-paragraph.
2. Recursivecharactertextsplitter: We can improve with RecursiveCharacterTextSplitter.

**Embeddings and Storage**
Embeddings are numerical representations of text.
Embedding models aim to capture the "meaning" of the text, and these numbers map the text's position in a high-dimensional, or vector space.
When documents are embedded and stored, similar documents are located closer together in the vector space. When the RAG application receives a user input, it will be embedded and used to query the database, returning the most similar documents.
